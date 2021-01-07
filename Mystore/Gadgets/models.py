from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=g)
	impf = models.ImageField(upload_to="Profile/",default="profile.jpg") 

@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)


from django.db import models

# Create your models here.

class Exam(models.Model):
	Question = models.CharField(max_length=100)
	Option1 = models.CharField(max_length=100)
	Option2 = models.CharField(max_length=100)
	Option3 = models.CharField(max_length=100)
	Option4 = models.CharField(max_length=100)
	Corrans = models.CharField(max_length=100)
	class Meta:
		db_table="onlineexam"


