from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ActiveStudent,Alumni,Head,Attendance,Speech, Portfolio,RecentEvent,UpComingEvent,Logo,FemaleStudent
from nsuapp.serializers import NewActiveStudentSerializer,OldStudentSerializer,HeadSerializer,AttendanceSerializer,SpeechSerializer, PortfolioSerializer,RecentEventSerializer,UpComingEventSerializer,LogoSerializer,FemaleStudentSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



# @csrf_exempt
# def index_view(request):
#     return render(request,'dist/index.html')
# Create your views here.

class StudentList(generics.ListCreateAPIView):
    queryset = ActiveStudent.objects.all()
    serializer_class = NewActiveStudentSerializer
    


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActiveStudent.objects.all()
    serializer_class = NewActiveStudentSerializer
    
    

class FemaleList(generics.ListCreateAPIView):
    queryset = FemaleStudent.objects.all()
    serializer_class = FemaleStudentSerializer
    


class FemaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FemaleStudent.objects.all()
    serializer_class = FemaleStudentSerializer
 
 
class AdminList(generics.ListCreateAPIView):
        queryset = Head.objects.all()
        serializer_class = HeadSerializer
    


class AdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Head.objects.all()
    serializer_class = HeadSerializer
    
class AttendList(generics.ListCreateAPIView):
        queryset = Attendance.objects.all()
        serializer_class = AttendanceSerializer
    


class AttendDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    
    
    
class LogoList(generics.ListCreateAPIView):
        queryset = Logo.objects.all()
        serializer_class = LogoSerializer
    


class LogoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

     
#Login#

# @csrf_exempt 
# def student_login(request):
#     auth_email=request.POST['auth_email']
#     auth_password=request.POST['auth_password']
#     StudentData=ActiveStudent.objects.get(auth_email=auth_email,auth_password=auth_password)
#     AdminData=Head.objects.get(email=auth_email,password=auth_password)
#     if StudentData:
#         return JsonResponse({'bool': True,'active_id':StudentData.id,'nav':'showactive'})
#     if AdminData:
#         return JsonResponse({'booll': True,'active_idd':Head.id})
#     else:
#         return JsonResponse({'bool': False})
       
  



@csrf_exempt
def student_login(request):
    if request.method == 'POST':
        auth_email = request.POST.get('auth_email')
        auth_password = request.POST.get('auth_password')

        try:
            StudentData = ActiveStudent.objects.get(auth_email=auth_email, auth_password=auth_password)
            return JsonResponse({'bool': True, 'active_id': StudentData.id, 'nav': 'showactive'})
        except ActiveStudent.DoesNotExist:
            pass
        
        try:
            FemaleData = FemaleStudent.objects.get(auth_email=auth_email, auth_password=auth_password)
            return JsonResponse({'boolll': True, 'active_iddd': FemaleData.id, 'nav': 'showactive'})
        except FemaleStudent.DoesNotExist:
            pass
        
        try:
            AdminData = Head.objects.get(email=auth_email, password=auth_password)
            return JsonResponse({'booll': True, 'active_idd': AdminData.id})
        except Head.DoesNotExist:
            pass

    return JsonResponse({'bool': False})

 
    

    
    
#otp#

# @csrf_exempt 
# def check_otp(request):
#     verify_token=request.POST['otp_digit']
#     verify=ActiveStudent.objects.get(verify_token=verify_token)
#     verifyfemale=FemaleStudent.objects.get(verify_token=verify_token)
#     if verify:
#        return JsonResponse({'bool': True,'verify':verify.id})
#     elif verifyfemale :
#        return JsonResponse({'booll': True,'verifyy':verifyfemale.id})
#     else:
#         return JsonResponse({'bool':False})
    
@csrf_exempt 
def check_otp(request):
        if request.method == 'POST':   
           verify_token = request.POST.get('otp_digit')
       

        try:
             verify=ActiveStudent.objects.get(verify_token=verify_token)
             return JsonResponse({'bool': True,'verify':verify.id})
        except ActiveStudent.DoesNotExist:
            pass
        
        try:
             verifyfemale=FemaleStudent.objects.get(verify_token=verify_token)
             return JsonResponse({'booll': True,'verifyy':verifyfemale.id})
        except FemaleStudent.DoesNotExist:
            pass
        
        return JsonResponse({'booll': False})          




  
 #forgot password#   

# @csrf_exempt 
# def forgot_login(request):
#     auth_email=request.POST['auth_email']
#     verify_token=request.POST['verify_token']
#     StudentData=ActiveStudent.objects.get(auth_email=auth_email)
    
