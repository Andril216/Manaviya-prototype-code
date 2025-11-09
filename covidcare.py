#kivy is the module used for the gui
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen,SlideTransition
from kivy.core.window import Window
Window.clearcolor = (1,1,1,1)#here we set the background color to white

di=[]
li=[]
li2=[]
li3=[]
li4=[]
cities={"Karnataka":['Bangalore'],"Tamil Nadu":['Chennai']}
pincodes={'Bangalore':["560001","560002","560003","560004","560005","560006","560007","560007","560008","560009","560010","560011","560012","560013","560014","560015","560016","560017","560018","560019","560020","560021","560022","560023","560024","560025","560026","560027","560029","560030","560032","560033","560034","560035","560036","560037","560038","560039","560040","560041","560042","560043","560045","560046","560047","560048","560049","560050","560051","560053","560054","560055","560056","560057","560058","560059","560060","560061","560062","560063","560064","560065","560066","560067","560068","560070","560071","560072","560073","560073","560074","560075","560076","560077","560078","560079","560080","560081","560082","560083","560084","560085","560086","560087","560090","560091","560092","560093","560094","560095","560096","560097","560098","560099","560100","560102","560103","560104","560105","560108","560109","560110","560112","560300","562106","562107","562120","562125","562130","562149","562157","562162","562164"]}

