from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('download/', views.download, name='download'),
    path('download-apk/<int:version_id>/', views.download_apk, name='download_apk'),
    path('screenshots/', views.screenshots, name='screenshots'),
    path('support/', views.support, name='support'),
]
