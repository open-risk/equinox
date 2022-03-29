const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: attribution}).addTo(map);
const geometry = JSON.parse(document.getElementById('geometry').textContent);
let feature = L.geoJSON(geometry).bindPopup(function (layer) {
    return layer.feature.properties.name;
}).addTo(map);
map.fitBounds(feature.getBounds(), {padding: [100, 100]});

// var map = L.map('map').setView([51.505, -0.09], 13);
//
// const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: attribution}).addTo(map);