#Builder.load_string allows us to load the kv code. Explaining each and every point will take time, so please look it up online yourself.
Builder.load_string('''
<Screen0>:
	AnchorLayout:
		anchor_x:'center'
        anchor_y:'center'
		Label:
			size_hint_y:None
			text:'Please Wait while we fetch the data...'
			font_size:60
			color:[0,0,0,1]		
			text_size:self.width,None
			height:self.texture_size[1]
<Screen1>:
	BoxLayout:
		orientation:'vertical'
    	ScrollView:
    		size_hint_y:0.8
    		do_scroll_x:False
    		do_scroll_y:True
			Label:
        		size_hint_y: None
        		height: self.texture_size[1]
        		text_size: self.width, None
        		padding: 10, 10
        		text:root.text
        		color:[0,0,0,1]
        AnchorLayout:
        	anchor_x:'center'
        	anchor_y:'bottom'
        	size_hint:1,0.2
        	BoxLayout:
        		size_hint_x:1
        		orientation:'vertical'        		
        		BoxLayout:
        			orientation:'horizontal'
        			CheckBox:
        				color:[0,0,0,1]
        				size_hint_x:None
        				width:50
        				id:ch
        			Label:
        				text:'I agree to this privacy policy'
        				halign:'left'
        				text_size:self.size
        				valign:'center'
        				color:[0,0,0,1]
        		Button:
        			size_hint_x:0.3
        			text:'next'
        			on_press:root.next(ch.active)

<Screen2>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
		BoxLayout:
			size_hint: 0.5,0.3
			orientation:'vertical'
			Image:
				source: 'MW Transparent.png'
				size_hint:1,1		
			TextInput:
				hint_text:'enter your name'
				id:na
				multiline:False
				size_hint:1,None
				height:self.minimum_height
			TextInput:
				id:ph
				hint_text:'enter your phone number'
				multiline:False
				size_hint:1,None
				height:self.minimum_height
			Button:
				text:'Enter'
				on_press:root.enter(na.text,ph.text)
				size_hint_y:None
				height:30
<Screen4>:
	AnchorLayout:
		anchor_x:'left'
		anchor_y:'top'
		BoxLayout:
			size_hint_y:0.2
			orientation:'vertical'
			size_hint_x:1
			BoxLayout:
				size_hint_y:0.8
				orientation:'horizontal'
				Image:
					source: 'MANAVIYA TOP BAR LOGO.png'
					size_hint_x:0.4
					allow_stretch:True
					keep_ratio:False
				Button:
					size_hint:0.1,0.7
					background_normal:'VOlll.jpg'
					background_down:'VOlll.jpg'
					on_press:root.vol()
			ProgressBar:
				size_hint_x:1
				size_hint_y:None
				valign:'top'
				value:100
				max:100
	AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
		BoxLayout:
			size_hint: 0.5,0.4
			orientation:'vertical'
			Label:
				text:'What is your requirement ?'
				color: [0,0,0,1]
			Label:
				size_hint:1,None
				height:20
			Button:
				text:'Beds without oxygen'
				on_press:root.bnox()
				color:[1,1,1,1]
				background_color:[0,0,3,1]
			Label:
				size_hint:1,None
				height:20
			Button:
				text:'Beds with oxygen'
				color:[1,1,1,1]
				background_color:[0,0,3,1]
				on_press:root.box()
			Label:
				size_hint:1,None
				height:20
			Button:
				text:'ICU without ventilator'
				color:[1,1,1,1]
				background_color:[0,0,3,1]
				on_press:root.inv()
			Label:
				size_hint:1,None
				height:20
			Button:
				text:'ICU with ventilator'
				color:[1,1,1,1]
				background_color:[0,0,3,1]
				on_press:root.iv()
	RelativeLayout:
		Button:
			size_hint:0.25,0.05
			background_normal:'Back button 2.png'
			background_down:'Back button 2.png'
			pos_hint:{'x':0.1,'y':0.1}
			on_press:root.back()
<Screen3>:
	AnchorLayout:
		anchor_x:'left'
		anchor_y:'top'
		BoxLayout:
			size_hint_y:0.2
			orientation:'vertical'
			size_hint_x:1
			BoxLayout:
				size_hint_y:0.8
				orientation:'horizontal'
				Image:
					source: 'MANAVIYA TOP BAR LOGO.png'
					size_hint_x:0.4
					allow_stretch:True
					keep_ratio:False
				Button:
					size_hint:0.1,0.7
					background_normal:'VOlll.jpg'
					background_down:'VOlll.jpg'
					on_press:root.vol()
			ProgressBar:
				size_hint_x:1
				size_hint_y:None
				valign:'top'
				value:100
				max:100			
	AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
		BoxLayout:
			size_hint:0.6,0.4
			orientation:'vertical'
			Label:
				text: "what is your location ?"
				color:[0,0,0,1]
			Label:
				size_hint:1,None
				height:20			
			Spinner:
				id:pin
				text:'Pincode'
				color:[1,1,1,1]
				background_color:[0,0,3,1]
				values:["560001","560002","560003","560004","560005","560006","560007","560007","560008","560009","560010","560011","560012","560013","560014","560015","560016","560017","560018","560019","560020","560021","560022","560023","560024","560025","560026","560027","560029","560030","560032","560033","560034","560035","560036","560037","560038","560039","560040","560041","560042","560043","560045","560046","560047","560048","560049","560050","560051","560053","560054","560055","560056","560057","560058","560059","560060","560061","560062","560063","560064","560065","560066","560067","560068","560070","560071","560072","560073","560073","560074","560075","560076","560077","560078","560079","560080","560081","560082","560083","560084","560085","560086","560087","560090","560091","560092","560093","560094","560095","560096","560097","560098","560099","560100","560102","560103","560104","560105","560108","560109","560110","560112","560300","562106","562107","562120","562125","562130","562149","562157","562162","562164"]
			Label:
				size_hint:1,None
				height:40
			AnchorLayout:
				anchor_x:'center'
				Button:
					text:'enter'
					size_hint:0.7,0.7
					color:[1,1,1,1]
					background_color:[0.5,0.5,0.5,0.5]
					on_press:root.loc(pin.text)
			Label:
				size_hint:1,None
				height:20
			Button:
				text:'Pan Bangalore'
				on_press:root.npin()
				color:[1,1,1,1]
				background_color:[2,0,0,1]
	RelativeLayout:
		Button:
			size_hint:0.25,0.05
			background_normal:'Back button 2.png'
			background_down:'Back button 2.png'
			pos_hint:{'x':0.1,'y':0.1}
			on_press:root.back()
<Screen5>:
	RelativeLayout:
		Button:
			size_hint:0.25,0.05
			background_normal:'Back button 2.png'
			background_down:'Back button 2.png'
			pos_hint:{'x':0.1,'y':0.1}
			on_press:root.back()
	BoxLayout:
		orientation:'vertical'
		AnchorLayout:
			anchor_x:'left'
			anchor_y:'top'
			size_hint:1,0.2
			BoxLayout:
				orientation:'vertical'
				size_hint_x:1
				BoxLayout:
					orientation:'horizontal'
					size_hint_y:0.8
					Image:
						source: 'MANAVIYA TOP BAR LOGO.png'
						size_hint_x:0.4
						allow_stretch:True
						keep_ratio:False
					Button:
						size_hint:0.1,0.7
						background_normal:'VOlll.jpg'
						background_down:'VOlll.jpg'
						on_press:root.vol()
				ProgressBar:
					size_hint_x:1
					size_hint_y:None
					valign:'top'
					value:100
					max:100	
		AnchorLayout:
        	anchor_x: 'center'
        	anchor_y: 'top'		  	
    		ScrollView:
    			size_hint:0.8,0.7
    			do_scroll_x:False
    			do_scroll_y:True
				GridLayout:
					size_hint_y:None
					height:self.minimum_height
    				cols:1
    				spacing:10
    				padding:10
    				Label:
    					text:'This is the list of providers for you'
    					size_hint_y:None
    					font_size:'20sp'
    					text_size:self.size
    					color:[0,0,0,1]
<Screen6>:
	AnchorLayout:
		anchor_x:'right'
		anchor_y:'bottom'
		Button:
			background_normal:'share.png'
			background_down:'share.png'
			size_hint:0.25,0.15
			on_press:root.share()
	RelativeLayout:
		Button:
			size_hint:0.25,0.05
			background_normal:'Back button 2.png'
			background_down:'Back button 2.png'
			pos_hint:{'x':0.1,'y':0.1}  
			on_press:root.back()
	AnchorLayout:
		anchor_x:'left'
		anchor_y:'top'
		BoxLayout:
			size_hint_y:0.2
			orientation:'vertical'
			size_hint_x:1
			BoxLayout:
				orientation:'horizontal'
				size_hint_y:0.8
				Image:
					source: 'MANAVIYA TOP BAR LOGO.png'
					size_hint_x:0.4
					allow_stretch:True
					keep_ratio:False
				Button:
					size_hint:0.1,0.7
					background_normal:'VOlll.jpg'
					background_down:'VOlll.jpg'
					on_press:root.vol()
			ProgressBar:
				size_hint_x:1
				size_hint_y:None
				valign:'top'
				value:100
				max:100
	AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'center'
        BoxLayout:
        	orientation:'vertical'
        	size_hint:1,0.35
        	Label:
        		bold:True
        		texture_size:self.size
        		halign:'left'
        		color:[0,0,0,1]
        	Label:
        		font_size:27
        		color:[0,0,0,1]
        		text_size:self.size
        		halign:'left' 
        	Label:
        		font_size:27
        		color:[0,0,0,1]
        		text_size:self.size
        		halign:'left' 
        	Label:
        		font_size:27
        		color:[0,0,0,1]
        		text_size:self.size
        		halign:'left' 
        	Label:
        		font_size:27
        		color:[0,0,0,1]
        		text_size:self.size
        		halign:'left' 
        	Label:
        		font_size:27
        		color:[0,0,0,1] 
        		text_size:self.size
        		halign:'left'  
''')

