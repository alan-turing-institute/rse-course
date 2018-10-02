define(["jquery"],function($){

/* IE support for this object */
if (!window.getComputedStyle) {
  
    window.getComputedStyle = function(el, pseudo) {
        this.el = el;
        this.getPropertyValue = function(prop) {
            var re = /(\-([a-z]){1})/g;
            if (prop == 'float') prop = 'styleFloat';
            if (re.test(prop)) {
                prop = prop.replace(re, function () {
                    return arguments[2].toUpperCase();
                });
            }
            return el.currentStyle[prop] ? el.currentStyle[prop] : null;
        }
        return this;
    }
}

var size = $(window).width();


$(document).ready(function(){
  	// We only want to target images / links with a
		$('.lightbox-img').addClass("let-there-be-light");
  	lightboxInit();
});


function lightboxInit() {

  $('.let-there-be-light').click(function(e){
    var positiontop= $(document).scrollTop();
    if(Modernizr.mq && parseInt(size)>45)
    {
      e.preventDefault();
      var $thisHref = $(this).attr('href');
      buildLightBox($thisHref,positiontop);
    }
  });
}

function buildLightBox(src, positiontop) {
	var height = $(document).height();
		$('<div class="lightbox">').appendTo('body').height(height).html('<div class="lightbox__item"><img src="'+src+'" alt="" />');

	$('body').on('click','.lightbox',function(e) {
	$('.lightbox').remove();
  });
}

$(window).resize(function() {
    size = window.getComputedStyle(document.body,':after').getPropertyValue('content');
});


});