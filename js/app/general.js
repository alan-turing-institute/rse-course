define(["jquery","allsite"],function($,gen){

	$(document).ready(function(){
		/* Browser feature detection and fixes
		-----------------------------------------------------------------*/
		if(Modernizr.svg===false) {//target browsers that don't support SVG
			
			//update all instances of SVG in img tag
			var $svgImage = $('img[src*="svg"]');
			$svgImage.each(function(){
				$(this).attr('src', function() {
					var tempSrc = $(this).attr('src');
					var newSrc = tempSrc.replace('.svg', '.png');
					$(this).attr('src',newSrc);
				});
			});

			//lazy load fix for the above svg fix
			$("img[data-src$='.svg']").each(function(){
				var tmpDataSrc = $(this).attr("data-src");
				$(this).attr("src",tmpDataSrc.replace(/([^\.]+)\.svg/i,'$1.png'));
			})

			//fix mobile header
			var mobileHeaderObj = $('.header--mobile');
			mobileHeaderObj.removeClass("default-header");
			mobileHeaderObj.addClass("no-svg");
		}
		if(!Modernizr.input.placeholder){//target browsers that doesn't support placeholder attribute
			$('[placeholder]').focus(function() {
			var input = $(this);
				if (input.val() == input.attr('placeholder')) {
				input.val('');
				input.removeClass('placeholder');
			}
			}).blur(function() {
				var input = $(this);
				if (input.val() == '' || input.val() == input.attr('placeholder')) {
					input.addClass('placeholder');
					input.val(input.attr('placeholder'));
				}
			}).blur();
			$('[placeholder]').parents('form').submit(function() {
				$(this).find('[placeholder]').each(function() {
					var input = $(this);
					if (input.val() == input.attr('placeholder')) {
						input.val('');
					}
				})
			});
		}
		Modernizr.load({
			test : Modernizr.touch//target browsers that support touch events
			//if old browser load the shiv
			,yep : '//cdn.ucl.ac.uk/indigo/js/lib/fastclick.min.js'
			,complete: function(){
				$(function() {
					if(typeof FastClick !=='undefined'){
						FastClick.attach(document.body);
					}
				});
			}
		});
		/* sticky nav
		-----------------------------------------------------------------*/
		var topNavObj = $("nav.nav--top");

		if(topNavObj.hasClass("nav--sticky-init")){
			var topNavFullHeight = parseInt(topNavObj.height()) + parseInt(topNavObj.css("padding-top")) + parseInt(topNavObj.css("padding-bottom"));
			var topNavHeightFromTop = parseInt(topNavObj.offset().top);

			function stickyNav(){
				var currentPos = parseInt($(window).scrollTop());

				if(currentPos > (topNavFullHeight + topNavHeightFromTop)){
					topNavObj.addClass("nav--sticky-active");
				}else{
					topNavObj.removeClass("nav--sticky-active");
				}
			}

			$(window).scroll(function(){
				stickyNav();
			})
			stickyNav();
		}
		/* layout hacks
		-----------------------------------------------------------------*/
		var bodyClass = $('body').attr("class");
		var leftNavList = $('.nav--left ul');
		var topNavList = $('.nav--top ul');
		var mobileNav = $('.nav--mobile');
		var mobileNavList = $('.nav--mobile ul');

		function resetCols(){
			$('.site-content__inner,.sidebar').css({
				'height':'auto'
				,'min-height':'0'}
			);
		}

		function equalizeVerticalCol(){
			//start off by resetting the columns
			resetCols();

			if($(window).width() >= 768){
				var mainColHeight = $('.site-content__inner').height();
				var verticalNavColHeight = $('.sidebar').height();
				if(verticalNavColHeight > mainColHeight){
					$('.site-content__inner').css('min-height',verticalNavColHeight);
				}
				else{
					$('.site-content__inner').css({
						'height':'auto'
						,'min-height':'0'}
					);
				}

				//set sub nav to height of main content
				$('.nav.nav--left.nav--subnav').height(
					parseInt($('.site-content__inner').height()) + 'px'
				);
			}else{
				$('.site-content__inner').css({
					'height':'auto'
					,'min-height':'0'}
				);
				//mobile sub nav
				$('.nav.nav--mobile.nav--subnav').height(
					parseInt($('nav.nav--mobile ul.subnav__list').height()) + 'px'
				);
			}
		}

		function buildmobileNav(){
			if(leftNavList.length > 0 && mobileNavList.length < 1){
				mobileNav.append("<ul>" + leftNavList.html() + "</ul>");
			}else if(topNavList.length > 0 && mobileNavList.length < 1){
				mobileNav.append("<ul>" + topNavList.html() + "</ul>");
			}
			return;
		}
		buildmobileNav();

		var verticalBodyClassPattern = /layout-vertical(.)*/i;
		if(verticalBodyClassPattern.test(bodyClass)){
			equalizeVerticalCol();
			$(window).resize(function(){
				equalizeVerticalCol();
			});
		}
		/* Detect IE compatability mode and show user alert
		-----------------------------------------------------------------*/
		var agentStr = navigator.userAgent;
		var isCompatabilityMode = false;
		var debug = false;//toggle this when in dev

		if(agentStr.indexOf("Trident/5.0") > -1){
			if (agentStr.indexOf("MSIE 7.0") > -1)
				isCompatabilityMode = true;
		}else if (agentStr.indexOf("Trident/4.0") > -1){
			if (agentStr.indexOf("MSIE 7.0") > -1)
				isCompatabilityMode = true;
		}
		if(isCompatabilityMode || debug){
			var messageStr = "<p>This website will not display correctly in compatibilty mode.";
			messageStr += " For more information please see <a href='http://www.ucl.ac.uk/indigo/design-foundation/indigo-constraints'>Indigo constraints</a></p>";
			
			$('body').prepend("<div class='announcement-bar'>" + messageStr + "</a><a href='#' class='announcement-bar--close'>x</span>");


			$('.announcement-bar--close').click(function(){
				$('.announcement-bar').remove();
			})
		}
		/* Multi-layer sliding navigation
		-----------------------------------------------------------------*/
		$(".subnav__item a").on('click', function(){
			var parentLevel = $(this).parents('ul').length -1;
			var currentMenu = $(this).closest('ul');
			var currentListItem = $(this).parent('li');
			var parentMenu = $('.subnav__list--level-' + parentLevel);
			var subMenu = $(this).next('ul');

			if(currentListItem.hasClass('back')) {
				// back button hit	
				currentMenu.removeClass('nav--active');
				parentMenu.removeClass('nav--hidden');
			} 
			else if(currentListItem.hasClass('back-1')) {
				$('.subnav__list').removeClass('nav--active');
				$('.subnav__list').removeClass('nav--hidden');
			} 
			else if (currentListItem.children('ul').length > 0) {
				// menu item has children - expand the menu
				subMenu.toggleClass('nav--active');
				currentMenu.addClass('nav--hidden');
			}
		});
		/* anything else that needs to appear on all pages
		-----------------------------------------------------------------*/

	});
});