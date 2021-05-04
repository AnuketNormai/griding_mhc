$(document).ready(function () {
    var endpoint = 'api/ampshrimp';
    var amp_pul = [];
    var labels = [];
  
    var setpointamp_pul = 1;

  
    var powerOn_color = "#00FF00"; //set color for device has normal #10B510
    var powerOff_color = "#A9A9A9"; //set color for device has normal #10B510
  
    setInterval(function () {
      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          amp_pul = data.shrimGriding; //from api_homedashboard.py

  
          // floor 1
          //   
          if (amp_pul[0] <= setpointamp_pul) {
            $("#bggriderMY1").addClass("bg-light");
          }
          if (amp_pul[0] > setpointamp_pul) {
            $("#bggriderMY1").removeClass("bg-light");
            $("#bggriderMY1").addClass("bg-warning");
          }
          //   
          if (amp_pul[1] <= setpointamp_pul) {
            $("#bggriderMY2").addClass("bg-light");
          }
          if (amp_pul[1] > setpointamp_pul) {
            $("#bggriderMY2").removeClass("bg-light");
            $("#bggriderMY2").addClass("bg-warning");
          }
          //  
          if (amp_pul[2] <= setpointamp_pul) {
            $("#bggriderMY3").addClass("bg-light");
          }
          if (amp_pul[2] > setpointamp_pul) {
            $("#bggriderMY3").removeClass("bg-light");
            $("#bggriderMY3").addClass("bg-warning");
          }
          //  
          if (amp_pul[3] <= setpointamp_pul) {
            $("#bggriderMY4").addClass("bg-light");
          }
          if (amp_pul[3] > setpointamp_pul) {
            $("#bggriderMY4").removeClass("bg-light");
            $("#bggriderMY4").addClass("bg-warning");
          }
          // 
          if (amp_pul[4] <= setpointamp_pul) {
            $("#bggriderMY5").addClass("bg-light");
          }
          if (amp_pul[4] > setpointamp_pul) {
            $("#bggriderMY5").removeClass("bg-light");
            $("#bggriderMY5").addClass("bg-warning");
          }
          //  
          if (amp_pul[5] <= setpointamp_pul) {
            $("#bggriderMY6").addClass("bg-light");
          }
          if (amp_pul[5] > setpointamp_pul) {
            $("#bggriderMY6").removeClass("bg-light");
            $("#bggriderMY6").addClass("bg-warning");
          }
          //  
          if (amp_pul[6] <= setpointamp_pul) {
            $("#bggriderMY7").addClass("bg-light");
          }
          if (amp_pul[6] > setpointamp_pul) {
            $("#bggriderMY7").removeClass("bg-light");
            $("#bggriderMY7").addClass("bg-warning");
          }
          //  
          if (amp_pul[7] <= setpointamp_pul) {
            $("#bggriderMY8").addClass("bg-light");
          }
          if (amp_pul[7] > setpointamp_pul) {
            $("#bggriderMY8").removeClass("bg-light");
            $("#bggriderMY8").addClass("bg-warning");
          }
          //   
          if (amp_pul[8] <= setpointamp_pul) {
            $("#bggriderMY9").addClass("bg-light");
          }
          if (amp_pul[8] > setpointamp_pul) {
            $("#bggriderMY9").removeClass("bg-light");
            $("#bggriderMY9").addClass("bg-warning");
          }
          //   
          if (amp_pul[9] <= setpointamp_pul) {
            $("#bggriderMY10").addClass("bg-light");
          }
          if (amp_pul[9] > setpointamp_pul) {
            $("#bggriderMY10").removeClass("bg-light");
            $("#bggriderMY10").addClass("bg-warning");
          }
          //   
          if (amp_pul[10] <= setpointamp_pul) {
            $("#bggriderMY11").addClass("bg-light");
          }
          if (amp_pul[10] > setpointamp_pul) {
            $("#bggriderMY11").removeClass("bg-light");
            $("#bggriderMY11").addClass("bg-warning");
          }
          //   
        //   if (amp_pul[11] <= setpointamp_pul) {
        //     $("#bggriderMY12").addClass("bg-light");
        //   }
        //   if (amp_pul[11] > setpointamp_pul) {
        //     $("#bggriderMY12").removeClass("bg-light");
        //     $("#bggriderMY12").addClass("bg-warning");
        //   }
          //  AT6
          //    
          if (amp_pul[11] <= setpointamp_pul) {
            $("#bggriderAT1").addClass("bg-light");
          }
          if (amp_pul[11] > setpointamp_pul) {
            $("#bggriderAT1").removeClass("bg-light");
            $("#bggriderAT1").addClass("bg-warning");
          }
          //   
          if (amp_pul[12] <= setpointamp_pul) {
            $("#bggriderAT2").addClass("bg-light");
          }
          if (amp_pul[12] > setpointamp_pul) {
            $("#bggriderAT2").removeClass("bg-light");
            $("#bggriderAT2").addClass("bg-warning");
          }
          //    
          if (amp_pul[13] <= setpointamp_pul) {
            $("#bggriderAT3").addClass("bg-light");
          }
          if (amp_pul[13] > setpointamp_pul) {
            $("#bggriderAT3").removeClass("bg-light");
            $("#bggriderAT3").addClass("bg-warning");
          }
          //   
          if (amp_pul[14] <= setpointamp_pul) {
            $("#bggriderAT4").addClass("bg-light");
          }
          if (amp_pul[14] > setpointamp_pul) {
            $("#bggriderAT4").removeClass("bg-light");
            $("#bggriderAT4").addClass("bg-warning");
          }
          //   
          if (amp_pul[15] <= setpointamp_pul) {
            $("#bggriderHMMY").addClass("bg-light");
          }
          if (amp_pul[15] > setpointamp_pul) {
            $("#bggriderHMMY").removeClass("bg-light");
            $("#bggriderHMMY").addClass("bg-warning");
          }
          //  Fish  AP1
          if (amp_pul[17] <= setpointamp_pul) {
            $("#bggriderFAP1").addClass("bg-light");
          }
          if (amp_pul[17] > setpointamp_pul) {
            $("#bggriderFAP1").removeClass("bg-light");
            $("#bggriderFAP1").addClass("bg-warning");
          }
          //  Fish  AP2
          if (amp_pul[18] <= setpointamp_pul) {
            $("#bggriderFAP2").addClass("bg-light");
          }
          if (amp_pul[18] > setpointamp_pul) {
            $("#bggriderFAP2").removeClass("bg-light");
            $("#bggriderFAP2").addClass("bg-warning");
          }
          //  Fish  AP3
          if (amp_pul[19] <= setpointamp_pul) {
            $("#bggriderFAP3").addClass("bg-light");
          }
          if (amp_pul[19] > setpointamp_pul) {
            $("#bggriderFAP3").removeClass("bg-light");
            $("#bggriderFAP3").addClass("bg-warning");
          }
          //  Fish  AP4
          if (amp_pul[20] <= setpointamp_pul) {
            $("#bggriderFAP4").addClass("bg-light");
          }
          if (amp_pul[20] > setpointamp_pul) {
            $("#bggriderFAP4").removeClass("bg-light");
            $("#bggriderFAP4").addClass("bg-warning");
          }
          //  Fish  AP5
          if (amp_pul[21] <= setpointamp_pul) {
            $("#bggriderFAP5").addClass("bg-light");
          }
          if (amp_pul[21] > setpointamp_pul) {
            $("#bggriderFAP5").removeClass("bg-light");
            $("#bggriderFAP5").addClass("bg-warning");
          }
          //  Fish  AP6
          if (amp_pul[22] <= setpointamp_pul) {
            $("#bggriderFAP6").addClass("bg-light");
          }
          if (amp_pul[22] > setpointamp_pul) {
            $("#bggriderFAP6").removeClass("bg-light");
            $("#bggriderFAP6").addClass("bg-warning");
          }
          //  Fish  MY7
          if (amp_pul[23] <= setpointamp_pul) {
            $("#bggriderFMY8").addClass("bg-light");
          }
          if (amp_pul[23] > setpointamp_pul) {
            $("#bggriderFMY8").removeClass("bg-light");
            $("#bggriderFMY8").addClass("bg-warning");
          }
          //  Fish  MY8
          if (amp_pul[24] <= setpointamp_pul) {
            $("#bggriderFMY8").addClass("bg-light");
          }
          if (amp_pul[24] > setpointamp_pul) {
            $("#bggriderFMY8").removeClass("bg-light");
            $("#bggriderFMY8").addClass("bg-warning");
          }

        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
        
        
      });
    }, 5000);
  });
  