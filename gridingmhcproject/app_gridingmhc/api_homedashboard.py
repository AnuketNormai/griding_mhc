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

class api_ampshrimp_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = [
         'MY1','MY2','MY3','MY4','MY5','MY6',
         'MY7','MY8','MY9','MY10','MY11','MY12',
         'AT1','AT2','AT3','AT4','AT5','AT6'
        ]

        time = []
        points_ampshrimp =[]
        List_ampshrimp =[]


        #!kwhAir Floor1 query
        qampMY1=client.query('SELECT last("amps_mhcgdpul1m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY2=client.query('SELECT last("amps_mhcgdpul2m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY3=client.query('SELECT last("amps_mhcgdpul3m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY4=client.query('SELECT last("amps_mhcgdpul4m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY5=client.query('SELECT last("amps_mhcgdpul5m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY6=client.query('SELECT last("amps_mhcgdpul6m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY7=client.query('SELECT last("amps_mhcgdpul7m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY8=client.query('SELECT last("amps_mhcgdpul8m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY9=client.query('SELECT last("amps_mhcgdpul9m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY10=client.query('SELECT last("amps_mhcgdpul10m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY11=client.query('SELECT last("amps_mhcgdpul11m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampMY12=client.query('SELECT last("amps_mhcgdpul12m2") FROM "grinding_1" GROUP BY "grinding_1"')
        qampAT61=client.query('SELECT last("amps_AP1_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qampAT62=client.query('SELECT last("amps_AP2_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qampAT63=client.query('SELECT last("amps_AP3_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qampAT64=client.query('SELECT last("amps_AP4_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qampHMMY=client.query('SELECT last("amps_AP5_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP1=client.query('SELECT last("amps_AP1_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP2=client.query('SELECT last("amps_AP2_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP3=client.query('SELECT last("amps_AP3_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP4=client.query('SELECT last("amps_AP4_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP5=client.query('SELECT last("amps_AP5_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP6=client.query('SELECT last("amps_AP6_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_MY7=client.query('SELECT last("amps_PUL#7F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_MY8=client.query('SELECT last("amps_PUL#8F") FROM "grinding_1" GROUP BY "grinding_1"')
        
       

        # todo point kwhAir Floor1
        points_ampshrimp.append(qampMY1.get_points(tags={'grinding_1': ''})) #index0
        points_ampshrimp.append(qampMY2.get_points(tags={'grinding_1': ''})) #index1
        points_ampshrimp.append(qampMY3.get_points(tags={'grinding_1': ''})) #index2
        points_ampshrimp.append(qampMY4.get_points(tags={'grinding_1': ''})) #index3
        points_ampshrimp.append(qampMY5.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampMY6.get_points(tags={'grinding_1': ''})) #index5
        points_ampshrimp.append(qampMY7.get_points(tags={'grinding_1': ''})) #index6
        points_ampshrimp.append(qampMY8.get_points(tags={'grinding_1': ''})) #index7
        points_ampshrimp.append(qampMY9.get_points(tags={'grinding_1': ''})) #index8
        points_ampshrimp.append(qampMY10.get_points(tags={'grinding_1': ''})) #index9
        points_ampshrimp.append(qampMY11.get_points(tags={'grinding_1': ''})) #index10
        points_ampshrimp.append(qampMY12.get_points(tags={'grinding_1': ''})) #index11
        points_ampshrimp.append(qampAT61.get_points(tags={'grinding_1': ''})) #index12
        points_ampshrimp.append(qampAT62.get_points(tags={'grinding_1': ''})) #index13
        points_ampshrimp.append(qampAT63.get_points(tags={'grinding_1': ''})) #index14
        points_ampshrimp.append(qampAT64.get_points(tags={'grinding_1': ''})) #index15
        points_ampshrimp.append(qampHMMY.get_points(tags={'grinding_1': ''})) #index16
        points_ampshrimp.append(qampF_AP1.get_points(tags={'grinding_1': ''})) #index17
        points_ampshrimp.append(qampF_AP2.get_points(tags={'grinding_1': ''})) #index18
        points_ampshrimp.append(qampF_AP3.get_points(tags={'grinding_1': ''})) #index19
        points_ampshrimp.append(qampF_AP4.get_points(tags={'grinding_1': ''})) #index20
        points_ampshrimp.append(qampF_AP5.get_points(tags={'grinding_1': ''})) #index21
        points_ampshrimp.append(qampF_AP6.get_points(tags={'grinding_1': ''})) #index22
        points_ampshrimp.append(qampF_MY7.get_points(tags={'grinding_1': ''})) #index23
        points_ampshrimp.append(qampF_MY8.get_points(tags={'grinding_1': ''})) #index24
  
        for amp in points_ampshrimp:
            for i in amp: 
                time.append(i['time'])
                List_ampshrimp.append(i['last'])

        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "labels":labels,
                "time": upd_time,
                "shrimGriding" : List_ampshrimp,
            }
        return Response(data)