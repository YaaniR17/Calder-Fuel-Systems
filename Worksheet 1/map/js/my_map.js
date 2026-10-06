var map = L.map('map').setView([53.71109,-1.871979], 10);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var marker = L.marker([53.702677, -1.853486],
	{title: 'salterhebble'}).addTo(map);
