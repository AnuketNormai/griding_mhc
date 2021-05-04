from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
print(client.get_list_database())
client.switch_database('hm_iot')
client.get_list_measurements()
# print(client.get_list_measurements())
# Create your views here

class api_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [
            'Normal Load',
            'Light Load',
            'No Load',
            'Offline',   
        ]

        time = []
        points_NormalLoad =[]
        List_normalload =[]
        points_LightLoad =[]
        List_LightLoad = []
        points_NoLoad =[]
        List_NoLoad = []
        points_offline =[]
        List_offline = []
        points_utilize =[]
        List_utilize = []
        points_temp =[]
        List_temp = []
        points_ampshrimp =[]
        List_ampshrimp =[]


        #!Normal Load query
        # todo normal load
        qNormalLoad_MY1=client.query('SELECT last("MY#1_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY2=client.query('SELECT last("MY#2_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY3=client.query('SELECT last("MY#3_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY4=client.query('SELECT last("MY#4_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY5=client.query('SELECT last("MY#5_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY6=client.query('SELECT last("MY#6_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY7=client.query('SELECT last("MY#7_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY8=client.query('SELECT last("MY#8_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY9=client.query('SELECT last("MY#9_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY10=client.query('SELECT last("MY#10_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY11=client.query('SELECT last("MY#11_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_MY12=client.query('SELECT last("MY#12_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_AT61=client.query('SELECT last("AT6#1_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_AT62=client.query('SELECT last("AT6#2_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_AT63=client.query('SELECT last("AT6#3_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_AT64=client.query('SELECT last("AT6#4_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoad_HMMY=client.query('SELECT last("HM-MY_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoadF_AP61=client.query('SELECT last("AP6#1_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoadF_AP62=client.query('SELECT last("AP6#2_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoadF_AP63=client.query('SELECT last("AP6#3_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoadF_AP64=client.query('SELECT last("AP6#4_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoadF_AP65=client.query('SELECT last("AP6#5_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoadF_AP66=client.query('SELECT last("AP6#6_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoadF_MY7=client.query('SELECT last("MY#7F_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNormalLoadF_MY8=client.query('SELECT last("MY#8F_Normal") FROM "grinding-utilize" GROUP BY "mhc-utilize"')

        # todo point list normal load
        points_NormalLoad.append(qNormalLoad_MY1.get_points(tags={'mhc-utilize': ''})) #index0
        points_NormalLoad.append(qNormalLoad_MY2.get_points(tags={'mhc-utilize': ''})) #index1
        points_NormalLoad.append(qNormalLoad_MY3.get_points(tags={'mhc-utilize': ''})) #index2
        points_NormalLoad.append(qNormalLoad_MY4.get_points(tags={'mhc-utilize': ''})) #index3
        points_NormalLoad.append(qNormalLoad_MY5.get_points(tags={'mhc-utilize': ''})) #index4
        points_NormalLoad.append(qNormalLoad_MY6.get_points(tags={'mhc-utilize': ''})) #index5
        points_NormalLoad.append(qNormalLoad_MY7.get_points(tags={'mhc-utilize': ''})) #index6
        points_NormalLoad.append(qNormalLoad_MY8.get_points(tags={'mhc-utilize': ''})) #index7
        points_NormalLoad.append(qNormalLoad_MY9.get_points(tags={'mhc-utilize': ''})) #index8
        points_NormalLoad.append(qNormalLoad_MY10.get_points(tags={'mhc-utilize': ''})) #index9
        points_NormalLoad.append(qNormalLoad_MY11.get_points(tags={'mhc-utilize': ''})) #index10
        points_NormalLoad.append(qNormalLoad_MY12.get_points(tags={'mhc-utilize': ''})) #index11
        points_NormalLoad.append(qNormalLoad_AT61.get_points(tags={'mhc-utilize': ''})) #index12
        points_NormalLoad.append(qNormalLoad_AT62.get_points(tags={'mhc-utilize': ''})) #index13
        points_NormalLoad.append(qNormalLoad_AT63.get_points(tags={'mhc-utilize': ''})) #index14
        points_NormalLoad.append(qNormalLoad_AT64.get_points(tags={'mhc-utilize': ''})) #index15
        points_NormalLoad.append(qNormalLoad_HMMY.get_points(tags={'mhc-utilize': ''})) #index16
        points_NormalLoad.append(qNormalLoadF_AP61.get_points(tags={'mhc-utilize': ''})) #index16
        points_NormalLoad.append(qNormalLoadF_AP62.get_points(tags={'mhc-utilize': ''})) #index16
        points_NormalLoad.append(qNormalLoadF_AP63.get_points(tags={'mhc-utilize': ''})) #index16
        points_NormalLoad.append(qNormalLoadF_AP64.get_points(tags={'mhc-utilize': ''})) #index16
        points_NormalLoad.append(qNormalLoadF_AP65.get_points(tags={'mhc-utilize': ''})) #index16
        points_NormalLoad.append(qNormalLoadF_AP66.get_points(tags={'mhc-utilize': ''})) #index16
        points_NormalLoad.append(qNormalLoadF_MY7.get_points(tags={'mhc-utilize': ''})) #index16
        points_NormalLoad.append(qNormalLoadF_MY8.get_points(tags={'mhc-utilize': ''})) #index16

        #!Light Load query
        # todo Light load
        qLightLoad_MY1=client.query('SELECT last("MY#1_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY2=client.query('SELECT last("MY#2_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY3=client.query('SELECT last("MY#3_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY4=client.query('SELECT last("MY#4_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY5=client.query('SELECT last("MY#5_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY6=client.query('SELECT last("MY#6_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY7=client.query('SELECT last("MY#7_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY8=client.query('SELECT last("MY#8_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY9=client.query('SELECT last("MY#9_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY10=client.query('SELECT last("MY#10_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY11=client.query('SELECT last("MY#11_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_MY12=client.query('SELECT last("MY#12_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_AT61=client.query('SELECT last("AT6#1_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_AT62=client.query('SELECT last("AT6#2_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_AT63=client.query('SELECT last("AT6#3_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_AT64=client.query('SELECT last("AT6#4_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoad_HMMY=client.query('SELECT last("HM-MY_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoadF_AP61=client.query('SELECT last("AP6#1_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoadF_AP62=client.query('SELECT last("AP6#2_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoadF_AP63=client.query('SELECT last("AP6#3_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoadF_AP64=client.query('SELECT last("AP6#4_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoadF_AP65=client.query('SELECT last("AP6#5_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoadF_AP66=client.query('SELECT last("AP6#6_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoadF_MY7=client.query('SELECT last("MY#7F_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qLightLoadF_MY8=client.query('SELECT last("MY#8F_Light") FROM "grinding-utilize" GROUP BY "mhc-utilize"')

        # todo point list Light load
        points_LightLoad.append(qLightLoad_MY1.get_points(tags={'mhc-utilize': ''})) #index0
        points_LightLoad.append(qLightLoad_MY2.get_points(tags={'mhc-utilize': ''})) #index1
        points_LightLoad.append(qLightLoad_MY3.get_points(tags={'mhc-utilize': ''})) #index2
        points_LightLoad.append(qLightLoad_MY4.get_points(tags={'mhc-utilize': ''})) #index3
        points_LightLoad.append(qLightLoad_MY5.get_points(tags={'mhc-utilize': ''})) #index4
        points_LightLoad.append(qLightLoad_MY6.get_points(tags={'mhc-utilize': ''})) #index5
        points_LightLoad.append(qLightLoad_MY7.get_points(tags={'mhc-utilize': ''})) #index6
        points_LightLoad.append(qLightLoad_MY8.get_points(tags={'mhc-utilize': ''})) #index7
        points_LightLoad.append(qLightLoad_MY9.get_points(tags={'mhc-utilize': ''})) #index8
        points_LightLoad.append(qLightLoad_MY10.get_points(tags={'mhc-utilize': ''})) #index9
        points_LightLoad.append(qLightLoad_MY11.get_points(tags={'mhc-utilize': ''})) #index10
        points_LightLoad.append(qLightLoad_MY12.get_points(tags={'mhc-utilize': ''})) #index11
        points_LightLoad.append(qLightLoad_AT61.get_points(tags={'mhc-utilize': ''})) #index12
        points_LightLoad.append(qLightLoad_AT62.get_points(tags={'mhc-utilize': ''})) #index13
        points_LightLoad.append(qLightLoad_AT63.get_points(tags={'mhc-utilize': ''})) #index14
        points_LightLoad.append(qLightLoad_AT64.get_points(tags={'mhc-utilize': ''})) #index15
        points_LightLoad.append(qLightLoad_HMMY.get_points(tags={'mhc-utilize': ''})) #index15
        points_LightLoad.append(qLightLoadF_AP61.get_points(tags={'mhc-utilize': ''})) #index16
        points_LightLoad.append(qLightLoadF_AP62.get_points(tags={'mhc-utilize': ''})) #index16
        points_LightLoad.append(qLightLoadF_AP63.get_points(tags={'mhc-utilize': ''})) #index16
        points_LightLoad.append(qLightLoadF_AP64.get_points(tags={'mhc-utilize': ''})) #index16
        points_LightLoad.append(qLightLoadF_AP65.get_points(tags={'mhc-utilize': ''})) #index16
        points_LightLoad.append(qLightLoadF_AP66.get_points(tags={'mhc-utilize': ''})) #index16
        points_LightLoad.append(qLightLoadF_MY7.get_points(tags={'mhc-utilize': ''})) #index16
        points_LightLoad.append(qLightLoadF_MY8.get_points(tags={'mhc-utilize': ''})) #index16

        #!No Load query
        # todo Light load
        qNoLoad_MY1=client.query('SELECT last("MY#1_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY2=client.query('SELECT last("MY#2_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY3=client.query('SELECT last("MY#3_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY4=client.query('SELECT last("MY#4_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY5=client.query('SELECT last("MY#5_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY6=client.query('SELECT last("MY#6_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY7=client.query('SELECT last("MY#7_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY8=client.query('SELECT last("MY#8_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY9=client.query('SELECT last("MY#9_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY10=client.query('SELECT last("MY#10_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY11=client.query('SELECT last("MY#11_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_MY12=client.query('SELECT last("MY#12_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_AT61=client.query('SELECT last("AT6#1_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_AT62=client.query('SELECT last("AT6#2_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_AT63=client.query('SELECT last("AT6#3_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_AT64=client.query('SELECT last("AT6#4_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoad_HMMY=client.query('SELECT last("HM-MY_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoadF_AP61=client.query('SELECT last("AP6#1_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoadF_AP62=client.query('SELECT last("AP6#2_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoadF_AP63=client.query('SELECT last("AP6#3_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoadF_AP64=client.query('SELECT last("AP6#4_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoadF_AP65=client.query('SELECT last("AP6#5_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoadF_AP66=client.query('SELECT last("AP6#6_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoadF_MY7=client.query('SELECT last("MY#7F_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qNoLoadF_MY8=client.query('SELECT last("MY#8F_NoLoad") FROM "grinding-utilize" GROUP BY "mhc-utilize"')

        # todo point list No load
        points_NoLoad.append(qNoLoad_MY1.get_points(tags={'mhc-utilize': ''})) #index0
        points_NoLoad.append(qNoLoad_MY2.get_points(tags={'mhc-utilize': ''})) #index1
        points_NoLoad.append(qNoLoad_MY3.get_points(tags={'mhc-utilize': ''})) #index2
        points_NoLoad.append(qNoLoad_MY4.get_points(tags={'mhc-utilize': ''})) #index3
        points_NoLoad.append(qNoLoad_MY5.get_points(tags={'mhc-utilize': ''})) #index4
        points_NoLoad.append(qNoLoad_MY6.get_points(tags={'mhc-utilize': ''})) #index5
        points_NoLoad.append(qNoLoad_MY7.get_points(tags={'mhc-utilize': ''})) #index6
        points_NoLoad.append(qNoLoad_MY8.get_points(tags={'mhc-utilize': ''})) #index7
        points_NoLoad.append(qNoLoad_MY9.get_points(tags={'mhc-utilize': ''})) #index8
        points_NoLoad.append(qNoLoad_MY10.get_points(tags={'mhc-utilize': ''})) #index9
        points_NoLoad.append(qNoLoad_MY11.get_points(tags={'mhc-utilize': ''})) #index10
        points_NoLoad.append(qNoLoad_MY12.get_points(tags={'mhc-utilize': ''})) #index11
        points_NoLoad.append(qNoLoad_AT61.get_points(tags={'mhc-utilize': ''})) #index12
        points_NoLoad.append(qNoLoad_AT62.get_points(tags={'mhc-utilize': ''})) #index13
        points_NoLoad.append(qNoLoad_AT63.get_points(tags={'mhc-utilize': ''})) #index14
        points_NoLoad.append(qNoLoad_AT64.get_points(tags={'mhc-utilize': ''})) #index15
        points_NoLoad.append(qNoLoad_HMMY.get_points(tags={'mhc-utilize': ''})) #index15
        points_NoLoad.append(qNoLoadF_AP61.get_points(tags={'mhc-utilize': ''})) #index16
        points_NoLoad.append(qNoLoadF_AP62.get_points(tags={'mhc-utilize': ''})) #index16
        points_NoLoad.append(qNoLoadF_AP63.get_points(tags={'mhc-utilize': ''})) #index16
        points_NoLoad.append(qNoLoadF_AP64.get_points(tags={'mhc-utilize': ''})) #index16
        points_NoLoad.append(qNoLoadF_AP65.get_points(tags={'mhc-utilize': ''})) #index16
        points_NoLoad.append(qNoLoadF_AP66.get_points(tags={'mhc-utilize': ''})) #index16
        points_NoLoad.append(qNoLoadF_MY7.get_points(tags={'mhc-utilize': ''})) #index16
        points_NoLoad.append(qNoLoadF_MY8.get_points(tags={'mhc-utilize': ''})) #index16

        #!Offline query
        # todo Offline
        qoffLine_MY1=client.query('SELECT last("MY#1_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY2=client.query('SELECT last("MY#2_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY3=client.query('SELECT last("MY#3_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY4=client.query('SELECT last("MY#4_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY5=client.query('SELECT last("MY#5_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY6=client.query('SELECT last("MY#6_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY7=client.query('SELECT last("MY#7_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY8=client.query('SELECT last("MY#8_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY9=client.query('SELECT last("MY#9_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY10=client.query('SELECT last("MY#10_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY11=client.query('SELECT last("MY#11_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_MY12=client.query('SELECT last("MY#12_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_AT61=client.query('SELECT last("AT6#1_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_AT62=client.query('SELECT last("AT6#2_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_AT63=client.query('SELECT last("AT6#3_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_AT64=client.query('SELECT last("AT6#4_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLine_HMMY=client.query('SELECT last("HM-MY_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLineF_AP61=client.query('SELECT last("AP6#1_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLineF_AP62=client.query('SELECT last("AP6#2_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLineF_AP63=client.query('SELECT last("AP6#3_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLineF_AP64=client.query('SELECT last("AP6#4_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLineF_AP65=client.query('SELECT last("AP6#5_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLineF_AP66=client.query('SELECT last("AP6#6_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLineF_MY7=client.query('SELECT last("MY#7F_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qoffLineF_MY8=client.query('SELECT last("MY#8F_offLine") FROM "grinding-utilize" GROUP BY "mhc-utilize"')

        # todo point list No load
        points_offline.append(qoffLine_MY1.get_points(tags={'mhc-utilize': ''})) #index0
        points_offline.append(qoffLine_MY2.get_points(tags={'mhc-utilize': ''})) #index1
        points_offline.append(qoffLine_MY3.get_points(tags={'mhc-utilize': ''})) #index2
        points_offline.append(qoffLine_MY4.get_points(tags={'mhc-utilize': ''})) #index3
        points_offline.append(qoffLine_MY5.get_points(tags={'mhc-utilize': ''})) #index4
        points_offline.append(qoffLine_MY6.get_points(tags={'mhc-utilize': ''})) #index5
        points_offline.append(qoffLine_MY7.get_points(tags={'mhc-utilize': ''})) #index6
        points_offline.append(qoffLine_MY8.get_points(tags={'mhc-utilize': ''})) #index7
        points_offline.append(qoffLine_MY9.get_points(tags={'mhc-utilize': ''})) #index8
        points_offline.append(qoffLine_MY10.get_points(tags={'mhc-utilize': ''})) #index9
        points_offline.append(qoffLine_MY11.get_points(tags={'mhc-utilize': ''})) #index10
        points_offline.append(qoffLine_MY12.get_points(tags={'mhc-utilize': ''})) #index11
        points_offline.append(qoffLine_AT61.get_points(tags={'mhc-utilize': ''})) #index12
        points_offline.append(qoffLine_AT62.get_points(tags={'mhc-utilize': ''})) #index13
        points_offline.append(qoffLine_AT63.get_points(tags={'mhc-utilize': ''})) #index14
        points_offline.append(qoffLine_AT64.get_points(tags={'mhc-utilize': ''})) #index15
        points_offline.append(qoffLine_HMMY.get_points(tags={'mhc-utilize': ''})) #index15
        points_offline.append(qoffLineF_AP61.get_points(tags={'mhc-utilize': ''})) #index16
        points_offline.append(qoffLineF_AP62.get_points(tags={'mhc-utilize': ''})) #index16
        points_offline.append(qoffLineF_AP63.get_points(tags={'mhc-utilize': ''})) #index16
        points_offline.append(qoffLineF_AP64.get_points(tags={'mhc-utilize': ''})) #index16
        points_offline.append(qoffLineF_AP65.get_points(tags={'mhc-utilize': ''})) #index16
        points_offline.append(qoffLineF_AP66.get_points(tags={'mhc-utilize': ''})) #index16
        points_offline.append(qoffLineF_MY7.get_points(tags={'mhc-utilize': ''})) #index16
        points_offline.append(qoffLineF_MY8.get_points(tags={'mhc-utilize': ''})) #index16

        #!utilize query
        # todo utilize
        qutilize_MY1=client.query('SELECT last("MY#1_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY2=client.query('SELECT last("MY#2_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY3=client.query('SELECT last("MY#3_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY4=client.query('SELECT last("MY#4_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY5=client.query('SELECT last("MY#5_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY6=client.query('SELECT last("MY#6_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY7=client.query('SELECT last("MY#7_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY8=client.query('SELECT last("MY#8_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY9=client.query('SELECT last("MY#9_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY10=client.query('SELECT last("MY#10_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY11=client.query('SELECT last("MY#11_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_MY12=client.query('SELECT last("MY#12_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_AT61=client.query('SELECT last("AT6#1_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_AT62=client.query('SELECT last("AT6#2_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_AT63=client.query('SELECT last("AT6#3_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_AT64=client.query('SELECT last("AT6#4_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilize_HMMY=client.query('SELECT last("HM-MY_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilizeF_AP61=client.query('SELECT last("AP6#1_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilizeF_AP62=client.query('SELECT last("AP6#2_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilizeF_AP63=client.query('SELECT last("AP6#3_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilizeF_AP64=client.query('SELECT last("AP6#4_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilizeF_AP65=client.query('SELECT last("AP6#5_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilizeF_AP66=client.query('SELECT last("AP6#6_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilizeF_MY7=client.query('SELECT last("MY#7F_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        qutilizeF_MY8=client.query('SELECT last("MY#8F_Utilize") FROM "grinding-utilize" GROUP BY "mhc-utilize"')
        

        # todo point list utilize
        points_utilize.append(qutilize_MY1.get_points(tags={'mhc-utilize': ''})) #index0
        points_utilize.append(qutilize_MY2.get_points(tags={'mhc-utilize': ''})) #index1
        points_utilize.append(qutilize_MY3.get_points(tags={'mhc-utilize': ''})) #index2
        points_utilize.append(qutilize_MY4.get_points(tags={'mhc-utilize': ''})) #index3
        points_utilize.append(qutilize_MY5.get_points(tags={'mhc-utilize': ''})) #index4
        points_utilize.append(qutilize_MY6.get_points(tags={'mhc-utilize': ''})) #index5
        points_utilize.append(qutilize_MY7.get_points(tags={'mhc-utilize': ''})) #index6
        points_utilize.append(qutilize_MY8.get_points(tags={'mhc-utilize': ''})) #index7
        points_utilize.append(qutilize_MY9.get_points(tags={'mhc-utilize': ''})) #index8
        points_utilize.append(qutilize_MY10.get_points(tags={'mhc-utilize': ''})) #index9
        points_utilize.append(qutilize_MY11.get_points(tags={'mhc-utilize': ''})) #index10
        points_utilize.append(qutilize_MY12.get_points(tags={'mhc-utilize': ''})) #index11
        points_utilize.append(qutilize_AT61.get_points(tags={'mhc-utilize': ''})) #index12
        points_utilize.append(qutilize_AT62.get_points(tags={'mhc-utilize': ''})) #index13
        points_utilize.append(qutilize_AT63.get_points(tags={'mhc-utilize': ''})) #index14
        points_utilize.append(qutilize_AT64.get_points(tags={'mhc-utilize': ''})) #index15
        points_utilize.append(qutilize_HMMY.get_points(tags={'mhc-utilize': ''})) #index15
        points_utilize.append(qutilizeF_AP61.get_points(tags={'mhc-utilize': ''})) #index16
        points_utilize.append(qutilizeF_AP62.get_points(tags={'mhc-utilize': ''})) #index16
        points_utilize.append(qutilizeF_AP63.get_points(tags={'mhc-utilize': ''})) #index16
        points_utilize.append(qutilizeF_AP64.get_points(tags={'mhc-utilize': ''})) #index16
        points_utilize.append(qutilizeF_AP65.get_points(tags={'mhc-utilize': ''})) #index16
        points_utilize.append(qutilizeF_AP66.get_points(tags={'mhc-utilize': ''})) #index16
        points_utilize.append(qutilizeF_MY7.get_points(tags={'mhc-utilize': ''})) #index16
        points_utilize.append(qutilizeF_MY8.get_points(tags={'mhc-utilize': ''})) #index16

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
        qampF_AP61=client.query('SELECT last("amps_AP1_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP62=client.query('SELECT last("amps_AP2_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP63=client.query('SELECT last("amps_AP3_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP64=client.query('SELECT last("amps_AP4_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP65=client.query('SELECT last("amps_AP5_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_AP66=client.query('SELECT last("amps_AP6_F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_MY7=client.query('SELECT last("amps_PUL#7F") FROM "grinding_1" GROUP BY "grinding_1"')
        qampF_MY8=client.query('SELECT last("amps_PUL#8F") FROM "grinding_1" GROUP BY "grinding_1"')

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
        points_ampshrimp.append(qampHMMY.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampF_AP61.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampF_AP62.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampF_AP63.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampF_AP64.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampF_AP65.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampF_AP66.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampF_MY7.get_points(tags={'grinding_1': ''})) #index4
        points_ampshrimp.append(qampF_MY8.get_points(tags={'grinding_1': ''})) #index4

        
        for normalload in points_NormalLoad:
            for i in normalload:
                time.append(i['time'])
                List_normalload.append(i['last'])
        
        for lightload in points_LightLoad:
            for j in lightload:
                List_LightLoad.append(j['last'])
        
        for noload in points_NoLoad:
            for k in noload:
                List_NoLoad.append(k['last'])

        for offline in points_offline:
            for l in offline:
                List_offline.append(l['last'])

        for utilize in points_utilize:
            for m in utilize:
                List_utilize.append(m['last'])

        for amp in points_ampshrimp:
            for m in amp:
                List_ampshrimp.append(m['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
            "labels":labels,
            "time": upd_time,
            "normalload": List_normalload,
            "lightload" : List_LightLoad,
            "noload" : List_NoLoad,
            "offline" : List_offline,
            "utilize" : List_utilize,
            "amp" : List_ampshrimp

        }
        return Response(data)


