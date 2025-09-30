"""
Data models for NubeFact API integration.
"""

from typing import List, Optional, Literal
from datetime import date
from pydantic import BaseModel, Field


class Item(BaseModel):
    """Model for invoice/receipt items."""
    
    unidad_de_medida: str = Field(..., description="Measurement unit (NIU=product, ZZ=service)")
    codigo: Optional[str] = Field(None, max_length=250, description="Internal product/service code")
    descripcion: str = Field(..., max_length=250, description="Product/service description")
    cantidad: float = Field(..., description="Quantity")
    valor_unitario: float = Field(..., description="Unit value without IGV")
    precio_unitario: float = Field(..., description="Unit price with IGV")
    descuento: Optional[float] = Field(None, description="Line discount")
    subtotal: float = Field(..., description="Subtotal (valor_unitario * cantidad - descuento)")
    tipo_de_igv: Optional[int] = Field(None, description="IGV type (1=Gravado, 8=Exonerado, 9=Inafecto, etc.)")
    tipo_de_ivap: Optional[str] = Field(None, description="IVAP type (alternative to IGV type)")
    igv: float = Field(..., description="IGV amount for the line")
    total: float = Field(..., description="Line total")
    anticipo_regularizacion: bool = Field(False, description="Advance regularization")
    anticipo_documento_serie: Optional[str] = Field(None, max_length=4, description="Advance document series")
    anticipo_documento_numero: Optional[int] = Field(None, ge=1, le=99999999, description="Advance document number")
    codigo_producto_sunat: Optional[str] = Field(None, max_length=8, description="SUNAT product code")
    tipo_de_isc: Optional[float] = Field(None, description="ISC type")
    isc: Optional[float] = Field(None, description="ISC amount")
    impuesto_bolsas: Optional[float] = Field(None, description="Plastic bag tax")


class Guia(BaseModel):
    """Model for related shipping guides."""
    
    guia_tipo: int = Field(..., description="Guide type (1=Remitente, 2=Transportista)")
    guia_serie_numero: str = Field(..., max_length=30, description="Guide series and number")


class VentaCredito(BaseModel):
    """Model for credit sale installments."""
    
    cuota: int = Field(..., ge=1, le=999, description="Installment number")
    fecha_de_pago: str = Field(..., description="Payment date (DD-MM-YYYY)")
    importe: float = Field(..., description="Installment amount")


class ComprobanteBase(BaseModel):
    """Base model for invoice/receipt operations."""
    
    operacion: str = Field(..., description="Operation type")
    tipo_de_comprobante: int = Field(..., description="Document type (1=Factura, 2=Boleta, 3=Nota Crédito, 4=Nota Débito)")
    serie: str = Field(..., max_length=4, description="Document series")
    numero: int = Field(..., ge=1, le=99999999, description="Document number")


