# Generated by Django 3.1.1 on 2020-12-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0005_orgprofile_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgprofile',
            name='staff',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