#     if StudentData:
#         instance = ActiveStudent.objects.get(pk=StudentData.id)
#         if request.method == 'POST':
#              instance.verify_token = verify_token
#              instance.email_sent_condition_met = True
#              instance.save()
        
#         return JsonResponse({'bool': True,'forgot_id':StudentData.id})
#     else:
#         return JsonResponse({'bool': False, 'error' :'invalid users'})
    
 
 #forgot OTP#
@csrf_exempt 
def forgot_otp(request):
    verify_token=request.POST['otp_digit']
    verify=ActiveStudent.objects.get(verify_token=verify_token)
    if verify:
       return JsonResponse({'bool': True,'verify':verify.id})
    else:
        return JsonResponse({'bool':False})
 
  #forgot OTP#
@csrf_exempt 
def forgot_otpf(request):
    verify_token=request.POST['otp_digit']
    verify=FemaleStudent.objects.get(verify_token=verify_token)
    if verify:
       return JsonResponse({'bool': True,'verify':verify.id})
    else:
        return JsonResponse({'bool':False})
 
 #change password#
    
@csrf_exempt
def edit_model(request, pk):
    instanx = ActiveStudent.objects.get(pk=pk)
    
    if request.method == 'POST':
        instanx.auth_password = request.POST.get('auth_password')
        instanx.email_sent_condition_met = False
        instanx .save()
       
        return JsonResponse({'message': 'Password updated successfully'})
    return render(request, 'edit_model.html', {'instance': instanx })


#female edit model#
@csrf_exempt
def edit_modelfemale(request, pk):
    instanx =   FemaleStudent.objects.get(pk=pk)
    
    if request.method == 'POST':
        instanx.auth_password = request.POST.get('auth_password')
        instanx.email_sent_condition_met = False
        instanx .save()
       
        return JsonResponse({'message': 'Password updated successfully'})
    return render(request, 'edit_model.html', {'instance': instanx })

#female otp for edit model#

# @csrf_exempt 
# def forgot_loginf(request):
#     auth_email=request.POST['auth_email']
#     verify_token=request.POST['verify_token']
#     StudentData=FemaleStudent.objects.get(auth_email=auth_email)
    
#     if StudentData:
#         instance = FemaleStudent.objects.get(pk=StudentData.id)
#         if request.method == 'POST':
#              instance.verify_token = verify_token
#              instance.email_sent_condition_met = True
#              instance.save()
        
#         return JsonResponse({'bool': True,'forgot_idd':StudentData.id})
#     else:
#         return JsonResponse({'bool': False, 'error' :'invalid users'})

#otp for delete model#
@csrf_exempt
def delete_otp(request, pk):
    instanx = ActiveStudent.objects.get(pk=pk)
    
    if request.method == 'POST':
        instanx.verify_token = request.POST.get('verify_token')
        instanx.email_sent_condition_met = True
        instanx .save()
       
        return JsonResponse({'message': 'Password updated successfully'})
    return render(request, 'edit_model.html', {'instance': instanx })




# @csrf_exempt
# def delete_model(request, pk):
#     try:
#         # Retrieve the ActiveStudent instance by primary key
#         instanx = ActiveStudent.objects.get(pk=pk)
        
#         if request.method == 'POST':
#             # Retrieve the verification code from POST data
#             verify_token = request.POST.get('otp_digit')
            
#             # Check if the provided verification code matches
#             if verify_token == instanx.verify_token:
#                 # If verification code matches, delete the instance
#                 instanx.delete()
#                 instanx.photo.delete()
#                 return JsonResponse({'bool': True, 'message': 'Data deleted successfully'})
#             else:
#                 # If verification code doesn't match, return error response
#                 return JsonResponse({'bool': False, 'message': 'Incorrect verification code'})
#     except ActiveStudent.DoesNotExist:
#         return JsonResponse({'bool': False, 'message': 'ActiveStudent instance not found'})
#     except Exception as e:
#         # Handle any other exceptions
#         return JsonResponse({'bool': False, 'message': str(e)})


