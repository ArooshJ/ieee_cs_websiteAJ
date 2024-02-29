from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null =True, blank =True)
    date = models.DateField(null=True, blank = True)
    registration_link = models.TextField(null = True, blank = True)
    mode = models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    total_regs = models.IntegerField(null = True, blank = True)
    

    def __str__(self):
        return self.title

class Event_Media(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    file = models.FileField(null=True,blank=True,upload_to='event_media')


class Sponsors(models.Model):
   name = models.CharField(max_length = 100)
   association = models.CharField(max_length = 500, null=True, blank =True)
   event = models.ForeignKey(Event,on_delete = models.CASCADE)
   image = models.ImageField(null=True,blank=True,upload_to='sponsor_imgs')
   

   def __str__(self):
       return self.name


class Faculty(models.Model):
    name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 500)
    department = models.CharField(max_length = 500)
    image = models.ImageField(null=True,blank=True,upload_to='faculty_imgs')
    def __str__(self):
        return self.name
    


class Member(models.Model):
   name = models.CharField(max_length = 100)
   College = models.CharField(max_length = 500)
   year_of_study = models.IntegerField()
   role = models.CharField(max_length = 500)
   image = models.ImageField(null=True,blank=True,upload_to='member_imgs')
   def __str__(self):
       return self.name



