# Generated by Django 2.2.20 on 2023-07-04 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0095_challenge_queue_aws_region"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="challenge",
            options={"ordering": ("title",)},
        ),
    ]
