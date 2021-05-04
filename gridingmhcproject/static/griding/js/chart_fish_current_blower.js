$(document).ready(function () {
    var endpoint = "api/fish_current_blower";
    var current = [];
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        current = data.fish_current_blower; //api_fish_current_blower.py

        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartcurrentfishblowerMHC1", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "currentfishblower": "MY-1",
              "valcurrentfishblower": current[0]
            }, {
              "currentfishblower": "MY-2",
              "valcurrentfishblower": current[1]
            }, {
              "currentfishblower": "WD-1",
              "valcurrentfishblower": current[2]
            }, {
              "currentfishblower": "WD-2",
              "valcurrentfishblower": current[3]
            }, {
              "currentfishblower": "HM-3",
              "valcurrentfishblower": current[4]
            }, {
              "currentfishblower": "HM-6",
              "valcurrentfishblower": current[5]
            }
          ];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "currentfishblower";
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
            series.dataFields.valueY = "valcurrentfishblower";
            series.dataFields.categoryX = "currentfishblower";
            series.name = "valcurrentfishblower";
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


            am4core.ready(function() {

              // Themes begin
              am4core.useTheme(am4themes_animated);
              // Themes end
              
              // Create chart instance
              var chart = am4core.create("chartcurrentfishblowerMHC2", am4charts.XYChart3D);
              
              // Add data
              chart.data = [{
                "currentfishblower": "AP6-1",
                "valcurrentfishblower": current[6]
              }, {
                "currentfishblower": "AP6-2",
                "valcurrentfishblower": current[7]
              }, {
                "currentfishblower": "AP6-3",
                "valcurrentfishblower": current[8]
              }, {
                "currentfishblower": "AP6-4",
                "valcurrentfishblower": current[9]
              }, {
                "currentfishblower": "AP6-5",
                "valcurrentfishblower": current[10]
              },{
                "currentfishblower": "AP6-6",
                "valcurrentfishblower": current[11]  
              },{
                  "currentfishblower": "AP6-CG",
                  "valcurrentfishblower": current[12]  
              }
            ];
              
              // Create axes
              let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
              categoryAxis.dataFields.category = "currentfishblower";
              categoryAxis.renderer.labels.template.rotation = 270;
              categoryAxis.renderer.labels.template.hideOversized = false;
              categoryAxis.renderer.minGridDistance = 20;
              categoryAxis.renderer.labels.template.horizontalCenter = "right";
              categoryAxis.renderer.labels.template.verticalCenter = "middle";
              categoryAxis.tooltip.label.rotation = 270;
              categoryAxis.tooltip.label.horizontalCenter = "right";
              categoryAxis.tooltip.label.verticalCenter = "middle";
              
              let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
              valueAxis.title.text = "กระแสไฟฟ้า Blower (แอมป์)";
              valueAxis.title.fontWeight = "bold";
              
              // Create series
              var series = chart.series.push(new am4charts.ColumnSeries3D());
              series.dataFields.valueY = "valcurrentfishblower";
              series.dataFields.categoryX = "currentfishblower";
              series.name = "valcurrentfishblower";
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
  