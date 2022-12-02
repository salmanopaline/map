const copy =
    "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 5 });
map.locate()
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([0, 0], 5));
map.fitWorld();

async function load_markers() {
    const markers_url = `/api/markers/?in_bbox=${map.getBounds().toBBoxString()}`;
    console.log("NOTE: " + markers_url);
    const response = await fetch(markers_url);
    const geojson = await response.json();
    //const geotext = await response.text();
    console.log("geojson: " + geojson);
    //console.log("geotext: " + geotext);
    return geojson;
}

async function render_markers() {
    //const markers = await load_markers();
    //L.marker([29.0, 62.0]).addTo(map);
    //L.GeoJSON(markers).bindPopup((layer) => layer.feature.properties.name.toString()).addTo(map);
}

function render_point() {
    var np = new L.marker([29.0, 62.0]);
    np.addTo(map);
}

var newp = L.marker();
var popup_info = L.popup();

function onMapClick(e) {
    newp
        .setLatLng(e.latlng)
        .addTo(map);
    popup_info
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);        
}

//map.on("moveend", render_markers);
map.on('click', onMapClick);

