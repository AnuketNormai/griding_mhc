from django.urls import path
from app_gridingmhc import views
from django.urls import path , include
from django.views.generic.base import TemplateView
from .views import dashboard,dashboard_11,dashboard_12
from .views import fish_tempgrider,fish_temp_bearingblower,fish_vibration_grider,fish_vibration_blower,fish_current_grider,fish_current_blower
from .views import shrimp_tempgrider,shrimp_temp_bearingblower,shrimp_vibration_grider,shrimp_vibration_blower,shrimp_current_grider,shrimp_current_blower
from .api_homedashboard import api_ampshrimp_Data
from .api_utilize import api_Data

from .api_fish_current_grider import api_fish_current_grider
from .api_fish_current_blower import api_fish_current_blower
from .api_fish_temp_bearingblower import api_fish_temp_bearingblower
from .api_fish_temp_grider import api_fish_temp_grider
from .api_fish_vibration_grider import api_fish_vibration_grider
from .api_fish_vibration_blower import api_fish_vibration_blower

from .api_shrimp_current_blower import api_shrimp_current_blower
from .api_shrimp_current_grider import api_shrimp_current_grider
from .api_shrimp_temp_bearingblower import api_shrimp_temp_bearingblower
from .api_shrimp_temp_grider import api_shrimp_temp_grider
from .api_shrimp_vibration_grider import api_shrimp_vibration_grider
from .api_shrimp_vibration_blower import api_shrimp_vibration_blower


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('',TemplateView.as_view(template_name='home.html'), name='home'),
    # API Fish
    path('api/data',api_Data.as_view()),   
    path('api/fish_current_grider',api_fish_current_grider.as_view()),
    path('api/fish_current_blower',api_fish_current_blower.as_view()),
    path('api/fish_temp_bearingblower',api_fish_temp_bearingblower.as_view()),
    path('api/fish_temp_grider',api_fish_temp_grider.as_view()),
    path('api/fish_vibration_grider',api_fish_vibration_grider.as_view()),
    path('api/fish_vibration_blower',api_fish_vibration_blower.as_view()),
    # API shrimp
    path('api/ampshrimp',api_ampshrimp_Data.as_view()),
    path('api/shrimp_current_blower',api_shrimp_current_blower.as_view()),
    path('api/shrimp_current_grider',api_shrimp_current_grider.as_view()),
    path('api/shrimp_temp_bearingblower',api_shrimp_temp_bearingblower.as_view()),
    path('api/shrimp_temp_grider',api_shrimp_temp_grider.as_view()),
    path('api/shrimp_vibration_grider',api_shrimp_vibration_grider.as_view()),
    path('api/shrimp_vibration_blower',api_shrimp_vibration_blower.as_view()),


    # Line Testing
    path('dashboard',dashboard),
    path('dashboard11',dashboard_11),
    path('dashboard12',dashboard_12),
    # Fish sensor
    path('fish_temp_grider',fish_tempgrider),
    path('fish_temp_bearingblower',fish_temp_bearingblower),
    path('fish_vibration_grider',fish_vibration_grider),
    path('fish_vibration_blower',fish_vibration_blower),
    path('fish_current_grider',fish_current_grider),
    path('fish_current_blower',fish_current_blower),
    # Shrimp sensor
    path('shrimp_temp_grider',shrimp_tempgrider),
    path('shrimp_temp_bearingblower',shrimp_temp_bearingblower),
    path('shrimp_vibration_grider',shrimp_vibration_grider),
    path('shrimp_vibration_blower',shrimp_vibration_blower),
    path('shrimp_current_grider',shrimp_current_grider),
    path('shrimp_current_blower',shrimp_current_blower),
    
]

