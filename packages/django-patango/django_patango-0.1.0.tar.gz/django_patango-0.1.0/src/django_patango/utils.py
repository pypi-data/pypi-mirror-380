import operator
import uuid
from functools import reduce

from django.db.models import (Avg, Count, Exists, ExpressionWrapper, F, Max,
                              Min, OuterRef, Q, QuerySet, Subquery, Sum, fields, FloatField)
from django.apps import apps
from django.db.models.functions import Coalesce

SUBQUERY_METHOD_DICT = {"__min": Min, "__max": Max, "__avg": Avg, "__sum": Sum, "__count": Count, }

class FakeField:
     def __init__(self, name):
        self.name = name


def handle_values(values, model, queryset, path=None):

    result = []
    for value in values:
        if isinstance(value, str):
            print (value, '__'.join((path or []) + [value]))
            result.append('__'.join((path or []) + [value]))
        else:
            result += handle_values(value["values"], model, queryset, (path or [])+[value["name"]])
    return result


def compute_node(node, node_model, queryset, path):
    clauses = []
    for child_key, child_value in node.items():
        queryset, node_clauses = handle_q_node(child_key, child_value, node_model, queryset, path)
        if node_clauses:
            clauses.append(node_clauses)
    return queryset, reduce(operator.and_, clauses, Q())


def handle_q_node(key, value, parent_model, queryset, path=None):

    if key in ["__exists", "__count", "__sum", "__min", "__max", "__avg"]:
        if key == "__exists":
            subqueryset = handle_q_node(None, value, parent_model, parent_model.objects.all(), [])
            return queryset , Exists(subqueryset)
        else:
            subqueryset = handle_q_node(None, value["query"], parent_model, parent_model.objects.all(), [])
            reversed_path = '__'.join(getattr(field.remote_field, 'related_name', getattr(field.remote_field, 'name')) for field in reversed(path))
            subqueryset = subqueryset.filter(**{f"{reversed_path}": OuterRef("pk")}).values(reversed_path)
            uid = str(uuid.uuid4())
            expression = value.get("column", "pk")
            field = find_field_by_name(parent_model, expression)
            if value.get("column_coalesce") is not None:
                expression = Coalesce(expression, value["column_coalesce"], output_field=field)
            subquery = Subquery(subqueryset.annotate(**{f"{uid}": SUBQUERY_METHOD_DICT[key](expression)}).values(uid))
            if value.get("coalesce") is not None:
                queryset = queryset.annotate(**{f"{uid}": Coalesce(subquery, value.get("coalesce"), output_field=field)}).values(uid) #
            else:
                queryset = queryset.annotate(**{f"{uid}": subquery}).values(uid)
            return compute_node(value["condition"], parent_model, queryset, [FakeField(uid)])

    elif key == "_or":
        clauses = []
        for child in value:
            queryset, clause = compute_node(child, parent_model, queryset, path)
            clauses.append(clause)
        return queryset, reduce(operator.or_, clauses, Q())

    elif key and key.startswith("__"):
        return queryset, Q(**{f"{'__'.join(field.name for field in path)+key}": value})

    elif key == "_not":
        queryset, clause = compute_node(value, parent_model, queryset, path)
        return queryset, ~clause

    elif key:
        field = find_field_by_name(parent_model, key)
        if field.__class__.__name__ in ["ManyToOneRel", "ManyToManyRel"]:  # autodetect # TODO check ManyToManyField if it works
            queryset = queryset.distinct()
        return compute_node(value, field.related_model or parent_model, queryset, (path or []) + [field])

    else:  #  not key -> root
        queryset, clause = compute_node(value, parent_model, queryset, path)
        print (clause)
        return queryset.filter(clause)


def get_model_by_db_table(db_table: str):
    try:
        return next(model for model in apps.get_models() if model._meta.db_table == db_table)
    except StopIteration:
        raise LookupError(f"No model found with db_table='{db_table}'")

def find_field_by_name(model, field_name):
    try:
        return next(field for field in model._meta.get_fields() if field.name == field_name)
    except StopIteration:
        raise LookupError(f"No field found with name='{field_name}' for db_table='{model._meta.db_table}'")

