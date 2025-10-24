from django.db import models
from django.contrib.auth.models import AbstractUser


class Specialty(models.Model):
    name = models.CharField(
        max_length=24,
        unique=True,
    )


class Worker(AbstractUser):
    specialty = models.ForeignKey(
        Specialty,
        related_name="workers",
        on_delete=models.DO_NOTHING
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class TaskType(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
    )


class Patient(models.Model):
    first_name = models.CharField(
        max_length=64,
    )
    last_name = models.CharField(
        max_length=64,
    )


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'
        CRITICAL = 'CRITICAL', 'Critical'

    name = models.CharField(max_length=255)
    description = models.TextField()
    planned_on = models.DateTimeField()
    is_canceled = models.BooleanField(default=False)
    priority = models.CharField(
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    task_type = models.ForeignKey(
        TaskType,
        related_name="tasks",
        on_delete=models.SET_NULL
    )
    assignees = models.ManyToManyField(
        Worker,
        related_name="tasks",
    )
    patients = models.ManyToManyField(
        Patient,
        related_name="tasks",
    )
