#!/usr/bin/env python

"""
    Script to import data from .csv file to Model Database DJango
    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('import_csv.py').read())
"""

import csv
from appmasgestion.models import Clientes

CSV_PATH = 'REPORTE.csv'      # Csv file path  

def fechaDecode(fecha):
    try:
        if not fecha: return None
        monthDecode = {
            'ene': '01',
            'feb': '02',
            'mar': '03',
            'abr': '04',
            'may': '05',
            'jun': '06',
            'jul': '07',
            'ago': '08',
            'sep': '09',
            'oct': '10',
            'nov': '11',
            'dic': '12',
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Ago': '08',
            'Aug': '08',
            'Sept': '09',
            'Oct': '10',
            'Nov': '11',
            'Dic': '12',
            'Dec': '12'
        }
        fields = fecha.split('-')
        if len(fields[2]) > 2:
            yr = fields[2][-2:]
        else:
            yr = fields[2]
        year = '20' + yr
        month = monthDecode[fields[1]]
        day = fields[0]
        if len(day) < 2: day = '0' + day

        return year + '-' + month + '-' + day
    except:
        return None

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    i=0
    for row in spamreader:
        # try:
        if i>=2:
            fecha_contacto = fechaDecode(row[2])
            fecha_agendado = fechaDecode(row[14])
            fecha_venta = fechaDecode(row[15])

            if row[3] != '':
                cliente=Clientes.objects.create(cliente=row[0],comercial=row[3],origen=row[1],fecha_contacto=fecha_contacto,DNI=row[4],segmento=row[5],CP=row[7],fijo=row[9],movil=row[10],operador=row[11],estado=row[12],motivo_no_interesa=row[13], fecha_agendado=fecha_agendado, fecha_venta=fecha_venta, FMC_porta_FIJO=row[16],FMC_Fijo_Nuevo=row[17],POSPAGO_MO=row[18],POSPAGO_MB_DUO_MB=row[19],CROSS_Fijo_Portado=row[20],CROSS_Fijo_Nuevo=row[21],RENUEVO=row[22],RENUEVO_CON_SUBIDA=row[23],TV=row[24],SEGURO=row[25],ACCESORIOS=row[26],TERMINAL_LIBRE=row[27],CAMBIO_TECNOLOGIA=row[28],PREPAGO=row[29],SEGURO_FAMILIA=row[30],PEPENERGY=row[31],ENERGY_GO=row[32],SMART_HOME=row[33],MO_ADICIONAL=row[34],notas=row[35])
                print(cliente.cliente)
        else:
            i=i+1