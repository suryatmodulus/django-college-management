from django.contrib import admin
from eventreg.models import Register

events_dic={'1': 'Eastern-Group', '2': 'Western-Group', '3': 'Solo', '4': 'Tapanguchi-Aaddu-Machi',
'5': 'Fashion-Show', '6': 'Mr-Ms-Event', '7': 'Indian-Group-Singing', '8': 'Filmy-Vocals-Solo',
'9': 'Western-Vocals-Solo', '10': 'War-of-Wits-Debate', '11': 'OTP-Quiz', '12': 'Jam', '13': 'Movie-Review', 
'14': 'Pocket-Full-Of-Words', '15': 'Mun', '16': 'Fix-The-Blot', '17': 'Scrap-Rap', '18':
"Its-Twisted", '19': 'Street-Play', '20': 'Mad-Ads', '21': 'Improv', '22': 'War-Of-Emcess', '23':
'Standup-Comdey', '24': 'Meme-Making', '25': 'Cooking-Without-Fire', '26': 'Friends-Quiz', '27':
'Marvel-Quiz', '28': 'Hagothon', '29': 'Strangely-Familiar', '30': 'DSI-Minute', '31': 'Treasure-Hunt',
 '32': 'Kannada-Anthakshari', '33': 'Away-We-Go', '34': 'Fifa-18', '35': 'NFS-MW', '36':
'Counter-Strike', '37': 'Onspot-Photography', '38': 'Shortfilm-Making', '39': 'Individual-Events','40':'Bhavageethe','41':'Instrumental-Solo'}




class RegisterModelAdmin(admin.ModelAdmin):
	
	list_display=["name","email","phone_number","registd_date","reg_id","amount","pay_mode","paid","pay_req_id","pay_id"]
	
	def events_list(self, obj):
		selected_events_list=[]
		raw_events_list=obj.events
		for item in raw_events_list:
			selected_events_list.append(events_dic[item])
		return list(selected_events_list)
	

	list_filter=["registd_date","paid","pay_mode"]
	search_fields=["name","events","email","phone_number","reg_id","amount"]
	
	class Meta:
		model = Register



admin.site.register(Register,RegisterModelAdmin)