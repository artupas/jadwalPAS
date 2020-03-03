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

    guru = Guru.objects.filter(jenis=0).order_by('?')
    for hari in range(1,7):
        print(hari)
        jadwal = Jadawl12.objects.filter(hari=hari).order_by('?')
        for data in jadwal:
            for x in guru:
                cek_jadwal = jadwal.filter(kode_guru=x.kode).count()
                if cek_jadwal > 1:
                    continue
                else:
                    data.kode_guru = x.kode
                    data.save()
    # print(Jadawl12.objects.filter(kode_guru__isnull=False).count())
    # jml = 0
    # for data in guru:
    #     jadwal = Jadawl12.objects.filter(kode_guru=data.kode).count()
    #     if jadwal>0:
    #         jml=jml+1
    # print(jml)
    return HttpResponse('ok')
