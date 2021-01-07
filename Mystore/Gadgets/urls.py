from django.urls import path
from Gadgets import views
from django.contrib.auth import views as g

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('rg/',views.register,name="reg"),
	path('ds/',views.dashboard,name="dsh"),
	path('pf/',views.prfle,name="pfe"),
	path('upf/',views.updf,name="upfe"),
	path('lg/',g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
	path('lgg/',g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	path('st/',views.start,name="str"),
	path('it/',views.introduction,name="itd"),
	path('ar/',views.arrays,name="arr"),
	path('sri/',views.strings,name="st"),
	path('fc/',views.function,name="fct"),
	path('exa/',views.examonline,name="ex"),
]