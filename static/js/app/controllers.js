var studDbControllers = angular.module('studDbControllers', ['studDbServices']);

StudDbApp.controller('MainCtrl', ['$scope', '$location',
    function ($scope, $location) {
        $scope.$location = $location;
    }
]);

StudDbApp.controller('GroupListCtrl', ['$scope', 'GroupService', '$window',
    function ($scope, GroupService, $window) {
        $scope.groups = [];
        $scope.getGroups = function () {
            GroupService.query({}, function (response) {
                $scope.groups = response;
            });
        };
        $scope.getGroups();
        $scope.newGroupTitle = "";

        $scope.addAlert = function (message) {
            $scope.alerts.push({type: 'danger', msg: message});
        };

        $scope.closeAlert = function (index) {
            $scope.alerts.splice(index, 1);
        };

        $scope.addGroup = function () {
            $scope.alerts = [];
            GroupService.save({title: $scope.newGroupTitle},
                function () {
                    $scope.getGroups();
                },
                function (errorResult) {
                    $scope.addAlert(errorResult.data['title']);
                });
            $scope.newGroupTitle = "";
        };


        $scope.deleteGroup = function (group) {
            // Alert when trying to remove not empty group
            if (group.students.length > 0) {
                var deleteGroup = $window.confirm(group.title + ' is not empty. Are you absolutely sure you want to delete?');

                if (deleteGroup) {
                    GroupService.delete({id: group.id},
                        function () {
                            $scope.getGroups();
                        },
                        function (errorResult) {
                        }
                    )
                }
            }
            else {
                GroupService.delete({id: group.id},
                    function () {
                        $scope.getGroups();
                    },
                    function (errorResult) {
                    }
                );
            }


        };
    }]);

StudDbApp.controller('GroupDetailCtrl', ['$scope', 'GroupService', 'StudentService', '$routeParams', 'dateFilter',
    function ($scope, GroupService, StudentService, $routeParams, dateFilter) {
        $scope.group = {};
        $scope.getGroup = function () {
            $scope.group = GroupService.get({id: $routeParams.id});
        };
        $scope.newStudentName = '';
        $scope.newStudentId = '';
        $scope.newStudentBirthDate = '';
        $scope.getGroup();
        $scope.groupMonitor = '';

        $scope.addStudent = function () {
            StudentService.save({
                full_name: $scope.newStudentName,
                id_number: $scope.newStudentId,
                birth_date: dateFilter($scope.newStudentBirthDate, 'yyyy-MM-dd'),
                group: $scope.group.url
            }, function () {
                $scope.getGroup();
            });
            $scope.newStudentName = '';
            $scope.newStudentId = '';
            $scope.newStudentBirthDate = '';
        };

        $scope.deleteStudent = function (student) {
            StudentService.delete({id: student.id}, function () {
                $scope.getGroup()
            });
        };

        $scope.changeMonitor = function () {
            var editedGroup = GroupService.get({id: $routeParams.id}, function () {
                editedGroup.monitor = $scope.groupMonitor.url;
                editedGroup.$update({}, function () {
                    $scope.getGroup();
                    $scope.groupMonitor = '';
                });
            });
        };

    }]);

StudDbApp.controller('StudentListCtrl', ['$scope', 'StudentService', 'GroupService', 'dateFilter',
    function ($scope, StudentService, GroupService, dateFilter) {
        $scope.groups = GroupService.query();

        $scope.students = '';
        $scope.newStudentName = '';
        $scope.newStudentId = '';
        $scope.newStudentBirthDate = '';
        $scope.newStudentGroup = '';

        $scope.getStudents = function () {
            $scope.students = StudentService.query();
        };

        $scope.addStudent = function () {
            var newStudent = new StudentService;
            newStudent.full_name = $scope.newStudentName;
            newStudent.id_number = $scope.newStudentId;
            newStudent.birth_date = dateFilter($scope.newStudentBirthDate, 'yyyy-MM-dd');
            if ($scope.newStudentGroup) {
                newStudent.group = $scope.newStudentGroup.url;
            }
            else {
                newStudent.group = '';
            }
            newStudent.$save({}, function () {
                $scope.getStudents();
            });
            $scope.newStudentName = '';
            $scope.newStudentId = '';
            $scope.newStudentBirthDate = '';
            $scope.newStudentGroup = '';
        }
        ;

        $scope.deleteStudent = function (student) {
            StudentService.delete({id: student.id}, function () {
                $scope.getStudents()
            });
        };

        $scope.getStudents();
    }])
;

StudDbApp.controller('StudentDetailCtrl', ['$scope', 'StudentService', 'GroupService', '$routeParams', '$window',
    function ($scope, StudentService, GroupService, $routeParams, $window) {
        $scope.student = {};
        $scope.newStudentName = '';
        $scope.newStudentId = '';
        $scope.newStudentBirthDate = '';
        $scope.newStudentGroup = '';
        $scope.groups = GroupService.query();

        $scope.addAlert = function (message) {
            $scope.alerts.push({type: 'danger', msg: message});
        };

        $scope.closeAlert = function (index) {
            $scope.alerts.splice(index, 1);
        };

        $scope.getStudent = function () {
            $scope.student = StudentService.get({id: $routeParams.id}, function () {
                $scope.newStudentName = $scope.student.full_name;
                $scope.newStudentId = $scope.student.id_number;
                $scope.newStudentBirthDate = $scope.student.birth_date;
                $scope.newStudentGroup = $scope.student.group;
            });
        };

        $scope.getStudent();

        $scope.updateStudent = function () {
            $scope.alerts = [];
            var editedStudent = StudentService.get({id: $routeParams.id}, function () {
                editedStudent.full_name = $scope.newStudentName;
                editedStudent.id_number = $scope.newStudentId;
                editedStudent.birth_date = $scope.newStudentBirthDate;
                editedStudent.group = $scope.newStudentGroup;
                var group = GroupService.get({id: editedStudent.group_id}, function () {
                    // Checking if user is going to change group of student which is monitor of group
                    if ((editedStudent.group != $scope.student.group) && (editedStudent.url == group.monitor)) {
                        var removeMonitor = $window.confirm(editedStudent.full_name + 'is monitor of ' + group.title +
                            ' are you sure to change group?');
                        if (removeMonitor) {
                            console.log(group);
                            group.monitor = '';
                            editedStudent.$update({}, function () {
                                $scope.getStudent();
                                group.$update({}, function () {
                                });
                            }, function (errorResult) {
                                $scope.addAlert(errorResult.data['id_number']);
                                $scope.getStudent();
                            });

                        }
                        else ($scope.getStudent())
                    }
                    else {
                        editedStudent.$update({$id: $routeParams.id}, function () {
                            $scope.getStudent();
                        }, function (errorResult) {
                            $scope.addAlert(errorResult.data['id_number']);
                            $scope.getStudent();
                        });
                    }
                });


            });


        };


    }]);