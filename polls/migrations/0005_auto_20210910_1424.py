# Generated by Django 3.2.7 on 2021-09-10 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_sign_assinado_signature'),
    ]

    operations = [
        migrations.DeleteModel(
            name='assinado',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
