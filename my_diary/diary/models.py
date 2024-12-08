from django.db import models
from django.utils import timezone


class Task(models.Model):
  STATUS_CHOICES = (
    ('planned', 'В планах'),
    ('in_progress', 'В работе'),
    ('completed', 'Выполнена'),
  )

  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
  created_at = models.DateTimeField(auto_now_add=True)
  due_date = models.DateField(null=True, blank=True)
  completed_date = models.DateField(null=True, blank=True)

  def save(self, *args, **kwargs):
    if self.status == 'completed':
      self.completed_date = timezone.now().date()
    super().save(*args, **kwargs)

  def __str__(self):
    return self.title
