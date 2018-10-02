define(["jquery","owl"],function($){
	$(document).ready(function(){
		if(typeof(globalSiteSpecificVars.carouselConfig)==="undefined"){
			carouselConfig = {
				margin:10, responsiveClass:true,
				loop:true,
				autoplay:true,
				lazyload:true,
				autoHeight: false,
				animateOut:'fadeOut',
				autoplayHoverPause: true,
				smartSpeed:450,
				autoplayTimeout:5000,
				dots:true,
				items:1,
				nav:false,
				responsive:{
					0:{
						
					},
					500:{
				 
					},
					700:{
						nav:true,
					  
					},
					1000:
					{
						nav:true,

					},
					1300:{
						nav:true,

					}
				}
			};
		}else{
			carouselConfig = (globalSiteSpecificVars.carouselConfig);
			
		}
		$('.owl-carousel').owlCarousel(carouselConfig);
	});
});


