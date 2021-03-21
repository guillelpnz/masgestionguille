import csv
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
from appmasgestion.forms import AnadirCliente
from appmasgestion.models import Clientes
from appmasgestion.funcs import estadisticas_comercial

# Create your views here.
# consulta OR: User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace

# DIC_MESES = {
# 	'enero':1,
#     'febrero':2,
#     'marzo':3,
#     'abril':4,
#     'mayo':5,
#     'junio':6,
#     'julio':7,
#     'agosto':8,
#     'septiembre':9,
#     'octubre':10,
#     'noviembre':11,
#     'diciembre':12,
# }

def index(request):
    descargarcsv = request.POST.get("descargar-csv", "")
    context={}

    if not request.method == 'POST':
        if 'paginate_post' in request.session:
            request.POST = request.session['paginate_post']
            request.method = 'POST'
    
    if request.method == "POST":
        request.session['paginate_post'] = request.POST
        busqueda = request.POST.get("input-busqueda", "")
        if busqueda != '':
            busqueda=busqueda.upper()
            clientes = Clientes.objects.filter(cliente__icontains=busqueda) | Clientes.objects.filter(DNI__icontains=busqueda) | Clientes.objects.filter(estado__icontains=busqueda) | Clientes.objects.filter(comercial__icontains=busqueda) | Clientes.objects.filter(operador__icontains=busqueda) | Clientes.objects.filter(movil__icontains=busqueda) | Clientes.objects.filter(fijo__icontains=busqueda) | Clientes.objects.filter(CP__icontains=busqueda) | Clientes.objects.filter(origen__icontains=busqueda) | Clientes.objects.filter(segmento__icontains=busqueda)
    else:
        clientes = Clientes.objects.all()

    clientes = clientes.order_by('-fecha_agendado')

    paginator = Paginator(clientes, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if descargarcsv != '':
        output = []
        response = HttpResponse (content_type='text/csv')
        writer = csv.writer(response)

        writer.writerow(['Nombre', 'OrigenBDD', 'Fecha Contacto', 'Comercial', 'DNI', 'Segmento', 'CP', 'Num Fijo', 'Num Movil', 'Operador', 'Estado', 'Motivo No Interesa', 'Fecha Agendado', 'Fecha venta', 'FMC_porta_FIJO', 'FMC_Fijo_Nuevo', 'POSPAGO_MO', 'POSPAGO_MB_DUO_MB', 'CROSS_Fijo_Portado', 'CROSS_Fijo_Nuevo', 'RENUEVO', 'RENUEVO_CON_SUBIDA', 'TV', 'SEGURO', 'ACCESORIOS', 'TERMINAL_LIBRE', 'CAMBIO_TECNOLOGIA', 'PREPAGO', 'SEGURO_FAMILIA', 'PEPENERGY', 'ENERGY_GO', 'SMART_HOME', 'MO_ADICIONAL'])

        for cliente in clientes:
            output.append([cliente.cliente,cliente.origen,cliente.fecha_contacto,cliente.comercial,cliente.DNI,cliente.segmento,cliente.CP,cliente.fijo,cliente.movil,cliente.motivo_no_interesa,cliente.fecha_agendado,cliente.fecha_venta,cliente.FMC_porta_FIJO,cliente.FMC_Fijo_Nuevo,cliente.POSPAGO_MO,cliente.POSPAGO_MB_DUO_MB,cliente.CROSS_Fijo_Portado,cliente.CROSS_Fijo_Nuevo,cliente.RENUEVO,cliente.RENUEVO_CON_SUBIDA,cliente.TV,cliente.SEGURO,cliente.ACCESORIOS,cliente.TERMINAL_LIBRE,cliente.CAMBIO_TECNOLOGIA,cliente.PREPAGO,cliente.SEGURO_FAMILIA,cliente.PEPENERGY,cliente.ENERGY_GO,cliente.SMART_HOME,cliente.MO_ADICIONAL,])
        #CSV Data
        writer.writerows(output)
        return response

    context['clientes'] = page_obj
    return render(request, 'index.html', context)

def anadir_cliente(request):
    form = AnadirCliente()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = AnadirCliente(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        else:
            render(request, 'index.html')

    return render(request, 'anadir_cliente.html', {'form': form})

def ver_cliente(request):
    context={}

    if request.method == 'POST':
        context['dni_cli'] = request.POST.get("hidden-dni", "")

    cliente = Clientes.objects.filter(id=request.POST.get("hidden-dni", ""))
    context['ver_cliente'] = cliente

    return render(request, 'ver_cliente.html', context)

def editar_cliente(request):
    context = {}
    if request.method == 'POST':
        if 'hidden-dni' in request.POST:
            cliente = Clientes.objects.get(id=request.POST.get("hidden-dni", ""))

            form = AnadirCliente(instance=cliente)

            print("holaaaaaaaaaaaaaaaaaaa")
            context['rehidden'] = cliente.id
        elif 'rehidden' in request.POST:
            cliente = Clientes.objects.get(id=request.POST.get("rehidden", ""))
            form = AnadirCliente(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            # print("holaaaaaaaa")

    context['form'] = form
    return render(request, 'editar_cliente.html', context)

def buscador_clientes(request):
    context = {}
    # form = BuscarClientes

    if not request.method == 'POST':
        if 'paginate_post_busq' in request.session:
            request.POST = request.session['paginate_post_busq']
            request.method = 'POST'

    if request.method=='POST':
        request.session['paginate_post_busq'] = request.POST
        filtro = request.POST.get("filtro", "")
        busqueda = request.POST.get("input-busqueda", "")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_final = request.POST.get("fecha_final")
        tarifas = request.POST.get("tarifas")

        consulta1=consulta2=consulta3=consulta4=consulta5=consulta6=consulta7=consulta8=consulta9=consulta10=consulta11=consulta12=consulta13=consulta14=consulta15=consulta16=consulta17=consulta18=consulta19=consulta20=consulta21=consulta22=Q()

        if busqueda != '':
            if filtro != '':
                if filtro == "DNI":
                    consulta1 = Q(DNI__icontains=busqueda)
                elif filtro == "cliente":
                    consulta1 = Q(cliente__icontains=busqueda)
                elif filtro == "CP" :
                    consulta1 = Q(CP__icontains=busqueda)
                elif filtro == "comercial" :
                    consulta1 = Q(comercial__icontains=busqueda)
                elif filtro == "origen" :
                    consulta1 = Q(origen__icontains=busqueda)
                elif filtro == "segmento" :
                    consulta1 = Q(segmento__icontains=busqueda)
                elif filtro == "movil" :
                    consulta1 = Q(movil__icontains=busqueda)
                elif filtro == "fijo" :
                    consulta1 = Q(fijo__icontains=busqueda)
                elif filtro == "operador" :
                    consulta1 = Q(operador__icontains=busqueda)
                elif filtro == "estado":
                    consulta1 = Q(estado__icontains=busqueda)
        
        if tarifas != '':
            if "FMC_porta_FIJO" in tarifas:
                consulta2 = Q(FMC_porta_FIJO__gt=0)
            if "FMC_Fijo_Nuevo" in tarifas:
                consulta3 = Q(FMC_Fijo_Nuevo__gt=0)
            if "POSPAGO_MO" in tarifas:
                consulta4 = Q(POSPAGO_MO__gt=0)
            if "POSPAGO_MB_DUO_MB" in tarifas:
                consulta5 = Q(POSPAGO_MB_DUO_MB__gt=0)
            if "CROSS_Fijo_Portado" in tarifas:
                consulta6 = Q(CROSS_Fijo_Portado__gt=0)
            if "CROSS_Fijo_Nuevo" in tarifas:
                consulta7 = Q(CROSS_Fijo_Nuevo__gt=0)
            if "RENUEVO" in tarifas:
                consulta8 = Q(RENUEVO__gt=0)
            if "RENUEVO_CON_SUBIDA" in tarifas:
                consulta9 = Q(RENUEVO_CON_SUBIDA__gt=0)
            if "TV" in tarifas:
                consulta10 = Q(TV__gt=0)
            if "SEGURO" in tarifas:
                consulta11 = Q(SEGURO__gt=0)
            if "ACCESORIOS" in tarifas:
                consulta12 = Q(ACCESORIOS__gt=0)
            if "TERMINAL_LIBRE" in tarifas:
                consulta13 = Q(TERMINAL_LIBRE__gt=0)
            if "CAMBIO_TECNOLOGIA" in tarifas:
                consulta14 = Q(CAMBIO_TECNOLOGIA__gt=0)
            if "PREPAGO" in tarifas:
                consulta15 = Q(PREPAGO__gt=0)
            if "SEGURO_FAMILIA" in tarifas:
                consulta16 = Q(SEGURO_FAMILIA__gt=0)
            if "PEPENERGY" in tarifas:
                consulta17 = Q(PEPENERGY__gt=0)
            if "ENERGY_GO" in tarifas:
                consulta18 = Q(ENERGY_GO__gt=0)
            if "SMART_HOME" in tarifas:
                consulta19 = Q(SMART_HOME__gt=0)
            if "MO_ADICIONAL" in tarifas:
                consulta20 = Q(MO_ADICIONAL__gt=0)


        if fecha_inicio != "":
            consulta21=Q(fecha_contacto__gte=fecha_inicio) | Q(fecha_agendado__gte=fecha_inicio)

        if fecha_final != "" :
            consulta22=Q(fecha_contacto__lte=fecha_final) | Q(fecha_agendado__lte=fecha_final)

        resultado=Clientes.objects.filter(consulta1&consulta2&consulta3&consulta4&consulta5&consulta6&consulta7&consulta8&consulta9&consulta10&consulta11&consulta12&consulta13&consulta14&consulta15&consulta16&consulta17&consulta18&consulta19&consulta20&consulta21&consulta22)
    else:
        resultado=Clientes.objects.all()

    paginator = Paginator(resultado, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {"titulo" : "Resultados Encontrados", "clase" : "success", "clientes": page_obj, "search": "search"}
    return render(request,'buscador-clientes.html', context)

def gestion_comerciales(request):
    contador, contadores, context = {},{},{}
    # nombres de los comerciales
    context['comerciales'] = Clientes.objects.values_list('comercial', flat=True).distinct()

    if request.method == 'POST':
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_final = request.POST.get("fecha_final")
        nombre_comercial = request.POST.get("nombre_comercial")
    
        args_consulta = {}
        if fecha_inicio != '':
            args_consulta['fecha_inicio__gte'] = fecha_inicio
        if fecha_final != '':
            args_consulta['fecha_final__lte'] = fecha_final
        
        #no entrar en un bucle y mostrar solo 1
        if nombre_comercial != '':
            args_consulta['comercial__contains'] = nombre_comercial
            contadores['nombre_comercial'] = estadisticas_comercial(nombre_comercial, fecha_inicio, fecha_final)
        else:
            for val in context['comerciales']:
                contador = estadisticas_comercial(val, fecha_inicio, fecha_final)

                contadores[val] = contador
    
        context = {'contadores':contadores, 'fecha_inicio':fecha_inicio, 'fecha_final':fecha_final, 'nombre_comercial':nombre_comercial}

    return render(request, 'gestion_comerciales.html', context)

def descargar_csv_comerciales(request):
    context = {}
    # nombres de los comerciales
    output = []
    response = HttpResponse (content_type='text/csv')
    writer = csv.writer(response)
    context['comerciales'] = Clientes.objects.values_list('comercial', flat=True).distinct()

    fecha_inicio = request.POST.get("fecha_inicio")
    fecha_final = request.POST.get("fecha_final")
    nombre_comercial = request.POST.get("nombre_comercial")

    args_consulta = {}
    if fecha_inicio != '':
        args_consulta['fecha_inicio__gte'] = fecha_inicio
    if fecha_final != '':
        args_consulta['fecha_final__lte'] = fecha_final
    
    #no entrar en un bucle y mostrar solo 1
    if nombre_comercial != '':
        args_consulta['comercial__contains'] = nombre_comercial
        fila = estadisticas_comercial(nombre_comercial, fecha_inicio, fecha_final)
        output.append([fila['comercial'],fila['agendado'],fila['llamado'],fila['no_contesta'],fila['no_existe'],fila['no_interesado'],fila['ofertado'],fila['vendido'],fila['total_general'],fila['total_ventas_valor'],fila['vendido'],])
    else:
        for val in context['comerciales']:
            fila = estadisticas_comercial(val, fecha_inicio, fecha_final)
            output.append([fila['comercial'],fila['agendado'],fila['llamado'],fila['no_contesta'],fila['no_existe'],fila['no_interesado'],fila['ofertado'],fila['vendido'],fila['total_general'],fila['total_ventas_valor'],fila['vendido'],])

    # boton de descargar csv

    writer.writerow(['val','agendado','llamado','no_contesta','no_existe','no_interesado','ofertado','vendido','total_general','total_ventas_valor','total_ventas',])

    #CSV Data
    writer.writerows(output)
    
    return response


