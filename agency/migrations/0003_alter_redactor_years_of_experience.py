# Generated by Django 4.1.7 on 2023-03-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agency", "0002_alter_redactor_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(blank=True),
        ),
    ]
