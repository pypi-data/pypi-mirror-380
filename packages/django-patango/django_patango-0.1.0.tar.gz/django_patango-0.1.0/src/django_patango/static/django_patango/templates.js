(function(module) {
try {
  module = angular.module('djangoPatango.templates');
} catch (e) {
  module = angular.module('djangoPatango.templates', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('templates/condition.html',
    '<span ng-if="$ctrl.inputType"><span ng-if="$ctrl.key.endsWith(\'__range\')">[<input ng-attr-type="{{$ctrl.inputType}}" required ng-model="$ctrl.value[$ctrl.key][0]"> <input ng-attr-type="{{$ctrl.inputType}}" required ng-model="$ctrl.value[$ctrl.key][1]">] </span><input ng-if="!$ctrl.key.endsWith(\'__range\')" ng-attr-type="{{$ctrl.inputType}}" ng-required="$ctrl.inputType !== \'checkbox\'" ng-model="$ctrl.value[$ctrl.key]"> </span><span ng-if="$ctrl.dateInput"><span ng-if="$ctrl.key.endsWith(\'__range\')">[<input-date-only model="$ctrl.value[$ctrl.key][0]" required="true"></input-date-only><input-date-only model="$ctrl.value[$ctrl.key][1]" required="true"></input-date-only>]</span><input-date-only ng-if="!$ctrl.key.endsWith(\'__range\')" model="$ctrl.value[$ctrl.key]" required="true"></input-date-only></span><span ng-if="$ctrl.key == \'__in\'"><ui-select class="multi-choices" ng-if="::$ctrl.field.choices.length > 0" ng-required="true" multiple="multiple" theme="bootstrap" ng-model="$ctrl.value[$ctrl.key]"><ui-select-match placeholder="{{::\'Select condition\' | translate}}">{{$item.label}}</ui-select-match><ui-select-choices repeat="c.value as c in ::$ctrl.choices | filter: {\'label\':$select.search}"><span ng-bind-html="c.label"></span></ui-select-choices></ui-select></span>');
}]);
})();

(function(module) {
try {
  module = angular.module('djangoPatango.templates');
} catch (e) {
  module = angular.module('djangoPatango.templates', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('templates/node.html',
    '<div class="node" ng-style="::{ \'background-color\': $ctrl.backGroundColor }"><span ng-if="$ctrl.nodeKey.startsWith(\'__\')"><subquery ng-if="$ctrl.isSubquery" subquery-type="$ctrl.nodeKey" subquery="$ctrl.nodeValue" field="$ctrl.nodeField" level="$ctrl.level +1"></subquery><span ng-if="!$ctrl.isSubquery"><b>{{$ctrl.nodeKey}}</b><condition value="$ctrl.parentValue" key="$ctrl.nodeKey" field="$ctrl.nodeField"></condition></span></span><span ng-if="!$ctrl.nodeKey.startsWith(\'__\')"><b>{{ $ctrl.label.toLowerCase() }} {</b> <select ng-required="$ctrl.contentRequired && $ctrl.isEmpty()" ng-change="$ctrl.addChild(_); _=null" ng-model="_" ng-options="f as f.label group by f.group for f in $ctrl.availableNodes"><option value="" disabled="disabled" selected="selected" hidden>{{::\'Add condition\' | translate}}</option></select><div style="margin-left:40px;"><div ng-if="$ctrl.nodeKey === \'_or\'"><span ng-repeat="node in $ctrl.nodeValue" style="display: flex; flex-direction: column; gap: 5px;"><node ng-repeat="(key, value) in node" node-key="key" parent-value="node" node-value="value" parent-field="$ctrl.nodeField" level="$ctrl.level +1"></node></span></div><div ng-if="$ctrl.nodeKey !== \'_or\'" style="display: flex; flex-direction: column; gap: 5px;"><node ng-repeat="(key, value) in $ctrl.nodeValue" parent-value="$ctrl.nodeValue" node-key="key" node-value="value" parent-field="$ctrl.nodeField" level="$ctrl.level +1"></node></div></div><b>}</b></span></div>');
}]);
})();

