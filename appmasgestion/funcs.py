import csv
from django.http import HttpResponse
from appmasgestion.models import Clientes

def descargar_csv(resultado):
    # boton de descargar csv
    output = []
    response = HttpResponse (content_type='text/csv')
    writer = csv.writer(response)

    writer.writerow(['Nombre', 'OrigenBDD', 'Fecha Contacto', 'Comercial', 'DNI', 'Segmento', 'CP', 'Num Fijo', 'Num Movil', 'Operador', 'Estado', 'Motivo No Interesa', 'Fecha Agendado', 'Fecha venta', 'FMC_porta_FIJO', 'FMC_Fijo_Nuevo', 'POSPAGO_MO', 'POSPAGO_MB_DUO_MB', 'CROSS_Fijo_Portado', 'CROSS_Fijo_Nuevo', 'RENUEVO', 'RENUEVO_CON_SUBIDA', 'TV', 'SEGURO', 'ACCESORIOS', 'TERMINAL_LIBRE', 'CAMBIO_TECNOLOGIA', 'PREPAGO', 'SEGURO_FAMILIA', 'PEPENERGY', 'ENERGY_GO', 'SMART_HOME', 'MO_ADICIONAL'])

    for cliente in resultado:
        output.append([cliente.cliente,cliente.origen,cliente.fecha_contacto,cliente.comercial,cliente.DNI,cliente.segmento,cliente.CP,cliente.fijo,cliente.movil,cliente.motivo_no_interesa,cliente.fecha_agendado,cliente.fecha_venta,cliente.FMC_porta_FIJO,cliente.FMC_Fijo_Nuevo,cliente.POSPAGO_MO,cliente.POSPAGO_MB_DUO_MB,cliente.CROSS_Fijo_Portado,cliente.CROSS_Fijo_Nuevo,cliente.RENUEVO,cliente.RENUEVO_CON_SUBIDA,cliente.TV,cliente.SEGURO,cliente.ACCESORIOS,cliente.TERMINAL_LIBRE,cliente.CAMBIO_TECNOLOGIA,cliente.PREPAGO,cliente.SEGURO_FAMILIA,cliente.PEPENERGY,cliente.ENERGY_GO,cliente.SMART_HOME,cliente.MO_ADICIONAL,])
    #CSV Data
    writer.writerows(output)
    return response

def estadisticas_comercial(nombre_comercial='', fecha_inicio='', fecha_final=''):
    args = {}

    if nombre_comercial != '':
        args['comercial'] = nombre_comercial

    if fecha_inicio != '':
        args['fecha_contacto__gte'] = fecha_inicio

    if fecha_final != '':
        args['fecha_contacto__lte'] = fecha_final

    clientes_atendidos = Clientes.objects.filter(**args)

    agendado = 0
    llamado = 0
    no_contesta = 0
    no_existe = 0
    no_interesado = 0
    ofertado = 0
    vendido = 0
    total_general = 0
    total_ventas_valor = 0

    for cliente in clientes_atendidos:
        if cliente.estado == 'AGENDADO':
            agendado +=1
        elif cliente.estado == 'LLAMADO':
            llamado +=1
        elif cliente.estado == 'NO CONTESTA':
            no_contesta += 1
        elif cliente.estado == 'NO EXISTE':
            no_existe += 1
        elif cliente.estado == 'NO INTERESADO':
            no_interesado += 1
        elif cliente.estado == 'OFERTADO':
            ofertado += 1
        elif cliente.estado == 'VENDIDO':
            vendido += 1

        if not cliente.FMC_porta_FIJO is None and cliente.FMC_porta_FIJO > 0:
            total_ventas_valor += cliente.FMC_porta_FIJO
        if not cliente.FMC_Fijo_Nuevo is None and cliente.FMC_Fijo_Nuevo > 0:
            total_ventas_valor += cliente.FMC_Fijo_Nuevo
        if not cliente.POSPAGO_MO is None and cliente.POSPAGO_MO > 0:
            total_ventas_valor += cliente.POSPAGO_MO
        if not cliente.POSPAGO_MB_DUO_MB is None and cliente.POSPAGO_MB_DUO_MB > 0:
            total_ventas_valor += cliente.POSPAGO_MB_DUO_MB
        if not cliente.CROSS_Fijo_Portado is None and cliente.CROSS_Fijo_Portado > 0:
            total_ventas_valor += cliente.CROSS_Fijo_Portado
        if not cliente.CROSS_Fijo_Nuevo is None and cliente.CROSS_Fijo_Nuevo > 0:
            total_ventas_valor += cliente.CROSS_Fijo_Nuevo

    total_general=agendado+llamado+no_contesta+no_existe+no_interesado+ofertado+vendido

    contador = {
        'comercial':nombre_comercial,
        'agendado':agendado,
        'llamado':llamado,
        'no_contesta':no_contesta,
        'no_existe':no_existe,
        'no_interesado':no_interesado,
        'ofertado':ofertado,
        'vendido':vendido,
        'total_general':total_general,
        'total_ventas_valor':total_ventas_valor,
        'total_ventas':vendido,
    }

    return contador
