# Django-project
16-11-2020:
===========

Good Morning to All:
--------------------
	-> Sublime Text Editor [geany,atom,vs code]
	-> Python
	
Front end: [static]
	HTML5,CSS3,Javascript,Jquery,Ajax
	
Back end: [Dynamic]
	Java,python,php,.Net
	
Databases:[storing some data]
	Mysql,Postregsql,Mongodb,Nosql
	
Django:
=======
	-> Web Application framework to create web apps
	-> Web technologies [HTML,CSS,jquery] -> site
	-> Free source to create web apps 
	-> framework => Collection of packages and modules
	-> Class,objects,variables,procedural and object oreinted
	-> to reduce the code[dry => dont run yourself]
	-> To create web applications easily with secure
	-> bottle,flask etc.,
	-> Administration site -> inbuilt
	-> MVC -> support and it follows MVT

Django Installation:
====================

	-> Python version
		-> python path => environment variables -> add
		-> cmd -> python => >>> 
		-> cmd -> python --version => 3.xxx
			   -> python -V
	-> Third party packages installation
		-> pip => python/scripts/..
	-> for installation of django
		-> pip install django
				or
		-> pip install django==3.xx
		-> pip install django==2.xx
	-> To check django version
		-> django-admin --version
				or
		-> python -> shell
			-> import django
			-> print(django.__version__)

Django Project Creation:
========================
	=> select particular path to create a project
	=> open cmd prmpt in the location
	=> to create a project we need to type a command as
		**** Project Creation Syntax
		=> django-admin startproject "project name"
		-> django-admin startproject djinternship
			-> djinternsip => [folder] -> Admin App
			-> manage.py => .py file
	-> manage.py -> servies will be started 
			-> Creation of App
			-> settings
			-> migrations
			-> running of server
	-> to display all services we need to type the cmd as
		=> manage.py
			
Django Running environment:
===========================
	-> First navigate to manage.py file path location
		-> url -> cmd and hit enter
		-> server run cmd to be typed such as
			-> python manage.py runserver
			           or
			-> python manage.py runserver portnumber
					   or
		    -> manage.py runserver
	-> To check it in browser
		-> just type the url such as http://127.0.0.1:8000/
						or
		-> By default out local server ip is:127.0.0.1
		-> our default name for local server is:
			=> "localhost:8000"
			
Django Files:
=============
	-> While creating a project we had observed some files in a [Admin]folder.
	-> __init__ => It states that interpreter to consider as python file.  
	-> asgi => Asynchronous gateway interface -> server deployment 
	-> settings => main configurations[html,css,js,images,mail,app]
	-> urls => admin -> access, admin -> user url
	-> wsgi => Web socket gateway interface -> development

17-11-2020:
===========

	Good Morning to All
	
	=> Django installation
	=> Project Creation
	=> All created files -> description -> [Admin folder,manage.py -> services] 
	=> Project[app] -> run
	
	
	=> Userapp creation,files,configure,run -> urls
	=> MVC and MVT
	=> Request and response
	
User App Creation:
==================
	-> We have to navigate into the path of a project
	-> open cmd and then we need to pass a command to create an user app ie., userdefined
	-> cmd pmpt
		=> django-admin startapp "userappname"
		=> djanog-admin startapp djpi
	
	-> Userapp created files
		=> __init__ -> It will be considered to be as a python file for an interpreter
		=> admin -> view,models
		=> apps -> app has some specific permissions to run in server or not
		=> models -> Database,tablename,fields [datatypes] 
		=> test -> unit testing,black box testing
		=> views -> class,function,method => work

MVC:
===	
	-> M = Model => Database
	-> V = View => html,css,js,jquery
	-> C = Controller => backend -> [php,java,.net]
	
MVT:
===	
	-> M = Model => Databases
	-> V = View[urls,views => controller] => backend -> [python]
	-> T = Template => [DTL = Django Template Language] Html,css,js,jquery
	