class ComprobanteGenerar(ComprobanteBase):
    """Model for generating invoices/receipts."""
    
    operacion: Literal["generar_comprobante"] = "generar_comprobante"
    sunat_transaction: int = Field(..., description="SUNAT transaction type (1=Venta Interna, 2=Exportación, etc.)")
    cliente_tipo_de_documento: int = Field(..., description="Client document type (6=RUC, 1=DNI, etc.)")
    cliente_numero_de_documento: str = Field(..., max_length=15, description="Client document number")
    cliente_denominacion: str = Field(..., max_length=100, description="Client name/company")
    cliente_direccion: str = Field(..., max_length=100, description="Client address")
    cliente_email: Optional[str] = Field(None, max_length=250, description="Client email")
    cliente_email_1: Optional[str] = Field(None, max_length=250, description="Client email 2")
    cliente_email_2: Optional[str] = Field(None, max_length=250, description="Client email 3")
    fecha_de_emision: str = Field(..., description="Emission date (DD-MM-YYYY)")
    fecha_de_vencimiento: Optional[str] = Field(None, description="Due date (DD-MM-YYYY)")
    moneda: int = Field(..., description="Currency (1=Soles, 2=Dólares, 3=Euros)")
    tipo_de_cambio: Optional[float] = Field(None, description="Exchange rate")
    porcentaje_de_igv: float = Field(..., description="IGV percentage")
    descuento_global: Optional[float] = Field(None, description="Global discount")
    total_descuento: Optional[float] = Field(None, description="Total discount")
    total_anticipo: Optional[float] = Field(None, description="Total advance")
    total_gravada: Optional[float] = Field(None, description="Total taxable")
    total_inafecta: Optional[float] = Field(None, description="Total non-taxable")
    total_exonerada: Optional[float] = Field(None, description="Total exempt")
    total_igv: Optional[float] = Field(None, description="Total IGV")
    total_gratuita: Optional[float] = Field(None, description="Total free")
    total_otros_cargos: Optional[float] = Field(None, description="Total other charges")
    total_isc: Optional[float] = Field(None, description="Total ISC amount")
    total: float = Field(..., description="Total amount")
    percepcion_tipo: Optional[int] = Field(None, description="Perception type")
    percepcion_base_imponible: Optional[float] = Field(None, description="Perception taxable base")
    total_percepcion: Optional[float] = Field(None, description="Total perception")
    total_incluido_percepcion: Optional[float] = Field(None, description="Total including perception")
    retencion_tipo: Optional[int] = Field(None, description="Retention type")
    retencion_base_imponible: Optional[float] = Field(None, description="Retention taxable base")
    total_retencion: Optional[float] = Field(None, description="Total retention")
    total_impuestos_bolsas: Optional[float] = Field(None, description="Total plastic bag taxes")
    detraccion: bool = Field(False, description="Withholding flag")
    detraccion_tipo: Optional[int] = Field(None, description="Withholding type (1=Azúcar, 2=Arroz, etc.)")
    detraccion_total: Optional[float] = Field(None, description="Total withholding amount")
    detraccion_porcentaje: Optional[float] = Field(None, description="Withholding percentage")
    medio_de_pago_detraccion: Optional[int] = Field(None, description="Withholding payment method (1=Depósito, 2=Giro, etc.)")
    ubigeo_origen: Optional[int] = Field(None, description="Origin UBIGEO code")
    direccion_origen: Optional[str] = Field(None, max_length=100, description="Origin address")
    ubigeo_destino: Optional[int] = Field(None, description="Destination UBIGEO code")
    direccion_destino: Optional[str] = Field(None, max_length=100, description="Destination address")
    detalle_viaje: Optional[str] = Field(None, max_length=100, description="Trip details")
    val_ref_serv_trans: Optional[float] = Field(None, description="Reference value for transport service")
    val_ref_carga_efec: Optional[float] = Field(None, description="Reference value for effective load")
    val_ref_carga_util: Optional[float] = Field(None, description="Reference value for useful load")
    punto_origen_viaje: Optional[int] = Field(None, description="Trip origin point UBIGEO")
    punto_destino_viaje: Optional[int] = Field(None, description="Trip destination point UBIGEO")
    descripcion_tramo: Optional[str] = Field(None, max_length=100, description="Route segment description")
    val_ref_carga_efec_tramo_virtual: Optional[float] = Field(None, description="Reference value for virtual segment effective load")
    configuracion_vehicular: Optional[str] = Field(None, max_length=15, description="Vehicle configuration")
    carga_util_tonel_metricas: Optional[float] = Field(None, description="Useful load in metric tons")
    carga_efec_tonel_metricas: Optional[float] = Field(None, description="Effective load in metric tons")
    val_ref_tonel_metrica: Optional[float] = Field(None, description="Reference value per metric ton")
    val_pre_ref_carga_util_nominal: Optional[float] = Field(None, description="Preliminary reference value for nominal useful load")
    indicador_aplicacion_retorno_vacio: Optional[bool] = Field(None, description="Empty return application indicator")
    matricula_emb_pesquera: Optional[str] = Field(None, max_length=15, description="Fishing vessel registration")
    nombre_emb_pesquera: Optional[str] = Field(None, max_length=50, description="Fishing vessel name")
    descripcion_tipo_especie_vendida: Optional[str] = Field(None, max_length=100, description="Description of sold species type")
    lugar_de_descarga: Optional[str] = Field(None, max_length=200, description="Unloading location")
    cantidad_especie_vendida: Optional[float] = Field(None, description="Quantity of sold species")
    fecha_de_descarga: Optional[str] = Field(None, description="Unloading date (YYYY-MM-DD)")
    observaciones: Optional[str] = Field(None, max_length=1000, description="Observations")
    documento_que_se_modifica_tipo: Optional[int] = Field(None, description="Modified document type")
    documento_que_se_modifica_serie: Optional[str] = Field(None, max_length=4, description="Modified document series")
    documento_que_se_modifica_numero: Optional[int] = Field(None, ge=1, le=99999999, description="Modified document number")
    tipo_de_nota_de_credito: Optional[int] = Field(None, description="Credit note type")
    tipo_de_nota_de_debito: Optional[int] = Field(None, description="Debit note type")
    enviar_automaticamente_a_la_sunat: bool = Field(True, description="Auto-send to SUNAT")
    enviar_automaticamente_al_cliente: bool = Field(False, description="Auto-send to client")
    codigo_unico: Optional[str] = Field(None, max_length=20, description="Unique code")
    condiciones_de_pago: Optional[str] = Field(None, max_length=250, description="Payment conditions")
    medio_de_pago: Optional[str] = Field(None, max_length=250, description="Payment method")
    placa_vehiculo: Optional[str] = Field(None, max_length=8, description="Vehicle plate")
    orden_compra_servicio: Optional[str] = Field(None, max_length=20, description="Purchase/service order")
    formato_de_pdf: Optional[str] = Field(None, description="PDF format (A4, A5, TICKET)")
    generado_por_contingencia: Optional[bool] = Field(None, description="Contingency generated")
    bienes_region_selva: Optional[bool] = Field(None, description="Goods from jungle region")
    servicios_region_selva: Optional[bool] = Field(None, description="Services from jungle region")
    nubecont_tipo_de_venta_codigo: Optional[str] = Field(None, max_length=5, description="NubeCont sale type code")
    items: List[Item] = Field(..., description="Document items")
    guias: Optional[List[Guia]] = Field(None, description="Related guides")
    venta_al_credito: Optional[List[VentaCredito]] = Field(None, description="Credit sale installments")


