$(function(){
	$(".title").click(function(){
		switch($(this).text()){
			case "Home":
				alert(1);
				break;
			case "Pages":
				alert(2);
				break;
			case "About":
				alert(3);
				break;
		}
	})
})