Userapp configurations:
=======================
	-> Admin app =[projectname folder] -> settings.py -> userapp => Installed apps => configure
	-> urls.py => userdefined url have to be created
		syntax for url patterns:
		-------------------------
		from package import modulename
		path("url to be typed in a browser/",module.functionaname,name="userdefinedname"),
		Ex:
		from djpi import views
		path("hel/",views.functioname,name="h"),
	
	-> views.py => imported HttpResponse from djangottp
		-> function => return with something message to be displayed for a user.
		Syntax:
		-------
			from django.http import HttpResponse
			
			def hel(request):
				return HttpResponse("Hi Welcome")
			
		-> 1. Configure our userapp in settings.py
		-> 2. Setted url in urls.py from admin app,import module
		-> 3. Module => functionality to work while accessing the particular url
		-> 4. function has been created in views
		-> 5. HttpResponse import
		
	=> localhost:8000/hi/ramu
		Output:
				
				hi ramu welcome to Django internship 	
	-> urls.py:
		-> path("hll/<str:n>/",views.hlp),
		
	-> views.py:
		-> def hlp(r,n):
				return HttpResponse("Hi "+n+"Welcome to Django Internship")
		=> return HttpResponse("Hi {} Welcome to Django Internship".format(n))
	
Task:
====
	1.
		localhost:8000/2
			
		output:
				
			2 x  1 = 2
			2 x  2 = 4
			|   |    |
			2 x 10 = 20
	
18-11-2020:
===========

	Good Morning to All..
	
	def srt(k,o):
		s=[] 
		//logic
		return s
	
	h = [34,5,6,12,8]
	m = 56
	z = srt(h,m)
	for j in z:
		print(j,end=",")
	
	list,string,tuple,set,dictionary => Data Structures or Iterators
	
	
Dynamic Url:
============
	-> single parameter value to an url
		syntax:
		-------
		path("pathurl/parameter/",views.functioname,name="namevalue")
		Ex:
		path("tbl/<int:y>/",views.tble),
		
	-> two parameter values to an url
		Ex:
		path("rcd/<str:name>/<int:age>/",views.record),
		
	-> two or more as like as two parameter values to an url
	
	def record(req,name,age):
		m = "Hi your name is: {}<br/>Your age is: {}<br/>".format(name,age)
		p = "Your sal is: "+str(sal)
	return HttpResponse(m+p)
	
	
	HttpResponse => HTML tags
				 => CSS
				 => Js
	
23-11-2020:
===========
	Good Morning to All.
		
	Inline elements -> span,i,b
	block elements -> div,h
	
	Hi Welcome <span style="?"> Raju </span> Your age is <span style="?">24</span>
	
	
	Templates: -> .html[saves in folder]
	
	django 2.0 we need to configure template path to acces all .html files to that particular project
	
	views:
	======
	d = {key:value}
	return render(request,"path of .html",{})
	
	DTL:[Django Template Language]
	=============================
	
	variable:
	=========
	return render(re,'home.html',{'a':12}) -> {} => .format
	
	your value is: {{a}} => .html
	
	Conditional Statements:
	=======================
	-> if
	syntax:
		{% if condition %}
			//stmnt
		{% endif %}
	-> if-else
	syntax:
		{% if condition %}
			//stmnt-1
		{% else %}
			//stmnt-2
		{% endif %}
	-> nested if
	syntax:
		{% if condition %}
			//stmnt-1
		{% elif condition %}
			//stmnt-2
		{% elif condition %}
			//stmnt-3
			|   |   |
		{% elif condition %}
			//stmnt-n	
		{% else %}
			//stmnt-2
		{% endif %}
	
	Loops:
	======
	-> for,while
	
	-> for 
	syntax:
		{% for iterationvariable in iterator %}
			{{iterationvariable}}
			//stmnts
		{% endfor %}
	
	
	url -> views -> html
	
	templates folder in our project
	
	djinpoly -> project name
		djpi -> app name
		=> templates
			=> prjc -> user defined name
				=> sample.html
	
	return render(request,'prjc/sample.html',{})
	
	Registration Page: -> inline style,internal
	-> data => submit -> 
	
	url -> views -> register.html -> data 
		   views <------------------ data	
		   views -> display.html
	
	
