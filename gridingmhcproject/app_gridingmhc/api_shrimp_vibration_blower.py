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

class api_shrimp_vibration_blower(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_shrimp_vibration_x_blower =[]
        List_shrimp_vibration_x_blower =[]
        points_shrimp_vibration_y_blower =[]
        List_shrimp_vibration_y_blower =[]
        points_shrimp_vibration_z_blower =[]
        List_shrimp_vibration_z_blower =[]

        #!Vibration x
        qvibration_x_MY1=client.query('SELECT last("mainshaft_bw_pul1_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY2=client.query('SELECT last("mainshaft_bw_pul2_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY3=client.query('SELECT last("mainshaft_bw_pul3_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY4=client.query('SELECT last("mainshaft_bw_pul4_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY5=client.query('SELECT last("mainshaft_bw_pul5_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY6=client.query('SELECT last("mainshaft_bw_pul6_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY7=client.query('SELECT last("mainshaft_bw_pul7_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY8=client.query('SELECT last("mainshaft_bw_pul8_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY9=client.query('SELECT last("mainshaft_bw_pul9_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY10=client.query('SELECT last("mainshaft_bw_pul10_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY11=client.query('SELECT last("mainshaft_bw_pul11_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_MY12=client.query('SELECT last("mainshaft_bw_pul12_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AT1=client.query('SELECT last("mainshaft_bw_at6-1cgs_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AT2=client.query('SELECT last("mainshaft_bw_at6-2cgs_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AT3=client.query('SELECT last("mainshaft_bw_at6-3cgs_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_AT4=client.query('SELECT last("mainshaft_bw_at6-4cgs_mhc2_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_x_HM2=client.query('SELECT last("mainshaft_HM2_C_vibra_x1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration x
        points_shrimp_vibration_x_blower.append(qvibration_x_MY1.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY2.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY3.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY4.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY5.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY6.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY7.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY8.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY9.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY10.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY11.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_MY12.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_AT1.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_AT2.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_AT3.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_AT4.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_vibration_x_blower.append(qvibration_x_HM2.get_points(tags={'grinding_1': ''})) #index0


        #!Vibration y
        qvibration_y_MY1=client.query('SELECT last("mainshaft_bw_pul1_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY2=client.query('SELECT last("mainshaft_bw_pul2_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY3=client.query('SELECT last("mainshaft_bw_pul3_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY4=client.query('SELECT last("mainshaft_bw_pul4_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY5=client.query('SELECT last("mainshaft_bw_pul5_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY6=client.query('SELECT last("mainshaft_bw_pul6_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY7=client.query('SELECT last("mainshaft_bw_pul7_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY8=client.query('SELECT last("mainshaft_bw_pul8_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY9=client.query('SELECT last("mainshaft_bw_pul9_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY10=client.query('SELECT last("mainshaft_bw_pul10_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY11=client.query('SELECT last("mainshaft_bw_pul11_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_MY12=client.query('SELECT last("mainshaft_bw_pul12_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AT1=client.query('SELECT last("mainshaft_bw_at6-1cgs_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AT2=client.query('SELECT last("mainshaft_bw_at6-2cgs_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AT3=client.query('SELECT last("mainshaft_bw_at6-3cgs_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_AT4=client.query('SELECT last("mainshaft_bw_at6-4cgs_mhc2_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_y_HM2=client.query('SELECT last("mainshaft_HM2_C_vibra_y1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration y
        points_shrimp_vibration_y_blower.append(qvibration_y_MY1.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY2.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY3.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY4.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY5.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY6.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY7.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY8.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY9.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY10.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY11.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_MY12.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_AT1.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_AT2.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_AT3.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_AT4.get_points(tags={'grinding_1': ''})) #indey0
        points_shrimp_vibration_y_blower.append(qvibration_y_HM2.get_points(tags={'grinding_1': ''})) #indey0
        

        #!Vibration z
        qvibration_z_MY1=client.query('SELECT last("mainshaft_bw_pul1_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY2=client.query('SELECT last("mainshaft_bw_pul2_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY3=client.query('SELECT last("mainshaft_bw_pul3_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY4=client.query('SELECT last("mainshaft_bw_pul4_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY5=client.query('SELECT last("mainshaft_bw_pul5_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY6=client.query('SELECT last("mainshaft_bw_pul6_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY7=client.query('SELECT last("mainshaft_bw_pul7_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY8=client.query('SELECT last("mainshaft_bw_pul8_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY9=client.query('SELECT last("mainshaft_bw_pul9_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY10=client.query('SELECT last("mainshaft_bw_pul10_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY11=client.query('SELECT last("mainshaft_bw_pul11_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_MY12=client.query('SELECT last("mainshaft_bw_pul12_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AT1=client.query('SELECT last("mainshaft_bw_at6-1cgs_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AT2=client.query('SELECT last("mainshaft_bw_at6-2cgs_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AT3=client.query('SELECT last("mainshaft_bw_at6-3cgs_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_AT4=client.query('SELECT last("mainshaft_bw_at6-4cgs_mhc2_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        qvibration_z_HM2=client.query('SELECT last("mainshaft_HM2_C_vibra_z1") FROM "grinding_1" GROUP BY "grinding_1"')
        
        # todo point Vibration z
        points_shrimp_vibration_z_blower.append(qvibration_z_MY1.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY2.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY3.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY4.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY5.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY6.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY7.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY8.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY9.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY10.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY11.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_MY12.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_AT1.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_AT2.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_AT3.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_AT4.get_points(tags={'grinding_1': ''})) #indez0
        points_shrimp_vibration_z_blower.append(qvibration_z_HM2.get_points(tags={'grinding_1': ''})) #indez0
        
  
        for vibration_x in points_shrimp_vibration_x_blower:
            for i in vibration_x: 
                time.append(i['time'])
                List_shrimp_vibration_x_blower.append(i['last'])
        
        for vibration_y in points_shrimp_vibration_y_blower:
            for i in vibration_y: 
                time.append(i['time'])
                List_shrimp_vibration_y_blower.append(i['last'])

        for vibration_z in points_shrimp_vibration_z_blower:
            for i in vibration_z: 
                time.append(i['time'])
                List_shrimp_vibration_z_blower.append(i['last'])
        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "shrimp_vibration_x_blower" : List_shrimp_vibration_x_blower,
                "shrimp_vibration_y_blower" : List_shrimp_vibration_y_blower,
                "shrimp_vibration_z_blower" : List_shrimp_vibration_z_blower,
            }
        return Response(data)