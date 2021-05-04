$(document).ready(function () {
    var endpoint = 'api/data';
    var labels = [];
    var amp_pul = [];
    var noload = []
    var lightload = []
    var normalload = []
    var turnoff = []
    var utilize = []

     
    setInterval(function () {
      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          amp_pul = data.amp; //from api_utilize.py
          noload = data.noload; //from api_utilize.py
          lightload = data.lightload; //from api_utilize.py
          normalload =data.normalload; //from api_utilize.py
          turnoff = data.offline; //from api_utilize.py
          utilize = data.utilize; //from api_utilize.py

          $("#ampMY1").text(amp_pul[0].toFixed(2) + " Amp");
          $("#pturnoffMY1").text(turnoff[0].toFixed(2) + " %");
          $("#pnoloadMY1").text(noload[0].toFixed(2) + " %");
          $("#plightloadMY1").text(lightload[0].toFixed(2) + " %");
          $("#pnormalloadMY1").text(normalload[0].toFixed(2) + " %");
          $("#putilizeloadMY1").text(utilize[0].toFixed(2) + " %");

          $("#ampMY2").text(amp_pul[1].toFixed(2) + " Amp");
          $("#pturnoffMY2").text(turnoff[1].toFixed(2) + " %");
          $("#pnoloadMY2").text(noload[1].toFixed(2) + " %");
          $("#plightloadMY2").text(lightload[1].toFixed(2) + " %");
          $("#pnormalloadMY2").text(normalload[1].toFixed(2) + " %");
          $("#putilizeloadMY2").text(utilize[1].toFixed(2) + " %");

          $("#ampMY3").text(amp_pul[2].toFixed(2) + " Amp");
          $("#pturnoffMY3").text(turnoff[2].toFixed(2) + " %");
          $("#pnoloadMY3").text(noload[2].toFixed(2) + " %");
          $("#plightloadMY3").text(lightload[2].toFixed(2) + " %");
          $("#pnormalloadMY3").text(normalload[2].toFixed(2) + " %");
          $("#putilizeloadMY3").text(utilize[2].toFixed(2) + " %");

          $("#ampMY4").text(amp_pul[3].toFixed(2) + " Amp");
          $("#pturnoffMY4").text(turnoff[3].toFixed(2) + " %");
          $("#pnoloadMY4").text(noload[3].toFixed(2) + " %");
          $("#plightloadMY4").text(lightload[3].toFixed(2) + " %");
          $("#pnormalloadMY4").text(normalload[3].toFixed(2) + " %");
          $("#putilizeloadMY4").text(utilize[3].toFixed(2) + " %");

          $("#ampMY5").text(amp_pul[4].toFixed(2) + " Amp");
          $("#pturnoffMY5").text(turnoff[4].toFixed(2) + " %");
          $("#pnoloadMY5").text(noload[4].toFixed(2) + " %");
          $("#plightloadMY5").text(lightload[4].toFixed(2) + " %");
          $("#pnormalloadMY5").text(normalload[4].toFixed(2) + " %");
          $("#putilizeloadMY5").text(utilize[4].toFixed(2) + " %");

          $("#ampMY6").text(amp_pul[5].toFixed(2) + " Amp");
          $("#pturnoffMY6").text(turnoff[5].toFixed(2) + " %");
          $("#pnoloadMY6").text(noload[5].toFixed(2) + " %");
          $("#plightloadMY6").text(lightload[5].toFixed(2) + " %");
          $("#pnormalloadMY6").text(normalload[5].toFixed(2) + " %");
          $("#putilizeloadMY6").text(utilize[5].toFixed(2) + " %");

          $("#ampMY7").text(amp_pul[6].toFixed(2) + " Amp");
          $("#pturnoffMY7").text(turnoff[6].toFixed(2) + " %");
          $("#pnoloadMY7").text(noload[6].toFixed(2) + " %");
          $("#plightloadMY7").text(lightload[6].toFixed(2) + " %");
          $("#pnormalloadMY7").text(normalload[6].toFixed(2) + " %");
          $("#putilizeloadMY7").text(utilize[6].toFixed(2) + " %");

          $("#ampMY8").text(amp_pul[7].toFixed(2) + " Amp");
          $("#pturnoffMY8").text(turnoff[7].toFixed(2) + " %");
          $("#pnoloadMY8").text(noload[7].toFixed(2) + " %");
          $("#plightloadMY8").text(lightload[7].toFixed(2) + " %");
          $("#pnormalloadMY8").text(normalload[7].toFixed(2) + " %");
          $("#putilizeloadMY8").text(utilize[7].toFixed(2) + " %");

          $("#ampMY9").text(amp_pul[8].toFixed(2) + " Amp");
          $("#pturnoffMY9").text(turnoff[8].toFixed(2) + " %");
          $("#pnoloadMY9").text(noload[8].toFixed(2) + " %");
          $("#plightloadMY9").text(lightload[8].toFixed(2) + " %");
          $("#pnormalloadMY9").text(normalload[8].toFixed(2) + " %");
          $("#putilizeloadMY9").text(utilize[8].toFixed(2) + " %");

          $("#ampMY10").text(amp_pul[9].toFixed(2) + " Amp");
          $("#pturnoffMY10").text(turnoff[9].toFixed(2) + " %");
          $("#pnoloadMY10").text(noload[9].toFixed(2) + " %");
          $("#plightloadMY10").text(lightload[9].toFixed(2) + " %");
          $("#pnormalloadMY10").text(normalload[9].toFixed(2) + " %");
          $("#putilizeloadMY10").text(utilize[9].toFixed(2) + " %");

          $("#ampMY11").text(amp_pul[10].toFixed(2) + " Amp");
          $("#pturnoffMY11").text(turnoff[10].toFixed(2) + " %");
          $("#pnoloadMY11").text(noload[10].toFixed(2) + " %");
          $("#plightloadMY11").text(lightload[10].toFixed(2) + " %");
          $("#pnormalloadMY11").text(normalload[10].toFixed(2) + " %");
          $("#putilizeloadMY11").text(utilize[10].toFixed(2) + " %");

        //   $("#ampMY12").text(amp_pul[11].toFixed(2) + " Amp");
        //   $("#pturnoffMY12").text(turnoff[11].toFixed(2) + " %");
        //   $("#pnoloadMY12").text(noload[11].toFixed(2) + " %");
        //   $("#plightloadMY12").text(lightload[11].toFixed(2) + " %");
        //   $("#pnormalloadMY12").text(normalload[11].toFixed(2) + " %");
        // $("#putilizeloadMY12").text(utilize[11].toFixed(2) + " %");

          $("#ampAT1").text(amp_pul[11].toFixed(2) + " Amp");
          $("#pturnoffAT1").text(turnoff[11].toFixed(2) + " %");
          $("#pnoloadAT1").text(noload[11].toFixed(2) + " %");
          $("#plightloadAT1").text(lightload[11].toFixed(2) + " %");
          $("#pnormalloadAT1").text(normalload[11].toFixed(2) + " %");
          $("#putilizeloadAT1").text(utilize[11].toFixed(2) + " %");

          $("#ampAT2").text(amp_pul[12].toFixed(2) + " Amp");
          $("#pturnoffAT2").text(turnoff[12].toFixed(2) + " %");
          $("#pnoloadAT2").text(noload[12].toFixed(2) + " %");
          $("#plightloadAT2").text(lightload[12].toFixed(2) + " %");
          $("#pnormalloadAT2").text(normalload[12].toFixed(2) + " %");
          $("#putilizeloadAT2").text(utilize[12].toFixed(2) + " %");

          $("#ampAT3").text(amp_pul[13].toFixed(2) + " Amp");
          $("#pturnoffAT3").text(turnoff[13].toFixed(2) + " %");
          $("#pnoloadAT3").text(noload[13].toFixed(2) + " %");
          $("#plightloadAT3").text(lightload[13].toFixed(2) + " %");
          $("#pnormalloadAT3").text(normalload[13].toFixed(2) + " %");
          $("#putilizeloadAT3").text(utilize[13].toFixed(2) + " %");

          $("#ampAT4").text(amp_pul[14].toFixed(2) + " Amp");
          $("#pturnoffAT4").text(turnoff[14].toFixed(2) + " %");
          $("#pnoloadAT4").text(noload[14].toFixed(2) + " %");
          $("#plightloadAT4").text(lightload[14].toFixed(2) + " %");
          $("#pnormalloadAT4").text(normalload[14].toFixed(2) + " %");
          $("#putilizeloadAT4").text(utilize[14].toFixed(2) + " %");

          $("#ampHMMY").text(amp_pul[15].toFixed(2) + " Amp");
          $("#pturnoffHMMY").text(turnoff[15].toFixed(2) + " %");
          $("#pnoloadHMMY").text(noload[15].toFixed(2) + " %");
          $("#plightloadHMMY").text(lightload[15].toFixed(2) + " %");
          $("#pnormalloadHMMY").text(normalload[15].toFixed(2) + " %");
          $("#putilizeloadHMMY").text(utilize[15].toFixed(2) + " %");

          $("#ampFAP1").text(amp_pul[17].toFixed(2) + " Amp");
          $("#pturnoffFAP1").text(turnoff[17].toFixed(2) + " %");
          $("#pnoloadFAP1").text(noload[17].toFixed(2) + " %");
          $("#plightloadFAP1").text(lightload[17].toFixed(2) + " %");
          $("#pnormalloadFAP1").text(normalload[17].toFixed(2) + " %");
          $("#putilizeloadFAP1").text(utilize[17].toFixed(2) + " %");

          $("#ampFAP2").text(amp_pul[18].toFixed(2) + " Amp");
          $("#pturnoffFAP2").text(turnoff[18].toFixed(2) + " %");
          $("#pnoloadFAP2").text(noload[18].toFixed(2) + " %");
          $("#plightloadFAP2").text(lightload[18].toFixed(2) + " %");
          $("#pnormalloadFAP2").text(normalload[18].toFixed(2) + " %");
          $("#putilizeloadFAP2").text(utilize[18].toFixed(2) + " %");

          $("#ampFAP3").text(amp_pul[19].toFixed(2) + " Amp");
          $("#pturnoffFAP3").text(turnoff[19].toFixed(2) + " %");
          $("#pnoloadFAP3").text(noload[19].toFixed(2) + " %");
          $("#plightloadFAP3").text(lightload[19].toFixed(2) + " %");
          $("#pnormalloadFAP3").text(normalload[19].toFixed(2) + " %");
          $("#putilizeloadFAP3").text(utilize[19].toFixed(2) + " %");

          $("#ampFAP4").text(amp_pul[20].toFixed(2) + " Amp");
          $("#pturnoffFAP4").text(turnoff[20].toFixed(2) + " %");
          $("#pnoloadFAP4").text(noload[20].toFixed(2) + " %");
          $("#plightloadFAP4").text(lightload[20].toFixed(2) + " %");
          $("#pnormalloadFAP4").text(normalload[20].toFixed(2) + " %");
          $("#putilizeloadFAP4").text(utilize[20].toFixed(2) + " %");

          $("#ampFAP5").text(amp_pul[21].toFixed(2) + " Amp");
          $("#pturnoffFAP5").text(turnoff[21].toFixed(2) + " %");
          $("#pnoloadFAP5").text(noload[21].toFixed(2) + " %");
          $("#plightloadFAP5").text(lightload[21].toFixed(2) + " %");
          $("#pnormalloadFAP5").text(normalload[21].toFixed(2) + " %");
          $("#putilizeloadFAP5").text(utilize[21].toFixed(2) + " %");

          $("#ampFAP6").text(amp_pul[22].toFixed(2) + " Amp");
          $("#pturnoffFAP6").text(turnoff[22].toFixed(2) + " %");
          $("#pnoloadFAP6").text(noload[22].toFixed(2) + " %");
          $("#plightloadFAP6").text(lightload[22].toFixed(2) + " %");
          $("#pnormalloadFAP6").text(normalload[22].toFixed(2) + " %");
          $("#putilizeloadFAP6").text(utilize[22].toFixed(2) + " %");

          $("#ampFMY7").text(amp_pul[23].toFixed(2) + " Amp");
          $("#pturnoffFMY7").text(turnoff[23].toFixed(2) + " %");
          $("#pnoloadFMY7").text(noload[23].toFixed(2) + " %");
          $("#plightloadFMY7").text(lightload[23].toFixed(2) + " %");
          $("#pnormalloadFMY7").text(normalload[23].toFixed(2) + " %");
          $("#putilizeloadFMY7").text(utilize[23].toFixed(2) + " %");

          $("#ampFMY8").text(amp_pul[24].toFixed(2) + " Amp");
          $("#pturnoffFMY8").text(turnoff[24].toFixed(2) + " %");
          $("#pnoloadFMY8").text(noload[24].toFixed(2) + " %");
          $("#plightloadFMY8").text(lightload[24].toFixed(2) + " %");
          $("#pnormalloadFMY8").text(normalload[24].toFixed(2) + " %");
          $("#putilizeloadFMY8").text(utilize[24].toFixed(2) + " %");

          
          
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
        
        
      });
    }, 5000);
  });
  