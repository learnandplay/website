var backofficeApp = angular.module('backofficeApp', ['ngRoute']);

backofficeApp.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
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

backofficeApp.controller('AdministratorsCtrl', function($scope, $http) {
    $scope.addAdministrator = function(administrator_username) {
    	$http({
    		url: "/backoffice/restapi/add_administrator",
    		method: "POST",
    		data: {"class_id": $scope.class_id, "username": administrator_username},
    		headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
		}).success(function(data, status, headers, config) {
			data = JSON.parse(data);
			$scope.administrators.push(data.added_administrator);
			$scope.administrators.sort(function(a, b) {return a.username.localeCompare(b.username);});
		}).error(function(data, status, headers, config) {
			$scope.alertError = true;
			$scope.administratorAlerError = "Impossible d'ajouter l'administrateur: Aucun professeur avec le nom d'utilisateur '"+administrator_username+"' existant";
		});
    	$scope.userData.administratorToAdd = "";
    };

    $scope.removeAdministrator = function(administrator) {
		$http({
    		url: "/backoffice/restapi/remove_administrator",
    		method: "POST",
    		data: {"class_id": $scope.class_id, "administrator_id": administrator.id},
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
			$scope.alertError = true;
			$scope.administratorAlerError = "Impossible de supprimer l'administrateur";
		});
    };

	$scope.getAdministratorsList = function() {
		$http({
			url: "/backoffice/restapi/get_schoolclass_administrators/" + $scope.class_id,
			method: "GET",
		}).success(function(data, status, headers, config) {
			$scope.administrators = JSON.parse(data);
		}).error(function(data, status, headers, config) {
			$scope.alertError = true;
			$scope.administratorAlerError = "Impossible de récupérer la liste des administrateurs";
		});
	};

	$scope.init = function(class_id) {
		$scope.class_id = class_id;
		$scope.getAdministratorsList();
	}
});