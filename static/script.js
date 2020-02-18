$(function(){
	var stable = 0
})

function click(name){
	if(name != "home" && name != "pages" && name != "about")
		name = "home"
	switch(name){
		case "home":
		alert("1")
		case "pages":
		alert("2")
		case "about":
		alert("3")
	}
}