$(function() {
$.ajax({
    type: "GET",
    url: "/calculatescore",
    success: function(data){
      console.log(data)
    }
  });
});

// Create a map object
var myMap = L.map("map", {
  center: [0, -0],
  zoom: 1
});

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

var darkmap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox/light-v10',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: API_KEY
  }).addTo(myMap);


//Read in Results JSON
  d3.csv("Country_Reference_Table_LATLONG.csv").then(function(results) {
    console.log(results);
    });


// Define a markerSize function that will give each city a different radius based on its population
// function markerSize(population) {
//   return population / 40;
// }

// Each city object contains the city's name, location and population
var results = [
  {
    name: "Dominican Republic",
    location: [18.735693, -70.162651],
    fitness: 2.5,
    gdp: 1.5,
    region: "Latin America and Caribbean",
    population: 8550405
  },
  {
    name: "Gambia",
    location: [-16.578193, 179.414413],
    region: "Sub-Saharan Africa",
    population: 2720546
  },
  {
    name: "Croatia",
    location: [45.1, 15.2],
    region: "Central and Eastern Europe",
    population: 2296224
  },
];

// Loop through the results array and create one marker for each city object
for (var i = 0; i < results.length; i++) {
  L.circle(results[i].location, {
    fillOpacity: 0.90,
    color: '#a2edff',
    fillColor: 'rgb(178,67,182)',
    // Setting our circle's radius equal to the output of our markerSize function
    // This will make our marker's size proportionate to its population
    // radius: markerSize(results[i].population)
    radius: 500000
  }).bindPopup("<h2>" + results[i].name + "</h2> <hr> <h3>Population: " + results[i].population + "</h3><h3>Fitness Index: " + results[i].fitness + "</h3>").addTo(myMap);
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////

// var values = [
//       ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
//       [1200000, 20000, 80000, 2000, 12120000],
//       [1300000, 20000, 70000, 2000, 130902000],
//       [1300000, 20000, 120000, 2000, 131222000],
//       [1400000, 20000, 90000, 2000, 14102000]]

// for (var i = 0; i < results.length; i++) {
//   var data = [{
//     type: 'table',
//     header: {
//       values: [["<b>COUNTRY</b>"], ["<b>" + results[i].name + "</b>"],
//            ["<b>" + results[i].name + "</b>"], ["<b>" + results[i].name + "</b>"], ["<b>" + results[i].name + "</b>"]],
//       align: ["left", "center"],
//       line: {width: 1, color: '#506784'},
//       // a2edff
//       fill: {color: '#bcffbc'},
//       //#119dff
//       font: {family: "Text", size: 12, color: "black"}
//     },
//     cells: {
//       values: values,
//       align: ["left", "center"],
//       line: {color: "#506784", width: 1},
//       // #506784
//      fill: {color: ['#a2edff', 'white']},
//      //#25fed
//       font: {family: "Arial", size: 11, color: ["#506784"]}
//     }
//   }]
// }
//   Plotly.newPlot('chart', data);

Plotly.d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv", function(err, rows){

  function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
  }

  var headerNames = Plotly.d3.keys(rows[0]);

  var headerValues = [];
  var cellValues = [];
  for (i = 0; i < headerNames.length; i++) {
    headerValue = [headerNames[i]];
    headerValues[i] = headerValue;
    cellValue = unpack(rows, headerNames[i]);
    cellValues[i] = cellValue;
  }

  // clean date
  for (i = 0; i < cellValues[1].length; i++) {
  var dateValue = cellValues[1][i].split(' ')[0]
  cellValues[1][i] = dateValue
  }


var data = [{
  type: 'table',
  columnwidth: [400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400],
  columnorder: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,12,16,17,18,19,20],
  header: {
    values: headerValues,
    align: "center",
    line: {width: 1, color: 'rgb(50, 50, 50)'},
    fill: {color: ['rgb(178,67,182)']},
    font: {family: "Text", size: 12, color: "white"}
  },
  cells: {
    values: cellValues,
    align: ["center", "center"],
    line: {color: "black", width: 1},
    // fill: {color: ['rgba(228, 222, 249, 0.65)','rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']},
    fill: {color: ['#a2edff']},
    font: {family: "Text", size: 9, color: ["black"]}
  }
}]

var layout = {
  title: "Top 5 Countries You Will Be Happiest"
}

Plotly.newPlot('chart', data, layout);
});