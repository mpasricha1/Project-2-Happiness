$(function() {
  $.ajax({
    type: "GET",
    url: "/calculatescore",
    success: function(data){
      var newData =  parseTableData(data)
      generateTable(newData)
      createMap(data)
    }
  });
});

function createMap(data) {
  console.log(data)
  // Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "light-v10",
    accessToken: "pk.eyJ1IjoibWZtNTEwNSIsImEiOiJja2VhaXlsY20wMTB0MnFvYnBlYnBxb28wIn0.URAgQMLtdtlVGg4APwqb0w"
  });
  // Create a baseMaps object to hold the lightmap layer
  var baseMaps = {
  "Light Map": lightmap
  };
  // Create an overlayMaps object to hold the map layer
  var overlayMaps = {
    "countries": data
  };

  // Create the map object with options
  var map = L.map("map", {
    center: [40.73, -74.0059],
    zoom: 12,
    layers: [lightmap, data]
  });
  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);

  // Initialize an array to hold  markers
  var mapMarkers = [];

  // Loop through the stations array
  
  data.forEach(function(row){
    
    var country={
    location: [row.latitude, row.longitude],
    name: [row.countryname],
    gdp: [row.gdppercapita]
    }
    mapMarkers.push(country)
  })
console.log(mapMarkers)
 // Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
// for (var i = 0; i < mapMarkers.length; i++) {
//   var country = mapMarkers[i];
//   L.marker(city.location)
//     .bindPopup("<h1>" + country.countryname + "</h1> <hr> <h3>Population " + country.gdp + "</h3>")
//     .addTo(myMap);

// }
}



////////////////////////////////////////////////////////////////////////////////////////////////////////////

 //Attempting to use Mark's function to pull the table
function generateTable(data){ 
    var tbody = d3.select("tbody");
    $("#tablebody tr").remove();
    data.forEach(function(results){
      var row = tbody.append("tr"); 
      Object.entries(results).forEach(function([key,value]){
        var cell = row.append("td"); 
        cell.text(value);
      });
    });

};

function parseTableData(data){ 
  var returnList = []
    data.forEach(function(row){
      var country = {
        "country": row.country, 
        "gdp": row.gdp, 
        "generosity": row.generosity, 
        "healthgrade": row.healthgrade, 
        "lifechoice": row.lifechoice, 
        "social": row.social, 
        "lifeexp": row.lifeexp, 
        "corruption": row.corruption, 
        "beer": row.beer, 
        "wine": row.wine, 
        "spirits": row.spirits, 
        "marymed": row.marymed, 
        "maryrec": row.maryrec, 
        "sports": row.sports, 
        "work": row.work
      }
      returnList.push(country)
    }); 
  return returnList
}
