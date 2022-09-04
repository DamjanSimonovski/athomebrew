# Generated by Django 4.1 on 2022-08-31 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cover-image/')),
                ('rating', models.IntegerField()),
                ('brew', models.CharField(choices=[('Cold Brew', 'Cold Brew'), ('Vacuum Pot', 'Vacuum Pot'), ('Moka Pot', 'Moka Pot'), ('French Press', 'French Press'), ('Espresso Machine', 'Espresso Machine'), ('Drip Brew', 'Drip Brew')], max_length=30)),
                ('roast', models.CharField(choices=[('Light Roast', 'Light Roast'), ('Medium Roast', 'Medium Roast'), ('Medium-Dark Roast', 'Medium-Dark Roast'), ('Dark Roast', 'Dark Roast')], max_length=30)),
                ('temp', models.CharField(choices=[('Hot', 'Hot'), ('Cold', 'Cold')], max_length=30)),
                ('extras', models.CharField(choices=[('Sugar', 'Sugar'), ('Chocolate', 'Chocolate'), ('Icecream', 'Icecream'), ('Milk', 'Milk'), ('Sparkling Water', 'Sparkling Water'), ('Spices', 'Spices')], max_length=30)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]