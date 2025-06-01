from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialty})"
    
    

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Appointment(models.Model):
        doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
        patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
        date = models.DateField()
        time = models.TimeField()
        description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.time} / {self.patient} with {self.doctor}"
