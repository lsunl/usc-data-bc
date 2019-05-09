// from data.js
var tableData = data;


// use d3 for selections
var tbody = d3.select("tbody");
var filterButton = d3.select("#filter-btn");
var allButton = d3.select("#all-btn");


// append each row of data to create table
tableData.forEach(ufo => {
  console.log(ufo);
  var row = tbody.append("tr");
  Object.entries(ufo).forEach(([key, value]) => {
    console.log(key, value);
    var cell = tbody.append("td");
      cell.text(value);
    });
  });


// button to display all data
allButton.on("click", () => {
  d3.event.preventDefault();
  tableData.forEach(ufo => {
    console.log(ufo);
    var row = tbody.append("tr");

  Object.entries(ufo).forEach(([key, value]) => {
    console.log(key, value);
    var cell = tbody.append("td");
      cell.text(value);
    });
  });
});


// event listener to filter data by date
filterButton.on("click", () => {

  d3.event.preventDefault();

  var row = d3.select("tbody").selectAll("td");
  row.remove();

  var inputDate = d3.select("#datetime");
  var inputValue = inputDate.property("value");
  console.log(inputValue);

  var filteredData = tableData.filter( tableData => tableData.datetime === inputValue);
  console.log(filteredData)

  filteredData.forEach(ufo => {
    console.log(ufo);
    var row = tbody.append("tr");

  Object.entries(ufo).forEach(([key, value]) => {
    console.log(key, value);
    var cell = tbody.append("td");
      cell.text(value);
});
});
});
