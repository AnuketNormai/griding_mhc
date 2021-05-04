$(document).ready(function () {
  var endpoint = "api/shrimp_temp_grider";
  var temp = [];
  $.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
      temp = data.shrimp_temp_grider; //api_shrimp_temp_grider.py

      am4core.ready(function() {

          // Themes begin
          am4core.useTheme(am4themes_animated);
          // Themes end
          
          // Create chart instance
          var chart = am4core.create("charttempshrimpgriderMHC2", am4charts.XYChart3D);
          
          // Add data
          chart.data = [{
            "tempshrimpgrider": "MY-1",
            "valtempshrimpgrider": temp[0]
          }, {
            "tempshrimpgrider": "MY-2",
            "valtempshrimpgrider": temp[1]
          }, {
            "tempshrimpgrider": "MY-3",
            "valtempshrimpgrider": temp[2]
          }, {
            "tempshrimpgrider": "MY-4",
            "valtempshrimpgrider": temp[3]
          }, {
            "tempshrimpgrider": "MY-5",
            "valtempshrimpgrider": temp[4]
          }, {
            "tempshrimpgrider": "MY-6",
            "valtempshrimpgrider": temp[5]
          }, {
            "tempshrimpgrider": "MY-7",
            "valtempshrimpgrider": temp[6]
          }, {
            "tempshrimpgrider": "MY-8",
            "valtempshrimpgrider": temp[7]
          }, {
            "tempshrimpgrider": "MY-9",
            "valtempshrimpgrider": temp[8]
          }, {
            "tempshrimpgrider": "MY-10",
            "valtempshrimpgrider": temp[9]
          }, {
            "tempshrimpgrider": "MY-11",
            "valtempshrimpgrider": temp[10]
          }, {
            "tempshrimpgrider": "MY-12",
            "valtempshrimpgrider": temp[11]
          }, {
            "tempshrimpgrider": "AT6-1",
            "valtempshrimpgrider": temp[12]
          }, {
            "tempshrimpgrider": "AT6-2",
            "valtempshrimpgrider": temp[13]
          }, {
            "tempshrimpgrider": "AT6-3",
            "valtempshrimpgrider": temp[14]
          }, {
            "tempshrimpgrider": "AT6-4",
            "valtempshrimpgrider": temp[15]
          }, {
            "tempshrimpgrider": "HM-MY",
            "valtempshrimpgrider": temp[16]
          }
        ];
          
          // Create axes
          let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
          categoryAxis.dataFields.category = "tempshrimpgrider";
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
          series.dataFields.valueY = "valtempshrimpgrider";
          series.dataFields.categoryX = "tempshrimpgrider";
          series.name = "valtempshrimpgrider";
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
