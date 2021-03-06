window.fbAsyncInit = function() {
	FB.init(
		{
			appId : 286279344852569,
			status : true,
			cookie : true,
			xfbml : true
		}
	);
	FB.Event.subscribe(
		'auth.authResponseChange',
		function(response) {
			if (response.status === 'connected') {
				testAPI();
			}
			else if (response.status === 'not_authorized') {
				FB.login();
			}
			else {
				FB.login();
			}
		}
	);
};

(
	function(d) {
		var js;
		id = 'facebook-jssdk';
		ref = d.getElementsByTagName('script')[0];
		if (d.getElementById(id)) {
			return;
		}
		js = d.createElement('script');
		js.id = id;
		js.async = true;
		js.src = "//connect.facebook.net/en_US/all.js";
		ref.parentNode.insertBefore(js, ref);
	} (document)
);

function testAPI() {
	console.log("Welcome! Fetching your information...");
	FB.api(
		'/me',
		function(response) {
			console.log("Good to see you, " + response.name + ".");
		}
	);
}
