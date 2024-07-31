from rest_framework import serializers
from .models import ActiveStudent, Alumni,Head, Attendance,Speech ,Portfolio,RecentEvent,UpComingEvent,Logo,FemaleStudent

class NewActiveStudentSerializer(serializers.ModelSerializer):
    class Meta:
     model=ActiveStudent
     fields='__all__'
     
class FemaleStudentSerializer(serializers.ModelSerializer):
    class Meta:
     model=FemaleStudent
     fields='__all__'
          
class OldStudentSerializer(serializers.ModelSerializer):
    class Meta:
     model=Alumni
     fields='__all__'
     

class HeadSerializer(serializers.ModelSerializer):
    class Meta:
     model=Head
     fields='__all__'
     
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
     model=Attendance
     fields='__all__'
     
class SpeechSerializer(serializers.ModelSerializer):
    class Meta:
     model=Speech
     fields='__all__'
     


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
     model=Portfolio
     fields='__all__'
     

class RecentEventSerializer(serializers.ModelSerializer):
    class Meta:
     model=RecentEvent
     fields='__all__'   
     
class UpComingEventSerializer(serializers.ModelSerializer):
    class Meta:
     model=UpComingEvent
     fields='__all__'    
     
     
class LogoSerializer(serializers.ModelSerializer):
    class Meta:
     model=Logo
     fields='__all__'    