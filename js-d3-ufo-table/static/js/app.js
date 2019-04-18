// from data.js
var tableData = data;


// use d3 to select table body
var tbody = d3.select("tbody");
var filterButton = d3.select("#filter-btn");
var allButton = d3.select("#all-btn");
// append each row of data to table

allButton.on("click", function(){
  d3.event.preventDefault();
  tableData.forEach(function(ufo){
    console.log(ufo);
    var row = tbody.append("tr");

    Object.entries(ufo).forEach(function([key, value]) {
      console.log(key, value);
      var cell = tbody.append("td");
        cell.text(value);
    });
  });
});


// add an event listener that will display rows that match the input data when button is clicked

filterButton.on("click", function(){

  d3.event.preventDefault();
  var inputDate = d3.select("#datetime");
  var inputValue = inputDate.property("value");

  tableData.forEach(function(ufo){
    console.log(ufo);
    var row = tbody.append("tr");

    Object.entries(ufo).forEach(function([key, value]) {
      if (value === inputValue){
        console.log(key, value);
        var cell = tbody.append("td");
          cell.text(value);
    };
  });
});
});
