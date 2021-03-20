from django.db import models
from django.utils import timezone
# Aquí creamos las BBDD como si fueran básicamente clases

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=200, default=None, null=True) #nombre y apellidos del cliente
    comercial = models.CharField(max_length=200, default=None, null=True) #nombre y apellidos del comercial que atiende al cliente

    DNI = models.CharField(max_length=50, default=None, null=True)
    CP = models.CharField(max_length=250, default=None, null=True) #codigo postal

    email = models.EmailField(null=True, default=None, blank=True)

    # toggle button para el campo origen
    REFERENCIADO = 'Cliente referenciado'
    CLIENTE_TIENDA = 'Cliente de tienda'
    CLIENTE_CARTERA = 'Cliente de cartera'
    ORIGEN = [
        (REFERENCIADO, 'Cliente referenciado'),
        (CLIENTE_TIENDA, 'Cliente de tienda'),
        (CLIENTE_CARTERA, 'Cliente de cartera'),
    ]

    origen = models.CharField(
        max_length=50,
        choices=ORIGEN,
        default=REFERENCIADO,
    )

    # fecha_contacto = models.DateField(default=timezone.now)
    fecha_contacto = models.DateField(default=None, null=True, blank=True)
    fecha_venta = models.DateField(default=None, null=True, blank=True)
    fecha_agendado = models.DateField(default=None, null=True, blank=True)

    PARTICULAR = 'Particular'
    AUTONOMO = 'Autónomo'
    EMPRESA = 'Empresa'

    SEGMENTO = [
        (PARTICULAR, 'Particular'),
        (AUTONOMO, 'Autónomo'),
        (EMPRESA, 'Empresa')
    ]

    segmento = models.CharField(
        max_length=50,
        choices=SEGMENTO,
        default=None,
        null=True,
    )

    movil = models.CharField(max_length=50, default=None, null=True) #
    fijo = models.CharField(max_length=50, default=None, blank=True, null=True) #

    YOIGO, MOVISTAR, VODAFONE, ORANGE, DIGI, LOWI, JAZZTEL, GRUPOMM, OTROS = 'Yoigo', 'Movistar', 'Vodafone', 'Orange', 'Digi', 'Lowi', 'Jazztel', 'Grupo MasMovil', 'Otros'

    OPERADORES = [
        (YOIGO, 'Yoigo'),
        (MOVISTAR, 'Movistar'),
        (VODAFONE, 'Vodafone'),
        (ORANGE, 'Orange'),
        (DIGI, 'Digi'),
        (LOWI, 'Lowi'),
        (JAZZTEL, 'Jazztel'),
        (GRUPOMM, 'Grupo MasMovil'),
        (OTROS, 'Otros'),
    ]
    operador = models.CharField(max_length=40, choices=OPERADORES, default=None, null=True)

    VENDIDO, OFERTADO, AGENDADO, NOINTERESA = 'Vendido', 'Ofertado', 'Agendado', 'No interesa'
    LLAMADO, NOCONTESTA, NOEXISTE = 'Llamado', 'No contesta', 'No existe'

    ESTADO = [
        (LLAMADO, 'Llamado'),
        (OFERTADO, 'Ofertado'),
        (AGENDADO, 'Agendado'),
        (NOCONTESTA, 'No contesta'),
        (NOINTERESA, 'No interesa'),
        (VENDIDO, 'Vendido'),
        (NOEXISTE, 'No existe'),
    ]

    #vendido, ofertado, agendado, no interesa
    estado = models.CharField(
        max_length=20,
        choices=ESTADO,
        default=None,
        null=True,
    )
    motivo_no_interesa = models.CharField(max_length=1000, null=True, default=None, blank=True)

    notas = models.CharField(max_length=1100, default=None, null=True, blank=True)

    # gestion de los palotes (tarifas)

    FMC_porta_FIJO = models.IntegerField(default=None, null=True)
    FMC_Fijo_Nuevo  = models.IntegerField(default=None, null=True)
    POSPAGO_MO = models.IntegerField(default=None, null=True)
    POSPAGO_MB_DUO_MB = models.IntegerField(default=None, null=True)
    CROSS_Fijo_Portado = models.IntegerField(default=None, null=True)
    CROSS_Fijo_Nuevo = models.IntegerField(default=None, null=True)
    RENUEVO = models.IntegerField(default=None, null=True)
    RENUEVO_CON_SUBIDA = models.IntegerField(default=None, null=True)
    TV = models.IntegerField(default=None, null=True)
    SEGURO = models.IntegerField(default=None, null=True)
    ACCESORIOS = models.IntegerField(default=None, null=True)
    TERMINAL_LIBRE = models.IntegerField(default=None, null=True)
    CAMBIO_TECNOLOGIA = models.IntegerField(default=None, null=True)
    PREPAGO = models.IntegerField(default=None, null=True)
    SEGURO_FAMILIA = models.IntegerField(default=None, null=True)
    PEPENERGY = models.IntegerField(default=None, null=True)
    ENERGY_GO = models.IntegerField(default=None, null=True)
    SMART_HOME = models.IntegerField(default=None, null=True)
    MO_ADICIONAL = models.IntegerField(default=None, null=True)

# Buscador completo AND, faltan valores en desplegables.

# Importar base de datos completa

# Fecha edicion de registro

# Tildes buscador

# Mensajes éxito y error

# Busqueda letra a letra

# Agendado para hoy
