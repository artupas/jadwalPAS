from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from snesma.models import Guru, Jadawl12, Jadawl3


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

    # guru = Guru.objects.filter(jenis=0).order_by('?')
    # for hari in range(1,7):
    #     print(hari)
    #     jadwal = Jadawl12.objects.filter(hari=hari).order_by('?')
    #     for data in jadwal:
    #         for x in guru:
    #             cek_jadwal = Jadawl12.objects.filter(kode_guru=x.kode,hari=hari).count()
    #             cek_jadwal2 = Jadawl12.objects.filter(kode_guru2=x.kode,hari=hari).count()
    #             total = cek_jadwal+cek_jadwal2
    #             if total >= 2:
    #                 continue
    #             else:
    #                 jadwal_get = Jadawl12.objects.get(kode_guru=x.kode,hari=hari)
    #                 if jadwal_get.jam_ke != data.jam_ke:
    #                     data.kode_guru2 = x.kode
    #                     data.save()

    # print(Jadawl12.objects.filter(kode_guru__isnull=False).count())
    # jml = 0
    # for data in guru:
    #     jadwal = Jadawl12.objects.filter(kode_guru=data.kode).count()
    #     if jadwal<1:
    #         jml=jml+1
    # print(jml)

    guru = Guru.objects.filter(jenis=0)
    list = []
    for data in guru:
        for hari in range(1,7):
            jadwal1 = Jadawl12.objects.filter(kode_guru=data.kode,hari=hari).count()
            jadwal1_1 = Jadawl12.objects.filter(kode_guru2=data.kode,hari=hari).count()
            jadwal3 = Jadawl3.objects.filter(kode_guru=data.kode,hari=hari).count()
            total = jadwal1+jadwal1_1+jadwal3

            if total > 3:
                print(hari, data.kode, total)


    return HttpResponse('ok')