(function(module) {
try {
  module = angular.module('djangoPatango.templates');
} catch (e) {
  module = angular.module('djangoPatango.templates', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('templates/query-builder.html',
    '<!DOCTYPE html><div style="height: 100%"><div class="col-sm-6"><div class="form-horizontal" ng-if="$ctrl.availableQueries"><div class="form-inline margin-bottom-15" style="display: flex;"><ui-select append-to-body="true" theme="bootstrap" on-select="$ctrl.newQuery($item); selectedQuery=null" ng-model="selectedQuery"><ui-select-match placeholder="{{::\'New query\' | translate}}">{{$select.selected.value.label}}</ui-select-match><ui-select-choices group-by="\'group\'" repeat="query in $ctrl.availableQueries | orderBy: [\'label\'] |  filter: {label: $select.search}"><span ng-bind-html="query.label"></span></ui-select-choices></ui-select><input type="text" ng-model="$ctrl.jsonText" placeholder="Import Query" style="margin-left: 50px"><button ng-click="$ctrl.importQuery($ctrl.jsonText)">Submit</button></div></div></div><div ng-if="$ctrl.query.q" ng-form="$ctrl.queryForm" class="form-horizontal col-sm-12"><h1 class="text-center">{{$ctrl.query.label}}</h1><div class="form-inline root-node"><node node-value="$ctrl.query.q" parent-field="{\'related_model\': $ctrl.model, \'label\': $ctrl.model.label}" level="0"></node><pre>{{ $ctrl.query | json }}</pre></div><div class="form-inline root-node">{{$ctrl.query.v}}<values values="$ctrl.query.v" model="$ctrl.model"></values></div><div class="text-center"><button ng-disabled="$ctrl.queryForm.$invalid" ng-click="$ctrl.getQuery(\'html\')" class="btn btn-validate fixed-button">QUERY</button> <button ng-disabled="$ctrl.queryForm.$invalid" ng-click="$ctrl.getQuery(\'csv\')" class="btn btn-validate fixed-button">CSV</button></div><div class="stats-result-table" ng-bind-html="$ctrl.result" ng-if="$ctrl.result"></div></div></div>');
}]);
})();

(function(module) {
try {
  module = angular.module('djangoPatango.templates');
} catch (e) {
  module = angular.module('djangoPatango.templates', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('templates/subquery.html',
    '<div style="margin:5px; display: flex;"><span ng-if="$ctrl.subqueryType === \'__exists\'"><node node-value="$ctrl.subquery" parent-field="$ctrl.field" label="exists" level="$ctrl.level"></node></span><span ng-if="$ctrl.subqueryType !== \'__exists\'"><b>{{ $ctrl.subqueryType }} {</b><div style="margin-left:40px; display: flex; flex-direction: column; gap: 5px;"><span ng-if="$ctrl.needColumn" style="display: contents"><div ng-if="$ctrl.needColumn" style="display: flex; align-items: center; gap: 5px"><b>column </b><select required ng-model="$ctrl.subquery.column" ng-options="f.name as f.label.toLowerCase() for f in $ctrl.field.related_model.fields | filterNumberField "><option value="" disabled="disabled" selected="selected" hidden>{{::\'Select column\' | translate}}</option></select> <span ng-if="$ctrl.getFieldByName($ctrl.subquery.column).nullable"><b>column coalesce </b><input type="number" ng-model="$ctrl.subquery.column_coalesce"></span></div></span><div ng-if="$ctrl.nullable"><b>coalesce </b><input type="number" ng-model="$ctrl.subquery.coalesce"></div><div style="display: flex; align-items: center; gap: 5px"><node parent-value="$ctrl.nodeValue" node-value="$ctrl.subquery.condition" parent-field="{db_type: \'FloatField\'}" label="check" content-required="true"></node></div><node node-value="$ctrl.subquery.query" parent-field="$ctrl.field" label="query" level="$ctrl.level"></node></div><b>}</b></span></div>');
}]);
})();

(function(module) {
try {
  module = angular.module('djangoPatango.templates');
} catch (e) {
  module = angular.module('djangoPatango.templates', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('templates/values.html',
    '<div class="node" ng-style="::{ \'background-color\': $ctrl.backGroundColor }"><select ng-change="$ctrl.addChild(_); _=null" ng-model="_" ng-options="f as f.label group by f.group for f in $ctrl.availableValues"><option value="" disabled="disabled" selected="selected" hidden>{{::\'Add value\' | translate}}</option></select> <select ng-change="$ctrl.addChild(_); _=null" ng-model="_" ng-options="f as f.label group by f.group for f in $ctrl.availableDirectRelatedModels"><option value="" disabled="disabled" selected="selected" hidden>{{::\'Add FK\' | translate}}</option></select> <select ng-change="$ctrl.addChild(_); _=null" ng-model="_" ng-options="f as f.label group by f.group for f in $ctrl.availableSubqueries"><option value="" disabled="disabled" selected="selected" hidden>{{::\'Add Subquery\' | translate}}</option></select> <span ng-repeat="value in $ctrl.values" style="display: flex; flex-direction: column; gap: 5px;"><span ng-if="$ctrl.isString(value)">{{value}} </span><span ng-if="!$ctrl.isString(value)">SUBQUERY </span></span><span ng-repeat="virtualNode in $ctrl.virtualNodes" style="display: flex; flex-direction: column; gap: 5px;">virtualNode {{virtualNode.name}} <select ng-change="$ctrl.addChild(_); _=null" ng-model="_" ng-options="f as f.label group by f.group for f in virtualNode.availableValues"><option value="" disabled="disabled" selected="selected" hidden>{{::\'Add value\' | translate}}</option></select></span></div>');
}]);
})();
