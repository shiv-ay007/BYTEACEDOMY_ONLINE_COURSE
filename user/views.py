from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Mobile = request.POST.get("mob")
        Email = request.POST.get("email")
        Message = request.POST.get("msg")
        # Here you can handle the form data, e.g., save it to the database or send an email
        tblcontact(name=Name, mobile=Mobile, email=Email, message=Message).save()
        return HttpResponse("<script>alert('Thank you for contacting us!');location.href='/index/';</script>")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
def team(request):
    return render(request, "team.html")
def gallery(request):
    data= tblgallery.objects.all()
    d={"gal": data}
    return render(request, "gallery.html", d)

def services(request):
    return render(request, "services.html")
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("passwd")
        users = tblregister.objects.filter(email=email, password=password)

        if users.count() == 1:
            user = users[0]  
            request.session["name"] =str(users[0].name)
            request.session["userpic"] =str(users[0].picture)
            b=users[0].batch
            if b:
                 request.session["batch"] =str(users[0].batch.id)
            request.session["email"] = email
            return HttpResponse("<script>alert('You are successfully logged in');location.href='/student/dashboard'</script>")
        else:
            return HttpResponse("<script>alert('Your Email ID or Password is incorrect');location.href='/login/'</script>")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        email = request.POST.get("email")
        Mobile = request.POST.get("mob")
        password = request.POST.get("passwd")
        Picture = request.FILES.get("fu")
        Address = request.POST.get("address")
        # Here you can handle the registration data, e.g., save it to the database
        tblregister(name=Name, email=email, mobile=Mobile, password=password, picture=Picture, address=Address, regdate=datetime.now().date()).save()
        return HttpResponse("<script>alert('Registration successful!');location.href='/register/';</script>")
    return render(request, "register.html")

def logout(request):
   
    return render(request,"logout.html")

def contact(request):
   
    return render(request,"contact.html")

