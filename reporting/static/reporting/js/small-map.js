const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

const smallMap = L.map('map')

// Add OSM tile layer (production)
// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
//     {attribution: attribution}).addTo(smallMap);

// Add CartoDB tile layer (development)

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  subdomains: 'abcd',
  maxZoom: 20
}).addTo(smallMap);

const geodata = JSON.parse(document.getElementById('geodata').textContent);

let feature = L.geoJSON(geodata).bindPopup(function (layer) {
}).addTo(smallMap);

function onEachFeature(feature, layer) {

    if (feature.properties && feature.properties.nuts_id) {
        layer.bindPopup(feature.properties.nuts_id);
    }
    if (feature.properties && feature.properties.operator) {
        var name = feature.properties.datacenter_name.toString();
        var popupContent = '<a href=" '+ feature.properties.local_url +' ">' + name + '</a>';
        layer.bindPopup(popupContent);
    }
}

L.geoJSON(geodata, {
    onEachFeature: onEachFeature
}).addTo(smallMap);

smallMap.fitBounds(feature.getBounds(), {padding: [100, 100]});