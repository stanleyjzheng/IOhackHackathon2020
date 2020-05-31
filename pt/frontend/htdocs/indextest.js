var fs = require('fs');
const data = JSON.parse(fs.readFileSync('./data.json', 'utf8'));

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 51.042417, lng: -114.072527},
    zoom: 13
  });

  var input = document.getElementById('pac-input');

  var autocomplete = new google.maps.places.Autocomplete(input);
  autocomplete.bindTo('bounds', map);

  // Specify just the place data fields that you need.
  autocomplete.setFields(
      ['place_id', 'geometry', 'name', 'formatted_address']);

  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  var infowindow = new google.maps.InfoWindow();
  var infowindowContent = document.getElementById('infowindow-content');
  infowindow.setContent(infowindowContent);

  var marker = new google.maps.Marker({map: map});

  marker.addListener('click', function() {
    infowindow.open(map, marker);
  });

  autocomplete.addListener('place_changed', function() {
    infowindow.close();

    var place = autocomplete.getPlace();

    if (!place.geometry) {
      return;
    }

    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);
    }

    // Set the position of the marker using the place ID and location.
    marker.setPlace({
      placeId: place.place_id,
      location: place.geometry.location
    });

    marker.setVisible(true);

    infowindowContent.children['place-name'].textContent = place.name;
    infowindowContent.children['place-id'].textContent = place.place_id;
    infowindowContent.children['place-address'].textContent =
        place.formatted_address;
    infowindow.open(map, marker);
    //variable
    function record() {
      document.getElementById("search").onclick = function() {
      document.getElementById("select").innerHTML = "Select";
//let userData = data[msg.author.id];
    //perhaps we should print place.place(id)
    data += place.place_id
    fs.appendFile('./data.json', JSON.stringify(data),(err)=>{
      if(err) throw err;
      console.log("saved!")
      });
      //let userData = XP[msg.author.id];
  
  //     console.log(place_id)
  // fs.appendFile('./data.json', JSON.stringify(data), console.error);
}

//writing js file
}
  });

}