from django.db import models
from django.utils import timezone


class MainPage(models.Model):
    about_text = models.TextField()
    dean_name = models.CharField(max_length=255)
    dean_degree = models.CharField(max_length=255)
    contacts = models.TextField()

    def __str__(self):
        return f"Головна сторінка ({self.dean_name})"


class Department(models.Model):
    name = models.CharField(max_length=255)
    head_of_department = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Program(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="programs"
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=255)
    coordinator_contact = models.CharField(max_length=255)
    disciplines = models.TextField()

    def __str__(self):
        return f"{self.code} {self.name}"


class Teacher(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="teachers"
    )
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.position}"


class ExchangeProgram(models.Model):
    university_name = models.CharField(
        max_length=255, verbose_name="Назва університету"
    )
    country = models.CharField(max_length=100, verbose_name="Країна", default="")
    languages = models.CharField(max_length=255, verbose_name="Мови навчання")
    places = models.IntegerField(verbose_name="Кількість місць")
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис", blank=True)

    def __str__(self):
        return self.university

    @property
    def university(self):
        return f"{self.university_name}, {self.country}".strip()

    @property
    def is_active(self):
        if self.deadline is None:
            return False
        return self.deadline >= timezone.now().date()
