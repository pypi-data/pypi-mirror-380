"""
NubeFact API client for Peruvian electronic invoicing.
"""

import json
from typing import Optional, Union
import httpx
from pydantic import BaseModel
from .models import (
    ComprobanteGenerar,
    ComprobanteConsultar,
    AnulacionGenerar,
    AnulacionConsultar,
    ComprobanteRespuesta,
    AnulacionRespuesta,
    ErrorRespuesta,
    # Guía de Remisión models
    GuiaGenerar,
    GuiaConsultar,
    GuiaRespuesta,
    # Percepción models
    PercepcionGenerar,
    PercepcionConsultar,
    PercepcionReversionGenerar,
    PercepcionReversionConsultar,
    PercepcionRespuesta,
    # Retención models
    RetencionGenerar,
    RetencionConsultar,
    RetencionReversionGenerar,
    RetencionReversionConsultar,
    RetencionRespuesta,
)


class NubeFactError(Exception):
    """Base exception for NubeFact API errors."""
    
    def __init__(self, message: str, code: Optional[int] = None):
        self.message = message
        self.code = code
        super().__init__(self.message)


class NubeFactClient:
    """Client for interacting with the NubeFact API."""
    
    def __init__(
        self, 
        ruta: str, 
        token: str,
        timeout: float = 30.0,
        verify_ssl: bool = True
    ):
        """
        Initialize the NubeFact client.
        
        Args:
            ruta: API endpoint URL
            token: Authentication token
            timeout: Request timeout in seconds
            verify_ssl: Whether to verify SSL certificates
        """
        self.ruta = ruta.rstrip('/')
        self.token = token
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        
        # Headers for JSON requests
        self.headers = {
            'Authorization': f'Token token="{self.token}"',
            'Content-Type': 'application/json',
        }
        
        # Create HTTP client
        self.client = httpx.Client(
            timeout=self.timeout,
            verify=self.verify_ssl,
            headers=self.headers
        )
    
    def _make_request(self, data: Union[dict, BaseModel]) -> dict:
        """
        Make a POST request to the NubeFact API.
        
        Args:
            data: Request data as dict or Pydantic model
            
        Returns:
            Response data as dict
            
        Raises:
            NubeFactError: If the API returns an error
        """
        # Convert Pydantic model to dict if needed
        if hasattr(data, 'model_dump'):
            data_dict = data.model_dump(exclude_none=True)
        else:
            data_dict = data
        
        try:
            response = self.client.post(
                self.ruta,
                json=data_dict
            )
            response.raise_for_status()
            
            result = response.json()
            
            # Check for API errors
            if 'errors' in result:
                error_msg = result.get('errors', 'Unknown error')
                error_code = result.get('codigo')
                raise NubeFactError(error_msg, error_code)
                
            return result
            
        except httpx.HTTPStatusError as e:
            # Handle HTTP errors
            if e.response.status_code == 401:
                raise NubeFactError("Authentication failed - invalid token or URL", 10)
            elif e.response.status_code == 400:
                # For 400 errors, check if it's a valid API response with error code
                try:
                    result = e.response.json()
                    if 'errors' in result and 'codigo' in result:
                        # This is a valid NubeFact API error response
                        error_msg = result.get('errors', 'Unknown error')
                        error_code = result.get('codigo')
                        raise NubeFactError(error_msg, error_code)
                    else:
                        # Generic 400 error
                        raise NubeFactError("Bad request - check your data", 12)
                except (json.JSONDecodeError, ValueError):
                    # Not a JSON response, generic error
                    raise NubeFactError("Bad request - check your data", 12)
            elif e.response.status_code == 500:
                raise NubeFactError("Internal server error", 40)
            else:
                raise NubeFactError(f"HTTP error {e.response.status_code}: {e.response.text}")
                
        except httpx.RequestError as e:
            raise NubeFactError(f"Request failed: {str(e)}")
        
        except json.JSONDecodeError as e:
            raise NubeFactError(f"Invalid JSON response: {str(e)}")
    
    def generar_comprobante(self, comprobante: ComprobanteGenerar) -> ComprobanteRespuesta:
        """
        Generate an invoice, receipt, or note.
        
        Args:
            comprobante: Comprobante data
            
        Returns:
            Response with document details
        """
        result = self._make_request(comprobante)
        return ComprobanteRespuesta(**result)
    
    def consultar_comprobante(self, comprobante: ComprobanteConsultar) -> ComprobanteRespuesta:
        """
        Query an existing invoice, receipt, or note.
        
        Args:
            comprobante: Query parameters
            
        Returns:
            Document details
        """
        result = self._make_request(comprobante)
        return ComprobanteRespuesta(**result)
    
    def generar_anulacion(self, anulacion: AnulacionGenerar) -> AnulacionRespuesta:
        """
        Generate a cancellation for a document.
        
        Args:
            anulacion: Cancellation data
            
        Returns:
            Cancellation response
        """
        result = self._make_request(anulacion)
        return AnulacionRespuesta(**result)
    
    def consultar_anulacion(self, anulacion: AnulacionConsultar) -> AnulacionRespuesta:
        """
        Query a cancellation status.
        
        Args:
            anulacion: Query parameters
            
        Returns:
            Cancellation details
        """
        result = self._make_request(anulacion)
        return AnulacionRespuesta(**result)
    
    def generar_guia(self, guia: GuiaGenerar) -> GuiaRespuesta:
        """
        Generate a Guía de Remisión (Shipping Guide).
        
        Args:
            guia: Guía de Remisión data
            
        Returns:
            Response with guide details
        """
        result = self._make_request(guia)
        return GuiaRespuesta(**result)
    
    def consultar_guia(self, guia: GuiaConsultar) -> GuiaRespuesta:
        """
        Query an existing Guía de Remisión.
        
        Args:
            guia: Query parameters
            
        Returns:
            Guide details
        """
        result = self._make_request(guia)
        return GuiaRespuesta(**result)
    
    # Percepción Operations
    
    def generar_percepcion(self, percepcion: PercepcionGenerar) -> PercepcionRespuesta:
        """
        Generate a Percepción (Perception) document.
        
        Args:
            percepcion: Percepción data
            
        Returns:
            Response with perception details
        """
        result = self._make_request(percepcion)
        return PercepcionRespuesta(**result)
    
    def consultar_percepcion(self, percepcion: PercepcionConsultar) -> PercepcionRespuesta:
        """
        Query an existing Percepción.
        
        Args:
            percepcion: Query parameters
            
        Returns:
            Perception details
        """
        result = self._make_request(percepcion)
        return PercepcionRespuesta(**result)
    
    def generar_reversion_percepcion(self, percepcion: PercepcionReversionGenerar) -> PercepcionRespuesta:
        """
        Generate a Percepción reversion.
        
        Args:
            percepcion: Reversion data
            
        Returns:
            Reversion response
        """
        result = self._make_request(percepcion)
        return PercepcionRespuesta(**result)
    
    def consultar_reversion_percepcion(self, percepcion: PercepcionReversionConsultar) -> PercepcionRespuesta:
        """
        Query a Percepción reversion status.
        
        Args:
            percepcion: Query parameters
            
        Returns:
            Reversion details
        """
        result = self._make_request(percepcion)
        return PercepcionRespuesta(**result)
    
    # Retención Operations
    
    def generar_retencion(self, retencion: RetencionGenerar) -> RetencionRespuesta:
        """
        Generate a Retención (Retention) document.
        
        Args:
            retencion: Retención data
            
        Returns:
            Response with retention details
        """
        result = self._make_request(retencion)
        return RetencionRespuesta(**result)
    
    def consultar_retencion(self, retencion: RetencionConsultar) -> RetencionRespuesta:
        """
        Query an existing Retención.
        
        Args:
            retencion: Query parameters
            
        Returns:
            Retention details
        """
        result = self._make_request(retencion)
        return RetencionRespuesta(**result)
    
    def generar_reversion_retencion(self, retencion: RetencionReversionGenerar) -> RetencionRespuesta:
        """
        Generate a Retención reversion.
        
        Args:
            retencion: Reversion data
            
        Returns:
            Reversion response
        """
        result = self._make_request(retencion)
        return RetencionRespuesta(**result)
    
    def consultar_reversion_retencion(self, retencion: RetencionReversionConsultar) -> RetencionRespuesta:
        """
        Query a Retención reversion status.
        
        Args:
            retencion: Query parameters
            
        Returns:
            Reversion details
        """
        result = self._make_request(retencion)
        return RetencionRespuesta(**result)
    
    def close(self):
        """Close the HTTP client."""
        self.client.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Convenience functions for common operations

