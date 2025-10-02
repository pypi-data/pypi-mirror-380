angular.module('djangoPatango', ['ui.select', 'ngSanitize', 'djangoPatango.templates', 'pascalprecht.translate']);


'use strict';


angular.module("djangoPatango").component("condition", {
  templateUrl: "templates/condition.html",
  bindings: {key: '<', field: '<', value: '<'},
  controller: function conditionCtrl(Utils) {
    var ctrl = this;
    ctrl.$onInit = function () {
      if (ctrl.key == '__in'){
        ctrl.choices = _.map(ctrl.field.choices, c => {return {label: c[1], value: c[0]}})
      }
      else if (ctrl.key === "__isnull"){ctrl.inputType = "checkbox"}
      else if (["DateTimeField", "TimescaleDateTimeField", "DateField"].includes(ctrl.field.db_type)){
        ctrl.dateInput = true
      }
      else if (Utils.isNumeric(ctrl.field)){ctrl.inputType = "number"}
      else if (Utils.isTextual(ctrl.field)){ctrl.inputType = "text"}
      else if (Utils.isBoolean(ctrl.field)){ctrl.inputType = "checkbox"}
    }
  },
});

angular.module('djangoPatango').component('inputDateOnly', {
  bindings: {model: '=', required: '<?'},
  template: '<input type="date" ng-model="$ctrl.internalDate" ng-required="$ctrl.required" ng-change="$ctrl.onChange()"/>',
  controller: function() {
    var ctrl = this;
    ctrl.$onInit = function () {if (ctrl.model) {ctrl.internalDate = new Date(ctrl.model)}}
    ctrl.onChange = function() {
      if (ctrl.internalDate instanceof Date) {ctrl.model = ctrl.internalDate.toISOString().split('T')[0];
      } else if (typeof ctrl.internalDate === 'string') {ctrl.model = ctrl.internalDate.split('T')[0];
      } else { ctrl.model = null; }
    }
  }
});
'use strict';

angular.module("djangoPatango").component("node", {
  templateUrl: "templates/node.html",
  bindings: {nodeKey: '<', nodeValue: '<', parentValue: '<?', parentField: '<', label: '@', contentRequired: "<", level: "<"},  // parentValue mandatory to allow double binding on conditions dicts
  controller: function nodeCtrl(Utils) {
    // SIN RESOLVERS permite fk in, choices, postgis, json annotations
    var ctrl = this;
    console.log("gfd gaqui caca dsqdfdsfd ^")
    ctrl.isArray = angular.isArray;
    ctrl.addChild = function(field) {
      if (Array.isArray(ctrl.nodeValue)) {ctrl.nodeValue.push({ [field.key]: field.value })}
      else {Object.assign(ctrl.nodeValue, { [field.key]: field.value }) }
    };

    ctrl.isEmpty = function(){return ctrl.nodeKey === "_or" ? ctrl.nodeValue.length === 0: Object.keys(ctrl.nodeValue).length === 0}
    ctrl.$onInit = function () {
        ctrl.backGroundColor = `hsl(0, 0%, ${Math.max(95 - ctrl.level * 3, 20)}%)`;
        ctrl.isRoot = !ctrl.nodeKey
        ctrl.isSubquery =  ["__exists", "__count", "__sum", "__min", "__max", "__avg"].includes(ctrl.nodeKey)
        ctrl.isExpansionNode = ["_or", "_not"].includes(ctrl.nodeKey)
        ctrl.isRelatedModelCondition = ["__in", "__isnull"].includes(ctrl.nodeKey)
        if (ctrl.parentField.related_model && !ctrl.isRoot && !ctrl.isSubquery && !ctrl.isExpansionNode && !ctrl.isRelatedModelCondition){
            ctrl.nodeField = _.find(ctrl.parentField.related_model.fields, {name: ctrl.nodeKey})
            ctrl.label =  ctrl.label || ctrl.nodeField.label
        } else{
            ctrl.nodeField = ctrl.parentField
            ctrl.label =  ctrl.label || ctrl.nodeKey || ctrl.nodeField.label // ctrl.nodeField.label only for root purposes
        }
        ctrl.availableNodes = Utils.getFieldOptions(ctrl.nodeField)
        }
  },
});

'use strict';


