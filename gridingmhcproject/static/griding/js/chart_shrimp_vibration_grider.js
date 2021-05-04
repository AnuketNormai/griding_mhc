$(document).ready(function () {
    var endpoint = "api/shrimp_vibration_grider";
    var vibration_x = [];
    var vibration_y = [];
    var vibration_z = [];
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        vibration_x = data.shrimp_vibration_x_grider; //api_shrimp_vibration_grider.py
        vibration_y = data.shrimp_vibration_y_grider; //api_shrimp_vibration_grider.py
        vibration_z = data.shrimp_vibration_z_grider; //api_shrimp_vibration_grider.py

        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
             // Create chart instance
            var chart = am4core.create("chartvibrationshrimpgriderMHC2", am4charts.XYChart);
            
            // Add data
            chart.data = [{
              "axis": "X - Axis",
              "val1": vibration_x[0],
              "val2": vibration_x[1],
              "val3": vibration_x[2],
              "val4": vibration_x[3],
              "val5": vibration_x[4],
              "val6": vibration_x[5],
              "val7": vibration_x[6],
              "val8": vibration_x[7],
              "val9": vibration_x[8],
              "val10": vibration_x[9],
              "val11": vibration_x[10],
              "val12": vibration_x[11],
              "val13": vibration_x[12],
              "val14": vibration_x[13],
              "val15": vibration_x[14],
              "val16": vibration_x[15],
            },{
              "axis": "Y - Axis",
              "val1": vibration_y[0],
              "val2": vibration_y[1],
              "val3": vibration_y[2],
              "val4": vibration_y[3],
              "val5": vibration_y[4],
              "val6": vibration_y[5],
              "val7": vibration_y[6],
              "val8": vibration_y[7],
              "val9": vibration_y[8],
              "val10": vibration_y[9],
              "val11": vibration_y[10],
              "val12": vibration_y[11],
              "val13": vibration_y[12],
              "val14": vibration_y[13],
              "val15": vibration_y[14],
              "val16": vibration_y[15],
            },{
              "axis": "Z - Axis",
              "val1": vibration_z[0],
              "val2": vibration_z[1],
              "val3": vibration_z[2],
              "val4": vibration_z[3],
              "val5": vibration_z[4],
              "val6": vibration_z[5],
              "val7": vibration_z[6],
              "val8": vibration_z[7],
              "val9": vibration_z[8],
              "val10": vibration_z[9],
              "val11": vibration_z[10],
              "val12": vibration_z[11],
              "val13": vibration_z[12],
              "val14": vibration_z[13],
              "val15": vibration_z[14],
              "val16": vibration_z[15],
            }];
            
            // Create axes
            var categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "axis";
            categoryAxis.numberFormatter.numberFormat = "#";
            categoryAxis.renderer.inversed = true;
            categoryAxis.renderer.grid.template.location = 0;
            categoryAxis.renderer.cellStartLocation = 0.1;
            categoryAxis.renderer.cellEndLocation = 0.9;
            
            var  valueAxis = chart.xAxes.push(new am4charts.ValueAxis()); 
            valueAxis.renderer.opposite = true;
            
            // Create series
            function createSeries(field, name) {
              var series = chart.series.push(new am4charts.ColumnSeries());
              series.dataFields.valueX = field;
              series.dataFields.categoryY = "axis";
              series.name = name;
              series.columns.template.tooltipText = "{name}: [bold]{valueX}[/]";
              series.columns.template.height = am4core.percent(100);
              series.sequencedInterpolation = true;
            
              var valueLabel = series.bullets.push(new am4charts.LabelBullet());
              valueLabel.label.text = "{valueX}";
              valueLabel.label.horizontalCenter = "left";
              valueLabel.label.dx = 10;
              valueLabel.label.hideOversized = false;
              valueLabel.label.truncate = false;
            
              var categoryLabel = series.bullets.push(new am4charts.LabelBullet());
              categoryLabel.label.text = "{name}";
              categoryLabel.label.horizontalCenter = "right";
              categoryLabel.label.dx = -10;
              categoryLabel.label.fill = am4core.color("#000000");
              categoryLabel.label.hideOversized = false;
              categoryLabel.label.truncate = false;
            }
            
            createSeries("val1", "MY-1");
            createSeries("val2", "MY-2");
            createSeries("val3", "MY-3");
            createSeries("val4", "MY-4");
            createSeries("val5", "MY-5");
            createSeries("val6", "MY-6");
            createSeries("val7", "MY-7");
            createSeries("val8", "MY-8");
            createSeries("val9", "MY-9");
            createSeries("val10", "MY-10");
            createSeries("val11", "MY-11");
            createSeries("val12", "MY-12");
            createSeries("val13", "AT6-1");
            createSeries("val14", "AT6-2");
            createSeries("val15", "AT6-4");
            createSeries("val16", "HM-MY");
            
            }); // end am4core.ready()
    },
    error: function (error_data) {
        console.log("error");
        console.log(error_data);
    },
    });

  });
  