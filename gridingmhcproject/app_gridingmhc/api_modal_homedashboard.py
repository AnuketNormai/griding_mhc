from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('hm_iot')
client.get_list_measurements()
#print(client.get_list_measurements())
# Create your views here

class api_modalGrider_Data(APIView):
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
        qampAT65=client.query('SELECT last("amps_AP5_C") FROM "grinding_1" GROUP BY "grinding_1"')
        qampAT66=client.query('SELECT last("amps_AP6_C") FROM "grinding_1" GROUP BY "grinding_1"')
       

        # todo point kwhAir Floor1
        points_ampshrimp.append(qampMY1.get_points(tags={'grinding_1': ''})) #index0
        points_ampshrimp.append(qampMY2.get_points(tags={'grinding_1': ''})) #index1
        points_ampshrimp.append(qampMY3.get_points(tags={'grinding_1': ''})) #index2
        points_ampshrimp.append(qampMY4.get_points(tags={'grinding_1': ''})) #index3
        points_ampshrimp.append(qampMY5.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampMY6.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampMY7.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampMY8.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampMY9.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampMY10.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampMY11.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampMY12.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampAT61.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampAT62.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampAT63.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampAT64.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampAT65.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampAT66.get_points(tags={'grinding_1': ''})) #index4
  
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