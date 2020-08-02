from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from multiselectfield import MultiSelectField
from django.utils import timezone
# Create your models here.

class Register(models.Model):

	person_choice =((1,"Eastern-Group"),
			(2,"Western-Group"),
			(3,"Solo"),
			(4,"Tapanguchi-Aaddu-Machi"),
			(5,"Fashion-Show"),
			(6,"Mr-Ms-Event"),
			(7,"Indian-Group-Singing"),
            (8,"Filmy-Vocals-Solo"),
            (9,"Western-Vocals-Solo"),
			(10,"War-of-Wits-Debate"),
			(11,"OTP-Quiz"),
			(12,"Jam"),
            (13,"Movie-Review"),
            (14,"Pocket-Full-Of-Words"),
			(15,"Mun"),
			(16,"Fix-The-Blot"),
			(17,"Scrap-Rap"),
			(18,"Its-Twisted"),
			(19,"Street-Play"),
			(20,"Mad-Ads"),
			(21,"Improv"),
            (22,"War-Of-Emcess"),
            (23,"Standup-Comdey"),
			(24,"Meme-Making"),
			(25,"Cooking-Without-Fire"),
			(26,"Friends-Quiz"),
			(27,"Marvel-Quiz"),
			(28,"Hagothon"),
            (29,"Strangely-Familiar"),
            (30,"DSI-Minute"),
			(31,"Treasure-Hunt"),
			(32,"Kannada-Anthakshari"),
			(33,"Away-We-Go"),
			(34,"Fifa-18"),
			(35,"NFS-MW"),
			(36,"Counter-Strike"),
			(37,"Onspot-Photography"),
			(38,"Shortfilm-Making"),
			(39,"Individual-Events"),
			(40,"Bhavageethe"),
			(41,"Instrumental-Solo"))
	
	name = models.CharField(max_length=100)
	email= models.EmailField(max_length=100)
	phone_regex = RegexValidator(regex=r'^\d{10,10}$', message="Enter Valid Phone Number (10-digits)")
	phone_number = models.CharField(max_length=10,validators=[phone_regex])
	registd_date = models.DateTimeField(default=timezone.now)
	events = MultiSelectField(choices=person_choice,default=None)
	amount = models.IntegerField(default=0)
	reg_id = models.CharField(max_length=100,default="None")
	pay_mode = models.CharField(max_length=20,default="None")
	paid = models.BooleanField(default=False)
	pay_req_id = models.CharField(max_length=100,default="None")
	pay_id = models.CharField(max_length=100,default="None")

	def __str__(self):
		return self.name

