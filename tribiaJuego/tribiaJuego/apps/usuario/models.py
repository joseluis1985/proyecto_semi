from django.db import models
import datetime
# Create your models here.
class usuarios(models.Model):
	nick =models.CharField(max_length=200)
	fecha=models.DateField(auto_now=True)
	email=models.EmailField()
	password=models.CharField(max_length=200)
	avatar=models.ImageField(upload_to="foto")
		def __unicode__(self):
		return self.nombre
class login(models.Model):
	dateInitSession=models.DateField()
	user=models.ForeignKey(usuario)