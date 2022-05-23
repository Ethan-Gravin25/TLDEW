const apiKey = 'pk.eyJ1IjoibGp4b3ZlcjI0OCIsImEiOiJjbDNldzI4b3QwOXlsM2puOHN2ZnJybmZoIn0.uDffgCcteIELi1wN-fOyEg';

<!--Beginning view coordinates, and zoom level-->
const mymap = L.map('map').setView([32.7157, 117.1611], 13);

<!--Map informtion and settings-->
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: apiKey
}).addTo(mymap);

// Adding Marker

const marker = L.marker([40.748708, -73.985433]).addTo(mymap);

// Add popup message
let template = `
<h3>Empire State Building</h3>
<div style="text-align:center">
    <img width="150" height="150"src="image.jpg"/>
</div>
`
marker.bindPopup(template);

// Add circle

const circle = L.circle([40.748708, -73.985433], {
    radius:500,
    color: 'green',
    fillColor: 'red',
    fillOpacity:0.2
}).addTo(mymap).bindPopup('I am a circle')

// Add Polygon

const polygon = L.polygon([

    [40.73618, -73.97545],
    [40.731497, -73.974342],
    [40.729324, -73.972234],
    [40.732368, -73.981293],
], {
    color:'blue',
    fillColor:'blue',
    fillOpacity:0.2
}).addTo(mymap).bindPopup(' I am a polygon')

// polygon.bindPopup(' I am a polygon')