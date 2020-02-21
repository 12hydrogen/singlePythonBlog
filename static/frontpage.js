$(function(){
	$("p.first").next().css("top", "16%");
	$("p.first").next().nextAll().css("top", "18%");
	var d = new Date();
	var t = d.getTime();
	$.post("/login", {"timestamp": t}, function(data, status){
		if (data["timestamp"] > t){
			switch(data["status"]){
				case "accept":
				$("p#status").html("Congratulate for successfully loged in!<br/>Hi, " + data['user'] + "!");
				break;
				case "refused":
				$("p#status").html("Emmm... the username or password seems wrong...<br/>Check again, please, " + data['user'] + "!");
				break;
				case "error":
				$("p#status").html("It seems like we've got something wrong here...<br/>Cannot find your login status, a bug, I suppose.");
				break;
			}
		}
	});
	$("input[value='Login']").click(function(){
		u = $("input[name='username']").val();
		p = sha256($("input[name='password']").val());
		d = new Date();
		t = d.getTime();
		h = sha256(u + p + t);
		$.post("/login", {"username": u, "password": p, "timestamp": t, "hash": h}, function(data, status){
			if (data["timestamp"] > t && sha256(data["status"] + data["user"] + data["timestamp"]) == data["hash"]){
				switch(data["status"]){
					case "accept":
					$("p#status").html("Congratulate for successfully loged in!<br/>Hi, " + data['user'] + "!");
					break;
					case "refused":
					$("p#status").html("Emmm... the username or password seems wrong...<br/>Check again, please, " + data['user'] + "!");
					break;
					case "error":
					$("p#status").html("It seems like we've got something wrong here...<br/>Cannot find your login status, a bug, I suppose.");
					break;
				}
			}
		});
	});
});