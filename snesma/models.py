from django.db import models

hari = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
)

jam = (
    ('1','1'),
    ('2','2'),
)

# Create your models here.
class Guru(models.Model):
    kode = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    jenis = models.ImageField()

class Jadawl12(models.Model):
    hari = models.IntegerField(choices=hari)
    ruang = models.IntegerField()
    mapel = models.CharField(max_length=100,null=True)
    jam_ke = models.CharField(max_length=100, choices=jam)
    kode_guru = models.CharField(max_length=10,null=True)