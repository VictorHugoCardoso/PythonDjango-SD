# Generated by Django 3.2.7 on 2021-09-10 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='assinado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=200)),
                ('privkey', models.CharField(max_length=500)),
            ],
        ),
    ]
