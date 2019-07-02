$(document).ready(function(){

	console.log("ola")
	$('.img-fluid').hover(function(){

  $(".artisName").fadeIn("slow");

	},
	function(){
		    $(".artisName").fadeOut("slow");
	})
})