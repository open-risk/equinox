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

function pointToLayer(feature, latlng) {
  let radius = feature.properties.radius || 10;

  return L.circleMarker(latlng, {
    radius: radius,
    fillColor: 'orange',
    color: 'white',
    weight: 2,
    opacity: 1,
    fillOpacity: 0.8
  });
}

function onEachFeature(feature, layer) {

    if (feature.properties && feature.properties.nuts_id) {
        layer.bindPopup(feature.properties.nuts_id);
    }
    if (feature.properties && feature.properties.operator) {

        let name = feature.properties.datacenter_name.toString();
        let popupContent = '<a href=" ' + feature.properties.local_url + ' ">' + name + '</a>';
        layer.bindPopup(popupContent);
    }
}

let feature = L.geoJSON(geodata, {
    pointToLayer: pointToLayer,
    onEachFeature: onEachFeature
}).addTo(smallMap);

smallMap.fitBounds(feature.getBounds(), {padding: [100, 100]});