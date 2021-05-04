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
          am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            am4core.disposeAllCharts();
            // Themes end
            
            
            
            // Create chart instance
            var chart = am4core.create("chartloadMY11", am4charts.RadarChart);
            
            // Add data
            chart.data = [{
              "category": labels[0],
              "value": normalload[10],
              "full": 100
            }, {
              "category": labels[1],
              "value": lightload[10],
              "full": 100
            }, {
              "category": labels[2],
              "value": noload[10],
              "full": 100
            }, {
              "category": labels[3],
              "value": offline[10],
              "full": 100
            }];
            
            // Make chart not full circle
            chart.startAngle = -90;
            chart.endAngle = 180;
            chart.innerRadius = am4core.percent(20);
            
            // Set number format
            chart.numberFormatter.numberFormat = "#.#'%'";
            
            // Create axes
            var categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "category";
            categoryAxis.renderer.grid.template.location = 0;
            categoryAxis.renderer.grid.template.strokeOpacity = 0;
            categoryAxis.renderer.labels.template.horizontalCenter = "right";
            categoryAxis.renderer.labels.template.fontWeight = 500;
            categoryAxis.renderer.labels.template.adapter.add("fill", function(fill, target) {
              return (target.dataItem.index >= 0) ? chart.colors.getIndex(target.dataItem.index) : fill;
            });
            categoryAxis.renderer.minGridDistance = 10;
            
            var valueAxis = chart.xAxes.push(new am4charts.ValueAxis());
            valueAxis.renderer.grid.template.strokeOpacity = 0;
            valueAxis.min = 0;
            valueAxis.max = 100;
            valueAxis.strictMinMax = true;
            
            // Create series
            var series1 = chart.series.push(new am4charts.RadarColumnSeries());
            series1.dataFields.valueX = "full";
            series1.dataFields.categoryY = "category";
            series1.clustered = false;
            series1.columns.template.fill = new am4core.InterfaceColorSet().getFor("alternativeBackground");
            series1.columns.template.fillOpacity = 0.08;
            series1.columns.template.cornerRadiusTopLeft = 20;
            series1.columns.template.strokeWidth = 0;
            series1.columns.template.radarColumn.cornerRadius = 20;
            
            var series2 = chart.series.push(new am4charts.RadarColumnSeries());
            series2.dataFields.valueX = "value";
            series2.dataFields.categoryY = "category";
            series2.clustered = false;
            series2.columns.template.strokeWidth = 0;
            series2.columns.template.tooltipText = "{category}: [bold]{value}[/]";
            series2.columns.template.radarColumn.cornerRadius = 20;
            
            series2.columns.template.adapter.add("fill", function(fill, target) {
              return chart.colors.getIndex(target.dataItem.index);
            });
            
            // Add cursor
            chart.cursor = new am4charts.RadarCursor();
            
            }); // end am4core.ready()
          
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
      });
    }, 60000); 
  });
  