class ComprobanteConsultar(ComprobanteBase):
    """Model for querying invoices/receipts."""
    
    operacion: Literal["consultar_comprobante"] = "consultar_comprobante"


class AnulacionGenerar(BaseModel):
    """Model for generating cancellations."""
    
    operacion: Literal["generar_anulacion"] = "generar_anulacion"
    tipo_de_comprobante: int = Field(..., description="Document type to cancel")
    serie: str = Field(..., max_length=4, description="Document series to cancel")
    numero: int = Field(..., ge=1, le=99999999, description="Document number to cancel")
    motivo: str = Field(..., max_length=100, description="Cancellation reason")
    codigo_unico: Optional[str] = Field(None, max_length=250, description="Unique code")


class AnulacionConsultar(BaseModel):
    """Model for querying cancellations."""
    
    operacion: Literal["consultar_anulacion"] = "consultar_anulacion"
    tipo_de_comprobante: int = Field(..., description="Document type")
    serie: str = Field(..., max_length=4, description="Document series")
    numero: int = Field(..., ge=1, le=99999999, description="Document number")


class ComprobanteRespuesta(BaseModel):
    """Model for invoice/receipt response."""
    
    tipo_de_comprobante: Optional[int] = None
    serie: Optional[str] = None
    numero: Optional[int] = None
    enlace: Optional[str] = None
    enlace_del_pdf: Optional[str] = None
    enlace_del_xml: Optional[str] = None
    enlace_del_cdr: Optional[str] = None
    aceptada_por_sunat: Optional[bool] = None
    sunat_description: Optional[str] = None
    sunat_note: Optional[str] = None
    sunat_responsecode: Optional[str] = None
    sunat_soap_error: Optional[str] = None
    cadena_para_codigo_qr: Optional[str] = None
    codigo_hash: Optional[str] = None
    codigo_de_barras: Optional[str] = None
    pdf_zip_base64: Optional[str] = None
    xml_zip_base64: Optional[str] = None
    cdr_zip_base64: Optional[str] = None
    anulado: Optional[bool] = None


