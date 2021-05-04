$(document).ready(function () {
    var endpoint = "api/shrimp_temp_bearingblower";
    var temp = [];
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        temp = data.shrimp_temp_bearingblower; //api_shrimp_temp_bearingblower.py

        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("charttempbearingshrimpblowerMHC2", am4charts.XYChart3D);
            
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
                "blower": "MY3",
                "temp1": temp[4],
                "temp2": temp[5]
            }, {
                "blower": "MY4",
                "temp1": temp[6],
                "temp2": temp[7]
            }, {
                "blower": "MY5",
                "temp1": temp[8],
                "temp2": temp[9]
            }, {
                "blower": "MY6",
                "temp1": temp[10],
                "temp2": temp[11]
            }, {
                "blower": "MY7",
                "temp1": temp[12],
                "temp2": temp[13]
            }, {
                "blower": "MY8",
                "temp1": temp[14],
                "temp2": temp[15]
            }, {
                "blower": "MY9",
                "temp1": 0,
                "temp2": 0
            }, {
                "blower": "MY10",
                "temp1": temp[16],
                "temp2": temp[17]
            }, {
                "blower": "MY11",
                "temp1": temp[18],
                "temp2": temp[19]
            }, {
                "blower": "MY12",
                "temp1": temp[20],
                "temp2": temp[21]
            }, {
                "blower": "AT6-1",
                "temp1": temp[22],
                "temp2": temp[23]
            }, {
                "blower": "AT6-2",
                "temp1": temp[24],
                "temp2": temp[25]
            }, {
                "blower": "AT6-3",
                "temp1": temp[26],
                "temp2": temp[27]
            }, {
                "blower": "AT6-4",
                "temp1": temp[28],
                "temp2": temp[29]
            }
        ];
            
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
  