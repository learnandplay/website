var backofficeApp = angular.module('backofficeApp', []);

backofficeApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

backofficeApp.controller('ClassesListCtrl', function($scope, $http) {
	$scope.deleteSchoolClass = function(schoolClass) {
		$http({
    		url: "/backoffice/restapi/delete_school_class",
    		method: "POST",
    		data: {"class_id": schoolClass.id},
    		headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
		}).success(function(data, status, headers, config) {
			var i = $scope.classes.length;
			while (i--) {
				if ($scope.classes[i].id == schoolClass.id) {
					$scope.classes.splice(i, 1);
				}
			}
		}).error(function(data, status, headers, config) {
    		console.log(status);
		});
	};

	$scope.getSchoolClasses = function() {
		$http({
	    	url: "/backoffice/restapi/get_user_schoolclasses",
	    	method: "GET",
		}).success(function(data, status, headers, config) {
	    	$scope.classes = data;
		}).error(function(data, status, headers, config) {
	    	console.log(status);
		});
	};

	$scope.getSchoolClasses();
});