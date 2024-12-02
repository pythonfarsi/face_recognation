from django.db import models

class Person(models.Model):
    face_id=models.CharField(max_length=225, unique=True)
    image=models.ImageField(upload_to='faces/')
    first_seen=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.face_id
    
class MovementLog(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.person.face_id} at {self.location} on {self.timestamp}"
    
    