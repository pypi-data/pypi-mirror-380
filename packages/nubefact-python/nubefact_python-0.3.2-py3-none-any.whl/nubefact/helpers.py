"""
Helper methods for NubeFact API constants.

This module provides helper methods to get lists of available options for UI selects
and to convert user selections back to API constants.
"""

from typing import List, Optional, Dict, Any
from .client import NubeFact


def get_categories() -> List[str]:
    """
    Get list of all available categories for helper methods.
    
    Returns:
        List of category names that can be used with get_options() and get_constant()
    """
    return [
        # Main comprobante types
        "tipo_de_comprobante",
        "sunat_transaction",
        "cliente_tipo_de_documento",
        "moneda",
        "tipo_de_igv",
        "percepcion_tipo",
        "retencion_tipo",
        "tipo_de_nota_de_credito",
        "tipo_de_nota_de_debito",
        
        # Guía de Remisión
        "motivo_de_traslado",
        "peso_bruto_unidad_de_medida",
        "tipo_de_transporte",
        "sunat_envio_indicador",
        
        # Percepción
        "tipo_de_tasa_de_percepcion",
        "documento_relacionado_tipo",
        
        # Retención
        "tipo_de_tasa_de_retencion",
        
        # Documento relacionado tipos
        "documento_relacionado_tipo_guia",
    ]


