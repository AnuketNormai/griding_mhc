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

class api_fish_vibration_grider(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_fish_vibration_x_grider =[]
        List_fish_vibration_x_grider =[]
        points_fish_vibration_y_grider =[]
        List_fish_vibration_y_grider =[]
        points_fish_vibration_z_grider =[]
        List_fish_vibration_z_grider =[]

        #!Vibration x
        qvibration_x_MY1=client.query('SELECT last("mainshaft_pul1-fmhc1_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY2=client.query('SELECT last("mainshaft_pul2-fmhc1_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_WD1=client.query('SELECT last("mainshaft_wender1-fmhc1_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_WD2=client.query('SELECT last("mainshaft_wender1-fmhc1_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_HM3=client.query('SELECT last("mainshaft_HM1_F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_HM6=client.query('SELECT last("mainshaft_HM2_F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AP61=client.query('SELECT last("mainshaft_AP1_F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AP62=client.query('SELECT last("mainshaft_AP2_F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AP63=client.query('SELECT last("mainshaft_AP3_F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AP64=client.query('SELECT last("mainshaft_AP4_F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AP65=client.query('SELECT last("mainshaft_AP5_F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AP66=client.query('SELECT last("mainshaft_AP6_F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY7=client.query('SELECT last("mainshaft_PUL#7F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY8=client.query('SELECT last("mainshaft_PUL#8F_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_HM20=client.query('SELECT last("mainshaft_HM1_C_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration x
        points_fish_vibration_x_grider.append(qvibration_x_MY1.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_MY2.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_WD1.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_WD2.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_HM3.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_HM6.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_AP61.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_AP62.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_AP63.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_AP64.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_AP65.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_AP66.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_MY7.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_MY8.get_points(tags={'grinding_1': ''})) #index0
        points_fish_vibration_x_grider.append(qvibration_x_HM20.get_points(tags={'grinding_1': ''})) #index0


        #!Vibration y
        qvibration_y_MY1=client.query('SELECT last("mainshaft_pul1-fmhc1_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY2=client.query('SELECT last("mainshaft_pul2-fmhc1_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_WD1=client.query('SELECT last("mainshaft_wender1-fmhc1_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_WD2=client.query('SELECT last("mainshaft_wender1-fmhc1_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_HM3=client.query('SELECT last("mainshaft_HM1_F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_HM6=client.query('SELECT last("mainshaft_HM2_F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AP61=client.query('SELECT last("mainshaft_AP1_F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AP62=client.query('SELECT last("mainshaft_AP2_F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AP63=client.query('SELECT last("mainshaft_AP3_F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AP64=client.query('SELECT last("mainshaft_AP4_F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AP65=client.query('SELECT last("mainshaft_AP5_F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AP66=client.query('SELECT last("mainshaft_AP6_F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY7=client.query('SELECT last("mainshaft_PUL#7F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY8=client.query('SELECT last("mainshaft_PUL#8F_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_HM20=client.query('SELECT last("mainshaft_HM1_C_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration y
        points_fish_vibration_y_grider.append(qvibration_y_MY1.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_MY2.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_WD1.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_WD2.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_HM3.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_HM6.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_AP61.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_AP62.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_AP63.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_AP64.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_AP65.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_AP66.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_MY7.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_MY8.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_y_grider.append(qvibration_y_HM20.get_points(tags={'grinding_1': ''})) #indey0
        

        #!Vibration z
        qvibration_z_MY1=client.query('SELECT last("mainshaft_pul1-fmhc1_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY2=client.query('SELECT last("mainshaft_pul2-fmhc1_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_WD1=client.query('SELECT last("mainshaft_wender1-fmhc1_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_WD2=client.query('SELECT last("mainshaft_wender1-fmhc1_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_HM3=client.query('SELECT last("mainshaft_HM1_F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_HM6=client.query('SELECT last("mainshaft_HM2_F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AP61=client.query('SELECT last("mainshaft_AP1_F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AP62=client.query('SELECT last("mainshaft_AP2_F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AP63=client.query('SELECT last("mainshaft_AP3_F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AP64=client.query('SELECT last("mainshaft_AP4_F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AP65=client.query('SELECT last("mainshaft_AP5_F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AP66=client.query('SELECT last("mainshaft_AP6_F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY7=client.query('SELECT last("mainshaft_PUL#7F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY8=client.query('SELECT last("mainshaft_PUL#8F_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_HM20=client.query('SELECT last("mainshaft_HM1_C_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration z
        points_fish_vibration_z_grider.append(qvibration_z_MY1.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_MY2.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_WD1.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_WD2.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_HM3.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_HM6.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_AP61.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_AP62.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_AP63.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_AP64.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_AP65.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_AP66.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_MY7.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_MY8.get_points(tags={'grinding_1': ''})) #indey0
        points_fish_vibration_z_grider.append(qvibration_z_HM20.get_points(tags={'grinding_1': ''})) #indey0
        
  
        for vibration_x in points_fish_vibration_x_grider:
            for i in vibration_x: 
                time.append(i['time'])
                List_fish_vibration_x_grider.append(i['last'])
        
        for vibration_y in points_fish_vibration_y_grider:
            for i in vibration_y: 
                time.append(i['time'])
                List_fish_vibration_y_grider.append(i['last'])

        for vibration_z in points_fish_vibration_z_grider:
            for i in vibration_z: 
                time.append(i['time'])
                List_fish_vibration_z_grider.append(i['last'])
        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "fish_vibration_x_grider" : List_fish_vibration_x_grider,
                "fish_vibration_y_grider" : List_fish_vibration_y_grider,
                "fish_vibration_z_grider" : List_fish_vibration_z_grider,
            }
        return Response(data)