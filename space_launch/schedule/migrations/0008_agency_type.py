# Generated by Django 4.1.5 on 2023-04-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_alter_agency_options_agency_content_agency_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='type',
            field=models.TextField(default="Unknown", max_length=64),
            preserve_default=False,
        ),
    ]
