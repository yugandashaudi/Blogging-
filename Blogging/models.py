from django.db import models
from django.contrib.auth.models import User


types_post = [
    ('PT','pratical_therapy'),
    ('RT','radio_therapy'),
    ('ET','emerging_therapy'),
    ('DI','Diagonistic_imaging'),
    ('NM','neuclear_medicine')
]



class Post(models.Model):
    associated_user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_type = models.CharField(max_length=10,choices=types_post)
    heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    video = models.FileField()
    comments = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
