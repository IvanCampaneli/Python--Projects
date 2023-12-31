# Generated by Django 4.2.3 on 2023-07-18 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_alter_profile_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('video', models.URLField()),
                ('projetos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='projetos.profile')),
            ],
        ),
    ]
