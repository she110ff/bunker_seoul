/**
 * Created by she110ff on 2014. 12. 4..
 */

var bunkerApp = angular.module('bunkerApp', [])
   .config(function($interpolateProvider) {
     $interpolateProvider.startSymbol('{$');
     $interpolateProvider.endSymbol('$}');
   })
   .config(['$httpProvider', function($httpProvider) {
     $httpProvider.defaults.xsrfCookieName = 'csrftoken';
     $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
   ])

  .controller('SubscriptionList', ['$scope', '$http', function($scope, $http) {
    $scope.todos = [
      {text:'learn angular', done:true},
      {text:'build an angular app', done:false}];

    $scope.products = []

    $scope.getProductList = function(savedURL){
        console.log("getProductList")
        $http.post('/seoul/product/subscription/', {"savedURL": savedURL})
            .success(function(data) {
                data_parsed = JSON.parse(data.products)
                console.log(data_parsed)
                $scope.products = data_parsed;
            })
            .error(function(err, status, headers, config) {
                console.log("err : ", err)
            })
    };
    $scope.doList = function() {
      console.log("run")
      $scope.getProductList("")
    };

    $scope.remaining = function() {
      var count = 0;
      angular.forEach($scope.todos, function(todo) {
        count += todo.done ? 0 : 1;
      });
      return count;
    };


    $scope.getProductList("")
  }])
  .directive('format', ['$filter', function ($filter) {
    return {
        require: '?ngModel',
        link: function (scope, elem, attrs, ctrl) {
            if (!ctrl) return;


            ctrl.$formatters.unshift(function (a) {
                return $filter(attrs.format)(ctrl.$modelValue)
            });


            ctrl.$parsers.unshift(function (viewValue) {
                var plainNumber = viewValue.replace(/[^\d|\-+|\.+]/g, '');
                elem.val($filter('number')(plainNumber));
                return plainNumber;
            });
        }
    };
}])
