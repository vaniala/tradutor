# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sinal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('configuracao_da_mao', models.CharField(max_length=5)),
                ('ponto_de_articulacao', models.CharField(max_length=5)),
                ('movimento', models.CharField(max_length=5)),
                ('orientacao_das_maos', models.CharField(max_length=5)),
                ('expressao_facil_corporal', models.CharField(max_length=5)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
