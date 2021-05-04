$(document).ready(function () {
    var endpoint = "api/fish_temp_bearingblower";
    var temp = [];
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        temp = data.fish_temp_bearingblower; //api_fish_temp_bearingblower.py

        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("charttempbearingfishblowerMHC1", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
                "blower": "MY1",
                "temp1": temp[0],
                "temp2": temp[1]
            }, {
                "blower": "MY2",
                "temp1": temp[2],
                "temp2": temp[3]
            }, {
                "blower": "HM3",
                "temp1": temp[4],
                "temp2": temp[5]
            }];
            
            // Create axes
            var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "blower";
            categoryAxis.renderer.grid.template.location = 0;
            categoryAxis.renderer.minGridDistance = 30;
            
            var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
            valueAxis.title.text = "อุณหภูมิลูกปืน";
            valueAxis.renderer.labels.template.adapter.add("text", function(text) {
              return text + " C";
            });
            
            // Create series
            var series = chart.series.push(new am4charts.ColumnSeries3D());
            series.dataFields.valueY = "temp1";
            series.dataFields.categoryX = "blower";
            series.name = "Year 2017";
            series.clustered = false;
            series.columns.template.tooltipText = "Temp(1) {categoryX} : [bold]{valueY} C[/]";
            series.columns.template.fillOpacity = 0.9;
            
            var series2 = chart.series.push(new am4charts.ColumnSeries3D());
            series2.dataFields.valueY = "temp2";
            series2.dataFields.categoryX = "blower";
            series2.name = "Year 2018";
            series2.clustered = false;
            series2.columns.template.tooltipText = "Temp(2) {categoryX} : [bold]{valueY} C[/]";
            
            }); // end am4core.ready()

            // MHC----2
            am4core.ready(function() {

                // Themes begin
                am4core.useTheme(am4themes_animated);
                // Themes end
                
                // Create chart instance
                var chart = am4core.create("charttempbearingfishblowerMHC2", am4charts.XYChart3D);
                
                // Add data
                chart.data = [{
                    "blower": "AP6-1",
                    "temp1": temp[6],
                    "temp2": temp[7]
                }, {
                    "blower": "AP6-2",
                    "temp1": temp[8],
                    "temp2": temp[9]
                }, {
                    "blower": "AP6-3",
                    "temp1": temp[10],
                    "temp2": temp[11]
                } ,{
                    "blower": "AP6-4",
                    "temp1": temp[12],
                    "temp2": temp[13]
                } ,{
                    "blower": "AP6-5",
                    "temp1": temp[14],
                    "temp2": temp[15]
                },{
                    "blower": "AP6-6",
                    "temp1": temp[16],
                    "temp2": temp[17]
                },{
                    "blower": "AP6-CG",
                    "temp1": temp[18],
                    "temp2": temp[19]
                },{
                    "blower": "HM-20",
                    "temp1": temp[20],
                    "temp2": temp[21]
                }];
                
                // Create axes
                var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
                categoryAxis.dataFields.category = "blower";
                categoryAxis.renderer.grid.template.location = 0;
                categoryAxis.renderer.minGridDistance = 30;
                
                var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
                valueAxis.title.text = "อุณหภูมิลูกปืน";
                valueAxis.renderer.labels.template.adapter.add("text", function(text) {
                  return text + " C";
                });
                
                // Create series
                var series = chart.series.push(new am4charts.ColumnSeries3D());
                series.dataFields.valueY = "temp1";
                series.dataFields.categoryX = "blower";
                series.name = "Year 2017";
                series.clustered = false;
                series.columns.template.tooltipText = "Temp(1) {categoryX} : [bold]{valueY} C[/]";
                series.columns.template.fillOpacity = 0.9;
                
                var series2 = chart.series.push(new am4charts.ColumnSeries3D());
                series2.dataFields.valueY = "temp2";
                series2.dataFields.categoryX = "blower";
                series2.name = "Year 2018";
                series2.clustered = false;
                series2.columns.template.tooltipText = "Temp(2) {categoryX} : [bold]{valueY} C[/]";
                
                }); // end am4core.ready()
        
    },
    error: function (error_data) {
        console.log("error");
        console.log(error_data);
    },
    });

  });
  