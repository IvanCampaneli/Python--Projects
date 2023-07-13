from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    #(armazenar_bd, aparecer_para_usuario)
    ("ANALYSIS", "Data Analysis"),
    ("SCIENCE", "Data Science"),
    ("AUTOMATIONS", "Web Scraping RPA"),
    ("CERTIFICADOS", "Certificados"),
    ("OUTROS", "Outros"),
)

class Profile(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_projetos')
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizações = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo