from django.db import models

# Create your models here.
class batch(models.Model): # Batch model to store batch information
    batchname = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.batchname
class tblcontact(models.Model): # Contact model to store user contact information
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    mobile = models.CharField(max_length=20, null=True)
    message = models.TextField(null=True)


class tblgallery(models.Model): # Gallery model to store images and titles
    title = models.CharField(max_length=50, null=True)
    picture = models.ImageField(upload_to='static/gallery/', null=True)

class tblregister(models.Model): # Registration model to store user registration details
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, primary_key=True)
    mobile = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=100, null=True)
    picture = models.ImageField(upload_to='static/userpic/', blank=True)
    batch = models.ForeignKey(batch,on_delete=models.CASCADE,null=True)
    address = models.TextField(null=True)
    regdate= models.DateTimeField(null=True)



class category(models.Model): 
    title = models.CharField(max_length=50, null=True) 
    picture = models.ImageField(upload_to='static/category/', null=True, blank=True) # Category model to store category information
    batch_name= models.ForeignKey(batch, on_delete=models.CASCADE)
    def __str__(self):
         return self.title

class softwarekit(models.Model): # Software Kit model to store software kit information
    title = models.CharField(max_length=100, null=True)
    software_info = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='static/softwarethumb/', null=True, blank=True)
    download_link = models.CharField(max_length=200, null=True)
    posted_date = models.DateField(null=True)

class mylecture(models.Model):
    title=models.CharField(max_length=300,null=True)
    video_info=models.TextField(null=True)
    vlink=models.CharField(max_length=300,null=True)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    posted_date=models.DateField(null=True)

class notes(models.Model):
    title=models.CharField(max_length=200,null=True)
    notes_info=models.TextField(null=True)
    batch = models.ForeignKey(batch,on_delete=models.CASCADE)
    posted_date=models.DateField(null=True)
    notesfile=models.FileField(upload_to="static/notes/", null=True,blank=True)

class mytask(models.Model):
    title=models.CharField(max_length=200,null=True)
    task_info=models.TextField(null=True)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE)
    taskfile=models.FileField (upload_to="static/task/",null=True,blank=True)
    posted_date=models.DateField(null=True)

class submittedtask(models.Model):
    userid=models.CharField(max_length=50,null=True)
    tid=models.IntegerField(null=True)
    title=models.CharField(max_length=50,null=True)
    upload_task=models.FileField(upload_to="static/submitted/",null=True,blank=True)
    marks=models.IntegerField(null=True)
    

