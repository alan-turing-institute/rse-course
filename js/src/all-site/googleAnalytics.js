if(globalSiteSpecificVars.googleAnalyticsIdsArray instanceof Array){
	//default UCL Google Analytics tracking
	var _gaq = _gaq || [];
	_gaq.push(['_setAccount', 'UA-943297-1']);
	_gaq.push(['_setDomainName', 'ucl.ac.uk']);
	_gaq.push(['_setSiteSpeedSampleRate', 100]);
	_gaq.push(['_trackPageview']);

	//set up site specif Google Analytics tracking
	if(globalSiteSpecificVars.googleAnalyticsIdsArray.length > 0){
		var gaIterator = 0;
		for(gaIterator in globalSiteSpecificVars.googleAnalyticsIdsArray){
			_gaq.push(['t' + gaIterator + '._setAccount', globalSiteSpecificVars.googleAnalyticsIdsArray[gaIterator]]);
			_gaq.push(['t' + gaIterator + '._setDomainName', 'ucl.ac.uk']);
			_gaq.push(['t' + gaIterator + '._trackPageview']);
		}
	}

	(function() {	
	var ga = document.createElement('script');
	ga.type = 'text/javascript';
	ga.async = true;
	ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
	var s =document.getElementsByTagName('script')[0];
	s.parentNode.insertBefore(ga, s);
	})();
}