class Screen0(Screen):
	def on_enter(self):
		from kivy.clock import Clock
		Clock.schedule_once(self.a,10)
	def a(self,z):
		import pygsheets
		gc = pygsheets.authorize(service_file='fluted-card-263518-363585642043.json')#this is a json file that's the key for connecting to the google sheet through the service account'1
		f=gc.open('Bangalore Database')
		for i in f.sheet1.get_all_records():
			di.append(i)
		try:
			open('a.txt')	
			self.manager.add_widget(Screen2(name ="screen_two"))
			self.manager.current='screen_two'
		except:
			self.manager.add_widget(Screen1(name ="screen_one"))
			self.manager.current='screen_one'
			open('a.txt','w')

class Screen1(Screen):
    text='''Privacy Policy
Manaviya built the Manaviya app as a Free app. This SERVICE is provided by Manaviya at no cost and is intended for use as is.
This page is used to inform visitors regarding our policies with the collection, use, and disclosure of Personal Information if anyone decided to use our Service.
If you choose to use our Service, then you agree to the collection and use of information in relation to this policy. The Personal Information that we collect is used for providing and improving the Service. We will not use or share your information with anyone except as described in this Privacy Policy.
The terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which is accessible at Manaviya unless otherwise defined in this Privacy Policy.
Information Collection and Use
For a better experience, while using our Service, we may require you to provide us with certain personally identifiable information, including but not limited to Name, Phone Number. The information that we request will be retained by us and used as described in this privacy policy.
The app does use third party services that may collect information used to identify you.
Link to privacy policy of third party service providers used by the app
Google Play Services
Facebook
Log Data
We want to inform you that whenever you use our Service, in a case of an error in the app we collect data and information (through third party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (“IP”) address, device name, operating system version, the configuration of the app when utilizing our Service, the time and date of your use of the Service, and other statistics.
Cookies
Cookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device's internal memory.
This Service does not use these “cookies” explicitly. However, the app may use third party code and libraries that use “cookies” to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies, you may not be able to use some portions of this Service.
Service Providers
We may employ third-party companies and individuals due to the following reasons:
To facilitate our Service;
To provide the Service on our behalf;
To perform Service-related services; or
To assist us in analyzing how our Service is used.
We want to inform users of this Service that these third parties have access to your Personal Information. The reason is to perform the tasks assigned to them on our behalf. However, they are obligated not to disclose or use the information for any other purpose.
Security
We value your trust in providing us your Personal Information, thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet, or method of electronic storage is 100% secure and reliable, and we cannot guarantee its absolute security.
Links to Other Sites
This Service may contain links to other sites. If you click on a third-party link, you will be directed to that site. Note that these external sites are not operated by us. Therefore, we strongly advise you to review the Privacy Policy of these websites. We have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party sites or services.
Children’s Privacy
These Services do not address anyone under the age of 13. We do not knowingly collect personally identifiable information from children under 13 years of age. In the case we discover that a child under 13 has provided us with personal information, we immediately delete this from our servers. If you are a parent or guardian and you are aware that your child has provided us with personal information, please contact us so that we will be able to do necessary actions.
Changes to This Privacy Policy
We may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. We will notify you of any changes by posting the new Privacy Policy on this page.
This policy is effective as of 2021-05-11
Contact Us
If you have any questions or suggestions about our Privacy Policy, do not hesitate to contact us at covidsynergy@gmail.com.
This privacy policy page was created at privacypolicytemplate.net and modified/generated by App Privacy Policy Generator
'''
    def next(self,ch):
    	if ch:
    		self.manager.add_widget(Screen2(name ="screen_two"))
    		self.manager.current='screen_two'#goes to net screen
    	
