// This function performs a GET request on the selects url
// All data is returned with no filter 
$(function() {
	$.ajax({
		type: "GET",
		url: "/chorandlinedata",
		success: function(data){
			console.log(data)
		}
	});
});

// This function performs a POST request on the selected url
// a date is required as it passes back to the date to act as
// a filter in the flask route 
$("#posttest").click(function() {
	date = 2019
	$.ajax({
		type: 'POST',
		url: '/scatterdata',
		datatype: 'json',
		data: JSON.stringify(date),
		contentType:"application/json",
		success: function(data){
			getScatterData(data);
		}
	});
});

$(function() {
	date = 2020
	$.ajax({
		type: 'POST',
		url: '/scatterdata',
		datatype: 'json',
		data: JSON.stringify(date),
		contentType:"application/json",
		success: function(data){
			getScatterData(data);
		}
	});
});