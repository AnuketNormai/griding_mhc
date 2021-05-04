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

class api_fish_temp_grider(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_fish_temp_grider =[]
        List_fish_temp_grider =[]


        #!kwhAir Floor1 query
        qtempbearinggriderMY1=client.query('SELECT last("outlet_pul1-fmhc1temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderMY2=client.query('SELECT last("outlet_pul2-fmhc1temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderHM6=client.query('SELECT last("outlet_HM2_Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        qtempbearinggriderAP61=client.query('SELECT last("outlet_AP1_Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderAP62=client.query('SELECT last("outlet_AP2_Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderAP63=client.query('SELECT last("outlet_AP3_Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderAP64=client.query('SELECT last("outlet_AP4_Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderAP65=client.query('SELECT last("outlet_AP5_Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderAP66=client.query('SELECT last("outlet_AP6_Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderMY7=client.query('SELECT last("outlet_PUL#7Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderMY8=client.query('SELECT last("outlet_PUL#8Ftemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderHM20=client.query('SELECT last("outlet_HM1_Ctemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearinggriderAPCG=client.query('SELECT last("outlet_AP5_Ctemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        

        # todo point kwhAir Floor1
        points_fish_temp_grider.append(qtempbearinggriderMY1.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderMY2.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderHM6.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderAP61.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderAP62.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderAP63.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderAP64.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderAP65.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderAP66.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderMY7.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderMY8.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderHM20.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_grider.append(qtempbearinggriderAPCG.get_points(tags={'grinding_1': ''})) #index0
        
        
  
        for curent in points_fish_temp_grider:
            for i in curent: 
                time.append(i['time'])
                List_fish_temp_grider.append(i['last'])

        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "fish_temp_grider" : List_fish_temp_grider,
            }
        return Response(data)