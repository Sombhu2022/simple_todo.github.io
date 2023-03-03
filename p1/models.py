from django.db import models

# Create your models here.

class curd(models.Model):
	name=models.CharField(max_length=70)
	email=models.EmailField(max_length=80)
	phone=models.IntegerField()
	college=models.CharField(max_length=200)


	#def __str__(self):

	#	return f" {self.name} {self.email} {self.phone}"




