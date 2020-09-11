
$(function() {
    date = 2020
    $.ajax({
        type: 'POST',
        url: '/scatterdata',
        datatype: 'json',
        data: JSON.stringify(date),
        contentType:"application/json",
        success: function(data){
            dropdownMenu = "GDP"
            getScatterData(data, dropdownMenu);

        }
    });
});
$(function() {
    $.ajax({
        type: 'GET',
        url: '/linedata',
        datatype: 'json',
        contentType:"application/json",
        success: function(data){
            getlineData(data);
        }
    });
});
function getScatterData(data, dropdownMenu){

  $('#factorlist a').on('click', function(){
    var dropdownMenu = $(this).text();
    getScatterData(data,dropdownMenu)

});
 var column_number=0
 var x_axis_title=""
    if (dropdownMenu=="GDP"){
        column_number= 3
        x_axis_title="GDP"
    }
    if (dropdownMenu=="Social Support"){
        column_number= 4
        x_axis_title="Social Support"
    }
    if (dropdownMenu=="Health Life Expectancy"){
        column_number= 5
        x_axis_title="Health Life Expectancy"
    }
    if (dropdownMenu=="Freedom Life"){
        column_number= 6
        x_axis_title="Freedom Life"
    }
    if (dropdownMenu=="Generosity"){
        column_number= 7
        x_axis_title="Generosity"
    }
    if (dropdownMenu=="Perception of Corruption"){
        column_number= 8
        x_axis_title="Perception of Corruption"
    }
    data.forEach(function(data){
        data[column_number]=+data[column_number]
        data[5]=+data[5]
        data[10]=+data[10]
    });    
//
    x_axis=data.map(function(row){
        return row[column_number]

    });
    console.log(x_axis)
//rating
    y_axis=data.map(function(row){
        return row[2]
    });
    console.log(y_axis)
    var region=data.map(function(row){
        return row[1]
    });

    var trace1 = {
        x: x_axis,
        y: y_axis,
        type: "scatter",
        mode: "markers",
        marker:{
            size:20,
        },
        transforms: [{
            type: 'groupby',
            groups: region,
            styles:[
                {target: 'Central and Eastern Europe', value: {marker: {color: 'rgb(71,212,196'}}},
                {target: 'Western Europe', value: {marker: {color: 'rgb(152,222,243'}}},
                {target: 'Latin America and Caribbean', value: {marker: {color: 'rgb(243,99,177'}}},
                {target: 'North America', value: {marker: {color: 'rgb(255,218,193'}}},
                {target: 'Middle East and North Africa', value: {marker: {color: 'rgb(178,67,182)'}}},
                {target: 'East Asia', value: {marker: {color: 'rgb(253,191,59'}}},
                {target: 'Southeast Asia', value: {marker: {color: 'rgb(159,228,129'}}},
                {target: 'Australia and New Zealand', value: {marker: {color: 'rgb(250,175,165'}}},
                {target: 'Commonwealth of Independent States', value: {marker: {color: 'rgb(220,149,221'}}},
                {target: 'Sub-Saharan Africa', value: {marker: {color: 'rgb(247,245,112'}}},
                {target: 'South Pacific', value: {marker: {color: 'rgb(38,163,199'}}}

    
            ]
          }]
      };

  var layout = {
    title: `Health Life Happiness v. ${x_axis_title} ${data[1][10]}`,
    font:{
        family: 'Courier New', 
        size:16,
    },
    yaxis: { title: "Happiness Rating"},
        font:{
            family:'Courier New',
            size:12
        },
    xaxis: { title: `${x_axis_title}`},
        font: {
            family: 'Courier New',
            size:12,
        }
  };

  Plotly.newPlot("plot", [trace1],layout);
    
    
};
//line
function getlineData(data){
    console.log(data);
    data.forEach(function(data){
        data[1]=+data[1]
        data[2]=+data[2]
    }); 
    x_axis=data.map(function(row){
        return row[2]

    });

    y_axis=data.map(function(row){
        return row[1]
    });

    var region=data.map(function(row){
        return row[0]
    });

    var trace1 = {
        x: [2016,2017,2018,2019,2020],
        y: [5.38,5.354,5.375,5.407,5.473],
        type: "scatter"
        // mode: "lines",
       // fill: 'tozeroy',
        // transforms: [{
        //     type: 'groupby',
        //     groups: y_axis
        // }]
      }

  var layout = {
    title: 'Happiness Rating Over the Years',
    font:{
        family: 'Courier New', 
        size:16,
    },
    yaxis: { title: "Happiness Rating"},
        font:{
            family:'Courier New',
            size:12
        },
    xaxis: { title: "year"},
        font: {
            family: 'Courier New',
            size:12,
        }
  };

  Plotly.newPlot("line", [trace1],layout);
    
    
}
