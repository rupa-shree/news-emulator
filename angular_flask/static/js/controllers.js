'use strict';

/* Controllers */

function IndexController($scope,$http) {
	$scope.content = {};

	$http({
        method: 'POST',
        url: '/getallcontent',
        params: $scope.data,
        headers: { 'Content-Type': 'application/json' }
    })
    .then(function(data) {
        console.log(data);
        $scope.allcontent = data.data.results;
    });
	
}

function AboutController($scope) {
	
}

function PostListController($scope, Post) {
	var postsQuery = Post.get({}, function(posts) {
		$scope.posts = posts.objects;
	});
}

function PostDetailController($scope, $routeParams, Post) {
	var postQuery = Post.get({ postId: $routeParams.postId }, function(post) {
		$scope.post = post;
	});
}
