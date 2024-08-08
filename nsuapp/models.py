from django.db import models
from django.utils.text import slugify
from django.core.mail import send_mail



# Create your models here.



#Active Student Auth


        
  


class ActiveStudent(models.Model):
    Surname= models.CharField(max_length=350)
    First_name=models.CharField(max_length=350)
    Degree = models.CharField(max_length=350)
    College = models.CharField(max_length=350)
    Phone_number = models.CharField(max_length=350)
    Address= models.CharField(max_length=350,null=True,blank=True)
    FamilyinSaudi = models.CharField(max_length=350)
    Building_number= models.CharField(max_length=350, null=True, blank=True)
    Room_number= models.CharField(max_length=350, null=True, blank=True)
    Nextofkin_mobile=models.CharField(max_length=350, blank=True,null=True)
    photo= models.ImageField(upload_to='image/', blank=True,null=True)
    auth_email=models.CharField(max_length=350,unique=True)
    auth_password=models.CharField(max_length=350)
    verify_token=models.CharField(max_length=16,null=True)
    email_sent_condition_met = models.BooleanField(default=True,null=True)
    Gender=models.CharField(max_length=350)
   
    
    


    

    def save(self, *args, **kwargs):
        # Check if the condition for sending the email is met
        if self.email_sent_condition_met:
            # Conditions are met, send email
            send_mail(
                'Verify Your nsuksu account(Active Student)',
                'Here is the message.',
                'ksunsu312@gmail.com',
                [self.auth_email],
                fail_silently=False,
                html_message=f"<p>your OTP is </p><p>{self.verify_token}</p><p>Do not share your OTP with others.</p>"
            )
        
        # Call the parent save method after sending email or skipping it
        super().save(*args, **kwargs)



class Alumni(models.Model):
    Surname= models.CharField(max_length=350)
    First_name=models.CharField(max_length=350)
    Graduation_year = models.CharField(max_length=350)
    Degree = models.CharField(max_length=350)
    College = models.CharField(max_length=350)
    Residence_Country=models.CharField(max_length=350)
    Occupation=models.CharField(max_length=350, blank=True,null=True)
    photo= models.ImageField(upload_to='image/', blank=True,null=True)
    Phone_number = models.CharField(max_length=350)
    auth_email=models.CharField(max_length=350,unique=True)
    auth_password=models.CharField(max_length=350)
    verify_token=models.CharField(max_length=16,null=True)
    email_sent_condition_met = models.BooleanField(default=True,null=True)
   
    
    
    
    
    def save(self, *args, **kwargs):
            # Check if the condition for sending the email is met
        if self.email_sent_condition_met:
            # Conditions are met, send email
            send_mail(
                'Verify Your nsuksu account (Alumni)',
                'Here is the message.',
                'nsuksu92@gmail.com',
                [self.auth_email],
                fail_silently=False,
                html_message=f"<p>your OTP is </p><p>{self.verify_token}</p><p>Do not share your OTP with others.</p>"
            )
        
        # Call the parent save method after sending email or skipping it
        super().save(*args, **kwargs)
        
 
class FemaleStudent(models.Model):
    Surname= models.CharField(max_length=350)
    First_name=models.CharField(max_length=350)
    Degree = models.CharField(max_length=350)
    College = models.CharField(max_length=350)
    Phone_number = models.CharField(max_length=350)
    Address= models.CharField(max_length=350,null=True,blank=True)
    FamilyinSaudi = models.CharField(max_length=350)
    Building_number= models.CharField(max_length=350, null=True, blank=True)
    Room_number= models.CharField(max_length=350, null=True, blank=True)
    Nextofkin_mobile=models.CharField(max_length=350, blank=True,null=True)
    photo= models.ImageField(upload_to='image/', blank=True,null=True)
    auth_email=models.CharField(max_length=350,unique=True)
    auth_password=models.CharField(max_length=350)
    verify_token=models.CharField(max_length=16,null=True)
    email_sent_condition_met = models.BooleanField(default=True,null=True)
    Gender=models.CharField(max_length=350)
   
    
    


    

    def save(self, *args, **kwargs):
        # Check if the condition for sending the email is met
        if self.email_sent_condition_met:
            # Conditions are met, send email
            send_mail(
                'Verify Your nsuksu account(Active Student)',
                'Here is the message.',
                'ksunsu312@gmail.com',
                [self.auth_email],
                fail_silently=False,
                html_message=f"<p>your OTP is </p><p>{self.verify_token}</p><p>Do not share your OTP with others.</p>"
            )
        
        # Call the parent save method after sending email or skipping it
        super().save(*args, **kwargs)       
        
        
class Head(models.Model):
    sur_name= models.CharField(max_length=350, blank=True)
    first_name=models.CharField(max_length=350, blank=True)
    email=models.CharField(max_length=350,unique=True)
    password=models.CharField(max_length=350)  
   

class Attendance(models.Model):
   
    name= models.CharField(max_length=350, blank=True)
    title= models.CharField(max_length=350, blank=True)
    date= models.DateField()
    
    
   
class Speech(models.Model):
    text= models.CharField(max_length=3500)
    name=models.CharField(max_length=350)
    
   
class Portfolio(models.Model):
    exco= models.CharField(max_length=350)
    name=models.CharField(max_length=350)  
    department=models.CharField(max_length=350)  
    degree=models.CharField(max_length=350 , default="taiwo") 
    mobile=models.CharField(max_length=350, default="foo") 
    photo= models.ImageField(upload_to='photo/' , default="photo")
    
    
class RecentEvent(models.Model):
    photo=models.ImageField(upload_to='event/' , default="event")
    title=models.CharField(max_length=350)
    
    
class UpComingEvent(models.Model):
    date=models.CharField(max_length=350)
    title=models.CharField(max_length=350)
    
    
class Logo(models.Model):
     photo=models.ImageField(upload_to='logo/' , default="logo")
