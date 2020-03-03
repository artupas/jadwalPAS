from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from snesma.models import Guru, Jadawl12


def GenerateJadwa(request):
    # for x in range(1,23):
    #     print(x)
    #     for y in range(1,7):
    #         for z in range(1,3):
    #             Jadawl12.objects.create(
    #                 hari=y,
    #                 ruang=x,
    #                 jam_ke=z,
    #             )
    jadwal = Jadawl12.objects.all()
    guru = Guru.objects.filter(jenis=0)
    for data in jadwal:
        for x in guru:
            cek_jatah = Jadawl12.objects.filter(kode_guru=x.kode).count()
            if cek_jatah != 3 and cek_jatah != 0:
                jadwal_eksis = Jadawl12.objects.filter(kode_guru=x.kode)



    return HttpResponse('ok')
