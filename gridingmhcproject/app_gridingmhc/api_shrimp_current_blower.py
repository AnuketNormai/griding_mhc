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

class api_shrimp_current_blower(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_shrimp_current_blower =[]
        List_shrimp_current_blower =[]


        #!kwhAir Floor1 query
        qcurrentblowerMY1=client.query('SELECT last("amps_bw_pul1_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY2=client.query('SELECT last("amps_bw_pul2_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY3=client.query('SELECT last("amps_bw_pul3_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY4=client.query('SELECT last("amps_bw_pul4_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY5=client.query('SELECT last("amps_bw_pul5_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY6=client.query('SELECT last("amps_bw_pul6_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY7=client.query('SELECT last("amps_bw_pul7_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY8=client.query('SELECT last("amps_bw_pul8_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY9=client.query('SELECT last("amps_bw_pul9_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY10=client.query('SELECT last("amps_bw_pul10_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY11=client.query('SELECT last("amps_bw_pul11_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerMY12=client.query('SELECT last("amps_bw_pul12_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAT61=client.query('SELECT last("amps_bw_at6-1cgs_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAT62=client.query('SELECT last("amps_bw_at6-2cgs_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAT63=client.query('SELECT last("amps_bw_at6-3cgs_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerAT64=client.query('SELECT last("amps_bw_at6-4cgs_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerHM2CG=client.query('SELECT last("amps_bw_hm-2cgs_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentblowerHMMY=client.query('SELECT last("amps_bw_hm-2cgs_mhc2") FROM "grinding_1" GROUP BY "grinding_1"')
        
        

        # todo point kwhAir Floor1
        points_shrimp_current_blower.append(qcurrentblowerMY1.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY2.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY3.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY4.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY5.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY6.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY7.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY8.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY9.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY10.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY11.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerMY12.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerAT61.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerAT62.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerAT63.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerAT64.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerHM2CG.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_blower.append(qcurrentblowerHMMY.get_points(tags={'grinding_1': ''})) #index0
        
        for curent in points_shrimp_current_blower:
            for i in curent: 
                time.append(i['time'])
                List_shrimp_current_blower.append(i['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "shrimp_current_blower" : List_shrimp_current_blower,
            }
        return Response(data)