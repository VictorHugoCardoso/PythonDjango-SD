# Generated by Django 3.2.7 on 2021-09-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_assinado'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinado',
            name='sign',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
