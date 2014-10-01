'use strict';

var StudDbApp = angular.module('StudDbApp', [
    'ngCookies',
    'ngResource',
    'ngRoute',
    'studDbControllers',
    'studDbServices',
    'ui.bootstrap'
]);

/*
 StudDbApp.config(['$resourceProvider', function ($resourceProvider) {
 // Don't strip trailing slashes from calculated URLs
 $resourceProvider.defaults.stripTrailingSlashes = false;
 }]);
 */
StudDbApp.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/group-list.html",
            controller: "GroupListCtrl"
        })
        .when("/group/:id", {
            templateUrl: "static/js/app/views/group-detail.html",
            controller: "GroupDetailCtrl"
        })
        .when("/students", {
            templateUrl: "static/js/app/views/student-list.html",
            controller: "StudentListCtrl"
        })
        .when("/student/:id", {
            templateUrl: "static/js/app/views/student-detail.html",
            controller: "StudentDetailCtrl"
        })
        .otherwise({
            redirectTo: '/'
        });
}]);

StudDbApp.run(['$http', '$cookies', '$rootScope', function ($http, $cookies, $rootScope) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    $rootScope.is_authenticated = false;
}]);