# Generated by Django 5.1.5 on 2025-01-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dae_web_sys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='custos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesorreg', models.CharField(default='', max_length=40)),
                ('regint', models.CharField(default='', max_length=40)),
                ('municipio', models.CharField(default='', max_length=40)),
                ('modalidade', models.CharField(default='', max_length=40)),
                ('tecnologia', models.CharField(default='', max_length=40)),
                ('mbps', models.CharField(default='', max_length=40)),
                ('cunittransp', models.FloatField(default=0.0)),
                ('cmanut', models.FloatField(default=0.0)),
            ],
        ),
    ]
