// UCL JS
$(document).ready(function() {

	$('.tabbed div').hide();
	$('.tabbed div:first').show();
	$('.tabbed ul li:first').addClass('is-active');

	$('.tabbed ul li a').click(function() {
		$('.tabbed ul li').removeClass('is-active');
		$(this).parent().addClass('is-active');
		var currentTab = $(this).attr('href');
		$('.tabbed div').hide();
		$(currentTab).show();
		return false;
	});

	function removeCurrentClassFromAll() {
		var allPanelsAnchor = $('.accordion a');
		allPanelsAnchor.each(function() {
			$(this).removeClass("currentAccordionAnchor");
		});
	}
	/* accordion - start
	---------------------------------------------------------------------*/
	var allPanels = $('.accordion__description');
	allPanels.slideUp();
	//open accordions that have this set in their class
	$('.accordion__title a').each(function() {
		var tmpAccordionClass = $(this).attr("class");
		if (typeof tmpAccordionClass !== 'undefined' && tmpAccordionClass.indexOf('currentAccordionAnchor') >= 0) {
			$(this).parent().next().slideDown();
		}
	});


	$('.accordion__title a').click(function() {
		allPanels.slideUp();
		var tmpAccordionClass = $(this).attr("class");
		removeCurrentClassFromAll();
		if (typeof tmpAccordionClass === 'undefined' || tmpAccordionClass.indexOf('currentAccordionAnchor') === -1) {
			$(this).parent().next().slideDown();
			$(this).addClass("currentAccordionAnchor");
		}
		return false;
	});
	/* accordion - end
	---------------------------------------------------------------------*/
	$('.header__open, .header__close').click(function(e) {
		var body = $('body');
		if (body.hasClass('mobile-open')) body.removeClass('mobile-open');
		else body.addClass('mobile-open');
		e.preventDefault();
	});

	if (Modernizr.mq('only screen and (max-width: 768px)')) {
		//Add Inactive Class To All Accordion Headers
		$('.collapse__header').addClass('collapse__header--inactive');
		
		// The Accordion Effect
		$('.collapse__header').click(function() {
			if ($(this).is('.collapse__header--inactive')) {
				//				$('.collapse__header--active').toggleClass('collapse__header--active').toggleClass('collapse__header--inactive').next().slideToggle().toggleClass('open-content');
				//				$(this).toggleClass('collapse__header--active').toggleClass('collapse__header--inactive');
				$(this).removeClass('collapse__header--inactive').addClass('collapse__header--active');
				$(this).next().slideToggle().toggleClass('open-content');
			} else {
				$(this).removeClass('collapse__header--active').addClass('collapse__header--inactive');
				$(this).next().slideToggle().toggleClass('open-content');
			}
		});
	}else{
		$('.collapse__header').addClass('collapse__header--active');
	}
});