"""first_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#Django Admin header costumization
admin.site.site_header = "Avinier's Website"
admin.site.site_title = "Welcome to the Site Dashboard"
admin.site.index_title = "Welcome to the DataBase Portal"

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include("home.urls"))
]

#Iz2Fa1d1fRc
#love technology, business, finance, design and philosopy. Consider me a ploymath, jack of all trades ;)
#I write anything and everything ranging from Steve Jobs to Nassim Taleb.
#I'm a web developer and designer, and a future app developer and a blockchian expert.
