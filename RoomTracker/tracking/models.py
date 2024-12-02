from django.db import models

class Person(models.Model):
    face_id=models.CharField(max_lenght=50, unique=True)
    image=models.ImageField(upload_to='faces/')
    first_seen=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.face_id