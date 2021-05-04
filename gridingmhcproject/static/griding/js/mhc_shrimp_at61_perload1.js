$(document).ready(function () {

  var endpoint = "/api/data";
  var normalload = [];
  var lightload = [];
  var noload = [];
  var offline = [];
  var labels = [];

  setInterval(function () {
    $.ajax({
      method: "GET",
      url: endpoint,
      success: function (data) {
        labels = data.labels;
        normalload = data.normalload; //from views.py
        lightload = data.lightload; //from views.py
        noload = data.noload; //from views.py
        offline = data.offline //from views.py

        //start amchart 
        am4core.ready(function () {
          // Themes begin
          am4core.useTheme(am4themes_animated);
          // Themes end
      
          // Create chart instance
          var chart = am4core.create("chartPercentLoadShrimpAT61", am4charts.PieChart);
      
          // Add and configure Series
          var pieSeries = chart.series.push(new am4charts.PieSeries());
          pieSeries.dataFields.value = "percent";
          pieSeries.dataFields.category = "Load";
      
          // Let's cut a hole in our Pie chart the size of 30% the radius
          chart.innerRadius = am4core.percent(30);
      
          // Put a thick white border around each Slice
          pieSeries.slices.template.stroke = am4core.color("#fff");
          pieSeries.slices.template.strokeWidth = 2;
          pieSeries.slices.template.strokeOpacity = 1;
          // change the cursor on hover to make it apparent the object can be interacted with
          pieSeries.slices.template.cursorOverStyle = [
            {
              property: "cursor",
              value: "pointer",
            },
          ];
      
          pieSeries.alignLabels = false;
          pieSeries.labels.template.bent = true;
          pieSeries.labels.template.radius = 3;
          pieSeries.labels.template.padding(0, 0, 0, 0);
      
          pieSeries.ticks.template.disabled = true;
      
          // Create a base filter effect (as if it's not there) for the hover to return to
          var shadow = pieSeries.slices.template.filters.push(
            new am4core.DropShadowFilter()
          );
          shadow.opacity = 0;
      
          // Create hover state
          var hoverState = pieSeries.slices.template.states.getKey("hover"); // normally we have to create the hover state, in this case it already exists
      
          // Slightly shift the shadow and make it more prominent on hover
          var hoverShadow = hoverState.filters.push(new am4core.DropShadowFilter());
          hoverShadow.opacity = 0.7;
          hoverShadow.blur = 5;
      
          // Add a legend
          chart.legend = new am4charts.Legend();
      
          chart.data = [
            {
              Load: labels[0],
              percent: normalload[12],
            },
            {
              Load: labels[1],
              percent: lightload[12],
            },
            {
              Load: labels[2],
              percent: noload[12],
            },
            {
              Load: labels[3],
              percent: offline[12],
            },
          ];
        }); // end am4core.ready()
        
      },
      error: function (error_data) {
        console.log("error");
        console.log(error_data);
      },
    });
  }, 5000); 
});