24-11-2020:
==========
	Good Morning to All..
	
	
	form => data => database[store]
	
		input : values => fill
		submit : values
		action : True
	
	Methods:
	-------
	- GET => data can be stored
		  => Fetching of data from database
		  => values can be visible in url
		  => some limit of data can be passed [250 characters]
		  
	- POST => data can be stored
		   => secure format of data can be used
		   => Complex data can be transfered from form
		   
	Login Page: [css]
	
	Username : raju
	password :
	
	username == raju password == 123
	
		hi user raju
		
		user name is incorrect
		password is incorrect
	
	CSS:[tag,*,#]
	= Inline -> within a tag[ style="property: value"]
	= Internal -> within a head tag[we need to use style tag]
		syntax:
			<style>
			h1,h5 
			{
				property: value;
			}
			</style>
	= External -> propert: value => styling -> sample.css
	<link rel="stylesheet" href="path of .css file">
	
	Static:[CSS,Js,Jquery,Images]
	=============================
	
	userdefined appname:
		-> static
			=> css
				-> sample.css
			=> js
				-> sample.js
			=> images
				-> userdefined images

25-11-2020:
===========
	Good Morning to All
	
	CSS
	jquery
	js
	
	static
		- css
			- sample.css
		- js
			- demo.js
		- images
			- first.jpg
			
	{% load static %}
	<link rel="stylesheet" href="{% static 'css/sample.css'%}">
	<script type="text/javascript" src="{% static 'js/demo.js'%}"></script>
	<img src="{% static 'images/first.jpg' %}">
	
	
	Bootstrap:
	==========
	- Reponsiveness, beautification of site
	- Online
		- internet => url access
	- Offline
		- download => static -> css,js,images,jquery

	djinpoly: [Project folder]
		- djinpoly -> [Admin app] -> urls,settings
		- djpi -> [own html,css,] => userapp 
		- djboot -> userapp => [bootstrap]
	
	m,p => points => class -> style 
	

30-11-2020:
===========
	Good Morning to All.
	
	Models -> To store/retrieve/update/delete the data in databases
	
	Class Student(models.Model):
		name = models.Charfield()
		age = models.IntegerField()
	
	Syntax:
		projectname_classname
			djpin_Student -> Tablename
			name,age => Fields
	
	makemigrations -> interfacing file -> create
	migrate -> updates model class to a database
	
	Class Student(models.Model):
		name = models.CharField()
		rollno = models.CharField()
		branch = models.CharField()
		year = models.IntegerField()
		
	url => views => .html => data
		   views <= data
		   views => models 	
	
	primary,secondary,danger,success,warning,info,light,dark
	margin:
		mx => left,right
		my => top,bottom
		m  => all directions
		
		m-4 p-4 => points
		
		
01-12-2020:
===========
	Good Morning to All..
	
	url => views => .html => views => models => .html
	from django.shortcuts import redirect
	return redirect('urlname/')
	
	path('urlname/',views.functioname,name="?")
	
02-12-2020:
===========
	Good Morning to All...
	
	own registration form [.html]
		- view
		- models[database]
		- html
		
	Forms.py:
	=========
	
	models => fields
	
	automatic generation[restrict]
	
	url -> views -> forms -> model
					form <- model
					form -> views -> .html -> data
					views <- data
					views -> models
	
	Widgets:[Bootstrap Styling] => Forms:
	=====================================
	from django import forms
	
	widgets = {
	"name":forms.TextInput(attrs = {
	"class":"form-control",
	"placeholder":"Enter Your name"
	})
	}
	
	
03-12-2020:
===========
	Good Morning to All...
	
	CRUD => Completed CRUD by using Bootstrap
	Creation -> basic,forms
	View -> Display
	Update -> Forms.py
	Delete -> .html -> confirm 

04-12-2020:
===========
	Good Morning to All..
	
	project:
		admin app
			> urls.py
			  
			  views -> views
			  views -> alias -> v 
			  frstapp => path(views.functionaname)
			  secondapp => path(v.functioname)
			  
	project:
		admin app
			> urls.py
			
	Projectname:
	
	-> DjPrjct => Projectname
		-> UsApp => Userdefined App

05-12-2020:
===========
	Good Morning to All.....
	
	
	navbar -> bootstrap -> site names -> rename
	
	base.html => header => links
	navabar.html => links
	html => body
	
	extends,include,dtl -> title,content
	
	
	Registration => models => table => forms -> views => html
	
07-12-2020:
===========
	Good Morning to All...

	card
	<table>
	<tr>
	<td><h2>User Registration</h2></td>
	</tr>
	{% for j in k %}
	<tr>
		<td>{{j}}</td>
	</tr>
	{% endfor %}
	<tr>
	<td><input type="button"></td>
	</tr>
	</table>
	
	password => sha algorithm(password1 + password2)
	

08-12-2020:
===========
	Good Morning to All..
	
	Authentication pages after login and logout
	Conditional statements in navbar only for authenticated persons view
	
09-12-2020:
===========
	Good Morning to All...
	
	decorator:
	==========
	urls.py:
	--------
	path('dash/',v.dashboard,name="dsh")
	
	views.py:
	----------
	from django.contrib.auth.decorators import login_required
	
	@login_required
	def dashboard(request):
		return
		
	navabar.html
	============
	{% if not user.is_authenticated %}
		// links
	{% else %}
		// links
	{% endif %}

	Mail Sending:
	=============
	
		-> 500 => mails -> per/day
		
	Google Account
		-> Account
			-> security
				-> less secure app => On
	
	email -> configure => emailid,password
	
	settings.py:
	------------
	
	EMAIL_USE_TLS = True
	EMAIL_HOST = "smtp.gmail.com"
	EMAIL_PORT = 587
	EMAIL_HOST_USER = "apssdcpolytechnicinternship2@gmail.com"
	EMAIL_HOST_PASSWORD = "xxxxxxxx"
	
	views.py:
	=========
	from DjPrjct import settings
	from django.core.mail import send_mail
	
	settings.EMAIL_HOST_USER
	send_mail(subject,message,emailconfigure,[to])

10-12-2020:
===========
	Good Morning to All...
	
	mail => concept => 1 single
	
	views.py: [Multiple users]
	==========================
	rec = request.POST['sndml'].split(",")
	
	s = send_mail(subject,message,fixed username,rec)
	
	views.py:[Existing users database]
	==================================
	empty fields,user => login => mail => x
	
	@login_required
	def mailsnd(request):
		pq = user.objects.values_list("email",flat=True)
		if request.method == "POST":
			# rec = request.POST['sndml'].split(",")
			# print(rec)
			rec = []
			adml = request.user.email
			rs = list(filter(None,pq)
			for m in rs:
				if m=="" or m==adml:
					continue
				else:
					rec.append(m)
			print(rec)
			sub = request.POST['subject']
			msg = request.POST['messg']
			sd = settings.EMAIL_HOST_USER
			t = send_mail(sub,msg,sd,rec)
			if t == 1:
				return redirect("/ml")
			return HttpResponse("Didnt send mail to particular person")
		return render(request,'sa/mailsending.html')
		
	Dropdowns,Profile page,updateprofile => forms [profile updation]
	
	Messages: => updates,data limit, => notification
	=========
	
	from django.contrib import messages
	
	messages.success(request,"msg")
	
	success -> green
	debug -> 
	warning ->
	
	html:
	
	{% if messages %}
	{% for m in messages %}
	<div class="alert alert-{{m.tags}} alert-dismissible">
	<button type="button" class="close" data-dismiss="alert">&times;</button>
	<strong>{{m}}</strong>
	</div>
	{% endfor %}
	{% endif %}
	
	Profile => Image Uploads [File uploading]
	
11-12-2020:
===========
	Good Morning to All...
	
	
	own table => models => class
	
	existing -> model => model

	profile => update -> OneToOneField()
	
	OneToManyField()
	
	ManyToManyField()
	
	ManyToOneField()
	
	signals:=> model -> own => Existing model => link

		new user => User => ownprofile[img,age] 
				 => id   => id
				 
	image => ImageField() => pip install pillow
	files => FileField()

12-12-2020:
===========
	- Drweabacks in SQLite3
		- if any modifications are made in browser 
			we may not effect in db(it will shows 'db is lock')
		- it has less storage space(it is preforble for practice only)
		
	- Mysql Connections:
			- for making mysql db connection ,
			we have to iinstall `mysqlclient`
			-mysqlclient is a external module in python
			- this mysqlclient will acts like a driver
			-for installing mysqlclient,we have to use a cmd
				`pip install mysqlclient`
			- after installation,we have to make 
				few configurations inside settings.py
				`DATABASES = {
								'default': {
								'ENGINE': 'django.db.backends.mysql',
								'NAME': 'djproject',
								'USER': 'root',
								'PASSWORD':''.
								'HOST':'',
								'PORT':'',
										}
								}`
				- once changes is done, we have 
				to run makemigrations and migrate cmds 
				to create tables iinside our db.

14-12-2020:
===========
	## Project Requirements:
		- you have to bulid a new project with name of 'worklog'
		- then  create app with name of 'dailyworkstatus'
		- inside project you have to make registration 
			form for user(have to access USER Model).
			- registration form need to include 
				- FirstName,
				- LastName,
				- User Name,
				- Password,
				- Mail Id.
			- after registration u have to send a mail 
				to registered user with his name and password,
				then show him conformation message 
				inside login.html page.
			- next you have to make a profile form for user
				- user image,
				- Mobile Numbber,
				- DOB,
				- Gender.
			
			


