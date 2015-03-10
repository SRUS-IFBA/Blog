from django.db import models

# Create your models here.
class Categoria(models.Model):
    id= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False)
    categorias = models.Manager()

    def __unicode__(self):
        return '%s' % self.nome

class Post(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False)
    texto = models.TextField(blank=False)
    criado = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=100, blank=False)
    posts = models.Manager()
    categoria = models.ForeignKey(Categoria)

    def __unicode__(self):
        return '%s' % self.titulo