angular.module("djangoPatango").component("queryBuilder", {
  templateUrl: "templates/query-builder.html",
  bindings: {introspectionUrl: "@", postUrl: "@"},
  controller: function queryBuilderCtrl($timeout, $q, $filter, $http, $scope, Utils) {
    var ctrl = this
    ctrl.jsonText = ""
    ctrl.newQuery = function (query) {
      ctrl.query = null
      ctrl.result = null
      var qq = {}
      $timeout(function () {
        ctrl.model = query; ctrl.query = {model: query.db_table, q: qq, v: [], s: {},}
      })
    }
    ctrl.importQuery = function (queryStr){
      var parsedJson = JSON.parse(queryStr);
      console.log(parsedJson)
      ctrl.query = null
      ctrl.result = null
      $timeout(function () {
        ctrl.model = _.find(ctrl.availableQueries, {db_table: parsedJson.model})
        ctrl.query = parsedJson
        ctrl.jsonText = ""
      })
    }

    ctrl.getQuery = function (resultType) {
      ctrl.result = null
      ctrl.resultType = resultType
      $http.post(ctrl.postUrl, _.assign({resultType: resultType}, ctrl.query)).then(function (response) {
        ctrl.result = response.data.result
      })
    }

    ctrl.$onInit = function () {
      $q.when(Utils.fetchAvailableQueries(ctrl.introspectionUrl)).then((availableQueries) => {
        ctrl.availableQueries = availableQueries
      })
    };
  },
});

'use strict';


angular.module("djangoPatango").component("subquery", {
  templateUrl: "templates/subquery.html",
  bindings: {subqueryType: '<', subquery: '<', field: '<', level: '<'},
  controller: function subqueryCtrl($rootScope, $q, Utils) {
    var ctrl = this;
    ctrl.getFieldByName = function(columnName){ return _.find(ctrl.field.related_model.fields, {name:columnName})}
    ctrl.$onInit = function () {
        console.log("subquery field", ctrl.field)
        ctrl.needColumn = ["__sum", "__min", "__max", "__avg"].includes(ctrl.subqueryType)
        ctrl.nullable = ctrl.field.nullable || ctrl.field.db_type === "ManyToManyRel" ||  ctrl.field.db_type === "ManyToManyField"
        if (ctrl.subqueryType !== "__exists"){
            ctrl.subquery.condition = ctrl.subquery.condition || {}
            ctrl.subquery.query = ctrl.subquery.query || {}
        }
    }
  },
});

'use strict';


angular.module("djangoPatango").factory('Utils', function ($q, $http, $filter) {



  var supportedFields = [
    // "PointField",
    "TimescaleDateTimeField",
    "BooleanField",
    "CharField",
    "EmailField",
    "DateField",
    "DateTimeField",
    "IntegerField",
    "BigAutoField",
    "AutoField",
    "FloatField",
    "DecimalField",
    "ForeignKey",
    "OneToOneField",
    "ManyToManyField",
    "ManyToManyRel",
    "OneToOneRel",
    "ManyToOneRel",
    // "DurationField",
    // "JSONField",
  ]

  var isRelationField = function(field){
    return field.related_model
//    return ["ForeignKey", "OneToOneField", "ManyToManyField", "ManyToManyRel", "OneToOneRel", "ManyToOneRel"].includes(field.db_type)
  }
  var isRelationFKField = function(field){ // TODO rename
    return ["ForeignKey", "OneToOneField", "OneToOneRel"].includes(field.db_type)
  }

    var allowSubquery = function(field){ // TODO rename
    return ["ManyToOneRel", "ManyToManyField", "ManyToManyRel"].includes(field.db_type)
  }

  var isBoolean = function(field){
    return ["BooleanField"].includes(field.db_type)
  }

  var isNumeric = function(field){
    return ["IntegerField", "AutoField", "FloatField", "BigAutoField", "DecimalField"].includes(field.db_type)
  }

  var isTextual = function(field){
    return ["CharField", "EmailField"].includes(field.db_type)
  }

  var fetchAvailableQueries = async function (introspectionUrl) {
    return $http.get(introspectionUrl).then(function (availableQueriesResponse) {
      var availableQueries = availableQueriesResponse.data
      _.forEach(_.keys(availableQueries), function (key) {  // Sanitize
        availableQueries[key].fields = _.orderBy(_.filter(availableQueries[key].fields, function (field) {
          return (!field.related_model || (field.related_model in availableQueries)) && supportedFields.includes(field.db_type)
        }), "label")
      })
      return _.flatMap(availableQueries, query => {
        _.forEach(_.filter(query.fields, "related_model"), relationField => {
          relationField.related_model = availableQueries[relationField.related_model]
          relationField.choices = relationField.related_model.choices
        })
        return query
      })
    })
  }


  var getFieldOptions = function(field){

      var options = [{label: "or",  key: "_or", value: [], group:"Expansion"},{label: "not",  key: "_not", value: {}, group:"Expansion"}]

      if (field.related_model){
        options = _.concat(options, _.map(field.related_model.fields, f => {return {label: f.label.toLowerCase()+ " "+ f.db_type, key: f.name, value: {}, group: isRelationField(f) ? "RelationField": "Field"}}),)
      }

      if (["ManyToOneRel", "ManyToManyField", "ManyToManyRel"].includes(field.db_type)){
        options = _.concat(options, [
          {label: "exists", key: "__exists", value: {}, group:"Subquery"},
          {label: "count", key: "__count", value: {}, group:"Subquery"},
        ])
        if ($filter('filterNumberField')(field.related_model.fields).length > 0){
            options = _.concat(options, [
              {label: "sum", key: "__sum", value: {}, group:"Subquery"},
              {label: "min", key: "__min", value: {}, group:"Subquery"},
              {label: "max", key: "__max", value: {}, group:"Subquery"},
              {label: "avg", key: "__avg", value: {}, group:"Subquery"},
            ])
        }
      }
      if (isTextual(field)){
        options = _.concat(options, [
          {label: "=", key:"__exact", value: ''},
          {label: "contains", key: "__contains", value: ''},
          {label: "icontains", key: "__icontains", value: ''},
          {label: "startswith", key: "__startswith",  value: ''},
          {label: "endswith", key: "__endswith", value: ''},
        ])
      }
      if (["DateTimeField", "TimescaleDateTimeField"].includes(field.db_type)){ // Hack __date by now waiting for input datetime working
        options = _.concat(options, [
          {label: "=", key: "__date__exact", value: ''},
          {label: ">=", key: "__date__gte", value: ''},
          {label: ">", key: "__date__gt", value: ''},
          {label: "<", key: "__date__lt", value: ''},
          {label: "<=", key: "__date__lte", value: ''},
          {label: "range", key: "__date__range", value: []},
        ])
      }
      if (["DateField"].includes(field.db_type)){
        options = _.concat(options, [
          {label: "=", key: "__exact", value: ''},
          {label: ">=", key: "__gte", value: ''},
          {label: ">", key: "__gt", value: ''},
          {label: "<", key: "__lt", value: ''},
          {label: "<=", key: "__lte", value: ''},
          {label: "range", key: "_range", value: []},
          // {label: "year =", input: "year", extra: {"function": "ExtractYear"}, lookup:"__exact"},
          // {label: "year >=", lookup: "__gte", input: "year", extra: {"function": "ExtractYear"}},
          // {label: "year >", lookup: "__gt", input: "year", extra: {"function": "ExtractYear"}},
          // {label: "year <", lookup: "__lt", input: "year", extra: {"function": "ExtractYear"}},
          // {label: "year <=", lookup: "__lte", input: "year", extra: {"function": "ExtractYear"}},
          // {label: "year range", lookup: "__range", input: "year_range", value: [1900, 2050], extra: {"function": "ExtractYear"}},
        ])
      }
      if (isNumeric(field)){
        options = _.concat(options, [
          {label: "=", key:"__exact", value: ''},
          {label: ">=", key: "__gte", value: ''},
          {label: ">", key: "__gt", value: ''},
          {label: "<", key: "__lt", value: ''},
          {label: "<=", key: "__lte", value: ''},
          {label: "range", key: "__range", value: []},
        ])
      }
      if (isBoolean(field)){
        options.push({label: "is", key:"__exact", value: true})
      }
      // if (["PointField"].includes(field.db_type)){
      //   options = _.concat(options, [
      //     {label: "distance <=", key: "__distance_lte", value: {}},
      //     {label: "distance >=", key: "__distance_gte", value: {}},
      //     {label: "distance >", key: "__distance_gt", value: {}},
      //     {label: "distance <", key: "__distance_lt", value: {}},
      //   ])
      // }
      if (field.nullable) {options.push({label: "exists", key: "__isnull", value: false, group:"Condition"})}
      if (field.choices && field.choices.length > 0) { options.push({label: "in",  key: "__in", value: [], group:"Condition"})}
      return _.orderBy(options, ["group", "label"])

  }

  return {
    fetchAvailableQueries: fetchAvailableQueries,
    getFieldOptions: getFieldOptions,
    isNumeric: isNumeric,
    isTextual: isTextual,
    isBoolean: isBoolean,
  }
});

angular.module('djangoPatango').filter('jsonPretty', function() {
  return function(obj) {return JSON.stringify(obj, null, 4);};
});

angular.module('djangoPatango').filter('filterNumberField', function (Utils) {
  return function (fields) {
    return _.filter(fields, function (field) {return Utils.isNumeric(field)})
  };
});
'use strict';

angular.module("djangoPatango").component("values", {
  templateUrl: "templates/values.html",
  bindings: {values: '<', model: '<'},
  controller: function nodeCtrl(Utils) {
    var ctrl = this;
    ctrl.virtualNodes = []
    ctrl.$onInit = function () {
        ctrl.availableValues =  _.map(_.filter(ctrl.model.fields, field => !field.related_model || ["ForeignKey", "OneToOneField"].includes(field.db_type)), field => {return {label: field.attname, value: field}})
        ctrl.availableDirectRelatedModels = _.map(_.filter(ctrl.model.fields, field => ["ForeignKey", "OneToOneField", "OneToOneRel"].includes(field.db_type)), field => {return {label: field.name, value: field}})
        ctrl.availableSubqueries = _.map(_.filter(ctrl.model.fields, field => [["ManyToOneRel", "ManyToManyField", "ManyToManyRel"]].includes(field.db_type)), field => {return {label: field.name, value: field}})
    }
  },
});