class Screen2(Screen):
	def enter(self,na,ph):
			try:
				int(ph)
				if(len(ph)==10 and len(na)>0):
					self.manager.add_widget(Screen3(name ="screen_three"))
					self.manager.current='screen_three'#there is acually more to be added as otp should be sent.code for that not written yet.
			except:
				pass
		
class Screen3(Screen):
	def vol(self):
		url='https://docs.google.com/forms/d/e/1FAIpQLSd2xeeOsmpmpfwMr73_DpPZUnRmthAHF447tDPOD-ybf-wiLQ/viewform?usp=pp_url'
		import webbrowser
		from kivy.utils import platform
		if platform == 'android':
			from jnius import autoclass, cast
			def open_url(url):
				PythonActivity = autoclass('org.kivy.android.PythonActivity')
				activity = PythonActivity.mActivity
				Intent = autoclass('android.content.Intent')
				Uri = autoclass('android.net.Uri')
				browserIntent = Intent()
				browserIntent.setAction(Intent.ACTION_VIEW)
				browserIntent.setData(Uri.parse(url))
				currentActivity = cast('android.app.Activity', activity)
				currentActivity.startActivity(browserIntent)
			class AndroidBrowser(object):
				def open(self, url, new=0, autoraise=True):
					open_url(url)
				def open_new(self, url):
					open_url(url)
				def open_new_tab(self, url):
					open_url(url)
        	   	
			webbrowser.register('android', AndroidBrowser, None)
			webbrowser.open(url)
	#we go through our list di, find dictionaries matching requirements for state,city and pincode and add those to li. then we go to next screen
	def loc(self,pin):
		try:
			for i in di:
				if(i["Pincode"]==int(pin)):
					li.append(i)
			self.manager.add_widget(Screen4(name ="screen_four"))
			self.manager.current="screen_four"
		except:
			pass
	#below we have functions to get list of cities for state and list of pincodes for the city.
	def back(self):
		self.manager.transition=SlideTransition(direction='right')
		self.manager.current='screen_two'
		self.manager.transition=SlideTransition(direction='left')
		self.manager.remove_widget(self.manager.get_screen("screen_three"))
	def npin(self):
		for i in di:
			li.append(i)
		self.manager.add_widget(Screen4(name ="screen_four"))
		self.manager.current='screen_four'

