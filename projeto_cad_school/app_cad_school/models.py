from django.db import models

# Create your models here.

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    senha = models.IntegerField()


class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)

class Notas(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia , on_delete=models.CASCADE)
    media = models.FloatField()
    
    def __str__(self):
        return (f"{self.aluno} {self.materia} , {self.media}")