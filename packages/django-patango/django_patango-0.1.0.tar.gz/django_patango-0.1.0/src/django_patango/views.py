import json

from django.apps import apps
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .utils import handle_q_node, handle_values, get_model_by_db_table


def angular_view(request):
    return render(
        request,
        'django_patango/index.html',
        context={
            "introspection_url": reverse('django_patango_introspection'),
            "post_url": reverse('django_patango_post'),
        }
    )


def extract_schemas(request):
    exclude_models = []
    models_dict = {}
    for model in apps.get_models():
        if model._meta.proxy:
            continue
        name = model._meta.db_table
        if name in exclude_models:
            continue

        models_dict[name] = {"label": model.__name__, "group": model._meta.app_label, "db_table": name}
        if hasattr(model, "fk_choices"):
            models_dict[name]["choices"] = [(item.pk, getattr(item, model.fk_choices)) for item in model.objects.all()]

        # manyTOManyRel tiene ya null, por que no field.__class__.__name__ in  ["ManyToManyRel", "ManyToManyField"]
        models_dict[name]["fields"] = [
            {**{
                "db_type": field.__class__.__name__,
                "related_model": field.related_model._meta.db_table if field.related_model else None,
                "accessor_name": getattr(field, "get_accessor_name", lambda: None)(),
                "attname": getattr(field, "get_attname", lambda: None)(),
                "name": field.name,
                "label": getattr(field, "verbose_name", field.name),
                "blank": getattr(field, 'blank', None),
                "nullable": field.null or field.__class__.__name__ == "ManyToManyField",
                "related_name": field.field.name if hasattr(field, "field") else None  # ManyToManyRel and ManyToOneRel
            }, ** ({"choices": field.choices} if getattr(field, 'choices', None) else {})}

            for field in model._meta.get_fields()
        ]

    return JsonResponse(models_dict)


@csrf_exempt
def post(request):

    data = json.loads(request.body)
    model = get_model_by_db_table(data["model"])
    queryset = handle_q_node(None, data["q"], model, model.objects.all())
    queryset_values = handle_values(data["v"], model, queryset)
    return JsonResponse(queryset.values(*queryset_values).order_by(*queryset_values))