def get_options(category: str) -> List[str]:
    """
    Get list of available options for a given category.
    
    Args:
        category: The category name (from get_categories())
        
    Returns:
        List of text options suitable for UI selects
        
    Raises:
        ValueError: If category is not recognized
    """
    options_map = {
        # Main comprobante types
        "tipo_de_comprobante": [
            "FACTURA",
            "BOLETA", 
            "NOTA DE CRÉDITO",
            "NOTA DE DÉBITO",
            "GUÍA DE REMISIÓN REMITENTE",
            "GUÍA DE REMISIÓN TRANSPORTISTA",
        ],
        "sunat_transaction": [
            "VENTA INTERNA",
            "EXPORTACIÓN",
            "VENTA INTERNA - ANTICIPOS",
            "VENTAS NO DOMICILIADOS QUE NO CALIFICAN COMO EXPORTACIÓN",
            "OPERACIÓN SUJETA A DETRACCIÓN",
            "DETRACCIÓN - SERVICIOS DE TRANSPORTE CARGA",
            "DETRACCIÓN - SERVICIOS DE TRANSPORTE DE PASAJEROS",
            "DETRACCIÓN - RECURSOS HIDROBIOLÓGICOS",
            "OPERACIÓN SUJETA A PERCEPCIÓN",
            "VENTA NACIONAL A TURISTAS - TAX FREE",
        ],
        "cliente_tipo_de_documento": [
            "RUC - REGISTRO ÚNICO DE CONTRIBUYENTE",
            "DNI - DOC. NACIONAL DE IDENTIDAD",
            "VARIOS - VENTAS MENORES A S/.700.00 Y OTROS",
            "CARNET DE EXTRANJERÍA",
            "PASAPORTE",
            "CÉDULA DIPLOMÁTICA DE IDENTIDAD",
            "DOC.IDENT.PAIS.RESIDENCIA-NO.D",
            "NO DOMICILIADO, SIN RUC (EXPORTACIÓN)",
            "Salvoconducto",
        ],
        "moneda": [
            "SOLES",
            "DÓLARES",
            "EUROS",
            "LIBRA ESTERLINA",
        ],
        "tipo_de_igv": [
            "GRAVADO - OPERACIÓN ONEROSA",
            "GRAVADO – RETIRO POR PREMIO",
            "GRAVADO – RETIRO POR DONACIÓN",
            "GRAVADO – RETIRO",
            "GRAVADO – RETIRO POR PUBLICIDAD",
            "GRAVADO – BONIFICACIONES",
            "GRAVADO – RETIRO POR ENTREGA A TRABAJADORES",
            "EXONERADO - OPERACIÓN ONEROSA",
            "INAFECTO - OPERACIÓN ONEROSA",
            "INAFECTO – RETIRO POR BONIFICACIÓN",
            "INAFECTO – RETIRO",
            "INAFECTO – RETIRO POR MUESTRAS MÉDICAS",
            "INAFECTO - RETIRO POR CONVENIO COLECTIVO",
            "INAFECTO – RETIRO POR PREMIO",
            "INAFECTO - RETIRO POR PUBLICIDAD",
            "EXPORTACIÓN",
            "EXONERADO - TRANSFERENCIA GRATUITA",
            "INAFECTO - TRANSFERENCIA GRATUITA",
        ],
        "percepcion_tipo": [
            "PERCEPCIÓN VENTA INTERNA - TASA 2%",
            "PERCEPCIÓN ADQUISICIÓN DE COMBUSTIBLE - TASA 1%",
            "PERCEPCIÓN REALIZADA AL AGENTE DE PERCEPCIÓN CON TASA ESPECIAL - TASA 0.5%",
        ],
        "retencion_tipo": [
            "TASA 3%",
            "TASA 6%",
        ],
        "tipo_de_nota_de_credito": [
            "ANULACIÓN DE LA OPERACIÓN",
            "ANULACIÓN POR ERROR EN EL RUC",
            "CORRECCIÓN POR ERROR EN LA DESCRIPCIÓN",
            "DESCUENTO GLOBAL",
            "DESCUENTO POR ÍTEM",
            "DEVOLUCIÓN TOTAL",
            "DEVOLUCIÓN POR ÍTEM",
            "BONIFICACIÓN",
            "DISMINUCIÓN EN EL VALOR",
            "OTROS CONCEPTOS",
            "AJUSTES AFECTOS AL IVAP",
            "AJUSTES DE OPERACIONES DE EXPORTACIÓN",
            "AJUSTES - MONTOS Y/O FECHAS DE PAGO",
        ],
        "tipo_de_nota_de_debito": [
            "INTERESES POR MORA",
            "AUMENTO DE VALOR",
            "PENALIDADES",
            "AJUSTES AFECTOS AL IVAP",
            "AJUSTES DE OPERACIONES DE EXPORTACIÓN",
        ],
        
        # Guía de Remisión
        "motivo_de_traslado": [
            "VENTA",
            "VENTA SUJETA A CONFIRMACION DEL COMPRADOR",
            "COMPRA",
            "TRASLADO ENTRE ESTABLECIMIENTOS DE LA MISMA EMPRESA",
            "TRASLADO EMISOR ITINERANTE CP",
            "IMPORTACION",
            "EXPORTACION",
            "OTROS",
            "CONSIGNACION",
            "TRASLADO DE BIENES PARA TRANSFORMACION",
            "VENTA CON ENTREGA A TERCEROS",
            "DEVOLUCION",
            "RECOJO DE BIENES TRANSFORMADOS",
        ],
        "peso_bruto_unidad_de_medida": [
            "KILOGRAMOS",
            "TONELADAS",
        ],
        "tipo_de_transporte": [
            "TRANSPORTE PÚBLICO",
            "TRANSPORTE PRIVADO",
        ],
        "sunat_envio_indicador": [
            "SUNAT_ENVIO_INDICADORPAGADORFLETE_REMITENTE",
            "SUNAT_ENVIO_INDICADORPAGADORFLETE_SUBCONTRATADOR",
            "SUNAT_ENVIO_INDICADORPAGADORFLETE_TERCERO",
            "SUNAT_ENVIO_INDICADORRETORNOVEHICULOENVASEVACIO",
            "SUNAT_ENVIO_INDICADORRETORNOVEHICULOVACIO",
            "SUNAT_ENVIO_INDICADORTRASLADOVEHICULOM1L",
        ],
        
        # Percepción
        "tipo_de_tasa_de_percepcion": [
            "TASA 2% - PERCEPCIÓN VENTA INTERNA",
            "TASA 1% - PERCEPCIÓN A LA ADQUISICIÓN DE COMBUSTIBLE",
            "TASA 0.5% - PERCEPCIÓN REALIZADA AL AGENTE DE PERCEPCIÓN CON TASA ESPECIAL",
        ],
        "documento_relacionado_tipo": [
            "FACTURA",
            "BOLETA DE VENTA",
            "NOTA DE CRÉDITO",
            "NOTA DE DÉBITO",
        ],
        
        # Retención
        "tipo_de_tasa_de_retencion": [
            "TASA 3%",
            "TASA 6%",
        ],
        
        # Documento relacionado tipos para Guías
        "documento_relacionado_tipo_guia": [
            "FACTURA",
            "BOLETA DE VENTA",
            "GUÍA DE REMISIÓN REMITENTE",
            "GUÍA DE REMISIÓN TRANSPORTISTA",
        ],
    }
    
    if category not in options_map:
        raise ValueError(f"Unknown category: {category}. Available categories: {get_categories()}")
    
    return options_map[category]


