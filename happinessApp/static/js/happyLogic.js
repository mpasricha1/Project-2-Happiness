//loading data
$(function() {
  $.ajax({
    type: "GET",
    url: "/calculatescore",
    success: function(data){
      var newData =  parseTableData(data)
      generateTable(newData)
      placeHeader(data)
      // createMap(data)
    }
  });
});
//creating a map 
function createMap(data) {
  console.log(data)
  // Create the tile layer that will be the background of our map
  var map = L.map("map", {
    center: [40.73, -74.0059],
    zoom: 2,
    // layers: [lightmap, data]
  });

//world map
  var lightmap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: "pk.eyJ1IjoibWZtNTEwNSIsImEiOiJja2VhaXlsY20wMTB0MnFvYnBlYnBxb28wIn0.URAgQMLtdtlVGg4APwqb0w"
  }).addTo(map);

  var baseMaps = {
  light: lightmap
}

  // Initialize an array to hold  markers
  var mapMarkers = [];

  // Loop through 
  
  data.forEach(function(row){
    
    var country={
    location: [row.latitude, row.longitude],
    name: [row.countryname],
    gdp: [row.gdppercapita]
    }
    // mapMarkers.push(country)
//// Loop through the results array and create one marker for each city object
  L.marker(country.location)
    .bindPopup("<h1>" + country.name + "</h1> <hr> <h3>GDP " + country.gdp + "</h3>")
    .addTo(map);
});
    
console.log(mapMarkers)


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
      console.log(row.marymed)
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
  
function placeHeader(data){
  var countryName = data[0].country
  $("#country").text(`Your Ideal Country is ${countryName}`)

}
