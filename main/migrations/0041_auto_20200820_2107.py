# Generated by Django 3.1 on 2020-08-20 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0040_postnotification_postnotificationrecord"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="postnotification", unique_together={("email", "blog_user")},
        ),
    ]
