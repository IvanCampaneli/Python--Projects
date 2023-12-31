# Generated by Django 4.2.3 on 2023-07-11 20:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_projetos')),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('ANALYSIS', 'Data Analysis'), ('SCIENCE', 'Data Science'), ('AUTOMATIONS', 'Web Scraping RPA'), ('OUTROS', 'Outros')], max_length=20)),
                ('visualizações', models.IntegerField(default=0)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
