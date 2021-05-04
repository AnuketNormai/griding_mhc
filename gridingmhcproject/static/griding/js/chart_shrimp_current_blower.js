$(document).ready(function () {
    var endpoint = "api/shrimp_current_blower";
    var current = [];
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        current = data.shrimp_current_blower; //api_shrimp_current_blower.py

        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartcurrentshrimpblowerMHC2", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "currentshrimpblower": "MY-1",
              "valcurrentshrimpblower": current[0]
            }, {
              "currentshrimpblower": "MY-2",
              "valcurrentshrimpblower": current[1]
            }, {
              "currentshrimpblower": "MY-3",
              "valcurrentshrimpblower": current[2]
            }, {
              "currentshrimpblower": "MY-4",
              "valcurrentshrimpblower": current[3]
            }, {
              "currentshrimpblower": "MY-5",
              "valcurrentshrimpblower": current[4]
            }, {
              "currentshrimpblower": "MY-6",
              "valcurrentshrimpblower": current[5]
            }, {
              "currentshrimpblower": "MY-7",
              "valcurrentshrimpblower": current[6]
            }, {
              "currentshrimpblower": "MY-8",
              "valcurrentshrimpblower": current[7]
            }, {
              "currentshrimpblower": "MY-9",
              "valcurrentshrimpblower": current[8]
            }, {
              "currentshrimpblower": "MY-10",
              "valcurrentshrimpblower": current[9]
            }, {
              "currentshrimpblower": "MY-11",
              "valcurrentshrimpblower": current[10]
            }, {
              "currentshrimpblower": "MY-12",
              "valcurrentshrimpblower": current[11]
            }, {
              "currentshrimpblower": "AT6-1",
              "valcurrentshrimpblower": current[12]
            }, {
              "currentshrimpblower": "AT6-2",
              "valcurrentshrimpblower": current[13]
            }, {
              "currentshrimpblower": "AT6-3",
              "valcurrentshrimpblower": current[14]
            }, {
              "currentshrimpblower": "AT6-4",
              "valcurrentshrimpblower": current[15]
            }, {
              "currentshrimpblower": "HM-2(CG)",
              "valcurrentshrimpblower": current[16]
            }, {
              "currentshrimpblower": "HM-MY",
              "valcurrentshrimpblower": current[17]
            }
          ];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "currentshrimpblower";
            categoryAxis.renderer.labels.template.rotation = 270;
            categoryAxis.renderer.labels.template.hideOversized = false;
            categoryAxis.renderer.minGridDistance = 20;
            categoryAxis.renderer.labels.template.horizontalCenter = "right";
            categoryAxis.renderer.labels.template.verticalCenter = "middle";
            categoryAxis.tooltip.label.rotation = 270;
            categoryAxis.tooltip.label.horizontalCenter = "right";
            categoryAxis.tooltip.label.verticalCenter = "middle";
            
            let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
            valueAxis.title.text = "กระแสไฟฟ้าฺ Blower (แอมป์)";
            valueAxis.title.fontWeight = "bold";
            
            // Create series
            var series = chart.series.push(new am4charts.ColumnSeries3D());
            series.dataFields.valueY = "valcurrentshrimpblower";
            series.dataFields.categoryX = "currentshrimpblower";
            series.name = "valcurrentshrimpblower";
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
  