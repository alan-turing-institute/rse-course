// Fit iframe JS

define(["jquery"],function($){

	//if(document.URL.search(/(\?|&)file=template(.*)?/i) < 0){
		function viewsource() {
			//var body = $('body')
			var body = $("iframe").contents().find("body"),
			patternhtml = body.html().replace(/[<>]/g, 
				function(m) { 
					return {
						'<':'&lt;','>':'&gt;'
					}[m]
				}
			).replace(/\t/g, '  ').replace(/((ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?)/gi,'<a href="$1">$1</a>').replace(/&lt;!--PATTERN-JS(.|\n)*/,'');
					body.addClass('viewsource').prepend( '<h2 class="label">Example</h2>').append( '<h2 class="label">HTML</h2><pre class="prettyprint">' + patternhtml + '</pre>' );
		};

		//has to be duped from demo site to work with require
		function resizeiframe(id, height){
			window.parent.$('#' + id).height(parseInt(height, 10) + 10 + 'px');

		};

		$(window).on('load',function(){
			viewsource();

			var body = $("iframe").contents().find("body");
			resizeiframe('gitProxyIframe', body[0].scrollHeight);
		});
	//}

});

