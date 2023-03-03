from django import forms
from p1.models import curd


class std(forms.Form):
	name=forms.CharField(label="enter your name:" )
	email=forms.EmailField(label="enter the email:" )
	phone=forms.IntegerField(label="enter the phone number:" )
	gender=forms.ChoiceField()

	
class pr2(forms.ModelForm):

	class Meta:
		model=curd
		fields= ("name" , "email", "phone", "college")
		widgets={
		  'name':forms.TextInput(attrs={'class':'form-control' , 'id':'floatingInputGroup1' ,'placeholder':'Name'}),
		  'email':forms.EmailInput(attrs={'class':'form-control' ,'id':'floatingInputGroup1' ,'placeholder':'Email'}),
		  'phone':forms.NumberInput( attrs={'class':'form-control' ,'id':'floatingInputGroup1' ,'placeholder':'Phone'}),
		  'college':forms.TextInput(attrs={'class':'form-control','id':'floatingInputGroup1' ,'placeholder':'college'}),

		}

		



	
	
		

	