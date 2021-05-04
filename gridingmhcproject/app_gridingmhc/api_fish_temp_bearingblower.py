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

class api_fish_temp_bearingblower(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_fish_temp_bearingblower =[]
        List_fish_temp_bearingblower =[]


        #!kwhAir Floor1 query
        qtempbearingblowerMY11=client.query('SELECT last("t_bw_my-1f_mhc1-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY12=client.query('SELECT last("t_bw_my-1f_mhc1-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY21=client.query('SELECT last("t_bw_my-2f_mhc1-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY22=client.query('SELECT last("t_bw_my-2f_mhc1-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerHM31=client.query('SELECT last("t_bw_hm-1f_mhc1-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerHM32=client.query('SELECT last("t_bw_hm-1f_mhc1-2") FROM "grinding_1" GROUP BY "grinding_1"')
        
        qtempbearingblowerAP611=client.query('SELECT last("t_bw_ap6_1f_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP612=client.query('SELECT last("t_bw_ap6_1f_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP621=client.query('SELECT last("t_bw_ap6_2f_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP622=client.query('SELECT last("t_bw_ap6_2f_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP631=client.query('SELECT last("t_bw_ap6_3f_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP632=client.query('SELECT last("t_bw_ap6_3f_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP641=client.query('SELECT last("t_bw_ap6_4f_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP642=client.query('SELECT last("t_bw_ap6_4f_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP651=client.query('SELECT last("t_bw_ap6_5f_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP652=client.query('SELECT last("t_bw_ap6_5f_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP661=client.query('SELECT last("t_bw_ap6_6f_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAP662=client.query('SELECT last("t_bw_ap6_6f_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAPCG1=client.query('SELECT last("t_bw_at6_5f_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAPCG2=client.query('SELECT last("t_bw_at6_5f_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerHM201=client.query('SELECT last("t_bw_hm-1cgf_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerHM202=client.query('SELECT last("t_bw_hm-1cgf_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        
        
        

        # todo point kwhAir Floor1
        points_fish_temp_bearingblower.append(qtempbearingblowerMY11.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerMY12.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerMY21.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerMY22.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerHM31.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerHM32.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP611.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP612.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP621.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP622.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP631.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP632.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP641.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP642.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP651.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP652.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP661.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAP662.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAPCG1.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerAPCG2.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerHM201.get_points(tags={'grinding_1': ''})) #index0
        points_fish_temp_bearingblower.append(qtempbearingblowerHM202.get_points(tags={'grinding_1': ''})) #index0
        
        
  
        for curent in points_fish_temp_bearingblower:
            for i in curent: 
                time.append(i['time'])
                List_fish_temp_bearingblower.append(i['last'])

        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "fish_temp_bearingblower" : List_fish_temp_bearingblower,
            }
        return Response(data)