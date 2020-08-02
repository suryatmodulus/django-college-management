from django.shortcuts import render,redirect
from eventreg.forms import RegForm
from eventreg.models import Register
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from eventreg.Sms_Api import Send_Sms
#from eventreg.way2sms_3 import Send_OTP
from eventreg.SG_Email import Send_Email
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from instamojo_wrapper import Instamojo
from django.contrib.auth.decorators import login_required



events_dic={'1': 'Eastern-Group', '2': 'Western-Group', '3': 'Solo', '4': 'Tapanguchi-Aaddu-Machi',
'5': 'Fashion-Show', '6': 'Mr-Ms-Event', '7': 'Indian-Group-Singing', '8': 'Filmy-Vocals-Solo',
'9': 'Western-Vocals-Solo', '10': 'War-of-Wits-Debate', '11': 'OTP-Quiz', '12': 'Jam', '13': 'Movie-Review', 
'14': 'Pocket-Full-Of-Words', '15': 'Mun', '16': 'Fix-The-Blot', '17': 'Scrap-Rap', '18':
"Its-Twisted", '19': 'Street-Play', '20': 'Mad-Ads', '21': 'Improv', '22': 'War-Of-Emcess', '23':
'Standup-Comdey', '24': 'Meme-Making', '25': 'Cooking-Without-Fire', '26': 'Friends-Quiz', '27':
'Marvel-Quiz', '28': 'Hagothon', '29': 'Strangely-Familiar', '30': 'DSI-Minute', '31': 'Treasure-Hunt',
 '32': 'Kannada-Anthakshari', '33': 'Away-We-Go', '34': 'Fifa-18', '35': 'NFS-MW', '36':
'Counter-Strike', '37': 'Onspot-Photography', '38': 'Shortfilm-Making', '39': 'Individual-Events','40':'Bhavageethe','41':'Instrumental-Solo'}

amount_dic = {"1":"800","2" :"800","3" :"200","4":"200","5":"3000","6":"200","7":"500","8":"100",
				"9" :"100","10":"200","11":"200","12":"100","13":"150","14":"100","15":"800","16":"150",
				"17":"150","18":"150","19":"800","20":"800","21":"300","22":"100","23":"100","24":"100",
				"25":"100","26":"100","27":"100","28":"100","29":"100","30":"100","31":"150","32":"100",
				"33":"150","34":"100","35" :"100","36":"250","37":"200","38" :"400","39" :"300","40":"50",
				"41":"100"}


# Create your views here.

#passwd="20130877274"
org_email="admin@gmail.com"
#api = Instamojo(api_key="test_5dadaf8ca078e3e72e2f9d574b5", auth_token="test_6be549862302733582f44a3659f", endpoint='https://test.instamojo.com/api/1.1/')

@login_required
def EventsView(request):
	return redirect("/events/register")

@login_required
def RegView(request):
	request.session['qr_key'] = None
	form = RegForm(request.POST or None)
	if form.is_valid():
		name=form.cleaned_data.get("name")
		email = form.cleaned_data.get("email")
		number=form.cleaned_data.get("phone_number")
		event_items=form.cleaned_data.get("events")
		amount=form.cleaned_data.get("amount")
		pay_mode = form.cleaned_data.get("pay_mode")
		amount_conf = sum([int(amount_dic[item]) for item in event_items])
		if(amount == amount_conf):
			rand_id=random.randrange(10000,99999)
			qr_value="dscef18"+str(int(int(number)/rand_id))+name[:3]
			new_register = form.save()
			Register.objects.filter(pk=new_register.pk).update(reg_id=qr_value)
			Register.objects.filter(phone_number=number,reg_id=qr_value).update(paid=True)
			request.session['qr_key'] = qr_value
			return redirect("/events/success")
		return redirect("/events/regerror")
	return render(request,"register.html",{})


@login_required
def SuccessView(request):
	if 'qr_key' in request.session:
		qr_id = request.session['qr_key']
		return render(request,"success.html",{"qr_id":qr_id})
	return redirect("/events/register")

@login_required
def ErrorView(request):
	return render(request,"error.html",{})
	

@login_required
def CheckView(request):
	if request.user.is_teacher:
		return render(request,"check.html",{})
	return redirect("/")

@login_required
def ResultView(request):
	if request.user.is_teacher:
		if 'uid' in request.POST:
			uid = request.POST.get('uid')
			data = list(Register.objects.filter(reg_id=uid).values_list("name","email","phone_number","events"))
			try:
				data = data[0]
				event_list=[]
				for item in data[3]:
					value=events_dic[item]
					event_list.append(value)
				return render(request,"result.html",{"name":data[0],"email":data[1],"number":data[2],"events":event_list})
			except:
				return render(request,"result.html",{"error":"Sorry, Not Registered"})
		return redirect("/events/check")
	return redirect("/")

