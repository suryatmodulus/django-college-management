from django import forms
from django.forms import ModelForm
from eventreg.models import Register
from django.contrib.auth import authenticate,login



# Create your forms here.


class RegForm(ModelForm):
	class Meta:
		model= Register
		fields=["name","email","phone_number","events","amount","pay_mode"]