class NubeFact:
    """Convenience class for common NubeFact operations with organized constants."""
    
    class TipoComprobante:
        """Constants for 'tipo_de_comprobante' field."""
        FACTURA = 1
        BOLETA = 2
        NOTA_CREDITO = 3
        NOTA_DEBITO = 4
        GUIA_REMITENTE = 7
        GUIA_TRANSPORTISTA = 8
    
    class SunatTransaction:
        """Constants for 'sunat_transaction' field."""
        VENTA_INTERNA = 1
        EXPORTACION = 2
        VENTA_INTERNA_ANTICIPOS = 4
        VENTA_NO_DOMICILIADOS = 29
        DETRACCION = 30
        DETRACCION_RECURSOS_HIDROBIOLOGICOS = 31
        DETRACCION_TRANSPORTE_PASAJEROS = 32
        DETRACCION_TRANSPORTE_CARGA = 33
        PERCEPCION = 34
        VENTA_NACIONAL_TURISTAS = 35
    
    class ClienteTipoDocumento:
        """Constants for 'cliente_tipo_de_documento' field."""
        RUC = 6
        DNI = 1
        VARIOS = "-"
        CARNET_EXTRANJERIA = 4
        PASAPORTE = 7
        CEDULA_DIPLOMATICA = "A"
        DOC_IDENT_PAIS_RESIDENCIA = "B"
        NO_DOMICILIADO = "0"
        SALVOCONDUCTO = "G"
    
    class Moneda:
        """Constants for 'moneda' field."""
        SOLES = 1
        DOLARES = 2
        EUROS = 3
        LIBRA_ESTERLINA = 4
    
    class TipoIGV:
        """Constants for 'tipo_de_igv' field in items."""
        GRAVADO_OPERACION_ONEROSA = 1
        GRAVADO_RETIRO_PREMIO = 2
        GRAVADO_RETIRO_DONACION = 3
        GRAVADO_RETIRO = 4
        GRAVADO_RETIRO_PUBLICIDAD = 5
        GRAVADO_BONIFICACIONES = 6
        GRAVADO_RETIRO_TRABAJADORES = 7
        EXONERADO_OPERACION_ONEROSA = 8
        INAFECTO_OPERACION_ONEROSA = 9
        INAFECTO_RETIRO_BONIFICACION = 10
        INAFECTO_RETIRO = 11
        INAFECTO_RETIRO_MUESTRAS_MEDICAS = 12
        INAFECTO_RETIRO_CONVENIO_COLECTIVO = 13
        INAFECTO_RETIRO_PREMIO = 14
        INAFECTO_RETIRO_PUBLICIDAD = 15
        EXPORTACION_ITEM = 16
        EXONERADO_TRANSFERENCIA_GRATUITA = 17
        INAFECTO_TRANSFERENCIA_GRATUITA = 20
    
    class GuiaRemision:
        """Constants for Guía de Remisión operations."""
        
        class MotivoTraslado:
            """Constants for 'motivo_de_traslado' field."""
            VENTA = "01"
            COMPRA = "02"
            VENTA_CON_ENTREGA_TERCEROS = "03"
            TRASLADO_ENTRE_ESTABLECIMIENTOS = "04"
            CONSIGNACION = "05"
            DEVOLUCION = "06"
            RECOJO_BIENES_TRANSFORMADOS = "07"
            IMPORTACION = "08"
            EXPORTACION = "09"
            VENTA_SUJETA_CONFIRMACION = "14"
            TRASLADO_EMISOR_ITINERANTE = "18"
            OTROS = "13"
        
        class TipoTransporte:
            """Constants for 'tipo_de_transporte' field."""
            PUBLICO = "01"
            PRIVADO = "02"
        
        class DocumentoRelacionado:
            """Constants for related document types."""
            FACTURA = 1
            BOLETA = 3
            GUIA_REMITENTE = 9
            GUIA_TRANSPORTISTA = 31
        
        class UnidadMedidaPeso:
            """Constants for 'peso_bruto_unidad_de_medida' field."""
            KILOGRAMOS = "KGM"
            TONELADAS = "TNE"
        
        class SunatEnvioIndicador:
            """Constants for 'sunat_envio_indicador' field."""
            PAGADOR_FLETE_REMITENTE = "01"
            PAGADOR_FLETE_SUBCONTRATADOR = "02"
            PAGADOR_FLETE_TERCERO = "03"
            RETORNO_VEHICULO_ENVASE_VACIO = "04"
            RETORNO_VEHICULO_VACIO = "05"
            TRASLADO_VEHICULO_M1L = "06"
    
    class Percepcion:
        """Constants for Percepción operations."""
        
        class TasaPercepcion:
            """Constants for 'tipo_de_tasa_de_percepcion' field."""
            TASA_2_PORCIENTO = 1  # 2% - Percepción Venta Interna
            TASA_1_PORCIENTO = 2  # 1% - Percepción a la Adquisición de Combustible
            TASA_0_5_PORCIENTO = 3  # 0.5% - Percepción con Tasa Especial
        
        class DocumentoRelacionado:
            """Constants for 'documento_relacionado_tipo' field."""
            FACTURA = "01"
            BOLETA = "03"
            NOTA_CREDITO = "07"
            NOTA_DEBITO = "08"
    
    class Retencion:
        """Constants for Retención operations."""
        
        class TasaRetencion:
            """Constants for 'tipo_de_tasa_de_retencion' field."""
            TASA_3_PORCIENTO = 1  # 3%
            TASA_6_PORCIENTO = 2  # 6%
        
        class DocumentoRelacionado:
            """Constants for 'documento_relacionado_tipo' field."""
            FACTURA = "01"
            BOLETA = "03"
            NOTA_CREDITO = "07"
            NOTA_DEBITO = "08"
    
    class Detraccion:
        """Constants for Detracción (Withholding) operations."""
        
        class TipoDetraccion:
            """Constants for 'detraccion_tipo' field."""
            AZUCAR = 1  # Azúcar y melaza de caña
            ARROZ = 2  # Arroz
            ALCOHOL = 3  # Alcohol etílico
            RECURSOS_HIDROBIOLOGICOS = 4  # Recursos Hidrobiológicos
            MAIZ = 5  # Maíz amarillo duro
            CANA_AZUCAR = 7  # Caña de azúcar
            MADERA = 8  # Madera
            ARENA_PIEDRA = 9  # Arena y piedra
            RESIDUOS = 10  # Residuos, subproductos, desechos
            BIENES_GRAVADOS = 11  # Bienes gravados con el IGV
            INTERMEDIACION = 12  # Intermediación laboral y tercerización
            CARNES = 13  # Carnes y despojos comestibles
            ACEITE_PESCADO = 14  # Aceite de pescado
            HARINA_PESCADO = 15  # Harina, polvo y pellets de pescado
            ARRENDAMIENTO = 17  # Arrendamiento de bienes muebles
            MANTENIMIENTO = 18  # Mantenimiento y reparación de bienes muebles
            MOVIMIENTO_CARGA = 19  # Movimiento de carga
            OTROS_SERVICIOS = 20  # Otros servicios empresariales
            LECHE = 21  # Leche
            COMISION = 22  # Comisión mercantil
            FABRICACION_ENCARGO = 23  # Fabricación de bienes por encargo
            TRANSPORTE_PERSONAS = 24  # Servicio de transporte de personas
            TRANSPORTE_CARGA = 25  # Servicio de transporte de carga
            TRANSPORTE_PASAJEROS = 26  # Transporte de pasajeros
            CONSTRUCCION = 28  # Contratos de construcción
            ORO_GRAVADO = 29  # Oro gravado con el IGV
            PAPRIKA = 30  # Paprika y otros frutos
            MINERALES = 32  # Minerales metálicos no auríferos
            BIENES_EXONERADOS = 33  # Bienes exonerados del IGV
            ORO_EXONERADO = 34  # Oro y demás minerales metálicos exonerados
            SERVICIOS_GRAVADOS = 35  # Demás servicios gravados con el IGV
            MINERALES_NO_METALICOS = 37  # Minerales no metálicos
            BIEN_INMUEBLE = 38  # Bien inmueble gravado con IGV
            PLOMO = 39  # Plomo
            ANIMALES_VIVOS = 40  # Animales vivos
            ABONOS = 41  # Abonos, cueros y pieles
            LEY_30737 = 42  # Ley 30737
            BENEFICIO_MINERALES = 43  # Servicio de beneficio de minerales metálicos
            ORO_CONCENTRADOS = 44  # Minerales de oro y sus concentrados
        
        class MedioPago:
            """Constants for 'medio_de_pago_detraccion' field."""
            DEPOSITO = 1  # Depósito en cuenta
            GIRO = 2  # Giro
            TRANSFERENCIA = 3  # Transferencia de fondos
            ORDEN_PAGO = 4  # Orden de pago
            TARJETA_DEBITO = 5  # Tarjeta de débito
            TARJETA_CREDITO = 6  # Tarjeta de crédito emitida en el país
            CHEQUES = 7  # Cheques con cláusula especial
            EFECTIVO_SIN_OBLIGACION = 8  # Efectivo, sin obligación
            EFECTIVO = 9  # Efectivo, en demás casos
            COMERCIO_EXTERIOR = 10  # Medios de pago usados en comercio exterior
            DOCUMENTOS_EDPYMES = 11  # Documentos emitidos por las EDPYMES
            TARJETA_CREDITO_NO_FINANCIERA = 12  # Tarjeta de crédito emitida por empresa no financiera
            TARJETA_CREDITO_EXTRANJERA = 13  # Tarjeta de crédito emitida en el exterior
            TRANSFERENCIAS_COMERCIO_EXTERIOR = 101  # Transferencias - Comercio exterior
            CHEQUES_BANCARIOS = 102  # Cheques bancarios - Comercio exterior
            ORDEN_PAGO_SIMPLE = 103  # Orden de pago simple - Comercio exterior
            ORDEN_PAGO_DOCUMENTARIO = 104  # Orden de pago documentario - Comercio exterior
            REMESA_SIMPLE = 105  # Remesa simple - Comercio exterior
            REMESA_DOCUMENTARIA = 106  # Remesa documentaria - Comercio exterior
            CARTA_CREDITO_SIMPLE = 107  # Carta de crédito simple - Comercio exterior
            CARTA_CREDITO_DOCUMENTARIO = 108  # Carta de crédito documentario - Comercio exterior
            OTROS = 999  # Otros medios de pago
    
    class TipoIVAP:
        """Constants for 'tipo_de_ivap' field in items."""
        GRAVADO = "17"  # IVAP Gravado
        GRATUITO = "101"  # IVAP Gratuito
    
    class NotaCredito:
        """Constants for credit note operations."""
        
        class TipoNotaCredito:
            """Constants for 'tipo_de_nota_de_credito' field."""
            ANULACION_OPERACION = 1  # Anulación de la operación
            ANULACION_ERROR_RUC = 2  # Anulación por error en el RUC
            CORRECCION_DESCRIPCION = 3  # Corrección por error en la descripción
            DESCUENTO_GLOBAL = 4  # Descuento global
            DESCUENTO_ITEM = 5  # Descuento por ítem
            DEVOLUCION_TOTAL = 6  # Devolución total
            DEVOLUCION_ITEM = 7  # Devolución por ítem
            BONIFICACION = 8  # Bonificación
            DISMINUCION_VALOR = 9  # Disminución en el valor
            OTROS_CONCEPTOS = 10  # Otros conceptos
            AJUSTES_IVAP = 11  # Ajustes afectos al IVAP
            AJUSTES_EXPORTACION = 12  # Ajustes de operaciones de exportación
            AJUSTES_MONTOS_FECHAS = 13  # Ajustes - montos y/o fechas de pago
    
    class NotaDebito:
        """Constants for debit note operations."""
        
        class TipoNotaDebito:
            """Constants for 'tipo_de_nota_de_debito' field."""
            INTERESES_MORA = 1  # Intereses por mora
            AUMENTO_VALOR = 2  # Aumento de valor
            PENALIDADES = 3  # Penalidades
            AJUSTES_IVAP = 4  # Ajustes afectos al IVAP
            AJUSTES_EXPORTACION = 5  # Ajustes de operaciones de exportación
    
    @staticmethod
    def create_client(ruta: str, token: str, **kwargs) -> NubeFactClient:
        """Create a new NubeFact client instance."""
        return NubeFactClient(ruta, token, **kwargs)