class AnulacionRespuesta(BaseModel):
    """Model for cancellation response."""
    
    numero: Optional[int] = None
    enlace: Optional[str] = None
    sunat_ticket_numero: Optional[str] = None
    aceptada_por_sunat: Optional[bool] = None
    sunat_description: Optional[str] = None
    sunat_note: Optional[str] = None
    sunat_responsecode: Optional[str] = None
    sunat_soap_error: Optional[str] = None
    enlace_del_pdf: Optional[str] = None
    enlace_del_xml: Optional[str] = None
    enlace_del_cdr: Optional[str] = None
    pdf_zip_base64: Optional[str] = None
    xml_zip_base64: Optional[str] = None
    cdr_zip_base64: Optional[str] = None


class ErrorRespuesta(BaseModel):
    """Model for error response."""
    
    errors: Optional[str] = None
    codigo: Optional[int] = None


# Guía de Remisión Models

class GuiaItem(BaseModel):
    """Model for Guía de Remisión items."""
    
    unidad_de_medida: str = Field(..., description="Measurement unit (NIU=product, etc.)")
    codigo: Optional[str] = Field(None, max_length=250, description="Internal product code")
    descripcion: str = Field(..., max_length=250, description="Product description")
    cantidad: float = Field(..., description="Quantity")
    codigo_dam: Optional[str] = Field(None, max_length=23, description="DAM/DS code for import/export")


class DocumentoRelacionado(BaseModel):
    """Model for related documents in Guía de Remisión."""
    
    tipo: int = Field(..., description="Document type (01=Factura, 03=Boleta, 09=Guía Remitente, 31=Guía Transportista)")
    serie: str = Field(..., max_length=4, description="Document series")
    numero: int = Field(..., ge=1, le=99999999, description="Document number")


class VehiculoSecundario(BaseModel):
    """Model for secondary vehicles in Guía de Remisión."""
    
    placa_numero: str = Field(..., max_length=8, description="Vehicle plate number")
    tuc: Optional[str] = Field(None, max_length=15, description="Tarjeta Única de Circulación")


class ConductorSecundario(BaseModel):
    """Model for secondary drivers in Guía de Remisión."""
    
    documento_tipo: int = Field(..., description="Document type (1=DNI, 4=Carnet Extranjería, 7=Pasaporte)")
    documento_numero: str = Field(..., max_length=15, description="Document number")
    nombre: str = Field(..., max_length=250, description="First name")
    apellidos: str = Field(..., max_length=250, description="Last name")
    numero_licencia: str = Field(..., max_length=10, description="Driver's license number")


class GuiaBase(BaseModel):
    """Base model for Guía de Remisión operations."""
    
    operacion: str = Field(..., description="Operation type")
    tipo_de_comprobante: int = Field(..., description="Document type (7=Guía Remitente, 8=Guía Transportista)")
    serie: str = Field(..., max_length=4, description="Document series")
    numero: int = Field(..., ge=1, le=99999999, description="Document number")


