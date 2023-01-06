# Generated by Django 4.1.4 on 2022-12-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("dob", models.DateTimeField()),
                ("gender", models.CharField(max_length=250)),
                ("phno", models.IntegerField()),
                ("mailid", models.EmailField(max_length=250)),
                ("addresss", models.CharField(max_length=250)),
                ("dist", models.CharField(max_length=250)),
                ("branch", models.CharField(max_length=250)),
                ("acctype", models.CharField(max_length=250)),
                ("matpro", models.CharField(max_length=250)),
            ],
        ),
    ]
