/**
 * Created by cifer on 18.09.14.
 */
var studDbServices = angular.module('studDbServices', ['ngResource']);

studDbServices.service('GlobalService', function () {
    var vars = {
        is_authenticated: false
    }
	return vars;
});

studDbServices.service('GroupService', [
    '$resource', function ($resource) {
        return $resource('/api/groups/:id', {id: '@id'},
            {update: {method: 'PUT'}}
        );
    }
]);

studDbServices.service('StudentService', [
    '$resource', function ($resource) {
        return $resource('/api/students/:id', {id: '@id'},
            {update: {method: 'PUT'}}
        );
    }
]);