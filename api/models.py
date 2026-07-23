from django.db import models

# Create your models here.
#create the company model

class Company(models.Model()):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100 choices=(('IT','IT'),('Finance','Finance'),('Healthcare','Healthcare'),('Education','Education'),('Other','Other')))
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
#emplloyee model
