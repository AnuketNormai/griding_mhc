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

class api_shrimp_vibration_grider(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_shrimp_vibration_x_grider =[]
        List_shrimp_vibration_x_grider =[]
        points_shrimp_vibration_y_grider =[]
        List_shrimp_vibration_y_grider =[]
        points_shrimp_vibration_z_grider =[]
        List_shrimp_vibration_z_grider =[]

        #!Vibration x
        qvibration_x_MY1=client.query('SELECT last("mainshaft_mhcgdpul1_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY2=client.query('SELECT last("mainshaft_mhcgdpul2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY3=client.query('SELECT last("mainshaft_mhcgdpul3_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY4=client.query('SELECT last("mainshaft_mhcgdpul4_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY5=client.query('SELECT last("mainshaft_mhcgdpul5_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY6=client.query('SELECT last("mainshaft_mhcgdpul6_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY7=client.query('SELECT last("mainshaft_mhcgdpul7_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY8=client.query('SELECT last("mainshaft_mhcgdpul8_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY9=client.query('SELECT last("mainshaft_mhcgdpul9_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY10=client.query('SELECT last("mainshaft_mhcgdpul10_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY11=client.query('SELECT last("mainshaft_mhcgdpul11_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY12=client.query('SELECT last("mainshaft_mhcgdpul12_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AT1=client.query('SELECT last("mainshaft_AP1_C_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AT2=client.query('SELECT last("mainshaft_AP2_C_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AT4=client.query('SELECT last("mainshaft_AP4_C_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_HM2=client.query('SELECT last("mainshaft_HM2_C_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration x
        points_shrimp_vibration_x_grider.append(qvibration_x_MY1.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY2.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY3.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY4.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY5.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY6.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY7.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY8.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY9.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY10.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY11.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_MY12.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_AT1.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_AT2.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_AT4.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_grider.append(qvibration_x_HM2.get_points(tags={'grinding_1': ''})) #index0


        #!Vibration y
        qvibration_y_MY1=client.query('SELECT last("mainshaft_mhcgdpul1_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY2=client.query('SELECT last("mainshaft_mhcgdpul2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY3=client.query('SELECT last("mainshaft_mhcgdpul3_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY4=client.query('SELECT last("mainshaft_mhcgdpul4_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY5=client.query('SELECT last("mainshaft_mhcgdpul5_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY6=client.query('SELECT last("mainshaft_mhcgdpul6_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY7=client.query('SELECT last("mainshaft_mhcgdpul7_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY8=client.query('SELECT last("mainshaft_mhcgdpul8_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY9=client.query('SELECT last("mainshaft_mhcgdpul9_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY10=client.query('SELECT last("mainshaft_mhcgdpul10_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY11=client.query('SELECT last("mainshaft_mhcgdpul11_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY12=client.query('SELECT last("mainshaft_mhcgdpul12_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AT1=client.query('SELECT last("mainshaft_AP1_C_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AT2=client.query('SELECT last("mainshaft_AP2_C_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AT4=client.query('SELECT last("mainshaft_AP4_C_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_HM2=client.query('SELECT last("mainshaft_HM2_C_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration y
        points_shrimp_vibration_y_grider.append(qvibration_y_MY1.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY2.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY3.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY4.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY5.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY6.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY7.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY8.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY9.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY10.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY11.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_MY12.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_AT1.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_AT2.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_AT4.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_grider.append(qvibration_y_HM2.get_points(tags={'grinding_1': ''})) #indey0
        

        #!Vibration z
        qvibration_z_MY1=client.query('SELECT last("mainshaft_mhcgdpul1_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY2=client.query('SELECT last("mainshaft_mhcgdpul2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY3=client.query('SELECT last("mainshaft_mhcgdpul3_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY4=client.query('SELECT last("mainshaft_mhcgdpul4_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY5=client.query('SELECT last("mainshaft_mhcgdpul5_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY6=client.query('SELECT last("mainshaft_mhcgdpul6_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY7=client.query('SELECT last("mainshaft_mhcgdpul7_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY8=client.query('SELECT last("mainshaft_mhcgdpul8_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY9=client.query('SELECT last("mainshaft_mhcgdpul9_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY10=client.query('SELECT last("mainshaft_mhcgdpul10_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY11=client.query('SELECT last("mainshaft_mhcgdpul11_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY12=client.query('SELECT last("mainshaft_mhcgdpul12_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AT1=client.query('SELECT last("mainshaft_AP1_C_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AT2=client.query('SELECT last("mainshaft_AP2_C_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AT4=client.query('SELECT last("mainshaft_AP4_C_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_HM2=client.query('SELECT last("mainshaft_HM2_C_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration z
        points_shrimp_vibration_z_grider.append(qvibration_z_MY1.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY2.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY3.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY4.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY5.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY6.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY7.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY8.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY9.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY10.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY11.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_MY12.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_AT1.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_AT2.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_AT4.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_grider.append(qvibration_z_HM2.get_points(tags={'grinding_1': ''})) #indez0
        
  
        for vibration_x in points_shrimp_vibration_x_grider:
            for i in vibration_x: 
                time.append(i['time'])
                List_shrimp_vibration_x_grider.append(i['last'])
        
        for vibration_y in points_shrimp_vibration_y_grider:
            for i in vibration_y: 
                time.append(i['time'])
                List_shrimp_vibration_y_grider.append(i['last'])

        for vibration_z in points_shrimp_vibration_z_grider:
            for i in vibration_z: 
                time.append(i['time'])
                List_shrimp_vibration_z_grider.append(i['last'])
        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "shrimp_vibration_x_grider" : List_shrimp_vibration_x_grider,
                "shrimp_vibration_y_grider" : List_shrimp_vibration_y_grider,
                "shrimp_vibration_z_grider" : List_shrimp_vibration_z_grider,
            }
        return Response(data)