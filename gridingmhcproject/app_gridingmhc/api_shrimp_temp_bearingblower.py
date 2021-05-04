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

class api_shrimp_temp_bearingblower(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        time = []
        points_shrimp_temp_bearingblower =[]
        List_shrimp_temp_bearingblower =[]


        #!Temp 1
        qtempbearingblowerMY11=client.query('SELECT last("t_bw_pul1_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY12=client.query('SELECT last("t_bw_pul1_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY21=client.query('SELECT last("t_bw_pul2_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY22=client.query('SELECT last("t_bw_pul2_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY31=client.query('SELECT last("t_bw_pul3_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY32=client.query('SELECT last("t_bw_pul3_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY41=client.query('SELECT last("t_bw_pul4_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY42=client.query('SELECT last("t_bw_pul4_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY51=client.query('SELECT last("t_bw_pul5_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY52=client.query('SELECT last("t_bw_pul5_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY61=client.query('SELECT last("t_bw_pul6_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY62=client.query('SELECT last("t_bw_pul6_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY71=client.query('SELECT last("t_bw_pul7_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY72=client.query('SELECT last("t_bw_pul7_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY81=client.query('SELECT last("t_bw_pul8_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY82=client.query('SELECT last("t_bw_pul8_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY91=client.query('SELECT last("t_bw_pul9_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY92=client.query('SELECT last("t_bw_pul9_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY101=client.query('SELECT last("t_bw_pul10_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY102=client.query('SELECT last("t_bw_pul10_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY111=client.query('SELECT last("t_bw_pul11_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY112=client.query('SELECT last("t_bw_pul11_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerMY121=client.query('SELECT last("t_bw_pul12_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerMY122=client.query('SELECT last("t_bw_pul12_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerAT11=client.query('SELECT last("t_bw_at6-1cgs_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAT12=client.query('SELECT last("t_bw_at6-1cgs_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerAT21=client.query('SELECT last("t_bw_at6-2cgs_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAT22=client.query('SELECT last("t_bw_at6-2cgs_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerAT31=client.query('SELECT last("t_bw_at6-3cgs_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAT32=client.query('SELECT last("t_bw_at6-3cgs_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')

        qtempbearingblowerAT41=client.query('SELECT last("t_bw_at6-4cgs_mhc2-1") FROM "grinding_1" GROUP BY "grinding_1"')
        qtempbearingblowerAT42=client.query('SELECT last("t_bw_at6-4cgs_mhc2-2") FROM "grinding_1" GROUP BY "grinding_1"')
        
        
        
        # todo point kwhAir Floor1
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY11.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY12.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY21.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY22.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY31.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY32.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY41.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY42.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY51.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY52.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY61.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY62.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY71.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY72.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY81.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY82.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY91.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY92.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY101.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY102.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY111.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY112.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY121.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerMY122.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerAT11.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerAT12.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerAT21.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerAT22.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerAT31.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerAT32.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerAT41.get_points(tags={'grinding_1': ''})) #index0
        points_shrimp_temp_bearingblower.append(qtempbearingblowerAT42.get_points(tags={'grinding_1': ''})) #index0
        
        for curent in points_shrimp_temp_bearingblower:
            for i in curent: 
                time.append(i['time'])
                List_shrimp_temp_bearingblower.append(i['last'])

        
        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "time": upd_time,
                "shrimp_temp_bearingblower" : List_shrimp_temp_bearingblower,
            }
        return Response(data)