class GuiaGenerar(GuiaBase):
    """Model for generating Guía de Remisión."""
    
    operacion: Literal["generar_guia"] = "generar_guia"
    cliente_tipo_de_documento: int = Field(..., description="Client document type (6=RUC, 1=DNI, etc.)")
    cliente_numero_de_documento: str = Field(..., max_length=15, description="Client document number")
    cliente_denominacion: str = Field(..., max_length=100, description="Client name/company")
    cliente_direccion: str = Field(..., max_length=100, description="Client address")
    cliente_email: Optional[str] = Field(None, max_length=250, description="Client email")
    cliente_email_1: Optional[str] = Field(None, max_length=250, description="Client email 2")
    cliente_email_2: Optional[str] = Field(None, max_length=250, description="Client email 3")
    fecha_de_emision: str = Field(..., description="Emission date (DD-MM-YYYY)")
    observaciones: Optional[str] = Field(None, max_length=1000, description="Observations")
    motivo_de_traslado: Optional[str] = Field(None, max_length=2, description="Transfer reason (01=Venta, 02=Compra, etc.)")
    motivo_de_traslado_otros_descripcion: Optional[str] = Field(None, max_length=70, description="Other transfer reason description")
    documento_relacionado_codigo: Optional[str] = Field(None, max_length=2, description="Related document code for import/export")
    peso_bruto_total: float = Field(..., description="Total gross weight")
    peso_bruto_unidad_de_medida: str = Field(..., max_length=3, description="Weight unit (KGM=kg, TNE=ton)")
    numero_de_bultos: Optional[int] = Field(None, description="Number of packages (GRE Remitente only)")
    tipo_de_transporte: Optional[str] = Field(None, max_length=2, description="Transport type (01=Público, 02=Privado)")
    fecha_de_inicio_de_traslado: str = Field(..., description="Transfer start date (DD-MM-YYYY)")
    transportista_documento_tipo: Optional[int] = Field(None, description="Carrier document type (GRE Remitente only)")
    transportista_documento_numero: Optional[str] = Field(None, max_length=15, description="Carrier document number (GRE Remitente only)")
    transportista_denominacion: Optional[str] = Field(None, max_length=100, description="Carrier name (GRE Remitente only)")
    transportista_placa_numero: str = Field(..., max_length=8, description="Vehicle plate number")
    tuc_vehiculo_principal: Optional[str] = Field(None, max_length=15, description="TUC for main vehicle (GRE Transportista only)")
    conductor_documento_tipo: Optional[int] = Field(None, description="Driver document type")
    conductor_documento_numero: Optional[str] = Field(None, max_length=15, description="Driver document number")
    conductor_nombre: Optional[str] = Field(None, max_length=250, description="Driver first name")
    conductor_apellidos: Optional[str] = Field(None, max_length=250, description="Driver last name")
    conductor_numero_licencia: Optional[str] = Field(None, max_length=10, description="Driver's license number")
    destinatario_documento_tipo: Optional[int] = Field(None, description="Recipient document type (GRE Transportista only)")
    destinatario_documento_numero: Optional[str] = Field(None, max_length=15, description="Recipient document number (GRE Transportista only)")
    destinatario_denominacion: Optional[str] = Field(None, max_length=100, description="Recipient name (GRE Transportista only)")
    mtc: Optional[str] = Field(None, max_length=20, description="MTC code")
    sunat_envio_indicador: Optional[str] = Field(None, max_length=2, description="SUNAT shipping indicator")
    subcontratador_documento_tipo: Optional[int] = Field(None, description="Subcontractor document type")
    subcontratador_documento_numero: Optional[str] = Field(None, max_length=15, description="Subcontractor document number")
    subcontratador_denominacion: Optional[str] = Field(None, max_length=250, description="Subcontractor name")
    pagador_servicio_documento_tipo_identidad: Optional[int] = Field(None, description="Service payer document type")
    pagador_servicio_documento_numero_identidad: Optional[str] = Field(None, max_length=15, description="Service payer document number")
    pagador_servicio_denominacion: Optional[str] = Field(None, max_length=250, description="Service payer name")
    punto_de_partida_ubigeo: str = Field(..., max_length=6, description="Departure location UBIGEO")
    punto_de_partida_direccion: str = Field(..., max_length=150, description="Departure address")
    punto_de_partida_codigo_establecimiento_sunat: Optional[str] = Field(None, max_length=4, description="Departure SUNAT establishment code")
    punto_de_llegada_ubigeo: str = Field(..., max_length=6, description="Arrival location UBIGEO")
    punto_de_llegada_direccion: str = Field(..., max_length=150, description="Arrival address")
    punto_de_llegada_codigo_establecimiento_sunat: Optional[str] = Field(None, max_length=4, description="Arrival SUNAT establishment code")
    enviar_automaticamente_al_cliente: bool = Field(False, description="Auto-send to client")
    formato_de_pdf: Optional[str] = Field(None, description="PDF format (A4, TICKET)")
    items: List[GuiaItem] = Field(..., description="Guide items")
    documento_relacionado: Optional[List[DocumentoRelacionado]] = Field(None, description="Related documents")
    vehiculos_secundarios: Optional[List[VehiculoSecundario]] = Field(None, description="Secondary vehicles")
    conductores_secundarios: Optional[List[ConductorSecundario]] = Field(None, description="Secondary drivers")


