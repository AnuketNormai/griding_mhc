from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
# print(client.get_list_database())
client.switch_database('hm_iot')
client.get_list_measurements()
# print(client.get_list_measurements())
# Create your views here

class api_fish_current_grider(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_fish_current_grider =[]
        List_fish_current_grider =[]


        #!kwhAir Floor1 query
        qcurrentMY1=client.query('SELECT last("amps_pul1-fmhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentMY2=client.query('SELECT last("amps_pul2-fmhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentWD1=client.query('SELECT last("amps_wender1-fmhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentWD2=client.query('SELECT last("amps_wender2-fmhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentHM3=client.query('SELECT last("amps_HM1_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentHM6=client.query('SELECT last("amps_HM2_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentHM20=client.query('SELECT last("amps_HM1_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentAP61=client.query('SELECT last("amps_AP1_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentAP62=client.query('SELECT last("amps_AP2_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentAP63=client.query('SELECT last("amps_AP3_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentAP64=client.query('SELECT last("amps_AP4_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentAP65=client.query('SELECT last("amps_AP5_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentAP66=client.query('SELECT last("amps_AP6_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentMY7=client.query('SELECT last("amps_PUL#7F") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentMY8=client.query('SELECT last("amps_PUL#8F") FROM "grinding_1" GROUP BY "grinding_1"')
        

        # todo point kwhAir Floor1
        points_fish_current_grider.append(qcurrentMY1.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentMY2.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentWD1.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentWD2.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentHM3.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentHM6.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentHM20.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentAP61.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentAP62.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentAP63.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentAP64.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentAP65.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentAP66.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentMY7.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_grider.append(qcurrentMY8.get_points(tags={'grinding_1': ''})) #index0
        
  
        for curent in points_fish_current_grider:
            for i in curent: 
                time.append(i['time'])
                List_fish_current_grider.append(i['last'])

        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "fish_current_grider" : List_fish_current_grider,
            }
        return Response(data)