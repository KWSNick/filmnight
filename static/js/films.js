$(document).ready(function () {
   let imageHeight = $('.card-img-top').first().height();
   $('.card-info').height(imageHeight);

   $('.right').click(function () {
      $(this).parent().siblings('.horz_scroll').animate({
         scrollLeft: "+=500"
      })
   });

   $('.left').click(function () {
      $(this).parent().siblings('.horz_scroll').animate({
         scrollLeft: "-=500"
      })
   });

   $('.home').click(function () {
      $(this).parent().siblings('.horz_scroll').animate({
         scrollLeft: "=0"
      })
   });

   // Bootstrap Modal JS
   let delete_modal = document.getElementById('delete_modal{{ film.id }}')
   let delete_focus = document.getElementById('delete_focus{{ film.id }}')

   delete_modal.addEventListener('shown.bs.modal', function () {
      delete_focus.focus()
   })
});