class GuiaConsultar(GuiaBase):
    """Model for querying Guía de Remisión."""
    
    operacion: Literal["consultar_guia"] = "consultar_guia"


class GuiaRespuesta(BaseModel):
    """Model for Guía de Remisión response."""
    
    nota_importante: Optional[str] = None
    tipo_de_comprobante: Optional[int] = None
    serie: Optional[str] = None
    numero: Optional[int] = None
    enlace: Optional[str] = None
    aceptada_por_sunat: Optional[bool] = None
    sunat_description: Optional[str] = None
    sunat_note: Optional[str] = None
    sunat_responsecode: Optional[str] = None
    sunat_soap_error: Optional[str] = None
    pdf_zip_base64: Optional[str] = None
    xml_zip_base64: Optional[str] = None
    cdr_zip_base64: Optional[str] = None
    cadena_para_codigo_qr: Optional[str] = None
    enlace_del_pdf: Optional[str] = None
    enlace_del_xml: Optional[str] = None
    enlace_del_cdr: Optional[str] = None


# Percepción Models

class PercepcionItem(BaseModel):
    """Model for Percepción items."""
    
    documento_relacionado_tipo: str = Field(..., max_length=2, description="Related document type (01=Factura, 03=Boleta, 07=Nota Crédito, 08=Nota Débito)")
    documento_relacionado_serie: str = Field(..., max_length=4, description="Related document series")
    documento_relacionado_numero: int = Field(..., ge=1, le=99999999, description="Related document number")
    documento_relacionado_fecha_de_emision: str = Field(..., description="Related document emission date (DD-MM-YYYY)")
    documento_relacionado_moneda: int = Field(..., description="Related document currency (1=Soles, 2=Dólares, 3=Euros)")
    documento_relacionado_total: float = Field(..., description="Related document total amount")
    cobro_fecha: str = Field(..., description="Collection date (DD-MM-YYYY)")
    cobro_numero: int = Field(..., ge=1, description="Collection number")
    cobro_total_sin_percepcion: float = Field(..., description="Collection amount without perception")
    tipo_de_cambio: Optional[float] = Field(None, description="Exchange rate")
    tipo_de_cambio_fecha: str = Field(..., description="Exchange rate date (DD-MM-YYYY)")
    importe_percibido: float = Field(..., description="Perceived amount")
    importe_percibido_fecha: str = Field(..., description="Perceived amount date (DD-MM-YYYY)")
    importe_cobrado_con_percepcion: float = Field(..., description="Collected amount with perception")


