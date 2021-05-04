$(document).ready(function () {
    var endpoint = "api/fish_temp_grider";
    var temp = [];
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        temp = data.fish_temp_grider; //api_fish_temp_grider.py

        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("charttempfishgriderMHC1", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "tempfishblower": "MY-1",
              "valtempfishblower": temp[0]
            }, {
              "tempfishblower": "MY-2",
              "valtempfishblower": temp[1]
            }, {
              "tempfishblower": "HM-6",
              "valtempfishblower": temp[2]
            }];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "tempfishblower";
            categoryAxis.renderer.labels.template.rotation = 270;
            categoryAxis.renderer.labels.template.hideOversized = false;
            categoryAxis.renderer.minGridDistance = 20;
            categoryAxis.renderer.labels.template.horizontalCenter = "right";
            categoryAxis.renderer.labels.template.verticalCenter = "middle";
            categoryAxis.tooltip.label.rotation = 270;
            categoryAxis.tooltip.label.horizontalCenter = "right";
            categoryAxis.tooltip.label.verticalCenter = "middle";
            
            let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
            valueAxis.title.text = "อุณหภูมิ (องศาเซลเซียส)";
            valueAxis.title.fontWeight = "bold";
            
            // Create series
            var series = chart.series.push(new am4charts.ColumnSeries3D());
            series.dataFields.valueY = "valtempfishblower";
            series.dataFields.categoryX = "tempfishblower";
            series.name = "valtempfishblower";
            series.tooltipText = "{categoryX}: [bold]{valueY} C[/]";
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
              var chart = am4core.create("charttempfishblowerMHC2", am4charts.XYChart3D);
              
              // Add data
              chart.data = [{
                "tempfishblower": "AP6-1",
                "valtempfishblower": temp[3]
              }, {
                "tempfishblower": "AP6-2",
                "valtempfishblower": temp[4]
              }, {
                "tempfishblower": "AP6-3",
                "valtempfishblower": temp[5]
              }, {
                "tempfishblower": "AP6-4",
                "valtempfishblower": temp[6]
              }, {
                "tempfishblower": "AP6-5",
                "valtempfishblower": temp[7]
              },{
                "tempfishblower": "AP6-6",
                "valtempfishblower": temp[8]  
              },{
                  "tempfishblower": "MY-7",
                  "valtempfishblower": temp[9]  
              },{
                "tempfishblower": "MY-8",
                "valtempfishblower": temp[10]  
              },{
                "tempfishblower": "AP-CG",
                "valtempfishblower": temp[11]  
              },{
                "tempfishblower": "HM-20",
                "valtempfishblower": temp[12]  
              }
            ];
              
              // Create axes
              let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
              categoryAxis.dataFields.category = "tempfishblower";
              categoryAxis.renderer.labels.template.rotation = 270;
              categoryAxis.renderer.labels.template.hideOversized = false;
              categoryAxis.renderer.minGridDistance = 20;
              categoryAxis.renderer.labels.template.horizontalCenter = "right";
              categoryAxis.renderer.labels.template.verticalCenter = "middle";
              categoryAxis.tooltip.label.rotation = 270;
              categoryAxis.tooltip.label.horizontalCenter = "right";
              categoryAxis.tooltip.label.verticalCenter = "middle";
              
              let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
              valueAxis.title.text = "อุณหภูมิ (องศาเซลเซียส)";
              valueAxis.title.fontWeight = "bold";
              
              // Create series
              var series = chart.series.push(new am4charts.ColumnSeries3D());
              series.dataFields.valueY = "valtempfishblower";
              series.dataFields.categoryX = "tempfishblower";
              series.name = "valtempfishblower";
              series.tooltipText = "{categoryX}: [bold]{valueY} C[/]";
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
  