def get_constant(category: str, label: str) -> Any:
    """
    Get the constant value for a given category and label.
    
    Args:
        category: The category name (from get_categories())
        label: The text label from get_options()
        
    Returns:
        The corresponding constant value
        
    Raises:
        ValueError: If category or label is not recognized
    """
    # Map from label text to constant values
    constant_map = {
        "tipo_de_comprobante": {
            "FACTURA": NubeFact.TipoComprobante.FACTURA,
            "BOLETA": NubeFact.TipoComprobante.BOLETA,
            "NOTA DE CRÉDITO": NubeFact.TipoComprobante.NOTA_CREDITO,
            "NOTA DE DÉBITO": NubeFact.TipoComprobante.NOTA_DEBITO,
            "GUÍA DE REMISIÓN REMITENTE": NubeFact.TipoComprobante.GUIA_REMITENTE,
            "GUÍA DE REMISIÓN TRANSPORTISTA": NubeFact.TipoComprobante.GUIA_TRANSPORTISTA,
        },
        "sunat_transaction": {
            "VENTA INTERNA": NubeFact.SunatTransaction.VENTA_INTERNA,
            "EXPORTACIÓN": NubeFact.SunatTransaction.EXPORTACION,
            "VENTA INTERNA - ANTICIPOS": NubeFact.SunatTransaction.VENTA_INTERNA_ANTICIPOS,
            "VENTAS NO DOMICILIADOS QUE NO CALIFICAN COMO EXPORTACIÓN": NubeFact.SunatTransaction.VENTA_NO_DOMICILIADOS,
            "OPERACIÓN SUJETA A DETRACCIÓN": NubeFact.SunatTransaction.DETRACCION,
            "DETRACCIÓN - SERVICIOS DE TRANSPORTE CARGA": NubeFact.SunatTransaction.DETRACCION_TRANSPORTE_CARGA,
            "DETRACCIÓN - SERVICIOS DE TRANSPORTE DE PASAJEROS": NubeFact.SunatTransaction.DETRACCION_TRANSPORTE_PASAJEROS,
            "DETRACCIÓN - RECURSOS HIDROBIOLÓGICOS": NubeFact.SunatTransaction.DETRACCION_RECURSOS_HIDROBIOLOGICOS,
            "OPERACIÓN SUJETA A PERCEPCIÓN": NubeFact.SunatTransaction.PERCEPCION,
            "VENTA NACIONAL A TURISTAS - TAX FREE": NubeFact.SunatTransaction.VENTA_NACIONAL_TURISTAS,
        },
        "cliente_tipo_de_documento": {
            "RUC - REGISTRO ÚNICO DE CONTRIBUYENTE": NubeFact.ClienteTipoDocumento.RUC,
            "DNI - DOC. NACIONAL DE IDENTIDAD": NubeFact.ClienteTipoDocumento.DNI,
            "VARIOS - VENTAS MENORES A S/.700.00 Y OTROS": NubeFact.ClienteTipoDocumento.VARIOS,
            "CARNET DE EXTRANJERÍA": NubeFact.ClienteTipoDocumento.CARNET_EXTRANJERIA,
            "PASAPORTE": NubeFact.ClienteTipoDocumento.PASAPORTE,
            "CÉDULA DIPLOMÁTICA DE IDENTIDAD": NubeFact.ClienteTipoDocumento.CEDULA_DIPLOMATICA,
            "DOC.IDENT.PAIS.RESIDENCIA-NO.D": NubeFact.ClienteTipoDocumento.DOC_IDENT_PAIS_RESIDENCIA,
            "NO DOMICILIADO, SIN RUC (EXPORTACIÓN)": NubeFact.ClienteTipoDocumento.NO_DOMICILIADO,
            "Salvoconducto": NubeFact.ClienteTipoDocumento.SALVOCONDUCTO,
        },
        "moneda": {
            "SOLES": NubeFact.Moneda.SOLES,
            "DÓLARES": NubeFact.Moneda.DOLARES,
            "EUROS": NubeFact.Moneda.EUROS,
            "LIBRA ESTERLINA": NubeFact.Moneda.LIBRA_ESTERLINA,
        },
        "tipo_de_igv": {
            "GRAVADO - OPERACIÓN ONEROSA": NubeFact.TipoIGV.GRAVADO_OPERACION_ONEROSA,
            "GRAVADO – RETIRO POR PREMIO": NubeFact.TipoIGV.GRAVADO_RETIRO_PREMIO,
            "GRAVADO – RETIRO POR DONACIÓN": NubeFact.TipoIGV.GRAVADO_RETIRO_DONACION,
            "GRAVADO – RETIRO": NubeFact.TipoIGV.GRAVADO_RETIRO,
            "GRAVADO – RETIRO POR PUBLICIDAD": NubeFact.TipoIGV.GRAVADO_RETIRO_PUBLICIDAD,
            "GRAVADO – BONIFICACIONES": NubeFact.TipoIGV.GRAVADO_BONIFICACIONES,
            "GRAVADO – RETIRO POR ENTREGA A TRABAJADORES": NubeFact.TipoIGV.GRAVADO_RETIRO_TRABAJADORES,
            "EXONERADO - OPERACIÓN ONEROSA": NubeFact.TipoIGV.EXONERADO_OPERACION_ONEROSA,
            "INAFECTO - OPERACIÓN ONEROSA": NubeFact.TipoIGV.INAFECTO_OPERACION_ONEROSA,
            "INAFECTO – RETIRO POR BONIFICACIÓN": NubeFact.TipoIGV.INAFECTO_RETIRO_BONIFICACION,
            "INAFECTO – RETIRO": NubeFact.TipoIGV.INAFECTO_RETIRO,
            "INAFECTO – RETIRO POR MUESTRAS MÉDICAS": NubeFact.TipoIGV.INAFECTO_RETIRO_MUESTRAS_MEDICAS,
            "INAFECTO - RETIRO POR CONVENIO COLECTIVO": NubeFact.TipoIGV.INAFECTO_RETIRO_CONVENIO_COLECTIVO,
            "INAFECTO – RETIRO POR PREMIO": NubeFact.TipoIGV.INAFECTO_RETIRO_PREMIO,
            "INAFECTO - RETIRO POR PUBLICIDAD": NubeFact.TipoIGV.INAFECTO_RETIRO_PUBLICIDAD,
            "EXPORTACIÓN": NubeFact.TipoIGV.EXPORTACION_ITEM,
            "EXONERADO - TRANSFERENCIA GRATUITA": NubeFact.TipoIGV.EXONERADO_TRANSFERENCIA_GRATUITA,
            "INAFECTO - TRANSFERENCIA GRATUITA": NubeFact.TipoIGV.INAFECTO_TRANSFERENCIA_GRATUITA,
        },
        "percepcion_tipo": {
            "PERCEPCIÓN VENTA INTERNA - TASA 2%": NubeFact.Percepcion.TasaPercepcion.TASA_2_PORCIENTO,
            "PERCEPCIÓN ADQUISICIÓN DE COMBUSTIBLE - TASA 1%": NubeFact.Percepcion.TasaPercepcion.TASA_1_PORCIENTO,
            "PERCEPCIÓN REALIZADA AL AGENTE DE PERCEPCIÓN CON TASA ESPECIAL - TASA 0.5%": NubeFact.Percepcion.TasaPercepcion.TASA_0_5_PORCIENTO,
        },
        "retencion_tipo": {
            "TASA 3%": NubeFact.Retencion.TasaRetencion.TASA_3_PORCIENTO,
            "TASA 6%": NubeFact.Retencion.TasaRetencion.TASA_6_PORCIENTO,
        },
        "tipo_de_nota_de_credito": {
            "ANULACIÓN DE LA OPERACIÓN": NubeFact.NotaCredito.TipoNotaCredito.ANULACION_OPERACION,
            "ANULACIÓN POR ERROR EN EL RUC": NubeFact.NotaCredito.TipoNotaCredito.ANULACION_ERROR_RUC,
            "CORRECCIÓN POR ERROR EN LA DESCRIPCIÓN": NubeFact.NotaCredito.TipoNotaCredito.CORRECCION_DESCRIPCION,
            "DESCUENTO GLOBAL": NubeFact.NotaCredito.TipoNotaCredito.DESCUENTO_GLOBAL,
            "DESCUENTO POR ÍTEM": NubeFact.NotaCredito.TipoNotaCredito.DESCUENTO_ITEM,
            "DEVOLUCIÓN TOTAL": NubeFact.NotaCredito.TipoNotaCredito.DEVOLUCION_TOTAL,
            "DEVOLUCIÓN POR ÍTEM": NubeFact.NotaCredito.TipoNotaCredito.DEVOLUCION_ITEM,
            "BONIFICACIÓN": NubeFact.NotaCredito.TipoNotaCredito.BONIFICACION,
            "DISMINUCIÓN EN EL VALOR": NubeFact.NotaCredito.TipoNotaCredito.DISMINUCION_VALOR,
            "OTROS CONCEPTOS": NubeFact.NotaCredito.TipoNotaCredito.OTROS_CONCEPTOS,
            "AJUSTES AFECTOS AL IVAP": NubeFact.NotaCredito.TipoNotaCredito.AJUSTES_IVAP,
            "AJUSTES DE OPERACIONES DE EXPORTACIÓN": NubeFact.NotaCredito.TipoNotaCredito.AJUSTES_EXPORTACION,
            "AJUSTES - MONTOS Y/O FECHAS DE PAGO": NubeFact.NotaCredito.TipoNotaCredito.AJUSTES_MONTOS_FECHAS,
        },
        "tipo_de_nota_de_debito": {
            "INTERESES POR MORA": NubeFact.NotaDebito.TipoNotaDebito.INTERESES_MORA,
            "AUMENTO DE VALOR": NubeFact.NotaDebito.TipoNotaDebito.AUMENTO_VALOR,
            "PENALIDADES": NubeFact.NotaDebito.TipoNotaDebito.PENALIDADES,
            "AJUSTES AFECTOS AL IVAP": NubeFact.NotaDebito.TipoNotaDebito.AJUSTES_IVAP,
            "AJUSTES DE OPERACIONES DE EXPORTACIÓN": NubeFact.NotaDebito.TipoNotaDebito.AJUSTES_EXPORTACION,
        },
        
        # Guía de Remisión
        "motivo_de_traslado": {
            "VENTA": NubeFact.GuiaRemision.MotivoTraslado.VENTA,
            "VENTA SUJETA A CONFIRMACION DEL COMPRADOR": NubeFact.GuiaRemision.MotivoTraslado.VENTA_SUJETA_CONFIRMACION,
            "COMPRA": NubeFact.GuiaRemision.MotivoTraslado.COMPRA,
            "TRASLADO ENTRE ESTABLECIMIENTOS DE LA MISMA EMPRESA": NubeFact.GuiaRemision.MotivoTraslado.TRASLADO_ENTRE_ESTABLECIMIENTOS,
            "TRASLADO EMISOR ITINERANTE CP": NubeFact.GuiaRemision.MotivoTraslado.TRASLADO_EMISOR_ITINERANTE,
            "IMPORTACION": NubeFact.GuiaRemision.MotivoTraslado.IMPORTACION,
            "EXPORTACION": NubeFact.GuiaRemision.MotivoTraslado.EXPORTACION,
            "OTROS": NubeFact.GuiaRemision.MotivoTraslado.OTROS,
            "CONSIGNACION": NubeFact.GuiaRemision.MotivoTraslado.CONSIGNACION,
            "TRASLADO DE BIENES PARA TRANSFORMACION": NubeFact.GuiaRemision.MotivoTraslado.RECOJO_BIENES_TRANSFORMADOS,
            "VENTA CON ENTREGA A TERCEROS": NubeFact.GuiaRemision.MotivoTraslado.VENTA_CON_ENTREGA_TERCEROS,
            "DEVOLUCION": NubeFact.GuiaRemision.MotivoTraslado.DEVOLUCION,
            "RECOJO DE BIENES TRANSFORMADOS": NubeFact.GuiaRemision.MotivoTraslado.RECOJO_BIENES_TRANSFORMADOS,
        },
        "peso_bruto_unidad_de_medida": {
            "KILOGRAMOS": NubeFact.GuiaRemision.UnidadMedidaPeso.KILOGRAMOS,
            "TONELADAS": NubeFact.GuiaRemision.UnidadMedidaPeso.TONELADAS,
        },
        "tipo_de_transporte": {
            "TRANSPORTE PÚBLICO": NubeFact.GuiaRemision.TipoTransporte.PUBLICO,
            "TRANSPORTE PRIVADO": NubeFact.GuiaRemision.TipoTransporte.PRIVADO,
        },
        "sunat_envio_indicador": {
            "SUNAT_ENVIO_INDICADORPAGADORFLETE_REMITENTE": NubeFact.GuiaRemision.SunatEnvioIndicador.PAGADOR_FLETE_REMITENTE,
            "SUNAT_ENVIO_INDICADORPAGADORFLETE_SUBCONTRATADOR": NubeFact.GuiaRemision.SunatEnvioIndicador.PAGADOR_FLETE_SUBCONTRATADOR,
            "SUNAT_ENVIO_INDICADORPAGADORFLETE_TERCERO": NubeFact.GuiaRemision.SunatEnvioIndicador.PAGADOR_FLETE_TERCERO,
            "SUNAT_ENVIO_INDICADORRETORNOVEHICULOENVASEVACIO": NubeFact.GuiaRemision.SunatEnvioIndicador.RETORNO_VEHICULO_ENVASE_VACIO,
            "SUNAT_ENVIO_INDICADORRETORNOVEHICULOVACIO": NubeFact.GuiaRemision.SunatEnvioIndicador.RETORNO_VEHICULO_VACIO,
            "SUNAT_ENVIO_INDICADORTRASLADOVEHICULOM1L": NubeFact.GuiaRemision.SunatEnvioIndicador.TRASLADO_VEHICULO_M1L,
        },
        
        # Percepción
        "tipo_de_tasa_de_percepcion": {
            "TASA 2% - PERCEPCIÓN VENTA INTERNA": NubeFact.Percepcion.TasaPercepcion.TASA_2_PORCIENTO,
            "TASA 1% - PERCEPCIÓN A LA ADQUISICIÓN DE COMBUSTIBLE": NubeFact.Percepcion.TasaPercepcion.TASA_1_PORCIENTO,
            "TASA 0.5% - PERCEPCIÓN REALIZADA AL AGENTE DE PERCEPCIÓN CON TASA ESPECIAL": NubeFact.Percepcion.TasaPercepcion.TASA_0_5_PORCIENTO,
        },
        "documento_relacionado_tipo": {
            "FACTURA": NubeFact.Percepcion.DocumentoRelacionado.FACTURA,
            "BOLETA DE VENTA": NubeFact.Percepcion.DocumentoRelacionado.BOLETA,
            "NOTA DE CRÉDITO": NubeFact.Percepcion.DocumentoRelacionado.NOTA_CREDITO,
            "NOTA DE DÉBITO": NubeFact.Percepcion.DocumentoRelacionado.NOTA_DEBITO,
        },
        
        # Retención
        "tipo_de_tasa_de_retencion": {
            "TASA 3%": NubeFact.Retencion.TasaRetencion.TASA_3_PORCIENTO,
            "TASA 6%": NubeFact.Retencion.TasaRetencion.TASA_6_PORCIENTO,
        },
        
        # Documento relacionado tipos para Guías
        "documento_relacionado_tipo_guia": {
            "FACTURA": NubeFact.GuiaRemision.DocumentoRelacionado.FACTURA,
            "BOLETA DE VENTA": NubeFact.GuiaRemision.DocumentoRelacionado.BOLETA,
            "GUÍA DE REMISIÓN REMITENTE": NubeFact.GuiaRemision.DocumentoRelacionado.GUIA_REMITENTE,
            "GUÍA DE REMISIÓN TRANSPORTISTA": NubeFact.GuiaRemision.DocumentoRelacionado.GUIA_TRANSPORTISTA,
        },
    }
    
    if category not in constant_map:
        raise ValueError(f"Unknown category: {category}. Available categories: {get_categories()}")
    
    if label not in constant_map[category]:
        raise ValueError(f"Unknown label '{label}' for category '{category}'. Available options: {get_options(category)}")
    
    return constant_map[category][label]


# Convenience function to get all options as a dictionary
def get_all_options() -> Dict[str, List[str]]:
    """
    Get all available options as a dictionary.
    
    Returns:
        Dictionary with category names as keys and option lists as values
    """
    return {category: get_options(category) for category in get_categories()}