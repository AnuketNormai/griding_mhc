from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

def login(request):
   return render(request,'griding/register/login.html')

def dashboard(request):
   return render(request,'griding/mhc/home_dashboard.html')

def dashboard_11(request):
   return render(request,'griding/mhc/line11_dashboard.html')

def dashboard_12(request):
   return render(request,'griding/mhc/line12_dashboard.html')
# Fish sensor
def fish_tempgrider(request):
   return render(request,'griding/mhc/chart_fish_temp_grider_page.html')

def fish_temp_bearingblower(request):
   return render(request,'griding/mhc/chart_fish_temp_bearingblower_page.html')

def fish_vibration_grider(request):
   return render(request,'griding/mhc/chart_fish_vibration_grider_page.html')

def fish_vibration_blower(request):
   return render(request,'griding/mhc/chart_fish_vibration_blower_page.html')

def fish_current_grider(request):
   return render(request,'griding/mhc/chart_fish_current_grider_page.html')

def fish_current_blower(request):
   return render(request,'griding/mhc/chart_fish_current_blower_page.html')
# Shrimp sensor
def shrimp_tempgrider(request):
   return render(request,'griding/mhc/chart_shrimp_temp_grider_page.html')

def shrimp_temp_bearingblower(request):
   return render(request,'griding/mhc/chart_shrimp_temp_bearingblower_page.html')

def shrimp_vibration_grider(request):
   return render(request,'griding/mhc/chart_shrimp_vibration_grider_page.html')

def shrimp_vibration_blower(request):
   return render(request,'griding/mhc/chart_shrimp_vibration_blower_page.html')

def shrimp_current_grider(request):
   return render(request,'griding/mhc/chart_shrimp_current_grider_page.html')

def shrimp_current_blower(request):
   return render(request,'griding/mhc/chart_shrimp_current_blower_page.html')







