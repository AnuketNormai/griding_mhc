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

class api_shrimp_temp_grider(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_shrimp_temp_grider =[]
        List_shrimp_temp_grider =[]


        #!kwhAir Floor1 query
        qtempgriderMY1=client.query('SELECT last("outlet_mhcgdpul1temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY2=client.query('SELECT last("outlet_mhcgdpul2temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY3=client.query('SELECT last("outlet_mhcgdpul3temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY4=client.query('SELECT last("outlet_mhcgdpul4temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY5=client.query('SELECT last("outlet_mhcgdpul5temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY6=client.query('SELECT last("outlet_mhcgdpul6temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY7=client.query('SELECT last("outlet_mhcgdpul7temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY8=client.query('SELECT last("outlet_mhcgdpul8temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY9=client.query('SELECT last("outlet_mhcgdpul9temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY10=client.query('SELECT last("outlet_mhcgdpul10temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY11=client.query('SELECT last("outlet_mhcgdpul11temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderMY12=client.query('SELECT last("outlet_mhcgdpul12temp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderAT61=client.query('SELECT last("outlet_AP1_Ctemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderAT62=client.query('SELECT last("outlet_AP2_Ctemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderAT63=client.query('SELECT last("outlet_AP3_Ctemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderAT64=client.query('SELECT last("outlet_AP4_Ctemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempgriderHMMY=client.query('SELECT last("outlet_AP5_Ctemp1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        

        # todo point kwhAir Floor1
        points_shrimp_temp_grider.append(qtempgriderMY1.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY2.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY3.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY4.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY5.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY6.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY7.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY8.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY9.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY10.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY11.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderMY12.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderAT61.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderAT62.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderAT63.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderAT64.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_grider.append(qtempgriderHMMY.get_points(tags={'grinding_1': ''})) #index0
        
        for curent in points_shrimp_temp_grider:
            for i in curent: 
                time.append(i['time'])
                List_shrimp_temp_grider.append(i['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "shrimp_temp_grider" : List_shrimp_temp_grider,
            }
        return Response(data)