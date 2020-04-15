// Make messages close after 4 seconds


$(document).ready(function() {
    setTimeout(function(){document.getElementById('messages').style.display='none';} ,4000);
});


// Goodbean location in Footer

function initMap() {
            {
                const goodbean = {
                    lat: 52.664292,
                    lng: -8.627918
                };

                const map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 4,
                    center: goodbean
                });
                const marker = new google.maps.Marker({
                    position: goodbean,
                    map: map
                });

            }
        }