class Screen4(Screen):
	def vol(self):
		url='https://docs.google.com/forms/d/e/1FAIpQLSd2xeeOsmpmpfwMr73_DpPZUnRmthAHF447tDPOD-ybf-wiLQ/viewform?usp=pp_url'
		import webbrowser
		from kivy.utils import platform
		if platform == 'android':
			from jnius import autoclass, cast
			def open_url(url):
				PythonActivity = autoclass('org.kivy.android.PythonActivity')
				activity = PythonActivity.mActivity
				Intent = autoclass('android.content.Intent')
				Uri = autoclass('android.net.Uri')
				browserIntent = Intent()
				browserIntent.setAction(Intent.ACTION_VIEW)
				browserIntent.setData(Uri.parse(url))
				currentActivity = cast('android.app.Activity', activity)
				currentActivity.startActivity(browserIntent)
			class AndroidBrowser(object):
				def open(self, url, new=0, autoraise=True):
					open_url(url)
				def open_new(self, url):
					open_url(url)
				def open_new_tab(self, url):
					open_url(url)
        	   	
			webbrowser.register('android', AndroidBrowser, None)
			webbrowser.open(url)
	def back(self):
		li.clear()
		self.manager.transition=SlideTransition(direction='right')
		self.manager.current='screen_three'
		self.manager.transition=SlideTransition(direction='left')
		self.manager.remove_widget(self.manager.get_screen("screen_four"))
	def bnox(self):
		from kivy.uix.button import Button
		#first we check if the particular resource is present by looking through each dictionary in the list li, and if resource is absent then we remove it. then we add buttons to Screen5 accordingly while also storing them in li2 to be used later. we also store the no. of units of resource in li3, again to be used later.. the other three functions work exactly the same way.
		for i in li:
			if("beds without oxygen" in i["Resource Type"].lower()):
				li4.append(i)
		self.manager.add_widget(Screen5(name ="screen_five"))
		self.manager.current="screen_five"
		p=self.manager.children[0].children[0].children[0].children[0].children[0]#refers to screen5
		p.rows=len(li4)+1
		for i in li4:
			if(i['Beds Without Oxygen']==0):
				x="[color=#ff0000]inactive[/color]"#red color to active
			else:
				x="[color=#008000]active[/color]"#green colour to active
			li3.append(i['Beds Without Oxygen'])
			b=Button(markup=True,text=i['SUPPLIER NAME']+"\n"+x,size_hint_y=None,on_press=lambda i:self.manager.children[0].det(i),background_color=[1,0,2,1],valign='center',halign='center')#check class Screen5 for det function. the argument passed by lambda is the button itself.
			li2.append(b)
			p.add_widget(b)
		p.height=p.minimum_height
		for i in li2:
			def a(instance,value):
				print(value,instance)
				instance.text_size=instance.width,None
			def b(instance,value):
				instance.height=instance.texture_size[1]
			i.bind(width=a)
			i.bind(texture_size=b)
	def box(self):
		from kivy.uix.button import Button
		for i in li:
			if("beds with oxygen" in i["Resource Type"].lower()):
				li4.append(i)
		self.manager.add_widget(Screen5(name ="screen_five"))
		self.manager.current='screen_five'
		p=self.manager.children[0].children[0].children[0].children[0].children[0]#refers to screen5
		p.rows=len(li4)+1
		for i in li4:
			if(i['Beds With Oxygen']==0):
				x="[color=#ff0000]inactive[/color]"#red color to inactive
			else:
				x="[color=#008000]active[/color]"#green colour to active
			li3.append(i['Beds With Oxygen'])
			b=Button(markup=True,text=i['SUPPLIER NAME']+"\n"+x,size_hint_y=None,on_press=lambda i:self.manager.children[0].det(i),background_color=[1,0,2,1],valign='middle',halign='center')#check class Screen5 for det function. the argument passed by lambda is the button itself.
			li2.append(b)
			p.add_widget(b)
		p.height=p.minimum_height
		for i in li2:
			def a(instance,value):
				print(value,instance)
				instance.text_size=instance.width,None
			def b(instance,value):
				instance.height=instance.texture_size[1]
			i.bind(width=a)
			i.bind(texture_size=b)
	def inv(self):
		from kivy.uix.button import Button
		for i in li:
			if("icu without ventilator" in i["Resource Type"].lower()):
				li4.append(i)
		self.manager.add_widget(Screen5(name ="screen_five"))
		self.manager.current='screen_five'
		p=self.manager.children[0].children[0].children[0].children[0].children[0]#refers to screen5
		p.rows=len(li4)+1
		for i in li4:
			if(i['ICU Without Ventilator']==0):
				x="[color=#ff0000]inactive[/color]"#red color to inactive
			else:
				x="[color=#008000]active[/color]"#green colour to active
			li3.append(i['ICU Without Ventilator'])
			b=Button(markup=True,text=i['SUPPLIER NAME']+"\n"+x,size_hint_y=None,on_press=lambda i:self.manager.children[0].det(i),background_color=[1,0,2,1],valign='middle',halign='center')#check class Screen5 for det function. the argument passed by lambda is the button itself.
			li2.append(b)
			p.add_widget(b)
		p.height=p.minimum_height
		for i in li2:
			def a(instance,value):
				print(value,instance)
				instance.text_size=instance.width,None
			def b(instance,value):
				instance.height=instance.texture_size[1]
			i.bind(width=a)
			i.bind(texture_size=b)
	def iv(self):
		from kivy.uix.button import Button
		for i in li:
			if("icu with ventilator" in i["Resource Type"].lower()):
				li4.append(i)
		self.manager.add_widget(Screen5(name ="screen_five"))
		self.manager.current='screen_five'
		p=self.manager.children[0].children[0].children[0].children[0].children[0]#refers to screen5
		p.rows=len(li4)+1
		for i in li4:
			if(i['ICU with ventilator']==0):
				x="[color=#ff0000]inactive[/color]"#red color to inactive
			else:
				x="[color=#008000]active[/color]"#green colour to active
			li3.append(i['ICU with ventilator'])
			b=Button(markup=True,text=i['SUPPLIER NAME']+"\n"+x,size_hint_y=None,on_press=lambda i:self.manager.children[0].det(i),background_color=[1,0,2,1],valign='middle',halign='center')#check class Screen5 for det function. the argument passed by lambda is the button itself.
			li2.append(b)
			p.add_widget(b)
		p.height=p.minimum_height
		for i in li2:
			def a(instance,value):
				print(value,instance)
				instance.text_size=instance.width,None
			def b(instance,value):
				instance.height=instance.texture_size[1]
			i.bind(width=a)
			i.bind(texture_size=b)
