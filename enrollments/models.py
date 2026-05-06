from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course as Course

User = get_user_model()

# Create your models here.
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
