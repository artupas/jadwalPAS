# Generated by Django 3.0.3 on 2020-03-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snesma', '0004_auto_20200302_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jadawl3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('ruang', models.IntegerField()),
                ('mapel', models.CharField(max_length=100, null=True)),
                ('jam_ke', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=100)),
                ('kode_guru', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]