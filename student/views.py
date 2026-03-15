from django.shortcuts import render, redirect
from user.models import *
from django.http import HttpResponse


# Create your views here.
def dashboard(request):
    return render(request, 'student/dashboard.html')
def mycategory(request):

    return render(request, "student/category.html")
def lectures(request):
    x=request.GET.get("cid")
    if x:
         data=mylecture.objects.all().filter(category=4)
    else:
        data=mylecture.object.all().order_by("-id")

    d={"vdo":data}
    return render(request, "student/lectures.html",d)
def lecturecat(request):
    bid=request.session.get("batch")
    cat=category.objects.all().filter(batch_name=bid)
    d={"categories":cat}
    return render(request, "student/lecturecat.html",d)
def enotes(request):
    bid=request.session.get("batch")
    data=notes.objects.all().filter(batch=bid)
    d={"notes":data}
    return render(request, "student/enotes.html",d)
def profile(request):
    user=request.session.get("email")
    data=tblregister.objects.all().filter(email=user)
    d={"userinfo":data}
    return render(request, "student/profile.html",d)
def signout(request):
    user=request.session.get("email")
    if user:
        del request.session["name"]
        del request.session["userpic"]
        del request.session["email"]
        return redirect("/login/")
    return render(request, "student/signout.html")
def software(request):
    data=softwarekit.objects.all().order_by("-id")
    d={"sdata":data}
    return render(request, "student/softwarekit.html",d)

def task(request):
    bid=request.session.get("batch")
    data=mytask.objects.all().filter(batch=bid)
    d={"data":data}
    return render(request,"student/task.html",d)

def tsubmitted(request):
    userid=request.session.get("email")
    if request.method=="POST":
        title=request.POST.get("title")
        tid=request.POST.get("tid")
        taskfile=request.FILES["FU"]
        x=submittedtask.objects.all().filter(userid=userid,tid=tid).cont()
        if x==1:
            return HttpResponse("<script>alert('this task is already submitted..');location.href='/student/task/'</script>") 
        else:
            submittedtask(title=title,tid=tid,upload_task=taskfile,userid=userid).save
            return HttpResponse("<script>alert('submitted succesfully');location.href='/student/task/'</script>") 
    return render(request,"student/tsubmitted.html")

def python(request):
    return render(request, "student/python.html")

def bootstrap(request):
    return render(request, "student/bootstrap.html")

def java(request):
    return render(request, "student/java.html")

def csharp(request):
    return render(request, "student/csharp.html")

def clanguage(request):
    return render(request, "student/clanguage.html")

def php(request):
    return render(request, "student/php.html")