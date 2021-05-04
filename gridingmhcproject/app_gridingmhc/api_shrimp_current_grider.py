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

class api_shrimp_current_grider(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_shrimp_current_grider =[]
        List_shrimp_current_grider =[]


        #!kwhAir Floor1 query
        qcurrentgriderMY1=client.query('SELECT last("amps_mhcgdpul1m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY2=client.query('SELECT last("amps_mhcgdpul2m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY3=client.query('SELECT last("amps_mhcgdpul3m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY4=client.query('SELECT last("amps_mhcgdpul4m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY5=client.query('SELECT last("amps_mhcgdpul5m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY6=client.query('SELECT last("amps_mhcgdpul6m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY7=client.query('SELECT last("amps_mhcgdpul7m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY8=client.query('SELECT last("amps_mhcgdpul8m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY9=client.query('SELECT last("amps_mhcgdpul9m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY10=client.query('SELECT last("amps_mhcgdpul10m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY11=client.query('SELECT last("amps_mhcgdpul11m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderMY12=client.query('SELECT last("amps_mhcgdpul12m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderAT61=client.query('SELECT last("amps_AP1_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderAT62=client.query('SELECT last("amps_AP2_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderAT63=client.query('SELECT last("amps_AP3_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderAT64=client.query('SELECT last("amps_AP4_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qcurrentgriderHMMY=client.query('SELECT last("amps_HM2_C") FROM "grinding_1" GROUP BY "grinding_1"')
        
        

        # todo point kwhAir Floor1
        points_shrimp_current_grider.append(qcurrentgriderMY1.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY2.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY3.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY4.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY5.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY6.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY7.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY8.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY9.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY10.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY11.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderMY12.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderAT61.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderAT62.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderAT63.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderAT64.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_current_grider.append(qcurrentgriderHMMY.get_points(tags={'grinding_1': ''})) #index0
        
        for curent in points_shrimp_current_grider:
            for i in curent: 
                time.append(i['time'])
                List_shrimp_current_grider.append(i['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "shrimp_current_grider" : List_shrimp_current_grider,
            }
        return Response(data)