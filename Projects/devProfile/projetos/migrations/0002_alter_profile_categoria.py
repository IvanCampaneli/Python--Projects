# Generated by Django 4.2.3 on 2023-07-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='categoria',
            field=models.CharField(choices=[('ANALYSIS', 'Data Analysis'), ('SCIENCE', 'Data Science'), ('AUTOMATIONS', 'Web Scraping RPA'), ('CERTIFICADOS', 'Certificados'), ('OUTROS', 'Outros')], max_length=20),
        ),
    ]
