"""nsu_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from nsuapp import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render



   
# def index_view(request):
#     return render(request,'dist/index.html')
urlpatterns = [
    # path('',index_view, name='index'),
    path('admin/', admin.site.urls),
    path('nsu/', views.StudentList.as_view()),
    path('nsu/<int:pk>/', views.StudentDetail.as_view()),
    path('female/', views.FemaleList.as_view()),
    path('female/<int:pk>/', views.FemaleDetail.as_view()),
    path('adm/', views.AdminList.as_view()),
    path('attend/', views.AttendList.as_view()),
     path('attend/<int:pk>/', views.AttendDetail.as_view()),
    
     path('attending/', views.AttendanceSearch.as_view(),name='attendancebydate'),
     path('pres/', views.SpeechList.as_view()),
    path('pres/<int:pk>/', views.SpeechDetail.as_view()),
    path('logo/', views.LogoList.as_view()),
    path('logo/<int:pk>/', views.LogoDetail.as_view()),
    
    path('port/', views.PortfolioList.as_view()),
    path('port/<int:pk>/', views.PortfolioDetail.as_view()),
    path('event/', views.RecentEventList.as_view()),
    path('event/<int:pk>/', views.RecentEventDetail.as_view()),
     path('upcoming/', views.UpComingEventList.as_view()),
    path('upcoming/<int:pk>/', views.UpComingEventDetail.as_view()),
    
    
    path('api-auth/', include('rest_framework.urls')),
    path('login/', views.student_login),
    path('check/', views.check_otp),
    path('forgot/', views.forgot_login),
    
    path('verify/', views.forgot_otp),
    path('verifyfemale/', views.forgot_otpf),
    path('editpass/<int:pk>/', views.edit_model), 
    path('editpassf/<int:pk>/', views. edit_modelfemale),
    path('deleteotp/<int:pk>/', views.delete_otp),
    path('deleteotpf/<int:pk>/', views.delete_otpfemale),
    path('remove/<int:pk>/', views.delete_model), 
    path('removefemale/<int:pk>/', views.delete_modelfemale),
    
    
     path('nsual/', views.AlumniList.as_view()),
     path('nsual/<int:pk>/', views.AlumniDetail.as_view()),
     path('checkal/', views.check_otpal),
     path('loginal/', views.alumni_login),
     path('forgotal/', views.forgotal_login),
     path('alverify/', views.alforgot_otp),
     path('aleditpass/<int:pk>/', views.aledit_model),
     path('alremove/<int:pk>/', views.aldelete_model),
     path('aldeleteotp/<int:pk>/', views.aldelete_otp),
     
     
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)