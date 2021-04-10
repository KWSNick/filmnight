$('.card-img-top').first().ready(function(){
   let imageHeight = $('.card-img-top').first().height();
   $('.card-info').height(imageHeight);

   $('.right').click(function() {
      $(this).parent().siblings('.horz_scroll').animate({
         scrollLeft: "+=500"
      })
   });

   $('.left').click(function() {
      $(this).parent().siblings('.horz_scroll').animate({
         scrollLeft: "-=500"
      })
   });
   
   $('.home').click(function() {
      $(this).parent().siblings('.horz_scroll').animate({
         scrollLeft: "=0"
      })
   });
});