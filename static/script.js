$(function(){
	$(".title").click(function(){
		switch($(this).text()){
			case "Home":
				window.location.href = '/home'
				break;
			case "Pages":
				window.location.href = '/pages'
				break;
			case "About":
				window.location.href = '/about'
				break;
		}
	})
})