@csrf_exempt
def delete_model(request, pk):
    try:
        # Retrieve the ActiveStudent instance by primary key
        instanx = ActiveStudent.objects.get(pk=pk)
        
        if request.method == 'POST':
            # Retrieve the verification code from POST data
            verify_token = request.POST.get('otp_digit')
            
            # Check if the provided verification code matches
            if verify_token == instanx.verify_token:
                # Delete the photo first if it exists
                if instanx.photo:
                    instanx.photo.delete()
                
                # Delete the ActiveStudent instance
                instanx.delete()

                return JsonResponse({'bool': True, 'message': 'Data deleted successfully'})
            else:
                # If verification code doesn't match, return error response
                return JsonResponse({'bool': False, 'message': 'Incorrect verification code'})
    except ActiveStudent.DoesNotExist:
        return JsonResponse({'bool': False, 'message': 'ActiveStudent instance not found'})
    except Exception as e:
        # Handle any other exceptions
        return JsonResponse({'bool': False, 'message': str(e)})

    
  
  

#    #female delete model#
# @csrf_exempt
# def delete_modelfemale(request, pk):
#     try:
#         # Retrieve the ActiveStudent instance by primary key
#         instanx = FemaleStudent.objects.get(pk=pk)
        
#         if request.method == 'POST':
#             # Retrieve the verification code from POST data
#             verify_token = request.POST.get('otp_digit')
            
#             # Check if the provided verification code matches
#             if verify_token == instanx.verify_token:
#                 # If verification code matches, delete the instance
#                 instanx.delete()
#                 instanx.photo.delete()
#                 return JsonResponse({'bool': True, 'message': 'Data deleted successfully'})
#             else:
#                 # If verification code doesn't match, return error response
#                 return JsonResponse({'bool': False, 'message': 'Incorrect verification code'})
#     except FemaleStudent.DoesNotExist:
#         return JsonResponse({'bool': False, 'message': 'ActiveStudent instance not found'})
#     except Exception as e:
#         # Handle any other exceptions
#         return JsonResponse({'bool': False, 'message': str(e)}) 
    
    
@csrf_exempt
def delete_modelfemale(request, pk):
    try:
        # Retrieve the ActiveStudent instance by primary key
        instanxx = FemaleStudent.objects.get(pk=pk)
        
        if request.method == 'POST':
            # Retrieve the verification code from POST data
            verify_token = request.POST.get('otp_digit')
            
            # Check if the provided verification code matches
            if verify_token == instanxx.verify_token:
                # Delete the photo first if it exists
                if instanxx.photo:
                    instanxx.photo.delete()
                
                # Delete the ActiveStudent instance
                instanxx.delete()

                return JsonResponse({'booll': True, 'message': 'Data deleted successfully'})
            else:
                # If verification code doesn't match, return error response
                return JsonResponse({'booll': False, 'message': 'Incorrect verification code'})
    except FemaleStudent.DoesNotExist:
        return JsonResponse({'booll': False, 'message': 'ActiveStudent instance not found'})
    except Exception as e:
        # Handle any other exceptions
        return JsonResponse({'booll': False, 'message': str(e)})

    
  
  
    
#delete otp female#
#otp for delete model#
@csrf_exempt
def delete_otpfemale(request, pk):
    instanx = FemaleStudent.objects.get(pk=pk)
    
    if request.method == 'POST':
        instanx.verify_token = request.POST.get('verify_token')
        instanx.email_sent_condition_met = True
        instanx .save()
       
        return JsonResponse({'message': 'Password updated successfully'})
    return render(request, 'edit_model.html', {'instance': instanx })

#ALUMNI VIEW#

class AlumniList(generics.ListCreateAPIView):
    queryset = Alumni.objects.all()
    serializer_class = OldStudentSerializer
    


class AlumniDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alumni.objects.all()
    serializer_class = OldStudentSerializer
    
    
#otpregister#

@csrf_exempt 
def check_otpal(request):
    verify_token=request.POST['otp_digit']
    verify=Alumni.objects.get(verify_token=verify_token)
    if verify:
       return JsonResponse({'bool': True,'verify':verify.id})
    else:
        return JsonResponse({'bool':False})
    


#Login#

@csrf_exempt 
def alumni_login(request):
    auth_email=request.POST['auth_email']
    auth_password=request.POST['auth_password']
    StudentData=Alumni.objects.get(auth_email=auth_email,auth_password=auth_password)
    if StudentData:
        return JsonResponse({'bool': True,'active_id':StudentData.id})
    else:
        return JsonResponse({'bool': False})
    
    

 #forgot password alumni #confirm password first##   

@csrf_exempt 
def forgotal_login(request):
    auth_email=request.POST['auth_email']
    verify_token=request.POST['verify_token']
    StudentDataa=Alumni.objects.get(auth_email=auth_email)
    
    if StudentDataa:
        instance = Alumni.objects.get(pk=StudentDataa.id)
        if request.method == 'POST':
             instance.verify_token = verify_token
             instance.email_sent_condition_met = True
             instance.save()
        
        return JsonResponse({'bool': True,'forgot_id':StudentDataa.id})
    else:
        return JsonResponse({'bool': False, 'error' :'invalid users'})
    



 #send OTP after confirming password#
