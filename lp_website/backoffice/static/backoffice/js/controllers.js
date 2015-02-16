var backofficeApp = angular.module('backofficeApp', []);

backofficeApp.controller('ClassesListCtrl', function($scope, $http) {
	$http({
    	url: "/backoffice/restapi/get_user_schoolclasses",
    	method: "GET",
	}).success(function(data, status, headers, config) {
    	$scope.classes = data;
	}).error(function(data, status, headers, config) {
    	console.log(status);
	});
});