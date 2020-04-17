/**
 * The idea for this code was referenced from testing Lukasz Suaresz site https://django-tech-ecommerce-app.herokuapp.com/
 */

$(document).ready(function () {
  const messages = $('#messages');
  if (messages.length > 0) {
    setTimeout(function () {
      messages.css('display', 'none');
    }, 4000);
  }
});
/**
 * Goodbean location in Footer
 */
    function initMap() {
        {
            const goodbean = {
                lat: 52.664292,
                lng: -8.627918,
            };
            const map = new google.maps.Map(document.getElementById('map'), {
                zoom: 4,
                center: goodbean,
            });
            const marker = new google.maps.Marker({
                position: goodbean,
                map: map,
            });
        }
    }

/**
 * Disable search bar until user inputs a key
 */

$(function () {
        $('#searchinput').keyup(function () {
            if ($(this).val() == '') {
                $('.enableOnInput').prop('disabled', true);
            } else {
                $('.enableOnInput').prop('disabled', false);
            }
        });
    });