from django.db import models


class Huddle(models.Model):
    key = models.CharField(max_length=100)


class Item(models.Model):
    huddle = models.ForeignKey(Huddle, related_name='items', on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']