class Screen5(Screen):
	def vol(self):
		url='https://docs.google.com/forms/d/e/1FAIpQLSd2xeeOsmpmpfwMr73_DpPZUnRmthAHF447tDPOD-ybf-wiLQ/viewform?usp=pp_url'
		import webbrowser
		from kivy.utils import platform
		if platform == 'android':
			from jnius import autoclass, cast
			def open_url(url):
				PythonActivity = autoclass('org.kivy.android.PythonActivity')
				activity = PythonActivity.mActivity
				Intent = autoclass('android.content.Intent')
				Uri = autoclass('android.net.Uri')
				browserIntent = Intent()
				browserIntent.setAction(Intent.ACTION_VIEW)
				browserIntent.setData(Uri.parse(url))
				currentActivity = cast('android.app.Activity', activity)
				currentActivity.startActivity(browserIntent)
			class AndroidBrowser(object):
				def open(self, url, new=0, autoraise=True):
					open_url(url)
				def open_new(self, url):
					open_url(url)
				def open_new_tab(self, url):
					open_url(url)
        	   	
			webbrowser.register('android', AndroidBrowser, None)
			webbrowser.open(url)
	def back(self):
		p=self.manager.children[0].children[0].children[0].children[0].children[0]
		for i in range(0,len(p.children)-1):
			p.remove_widget(p.children[0])
		li2.clear()
		li3.clear()
		li4.clear()
		self.manager.transition=SlideTransition(direction='right')
		self.manager.current='screen_four'
		self.manager.transition=SlideTransition(direction='left')
		self.manager.remove_widget(self.manager.get_screen("screen_five"))
	#we get index of button pressed, get dictionary needed from that, and then display with a label.
	def det(self,v):
		self.manager.add_widget(Screen6(name ="screen_six"))
		self.manager.current="screen_six"
		m=self.manager.children[0].children[0].children[0].children#refers to screen6
		q=li4[li2.index(v)]
		m[5].text=q['SUPPLIER NAME']+'\n'
		m[4].text='Address : ' + q['Locality'] + ','+q['State']+','+q['City']+','+str(q['Pincode'])
		m[3].text='Phone No : '+str(q['Phone'])
		m[2].text='No of Units : '+str(li3[li2.index(v)])
		m[1].text='Verified on :\n'+q['Verified date & time']
		m[0].text='Updated date and time :\n'+q['Updated on']
		
