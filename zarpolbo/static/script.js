$("#search-form").on('submit', function (e) {
    e.preventDefault();
    search();
});

$(".tt-susggestion").on('click', function (e) {
    e.preventDefault();
    search();
});

function search() {
    $this = $("#search-form");
    $.get($this.prop('action'), $this.serialize(), function (data) {

        $("#container").empty();
        for (cafe of data) {
            $("#container").append(`
                    <h1 class="text">${cafe.fields.name}</h1>
                    <img src="${cafe.fields.main_image_url}" alt="Avatar" class="image">
                    <div class="middle">
                    <div class="h-text">${cafe.fields.description}</div>
                    </div>
                    <br/>
                `);
        }

        $("#mapp").empty();
        loadMap(data);

    }, "json");
}

function loadMap(data)
{
    var latSum = 0, lngSum = 0, cnt = 0;

    for (cafe of data)
    {
        latSum += cafe.fields.latitude;
        lngSum += cafe.fields.longitude;
        cnt++;
    }

    var locations = [];
    for (cafe of data)
        locations.push([cafe.fields.name, cafe.fields.latitude, cafe.fields.longitude]);

    var map = new google.maps.Map(document.getElementById('mapp'), {
        zoom: 10,
        center: new google.maps.LatLng(latSum / cnt, lngSum / cnt),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map
        });

        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
        })(marker, i));
    }
}