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

class api_fish_current_blower(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_fish_current_blower =[]
        List_fish_current_blower =[]


        #!kwhAir Floor1 query
        qcurrentblowerMY1=client.query('SELECT last("amps_bw_my-1f_mhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY2=client.query('SELECT last("amps_bw_my-2f_mhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerWD1=client.query('SELECT last("amps_bw_wd-1f_mhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerWD2=client.query('SELECT last("amps_bw_wd-2f_mhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerHM3=client.query('SELECT last("amps_bw_hm-1f_mhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerHM6=client.query('SELECT last("amps_bw_hm-2f_mhc1") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAP61=client.query('SELECT last("amps_bw_ap6_1f_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAP62=client.query('SELECT last("amps_bw_ap6_2f_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAP63=client.query('SELECT last("amps_bw_ap6_3f_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAP64=client.query('SELECT last("amps_bw_ap6_4f_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAP65=client.query('SELECT last("amps_bw_ap6_5f_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAP66=client.query('SELECT last("amps_bw_ap6_6f_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAPCG=client.query('SELECT last("amps_bw_at6-5cgf_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        
        
        

        # todo point kwhAir Floor1
        points_fish_current_blower.append(qcurrentblowerMY1.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerMY2.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerWD1.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerWD2.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerHM3.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerHM6.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerAP61.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerAP62.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerAP63.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerAP64.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerAP65.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerAP66.get_points(tags={'grinding_1': ''})) #index0
        points_fish_current_blower.append(qcurrentblowerAPCG.get_points(tags={'grinding_1': ''})) #index0
        
        
  
        for curent in points_fish_current_blower:
            for i in curent: 
                time.append(i['time'])
                List_fish_current_blower.append(i['last'])

        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "fish_current_blower" : List_fish_current_blower,
            }
        return Response(data)