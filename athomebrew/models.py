from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="cover-image/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()
    brew_choice = (
        ("Cold Brew", "Cold Brew"),
        ("Vacuum Pot", "Vacuum Pot"),
        ("Moka Pot", "Moka Pot"),
        ("French Press", "French Press"),
        ("Espresso Machine", "Espresso Machine"),
        ("Drip Brew", "Drip Brew")
    )
    brew = models.CharField(max_length=30, choices=brew_choice)
    roast_choice = (
        ("Light Roast", "Light Roast"),
        ("Medium Roast", "Medium Roast"),
        ("Medium-Dark Roast", "Medium-Dark Roast"),
        ("Dark Roast", "Dark Roast")
    )
    roast = models.CharField(max_length=30, choices=roast_choice)
    temp_choice = (
        ("Hot", "Hot"),
        ("Cold", "Cold")
    )
    temp = models.CharField(max_length=30, choices=temp_choice)
    extras_choice = (
        ("Sugar", "Sugar"),
        ("Chocolate", "Chocolate"),
        ("Icecream", "Icecream"),
        ("Milk", "Milk"),
        ("Sparkling Water", "Sparkling Water"),
        ("Spices", "Spices")
    )
    extras = models.CharField(max_length=30, choices=extras_choice)