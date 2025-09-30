"""
NubeFact Python Client - Peruvian electronic invoicing API integration.

This library provides a Python client for the NubeFact API, allowing you to
generate and manage electronic invoices, receipts, credit/debit notes,
and cancellations according to Peruvian SUNAT regulations.

Example usage:
    >>> from nubefact import NubeFact, ComprobanteGenerar, Item
    >>> 
    >>> # Create client with your credentials
    >>> client = NubeFact.create_client(
    ...     ruta="https://api.nubefact.com/api/v1/your-route",
    ...     token="your-token-here"
    ... )
    >>> 
    >>> # Create an invoice
    >>> comprobante = ComprobanteGenerar(
    ...     operacion="generar_comprobante",
    ...     tipo_de_comprobante=NubeFact.TipoComprobante.FACTURA,
    ...     serie="F001",
    ...     numero=1,
    ...     # ... other required fields
    ... )
    >>> 
    >>> # Send to NubeFact
    >>> response = client.generar_comprobante(comprobante)
    >>> print(f"Document created: {response.enlace}")
"""

from .client import NubeFactClient, NubeFact, NubeFactError
from .helpers import get_categories, get_options, get_constant, get_all_options
from .models import (
    ComprobanteGenerar,
    ComprobanteConsultar,
    AnulacionGenerar,
    AnulacionConsultar,
    ComprobanteRespuesta,
    AnulacionRespuesta,
    Item,
    Guia,
    VentaCredito,
    ErrorRespuesta,
    # Guía de Remisión models
    GuiaGenerar,
    GuiaConsultar,
    GuiaRespuesta,
    GuiaItem,
    DocumentoRelacionado,
    VehiculoSecundario,
    ConductorSecundario,
    # Percepción models
    PercepcionGenerar,
    PercepcionConsultar,
    PercepcionReversionGenerar,
    PercepcionReversionConsultar,
    PercepcionRespuesta,
    PercepcionItem,
    # Retención models
    RetencionGenerar,
    RetencionConsultar,
    RetencionReversionGenerar,
    RetencionReversionConsultar,
    RetencionRespuesta,
    RetencionItem,
)

__version__ = "0.3.0"
__author__ = "Quanta Solutions"
__email__ = "sumaerp@bequanta.com"

__all__ = [
    # Client classes
    "NubeFactClient",
    "NubeFact",
    "NubeFactError",
    
    # Helper functions
    "get_categories",
    "get_options", 
    "get_constant",
    "get_all_options",
    
    # Request models
    "ComprobanteGenerar",
    "ComprobanteConsultar", 
    "AnulacionGenerar",
    "AnulacionConsultar",
    "GuiaGenerar",
    "GuiaConsultar",
    "PercepcionGenerar",
    "PercepcionConsultar",
    "PercepcionReversionGenerar",
    "PercepcionReversionConsultar",
    "RetencionGenerar",
    "RetencionConsultar",
    "RetencionReversionGenerar",
    "RetencionReversionConsultar",
    
    # Response models
    "ComprobanteRespuesta",
    "AnulacionRespuesta",
    "GuiaRespuesta",
    "PercepcionRespuesta",
    "RetencionRespuesta",
    "ErrorRespuesta",
    
    # Sub-models
    "Item",
    "Guia", 
    "VentaCredito",
    "GuiaItem",
    "DocumentoRelacionado",
    "VehiculoSecundario",
    "ConductorSecundario",
    "PercepcionItem",
    "RetencionItem",
]