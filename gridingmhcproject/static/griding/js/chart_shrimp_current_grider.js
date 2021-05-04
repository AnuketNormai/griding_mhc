$(document).ready(function () {
    var endpoint = "api/shrimp_current_grider";
    var current = [];
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        current = data.shrimp_current_grider; //api_shrimp_current_grider.py

        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartcurrentshrimpgriderMHC2", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "currentshrimpgrider": "MY-1",
              "valcurrentshrimpgrider": current[0]
            }, {
              "currentshrimpgrider": "MY-2",
              "valcurrentshrimpgrider": current[1]
            }, {
              "currentshrimpgrider": "MY-3",
              "valcurrentshrimpgrider": current[2]
            }, {
              "currentshrimpgrider": "MY-4",
              "valcurrentshrimpgrider": current[3]
            }, {
              "currentshrimpgrider": "MY-5",
              "valcurrentshrimpgrider": current[4]
            }, {
              "currentshrimpgrider": "MY-6",
              "valcurrentshrimpgrider": current[5]
            }, {
              "currentshrimpgrider": "MY-7",
              "valcurrentshrimpgrider": current[6]
            }, {
              "currentshrimpgrider": "MY-8",
              "valcurrentshrimpgrider": current[7]
            }, {
              "currentshrimpgrider": "MY-9",
              "valcurrentshrimpgrider": current[8]
            }, {
              "currentshrimpgrider": "MY-10",
              "valcurrentshrimpgrider": current[9]
            }, {
              "currentshrimpgrider": "MY-11",
              "valcurrentshrimpgrider": current[10]
            }, {
              "currentshrimpgrider": "MY-12",
              "valcurrentshrimpgrider": current[11]
            }, {
              "currentshrimpgrider": "AT6-1",
              "valcurrentshrimpgrider": current[12]
            }, {
              "currentshrimpgrider": "AT6-2",
              "valcurrentshrimpgrider": current[13]
            }, {
              "currentshrimpgrider": "AT6-3",
              "valcurrentshrimpgrider": current[14]
            }, {
              "currentshrimpgrider": "AT6-4",
              "valcurrentshrimpgrider": current[15]
            }, {
              "currentshrimpgrider": "HM-MY",
              "valcurrentshrimpgrider": current[16]
            }
          ];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "currentshrimpgrider";
            categoryAxis.renderer.labels.template.rotation = 270;
            categoryAxis.renderer.labels.template.hideOversized = false;
            categoryAxis.renderer.minGridDistance = 20;
            categoryAxis.renderer.labels.template.horizontalCenter = "right";
            categoryAxis.renderer.labels.template.verticalCenter = "middle";
            categoryAxis.tooltip.label.rotation = 270;
            categoryAxis.tooltip.label.horizontalCenter = "right";
            categoryAxis.tooltip.label.verticalCenter = "middle";
            
            let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
            valueAxis.title.text = "กระแสไฟฟ้าฺ grider (แอมป์)";
            valueAxis.title.fontWeight = "bold";
            
            // Create series
            var series = chart.series.push(new am4charts.ColumnSeries3D());
            series.dataFields.valueY = "valcurrentshrimpgrider";
            series.dataFields.categoryX = "currentshrimpgrider";
            series.name = "valcurrentshrimpgrider";
            series.tooltipText = "{categoryX}: [bold]{valueY} Amp[/]";
            series.columns.template.fillOpacity = .8;
            
            var columnTemplate = series.columns.template;
            columnTemplate.strokeWidth = 2;
            columnTemplate.strokeOpacity = 1;
            columnTemplate.stroke = am4core.color("#FFFFFF");
            
            columnTemplate.adapter.add("fill", function(fill, target) {
              return chart.colors.getIndex(target.dataItem.index);
            })
            
            columnTemplate.adapter.add("stroke", function(stroke, target) {
              return chart.colors.getIndex(target.dataItem.index);
            })
            
            chart.cursor = new am4charts.XYCursor();
            chart.cursor.lineX.strokeOpacity = 0;
            chart.cursor.lineY.strokeOpacity = 0;
            
            }); // end am4core.ready()
 
    },
    error: function (error_data) {
        console.log("error");
        console.log(error_data);
    },
    });

  });
  