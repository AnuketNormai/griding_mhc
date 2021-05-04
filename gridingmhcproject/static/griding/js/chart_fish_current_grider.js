$(document).ready(function () {
    var endpoint = "api/fish_current_grider";
    var current = [];
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        current = data.fish_current_grider; //api_fish_current_grider.py

        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartcurrentfishgriderMHC1", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "currentfishgrider": "MY-1",
              "valcurrentfishgrider": current[0]
            }, {
              "currentfishgrider": "MY-2",
              "valcurrentfishgrider": current[1]
            }, {
              "currentfishgrider": "WD-1",
              "valcurrentfishgrider": current[2]
            }, {
              "currentfishgrider": "WD-2",
              "valcurrentfishgrider": current[3]
            }, {
              "currentfishgrider": "HM-3",
              "valcurrentfishgrider": current[4]
            }, {
              "currentfishgrider": "HM-6",
              "valcurrentfishgrider": current[5]
            }
          ];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "currentfishgrider";
            categoryAxis.renderer.labels.template.rotation = 270;
            categoryAxis.renderer.labels.template.hideOversized = false;
            categoryAxis.renderer.minGridDistance = 20;
            categoryAxis.renderer.labels.template.horizontalCenter = "right";
            categoryAxis.renderer.labels.template.verticalCenter = "middle";
            categoryAxis.tooltip.label.rotation = 270;
            categoryAxis.tooltip.label.horizontalCenter = "right";
            categoryAxis.tooltip.label.verticalCenter = "middle";
            
            let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
            valueAxis.title.text = "กระแสไฟฟ้าเครื่องบด (แอมป์)";
            valueAxis.title.fontWeight = "bold";
            
            // Create series
            var series = chart.series.push(new am4charts.ColumnSeries3D());
            series.dataFields.valueY = "valcurrentfishgrider";
            series.dataFields.categoryX = "currentfishgrider";
            series.name = "valcurrentfishgrider";
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
              var chart = am4core.create("chartcurrentfishgriderMHC2", am4charts.XYChart3D);
              
              // Add data
              chart.data = [{
                "currentfishgrider": "HM-20",
                "valcurrentfishgrider": current[6]
              },{
                "currentfishgrider": "AP6-1",
                "valcurrentfishgrider": current[7]
              }, {
                "currentfishgrider": "AP6-2",
                "valcurrentfishgrider": current[8]
              }, {
                "currentfishgrider": "AP6-3",
                "valcurrentfishgrider": current[9]
              }, {
                "currentfishgrider": "AP6-4",
                "valcurrentfishgrider": current[10]
              }, {
                "currentfishgrider": "AP6-5",
                "valcurrentfishgrider": current[11]
              },{
                "currentfishgrider": "AP6-6",
                "valcurrentfishgrider": current[12]  
              },{
                  "currentfishgrider": "MY-7",
                  "valcurrentfishgrider": current[13]  
              },{
                  "currentfishgrider": "MY-8",
                  "valcurrentfishgrider": current[14]  
              }
            ];
              
              // Create axes
              let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
              categoryAxis.dataFields.category = "currentfishgrider";
              categoryAxis.renderer.labels.template.rotation = 270;
              categoryAxis.renderer.labels.template.hideOversized = false;
              categoryAxis.renderer.minGridDistance = 20;
              categoryAxis.renderer.labels.template.horizontalCenter = "right";
              categoryAxis.renderer.labels.template.verticalCenter = "middle";
              categoryAxis.tooltip.label.rotation = 270;
              categoryAxis.tooltip.label.horizontalCenter = "right";
              categoryAxis.tooltip.label.verticalCenter = "middle";
              
              let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
              valueAxis.title.text = "กระแสไฟฟ้าเครื่องบด (แอมป์)";
              valueAxis.title.fontWeight = "bold";
              
              // Create series
              var series = chart.series.push(new am4charts.ColumnSeries3D());
              series.dataFields.valueY = "valcurrentfishgrider";
              series.dataFields.categoryX = "currentfishgrider";
              series.name = "valcurrentfishgrider";
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
  