class PercepcionBase(BaseModel):
    """Base model for Percepción operations."""
    
    operacion: str = Field(..., description="Operation type")
    serie: str = Field(..., max_length=4, description="Document series (must start with 'P')")
    numero: int = Field(..., ge=1, le=99999999, description="Document number")


class PercepcionGenerar(PercepcionBase):
    """Model for generating Percepción."""
    
    operacion: Literal["generar_percepcion"] = "generar_percepcion"
    cliente_tipo_de_documento: int = Field(..., description="Client document type (must be 6=RUC)")
    cliente_numero_de_documento: str = Field(..., max_length=15, description="Client document number (RUC)")
    cliente_denominacion: str = Field(..., max_length=100, description="Client name/company")
    cliente_direccion: str = Field(..., max_length=100, description="Client address")
    cliente_email: Optional[str] = Field(None, max_length=250, description="Client email")
    cliente_email_1: Optional[str] = Field(None, max_length=250, description="Client email 2")
    cliente_email_2: Optional[str] = Field(None, max_length=250, description="Client email 3")
    fecha_de_emision: str = Field(..., description="Emission date (DD-MM-YYYY)")
    moneda: int = Field(..., description="Currency (must be 1=Soles)")
    tipo_de_tasa_de_percepcion: int = Field(..., description="Perception rate type (1=2%, 2=1%, 3=0.5%)")
    total_percibido: float = Field(..., description="Total perceived amount")
    total_cobrado: float = Field(..., description="Total collected amount")
    observaciones: Optional[str] = Field(None, max_length=1000, description="Observations")
    enviar_automaticamente_a_la_sunat: bool = Field(True, description="Auto-send to SUNAT")
    enviar_automaticamente_al_cliente: bool = Field(False, description="Auto-send to client")
    codigo_unico: Optional[str] = Field(None, max_length=20, description="Unique code")
    formato_de_pdf: Optional[str] = Field(None, description="PDF format")
    items: List[PercepcionItem] = Field(..., description="Perception items")


class PercepcionConsultar(PercepcionBase):
    """Model for querying Percepción."""
    
    operacion: Literal["consultar_percepcion"] = "consultar_percepcion"


class PercepcionReversionGenerar(PercepcionBase):
    """Model for generating Percepción reversion."""
    
    operacion: Literal["generar_reversion_percepcion"] = "generar_reversion_percepcion"


class PercepcionReversionConsultar(PercepcionBase):
    """Model for querying Percepción reversion."""
    
    operacion: Literal["consultar_reversion_percepcion"] = "consultar_reversion_percepcion"
    motivo: Optional[str] = Field(None, max_length=100, description="Reversion reason")


class PercepcionRespuesta(BaseModel):
    """Model for Percepción response."""
    
    serie: Optional[str] = None
    numero: Optional[int] = None
    enlace: Optional[str] = None
    enlace_del_pdf: Optional[str] = None
    enlace_del_xml: Optional[str] = None
    enlace_del_cdr: Optional[str] = None
    aceptada_por_sunat: Optional[bool] = None
    sunat_description: Optional[str] = None
    sunat_note: Optional[str] = None
    sunat_responsecode: Optional[str] = None
    sunat_soap_error: Optional[str] = None


# Retención Models

