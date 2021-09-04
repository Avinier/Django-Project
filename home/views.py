from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("WELCOME TO AVINIER'S WEBSITE!")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("About me")
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        #print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("DATA HAS BEEN SAVED!")
 
    return render(request, 'contact.html')

def projects(request):
    #return HttpResponse("My Projects")
    return render(request, 'projects.html')