class Screen6(Screen):
	def vol(self):
		url='https://docs.google.com/forms/d/e/1FAIpQLSd2xeeOsmpmpfwMr73_DpPZUnRmthAHF447tDPOD-ybf-wiLQ/viewform?usp=pp_url'
		import webbrowser
		from kivy.utils import platform
		if platform == 'android':
			from jnius import autoclass, cast
			def open_url(url):
				PythonActivity = autoclass('org.kivy.android.PythonActivity')
				activity = PythonActivity.mActivity
				Intent = autoclass('android.content.Intent')
				Uri = autoclass('android.net.Uri')
				browserIntent = Intent()
				browserIntent.setAction(Intent.ACTION_VIEW)
				browserIntent.setData(Uri.parse(url))
				currentActivity = cast('android.app.Activity', activity)
				currentActivity.startActivity(browserIntent)
			class AndroidBrowser(object):
				def open(self, url, new=0, autoraise=True):
					open_url(url)
				def open_new(self, url):
					open_url(url)
				def open_new_tab(self, url):
					open_url(url)
        	   	
			webbrowser.register('android', AndroidBrowser, None)
			webbrowser.open(url)
	def back(self):
		try:
			self.manager.transition=SlideTransition(direction='right')
			self.manager.current='screen_five'
			self.manager.transition=SlideTransition(direction='left')
			self.manager.remove_widget(self.manager.get_screen("screen_six"))
		except:
			pass
	def share(self):
		m=self.manager.children[0].children[0].children[0].children
		text=m[5].text+"\n"+m[4].text+"\n"+m[3].text+"\n"+m[2].text+"\n"+m[1].text+"\n"+m[0].text
		title='Info provided by manaviya'
		from kivy import platform
		if platform == 'android':
			from jnius import autoclass
			PythonActivity = autoclass('org.kivy.android.PythonActivity')
			Intent = autoclass('android.content.Intent')
			String = autoclass('java.lang.String')
			intent = Intent()
			intent.setAction(Intent.ACTION_SEND)
			intent.putExtra(Intent.EXTRA_TEXT, String('{}'.format(text)))
			intent.setType('text/plain')
			chooser = Intent.createChooser(intent, String(title))
			PythonActivity.mActivity.startActivity(chooser)

screen_manager = ScreenManager(transition=SlideTransition())
screen_manager.add_widget(Screen0(name='screen_zero'))

class CovidCareApp(App):
	def build(self):
		return screen_manager
CovidCareApp().run()