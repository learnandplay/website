var backofficeApp = angular.module("backofficeApp", ['ngRoute', 'chart.js']);

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
    		$scope.alertError = true;
			$scope.schoolClassAlertError = "Impossible de supprimer la classe";
		});
	};

	$scope.getSchoolClasses = function() {
		$http({
	    	url: "/backoffice/restapi/get_user_schoolclasses",
	    	method: "GET",
		}).success(function(data, status, headers, config) {
	    	$scope.classes = data;
		}).error(function(data, status, headers, config) {
    		$scope.alertError = true;
			$scope.schoolClassAlertError = "Impossible de récupérer la liste des classes";
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
			$scope.alertError = true;
			$scope.studentsAlertError = "Impossible de supprimer l'étudiant";
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
			$scope.alertError = true;
			$scope.studentsAlertError = "Impossible de récupérer la liste des étudiants";
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
			$scope.administratorAlertError = "Impossible d'ajouter l'administrateur: Aucun professeur avec le nom d'utilisateur '"+administrator_username+"' existant";
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
			$scope.administratorAlertError = "Impossible de supprimer l'administrateur";
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
			$scope.administratorAlertError = "Impossible de récupérer la liste des administrateurs";
		});
	};

	$scope.init = function(class_id) {
		$scope.class_id = class_id;
		$scope.getAdministratorsList();
	}
});


backofficeApp.controller('StatisticsCtrl', function($scope, $http) {
  $scope.loadedStatisticsType = undefined;
  $scope.statisticsTypes = [{'type': 'stats_solo_multi', 'name': 'Solo/Multijoueur'},
                          {'type': 'stats_time_subject', 'name': 'Temps par matière'},
                          {'type': 'stats_success_fail', 'name': 'Echec/Reussite'}];
  $scope.selectedStatisticsType = $scope.statisticsTypes[0];
  $scope.previousSchoolClass = undefined;
  $scope.previousStudent = undefined;
  $scope.options_stats_solo_multi = {animationSteps: 20, animationEasing: "linear", responsive: true, tooltipTemplate: "<%if (label){%><%=label%>: <%}%><%= value %>%"};
  $scope.colours_stats_solo_multi = ['#81CFE0', '#1E8BC3'];
  $scope.options_stats_time_subject = {animationSteps: 20, animationEasing: "linear", responsive: true};
  $scope.colours_stats_time_subject = ['#2ECC71'];
  $scope.options_stats_success_fail = {animationSteps: 20, animationEasing: "linear", responsive: true, tooltipTemplate: "<%if (label){%><%=label%>: <%}%><%= value %>%"};
  $scope.colours_stats_success_fail = ['#2ECC71', '#F7464A'];

  $scope.display_stats_solo_multi = function() {
    $scope.labels = ["Solo", "Multijoueur"];
    var solo = 0;
    var multi = 0;
    var percentSolo;
    var percentMulti;
    $scope.data.forEach(function(stat) {
      if (stat.data.multi && (stat.data.multi == 'true' || stat.data.multi == true))
        multi++;
      else
        solo++
    });
    percentSolo = Math.round(solo * 100 / (solo + multi));
    percentMulti = Math.round(multi * 100 / (solo + multi));
    if (solo || multi) {
      $scope.prepared_data = [percentSolo, percentMulti];
      $scope.loadedStatisticsType = $scope.selectedStatisticsType;
    }
    else {
      $scope.noStatToDisplay = true;
    }
  }

  $scope.display_stats_time_subject = function() {
    $scope.labels = ["Mathématiques", "Français", "Histoire"];
    $scope.prepared_data = [
      [65, 59, 90]
    ];
    $scope.loadedStatisticsType = $scope.selectedStatisticsType;
  }

  $scope.display_stats_success_fail = function() {
    var success = 0;
    var failure = 0;
    var percentSuccesss;
    var percentFailure;
    $scope.labels = ["Réussite", "Echec"];
    $scope.data.forEach(function(stat) {
      if (stat.data.success && stat.data.failure) {
        success += parseInt(stat.data.success);
        failure += parseInt(stat.data.failure);
      }
    });
    percentSuccesss = Math.round(success * 100 / (success + failure));
    percentFailure = Math.round(failure * 100 / (success + failure));
    if (success || failure) {
      $scope.prepared_data = [percentSuccesss, percentFailure];
      $scope.loadedStatisticsType = $scope.selectedStatisticsType;
    }
    else {
      $scope.noStatToDisplay = true;
    }
  }

  $scope.displayStatistics = function() {
    switch($scope.selectedStatisticsType.type) {
      case 'stats_solo_multi':
        $scope.display_stats_solo_multi();
        break;
      case 'stats_time_subject':
        $scope.display_stats_time_subject();
        break;
      case 'stats_success_fail':
        $scope.display_stats_success_fail();
        break;
      default:
        break;
    }
  }

  $scope.getStatistics = function() {
    $scope.noStatToDisplay = false;
    $scope.loadedStatisticsType = undefined;
    if ($scope.previousSchoolClass != $scope.selectedSchoolClass ||
        $scope.previousStudent != $scope.selectedStudent) {
          $http({
            url: "/backoffice/restapi/get_statistics/" + $scope.selectedSchoolClass.id + "/" + ($scope.selectedStudent ? $scope.selectedStudent.id : "-1"),
            method: "GET",
          }).success(function(data, status, headers, config) {
            $scope.data = JSON.parse(data);
            $scope.data.forEach(function (item) {
              item.data = JSON.parse(item.data);
            });
            $scope.displayStatistics();
          }).error(function(data, status, headers, config) {
            $scope.alertError = true;
            $scope.alertErrorMessage = "Impossible de récupérer les statistiques";
          });
    }
    else {
      $scope.displayStatistics();
    }
    $scope.previousSchoolClass = $scope.selectedSchoolClass;
    $scope.previousStudent = $scope.selectedStudent;
  }



  $scope.changeSelectedSchoolClass = function() {
    $scope.students = $scope.initialData.students[$scope.selectedSchoolClass.id];
    $scope.selectedStudent = null;
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
        $scope.students = data.students[data.school_classes[0].id];
        $scope.selectedSchoolClass = $scope.classes[0];
      }
      else {
        $scope.students = undefined;
        $scope.selectedSchoolClass = undefined;
      }
      $scope.selectedStudent = null;
    }).error(function(data, status, headers, config) {
      $scope.alertError = true;
      $scope.alertErrorMessage = "Impossible de récupérer la liste des étudiants";
    });
  };

  $scope.getStudentsList();
});
