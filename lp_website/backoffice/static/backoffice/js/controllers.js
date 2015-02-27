var backofficeApp = angular.module('backofficeApp', ['ngRoute']);

backofficeApp.config(function($httpProvider, $routeProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $routeProvider.when('/backoffice/class_administrators/:class_id/', {
        controller: 'AdministratorsCtrl'
    });

    $locationProvider.html5Mode(true);
});

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

backofficeApp.controller('StudentsListCtrl', function($scope, $http) {
	$scope.deleteStudent = function(student) {
		$http({
    		url: "/backoffice/restapi/delete_user",
    		method: "POST",
    		data: {"user_id": student.id},
    		headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
		}).success(function(data, status, headers, config) {
			var i = $scope.students.length;
			while (i--) {
				if ($scope.students[i].id == student.id) {
					$scope.students.splice(i, 1);
				}
			}
		}).error(function(data, status, headers, config) {
    		console.log(status);
		});
	};

	$scope.changeSelectedSchoolClass = function() {
		$scope.students = $scope.initialData.students[$scope.selectedSchoolClass.id];
	};

	$scope.getStudentsList = function() {
		$http({
			url: "/backoffice/restapi/get_all_classes_students",
			method: "GET",
		}).success(function(data, status, headers, config) {
			data = JSON.parse(data);
			$scope.initialData = data;
			$scope.classes = data.school_classes;
			if ($scope.classes[0]) {
				$scope.selectedSchoolClass = $scope.classes[0];
				$scope.students = data.students[data.school_classes[0].id];
			}
			else {
				$scope.selectedSchoolClass = undefined;
				$scope.students = undefined;
			}
		}).error(function(data, status, headers, config) {
	    	console.log(status);
		});
	};

	$scope.getStudentsList();
});

backofficeApp.controller('AdministratorsCtrl', function($rootScope, $scope, $routeParams, $route, $http) {
    $rootScope.$on('$routeChangeSuccess', function () {
        $scope.getAdministratorsList();
    });

    $scope.removeAdministrator = function(administrator) {
		$http({
    		url: "/backoffice/restapi/remove_administrator",
    		method: "POST",
    		data: {"class_id": $routeParams.class_id, "administrator_id": administrator.id},
    		headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
		}).success(function(data, status, headers, config) {
			data = JSON.parse(data)
			if (data.needRedirect) {
				window.location = data.needRedirect
			}
			var i = $scope.administrators.length;
			while (i--) {
				if ($scope.administrators[i].id == administrator.id) {
					$scope.administrators.splice(i, 1);
				}
			}
		}).error(function(data, status, headers, config) {
    		console.log(status);
		});
    };

	$scope.getAdministratorsList = function() {
		$http({
			url: "/backoffice/restapi/get_schoolclass_administrators/" + $routeParams.class_id,
			method: "GET",
		}).success(function(data, status, headers, config) {
			$scope.administrators = JSON.parse(data);
		}).error(function(data, status, headers, config) {
	    	console.log(status);
		});
	};
});