@csrf_exempt 
def alforgot_otp(request):
    verify_token=request.POST['otp_digit']
    verify=Alumni.objects.get(verify_token=verify_token)
    if verify:
       return JsonResponse({'bool': True,'verify':verify.id})
    else:
        return JsonResponse({'bool':False})
    

 #change password#
    
@csrf_exempt
def aledit_model(request, pk):
    instanx = Alumni.objects.get(pk=pk)
    
    if request.method == 'POST':
        instanx.auth_password = request.POST.get('auth_password')
        instanx.email_sent_condition_met = False
        instanx .save()
       
        return JsonResponse({'message': 'Password updated successfully'})
    return render(request, 'edit_model.html', {'instance': instanx })




#delete Model#

#otp for delete model#
@csrf_exempt
def aldelete_otp(request, pk):
    instanx = Alumni.objects.get(pk=pk)
    
    if request.method == 'POST':
        instanx.verify_token = request.POST.get('verify_token')
        instanx.email_sent_condition_met = True
        instanx .save()
       
        return JsonResponse({'message': 'Password updated successfully'})
    return render(request, 'edit_model.html', {'instance': instanx })




@csrf_exempt
def aldelete_model(request, pk):
    try:
        # Retrieve the Alumni instance by primary key
        instanx = Alumni.objects.get(pk=pk)
        
        if request.method == 'POST':
            # Retrieve the verification code from POST data
            verify_token = request.POST.get('otp_digit')
            
            # Check if the provided verification code matches
            if verify_token == instanx.verify_token:
                # If verification code matches, delete the instance
                instanx.delete()
                return JsonResponse({'bool': True, 'message': 'Data deleted successfully'})
            else:
                # If verification code doesn't match, return error response
                return JsonResponse({'bool': False, 'message': 'Incorrect verification code'})
    except Alumni.DoesNotExist:
        return JsonResponse({'bool': False, 'message': 'ActiveStudent instance not found'})
    except Exception as e:
        # Handle any other exceptions
        return JsonResponse({'bool': False, 'message': str(e)})
    
    
    
#attendance search#
class AttendanceSearch(generics.ListAPIView):
    serializer_class=AttendanceSerializer
    
    def get_queryset(self):
        queryset=Attendance.objects.all()
        date=self.request.query_params.get('date')
        if queryset is not None:
            queryse=queryset.filter(date=date)
        return queryse
    

   
class SpeechList(generics.ListCreateAPIView):
    queryset = Speech.objects.all()
    serializer_class =SpeechSerializer
    


class SpeechDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speech.objects.all()
    serializer_class =SpeechSerializer
    
    

class PortfolioList(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    


# class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Portfolio.objects.all()
#     serializer_class =PortfolioSerializer

class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()
    
    

class RecentEventList(generics.ListCreateAPIView):
     queryset = RecentEvent.objects.all()
     serializer_class = RecentEventSerializer
    


class RecentEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecentEvent.objects.all()
    serializer_class = RecentEventSerializer
    
    
class UpComingEventList(generics.ListCreateAPIView):
     queryset = UpComingEvent.objects.all()
     serializer_class = UpComingEventSerializer
    


class UpComingEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpComingEvent.objects.all()
    serializer_class = UpComingEventSerializer
    
    
@csrf_exempt 
def forgot_login(request):
 if request.method == 'POST':   
    auth_email=request.POST.get('auth_email')
    verify_token=request.POST.get('verify_token')

   
   
    try:
         StudentData=ActiveStudent.objects.get(auth_email=auth_email)
         StudentData.verify_token = verify_token
         StudentData.email_sent_condition_met = True
         StudentData.save()
         return JsonResponse({'bool': True,'forgot_id':StudentData.id})
    except ActiveStudent.DoesNotExist:
            pass 
    try:
        StudentDataf=FemaleStudent.objects.get(auth_email=auth_email)
        StudentDataf.verify_token = verify_token
        StudentDataf.email_sent_condition_met = True
        StudentDataf.save()
        return JsonResponse({'booll': True,'forgot_idd':StudentDataf.id})
    except ActiveStudent.DoesNotExist:
            pass 
      
    return JsonResponse({'bool': False, 'error' :'invalid users'})