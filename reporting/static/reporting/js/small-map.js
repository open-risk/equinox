const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

const smallMap = L.map('map')

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: attribution}).addTo(smallMap);
const geodata = JSON.parse(document.getElementById('geodata').textContent);

let feature = L.geoJSON(geodata).bindPopup(function (layer) {
}).addTo(smallMap);

function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.nuts_id) {
        layer.bindPopup(feature.properties.nuts_id);
    }
}

L.geoJSON(geodata, {
    onEachFeature: onEachFeature
}).addTo(smallMap);

smallMap.fitBounds(feature.getBounds(), {padding: [100, 100]});