class RetencionItem(BaseModel):
    """Model for Retención items."""
    
    documento_relacionado_tipo: str = Field(..., max_length=2, description="Related document type (01=Factura, 03=Boleta, 07=Nota Crédito, 08=Nota Débito)")
    documento_relacionado_serie: str = Field(..., max_length=4, description="Related document series")
    documento_relacionado_numero: int = Field(..., ge=1, le=99999999, description="Related document number")
    documento_relacionado_fecha_de_emision: str = Field(..., description="Related document emission date (DD-MM-YYYY)")
    documento_relacionado_moneda: int = Field(..., description="Related document currency (1=Soles, 2=Dólares, 3=Euros)")
    documento_relacionado_total: float = Field(..., description="Related document total amount")
    pago_fecha: str = Field(..., description="Payment date (DD-MM-YYYY)")
    pago_numero: int = Field(..., ge=1, description="Payment number")
    pago_total_sin_retencion: float = Field(..., description="Payment amount without retention")
    tipo_de_cambio: Optional[float] = Field(None, description="Exchange rate")
    tipo_de_cambio_fecha: str = Field(..., description="Exchange rate date (DD-MM-YYYY)")
    importe_retenido: float = Field(..., description="Retained amount")
    importe_retenido_fecha: str = Field(..., description="Retained amount date (DD-MM-YYYY)")
    importe_pagado_con_retencion: float = Field(..., description="Paid amount with retention")


class RetencionBase(BaseModel):
    """Base model for Retención operations."""
    
    operacion: str = Field(..., description="Operation type")
    serie: str = Field(..., max_length=4, description="Document series (must start with 'R')")
    numero: int = Field(..., ge=1, le=99999999, description="Document number")


class RetencionGenerar(RetencionBase):
    """Model for generating Retención."""
    
    operacion: Literal["generar_retencion"] = "generar_retencion"
    cliente_tipo_de_documento: int = Field(..., description="Client document type (must be 6=RUC)")
    cliente_numero_de_documento: str = Field(..., max_length=15, description="Client document number (RUC)")
    cliente_denominacion: str = Field(..., max_length=100, description="Client name/company")
    cliente_direccion: str = Field(..., max_length=100, description="Client address")
    cliente_email: Optional[str] = Field(None, max_length=250, description="Client email")
    cliente_email_1: Optional[str] = Field(None, max_length=250, description="Client email 2")
    cliente_email_2: Optional[str] = Field(None, max_length=250, description="Client email 3")
    fecha_de_emision: str = Field(..., description="Emission date (DD-MM-YYYY)")
    moneda: int = Field(..., description="Currency (must be 1=Soles)")
    tipo_de_tasa_de_retencion: int = Field(..., description="Retention rate type (1=3%, 2=6%)")
    total_retenido: float = Field(..., description="Total retained amount")
    total_pagado: float = Field(..., description="Total paid amount")
    observaciones: Optional[str] = Field(None, max_length=1000, description="Observations")
    enviar_automaticamente_a_la_sunat: bool = Field(True, description="Auto-send to SUNAT")
    enviar_automaticamente_al_cliente: bool = Field(False, description="Auto-send to client")
    codigo_unico: Optional[str] = Field(None, max_length=20, description="Unique code")
    formato_de_pdf: Optional[str] = Field(None, description="PDF format")
    items: List[RetencionItem] = Field(..., description="Retention items")


class RetencionConsultar(RetencionBase):
    """Model for querying Retención."""
    
    operacion: Literal["consultar_retencion"] = "consultar_retencion"


class RetencionReversionGenerar(RetencionBase):
    """Model for generating Retención reversion."""
    
    operacion: Literal["generar_reversion_retencion"] = "generar_reversion_retencion"
    motivo: Optional[str] = Field(None, max_length=100, description="Reversion reason")


class RetencionReversionConsultar(RetencionBase):
    """Model for querying Retención reversion."""
    
    operacion: Literal["consultar_reversion_retencion"] = "consultar_reversion_retencion"


class RetencionRespuesta(BaseModel):
    """Model for Retención response."""
    
    serie: Optional[str] = None
    numero: Optional[int] = None
    enlace: Optional[str] = None
    enlace_del_pdf: Optional[str] = None
    enlace_del_xml: Optional[str] = None
    enlace_del_cdr: Optional[str] = None
    aceptada_por_sunat: Optional[bool] = None
    sunat_description: Optional[str] = None
    sunat_note: Optional[str] = None
    sunat_responsecode: Optional[str] = None
    sunat_soap_error: Optional[str] = None