from functools import partial
from django import forms
from appmasgestion.models import Clientes
from django.core.exceptions import ValidationError


class AnadirCliente(forms.ModelForm):
    cliente = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Nombre cliente', 'required':True}),
                               label='') #nombre y apellidos del cliente
    DNI = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'DNI'}), label='')
    comercial = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Comercial'}),
                                label='') #nombre y apellidos del comercial que atiende al cliente
    CP = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Código postal'}),
                         label='') #codigo postal
    REFERENCIADO = 'Cliente referenciado'
    CLIENTE_TIENDA = 'Cliente de tienda'
    CLIENTE_CARTERA = 'Cliente de cartera'
    ORIGENES = [
        (REFERENCIADO, 'Cliente referenciado'),
        (CLIENTE_TIENDA, 'Cliente de tienda'),
        (CLIENTE_CARTERA, 'Cliente de cartera'),
    ]

    DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    FechaContacto = partial(forms.DateInput, {'class': 'datepicker', 'id':'fechacontacto'})
    fecha_contacto = forms.DateField(required=False, widget=FechaContacto())
    fecha_venta = forms.DateField(required=False, widget=DateInput())
    fecha_agendado = forms.DateField(required=False, widget=DateInput())

    # clientetienda, referenciado, clientecartera
    origen = forms.ChoiceField(required=False, label='Origen cliente', choices=ORIGENES)

    PARTICULAR = 'Particular'
    AUTONOMO = 'Autónomo'
    EMPRESA = 'Empresa'

    SEGMENTOS = [
        (PARTICULAR, 'Particular'),
        (AUTONOMO, 'Autónomo'),
        (EMPRESA, 'Empresa')
    ]

    #particular, autónomo o empresa
    segmento = forms.ChoiceField(label='Segmento', choices=SEGMENTOS, required=False)


    movil = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Teléfono movil'}),
                            label='')
    fijo = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Teléfono fijo'}),
                           label='')

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

    operador = forms.ChoiceField(choices=OPERADORES, required=False, label="Operador")

    VENDIDO, OFERTADO, AGENDADO, NOINTERESA = 'Vendido', 'Ofertado', 'Agendado', 'No interesa'

    ESTADO = [
        (VENDIDO, 'Vendido'),
        (OFERTADO, 'Ofertado'),
        (AGENDADO, 'Agendado'),
        (NOINTERESA, 'No interesa')
    ]

    motivo_no_interesa= forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":4, "cols":20}))
    notas= forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":4, "cols":20}))

    estado = forms.ChoiceField(choices=ESTADO, required=False)

        # gestion de los palotes (tarifas)

    FMC_porta_FIJO = forms.IntegerField(min_value=0, required=False)
    FMC_Fijo_Nuevo  = forms.IntegerField(min_value=0, required=False)
    POSPAGO_MO = forms.IntegerField(min_value=0, required=False)
    POSPAGO_MB_DUO_MB = forms.IntegerField(min_value=0, required=False)
    CROSS_Fijo_Portado = forms.IntegerField(min_value=0, required=False)
    CROSS_Fijo_Nuevo = forms.IntegerField(min_value=0, required=False)
    RENUEVO = forms.IntegerField(min_value=0, required=False)
    RENUEVO_CON_SUBIDA = forms.IntegerField(min_value=0, required=False)
    TV = forms.IntegerField(min_value=0, required=False)
    SEGURO = forms.IntegerField(min_value=0, required=False)
    ACCESORIOS = forms.IntegerField(min_value=0, required=False)
    TERMINAL_LIBRE = forms.IntegerField(min_value=0, required=False)
    CAMBIO_TECNOLOGIA = forms.IntegerField(min_value=0, required=False)
    PREPAGO = forms.IntegerField(min_value=0, required=False)
    SEGURO_FAMILIA = forms.IntegerField(min_value=0, required=False)
    PEPENERGY = forms.IntegerField(min_value=0, required=False)
    ENERGY_GO = forms.IntegerField(min_value=0, required=False)
    SMART_HOME = forms.IntegerField(min_value=0, required=False)
    MO_ADICIONAL = forms.IntegerField(min_value=0, required=False)

    def clean_obligatorio(self):
        data = self.cleaned_data
        email = data["email")
        movil = data"movil"]
        fijo = data["fijo"]

        if email == '' and movil == '' and fijo == '':
            raise ValidationError(
                "Debes rellenar email, fijo o móvil"
            )
        return data
    class Meta:
        model = Clientes
        fields = ['cliente', 'DNI', 'comercial', 'CP', 'origen', 'fecha_contacto',
                'fecha_venta', 'fecha_agendado', 'segmento', 'movil', 'fijo', 'email',
                'operador', 'estado', 'motivo_no_interesa' ,'notas', 'FMC_porta_FIJO', 'FMC_Fijo_Nuevo', 'POSPAGO_MO', 'POSPAGO_MB_DUO_MB',
                'CROSS_Fijo_Portado','CROSS_Fijo_Nuevo','RENUEVO','RENUEVO_CON_SUBIDA',
                'TV','SEGURO','ACCESORIOS','TERMINAL_LIBRE','CAMBIO_TECNOLOGIA','PREPAGO',
                'SEGURO_FAMILIA','PEPENERGY','ENERGY_GO','SMART_HOME', 'MO_ADICIONAL'
                ]
    