from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name
    
class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
    email=models.EmailField()

    def __str__(self):
        return self.name
class AccessRecords(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    auother=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.auother