define(['jquery'],function($){
  
  function genMap(mapItem){
    var sw = document.body.clientWidth;
    var bp = 768;
    var mapObj = $('.map--' + mapItem.mapId);

    var staticImgSrc = mapItem.imgSrc;
    var embed = mapItem.embedSrc;

    function buildMap() {
      if(sw >= bp) { //If Large Screen
          if($('.map-container--' + mapItem.mapId).length < 1) { //If map doesn't already exist
            buildEmbed();

          }
      } else {
          if($('.static-img--' + mapItem.mapId).length < 1) { //If static image doesn't exist
            buildStatic();
          }
      }
    };

    function buildEmbed() { //Build iframe view
        if($('.map--container--' + mapItem.mapId).length < 1){
          $('<div class="map-container map--container--' + mapItem.mapId + '"/>').html(embed).prependTo(mapObj);
        }
    };
      
    function buildStatic() { //Build static map
      var mapLink = $('.map-link--' + mapItem.mapId).attr('href');
      var imgObj = $('<img class="static-img static-img--' + mapItem.mapId + '" />').attr('src',staticImgSrc);
       $('<a/>').attr('href',mapLink).html(imgObj).prependTo(mapObj); 
    }

    //kick off the map builder
    buildMap();
  }
  function genMaps(){
    var item = {};
    if(typeof globalSiteSpecificVars.maps!=='undefined' && globalSiteSpecificVars.maps.length > 0){
      for(item in globalSiteSpecificVars.maps){
        genMap(globalSiteSpecificVars.maps[item]);
      } 
    }
  }
  $(document).ready(function(){
    genMaps();
    $(window).resize(function() {
      genMaps();
    });
  });

});