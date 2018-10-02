define([
		"jquery"
		,"typeAheadBundle"
		,"handleBars"
	]
	,function($,Bloodhound,Handlebars){


		$(document).ready(function(){
			/* Call scripts as a result of new require set up
			-----------------------------------------------------------------*/
			var baseUrl = "//search2.ucl.ac.uk/s/";
			var ie7patt = /msie(\s)+[0-7]\.[0-9]+/ig;

			// The all link trigger
			function triggerSearch (tab) {
			   var baseUrlHtml = baseUrl + 'search.html?collection=website-meta'
			   window.location.assign(baseUrlHtml + "&tab=" + tab + "&profile=_" + tab + "&query=" + $('input#searchIndigo').val().replace(/\s/g,"+"));
			}

			function typeAhead(){
				if(!ie7patt.test(navigator.userAgent)){
					var jsonUrl = '/suggest.json?&collection=website-meta&show=10&sort=0&fmt=json++&';
					var baseUrlHtml = baseUrl + 'search.html?collection=website-meta'; 

					var url = baseUrl + jsonUrl + "partial_query=%QUERY&";

					// Reset checkboxes
					$('input.unchecked:checkbox').attr('checked', false);

					// Our templates for results
					var result__website = "<p><a href=\"{{url}}\">{{value}}</a></p>";

					var result__research = "<p><a href=\"{{url}}\">{{value}}</a></p>";

					var result__degree = "{{#if name}}<p class=\"result__title\"><a href=\"{{url}}\">{{name}}<span>{{qual}}</span></p>{{/if}}";

					var result__directory = "<div class=\"AC-details\"><ul class=\"profile-details\">{{#if name}}<li class=\"fn\">{{name}}</li>{{/if}}{{#if external}}<li class=\"tel tel--external\"><span>external: </span>{{external}}</li>{{/if}}{{#if email}}<li class=\"email\"><a href=\"mailto:{{email}}\">{{email}}</a></li>{{/if}}</ul></div>{{#if image}}<img src=\"{{image}}\" alt=\"image of {{name}}\">{{/if}}";

					
					var limit = 5;

					// apparently i can only use bloodhound for suggestions now

					var website =  new Bloodhound({
						datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value')
						,queryTokenizer: Bloodhound.tokenizers.whitespace
						,limit:  limit
						,remote:{
							url : url + "profile=_website" 
							,filter: function(list){
								return $.map(list, function(suggestion){
									return { 
										"value" : suggestion.disp
										,"url" : baseUrlHtml + "&query=" + suggestion.disp + '&profile=_website&tab=websites'
									}
								})
							}
							,ajax: {dataType: "jsonp"}
						}
					});

					var directory =  new Bloodhound({
						datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value')
						,queryTokenizer: Bloodhound.tokenizers.whitespace
						,limit: limit
						,remote: {
							url : url + "profile=_directory"
							,filter: function(list){
								return $.map(list, function(suggestion) {
									return suggestion.disp
								})
							}
							,ajax: {dataType: "jsonp"}
						}
					});

					var degrees =  new Bloodhound({
						datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value')
						,queryTokenizer: Bloodhound.tokenizers.whitespace
						,limit: limit
						,remote: {
							url : url + "profile=_degree"
							,filter: function(list){
								return $.map(list, function(suggestion) {
									return suggestion.disp
								})
							}
							,ajax: {dataType: "jsonp"}
						}
					});

					var research =  new Bloodhound({
						datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value')
						,queryTokenizer: Bloodhound.tokenizers.whitespace
						,limit: limit
						,remote: {
							url : url + "profile=_research"
							,filter: function(list){
								return $.map(list, function(suggestion) {
									return suggestion.disp
								})
							}
							,ajax: {dataType: "jsonp"}
						}
					 });

					directory.initialize();
					website.initialize();
					research.initialize();
					degrees.initialize();

				  	$(".search-form__input.search-form__input--search").typeahead({
						minLength : 2,
						hint: false 
					}
					,{
						name : "websites"
						,displayKey : "value"
						,source : website.ttAdapter()
						,templates : {
								empty : "<p class=\"no-results\">No Results</p>"
								,header : "<h2>Websites</h2>"
								,footer : ""
								,suggestion : Handlebars.compile(result__website)
							}
						}
					,{
						name : "degrees"
						,displayKey : "value"
						,source : degrees.ttAdapter()
						,templates : {
							empty : "<p class=\"no-results\">No Results</p>"
							,header : "<h2>Degrees and Short Courses</h2>"
							,footer : ""
							,suggestion : Handlebars.compile(result__degree)
						}
					}
					,{  
						name : "directory"
						,displayKey : "value"
						,source : directory.ttAdapter()
						,templates : {
							empty : "<p class=\"no-results\">No Results</p>"
							,header : "<h2>People</h2>"
							,footer : ""
							,suggestion : Handlebars.compile(result__directory)
						}
					}
					,{
						name : "research"
						,displayKey : "value"
						,source : research.ttAdapter()
						,templates : {
							empty : "<p class=\"no-results\">No Results</p>"
							,header : "<h2>Research</h2>"
							,footer : ""
							,suggestion : Handlebars.compile(result__research)
						}
					}
					).on('typeahead:selected',function($e, datum){
						// Debug only
						// For entries with a URL that are not profiles
						 if(datum.url && !datum.email){
							location = datum.url
							return false
						 }
						// Profiles and Websites should just fire the value
						if(!datum.email){
						// websites, fire ot websites tab
						}
						//$(".search-form__input.search-form__input--search").val(datum.value);
					});
				}
			};
			typeAhead();
		})
});