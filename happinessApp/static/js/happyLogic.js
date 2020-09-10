$(function() {
  $.ajax({
    type: "GET",
    url: "/calculatescore",
    success: function(data){
      var newData =  parseTableData(data)
      generateTable(newData)
    }
  });
});


// // Create a map object
// var myMap = L.map("map", {
//   center: [0, -0],
//   zoom: 1.25
// });

// L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//   attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: API_KEY
// }).addTo(myMap);

// var darkmap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//   attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//   maxZoom: 18,
//   id: 'mapbox/light-v10',
//   tileSize: 512,
//   zoomOffset: -1,
//   accessToken: API_KEY
//   }).addTo(myMap);


// //Read in Results JSON
// d3.json("happyMapTestJSON.json").then (results =>{
//     var lat = Object.values(results.latitude);
//     var long = Object.values(results.longitude);
//     var countryname = Object.values(results.countryName);
//     var happyIndex = Object.values(results.happinessRating);
//     console.log(lat,long,countryname,happyIndex);


//     // Loop through the Results Object and create one marker for each country
//       Object.entries(results).forEach(([key, value]) => {

//       var lat = results.latitude[1];
//       var long = results.longitude[1];
//       var country = results.countryName[1]
//       var rating = results.happinessRating[1]
//       console.log(lat, long, country,rating);

//       L.circle(lat, long, {
//         fillOpacity: 0.90,
//         color: '#a2edff',
//         fillColor: 'rgb(178,67,182)',
//         radius: 500000
//       }).bindPopup("<h2>" + country + "</h2> <hr> <h3>Happiness Index: " + rating + "</h3>").addTo(myMap);
//           });



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
