# NubeFact Python Client

A Python client library for the NubeFact API - Peruvian electronic invoicing system.

## Features

- ✅ Generate electronic invoices, receipts, credit/debit notes
- ✅ Query document status and details
- ✅ Generate cancellations (anulaciones)
- ✅ Query cancellation status
- ✅ Generate Guías de Remisión (Shipping Guides)
- ✅ Query Guía de Remisión status
- ✅ Generate Percepción (Perception) documents
- ✅ Query Percepción status and generate reversions
- ✅ Generate Retención (Retention) documents
- ✅ Query Retención status and generate reversions
- ✅ Full type hints and validation with Pydantic
- ✅ Comprehensive error handling
- ✅ Support for both online and offline NubeFact versions
- ✅ Async/await support (via httpx)
- ✅ Context manager support for automatic resource cleanup

## Installation

```bash
pip install nubefact-python
```

## Quick Start

```python
from nubefact import NubeFact, ComprobanteGenerar, Item
from datetime import datetime

# Create client with your credentials
client = NubeFact.create_client(
    ruta="https://api.nubefact.com/api/v1/your-route-id",
    token="your-token-here",
)

# Create invoice items
items = [
    Item(
        unidad_de_medida="NIU",
        descripcion="Laptop Dell Inspiron 15",
        cantidad=1.0,
        valor_unitario=2500.0,
        precio_unitario=2950.0,
        subtotal=2500.0,
        tipo_de_igv=NubeFact.TipoIGV.GRAVADO_OPERACION_ONEROSA,
        igv=450.0,
        total=2950.0,
    )
]

# Create the invoice
comprobante = ComprobanteGenerar(
    operacion="generar_comprobante",
    tipo_de_comprobante=NubeFact.TipoComprobante.FACTURA,
    serie="FFF1",  # Use FFF1 for test account
    numero=1,
    sunat_transaction=NubeFact.SunatTransaction.VENTA_INTERNA,
    cliente_tipo_de_documento=NubeFact.ClienteTipoDocumento.RUC,
    cliente_numero_de_documento="20600695771",
    cliente_denominacion="EMPRESA EJEMPLO SAC",
    cliente_direccion="AV. EJEMPLO 123 - LIMA - LIMA",
    fecha_de_emision=datetime.now().strftime("%d-%m-%Y"),
    moneda=NubeFact.Moneda.SOLES,
    porcentaje_de_igv=18.0,
    total_gravada=2500.0,
    total_igv=450.0,
    total=2950.0,
    items=items,
)

# Send to NubeFact
response = client.generar_comprobante(comprobante)

print(f"Invoice created: {response.serie}-{response.numero}")
print(f"PDF link: {response.enlace_del_pdf}")
print(f"SUNAT accepted: {response.aceptada_por_sunat}")

client.close()
```

## Authentication

You need two pieces of information to use the NubeFact API:

1. **RUTA**: Your unique API endpoint URL
2. **TOKEN**: Your authentication token

You can get these from your NubeFact account under the "API Integration" section.

**Test Series for Demo Account**:
- **Factura (Invoice)**: Use series `FFF1`
- **Boleta (Receipt)**: Use series `BBB1`
- **Credit/Debit Notes**: Use same series as the original document
- **Guía de Remisión Remitente**: Use series `TTT1` (must start with 'T')
- **Guía de Remisión Transportista**: Use series `VVV1` (must start with 'V')
- **Percepción**: Use series `PPP1` (must start with 'P')
- **Retención**: Use series `RRR1` (must start with 'R')

**Important**: Numbers must be sequential within 200 of the last used number for each series.

## API Operations

### 1. Generate Documents

Create invoices, receipts, credit notes, or debit notes:

```python
from nubefact import ComprobanteGenerar

comprobante = ComprobanteGenerar(
    operacion="generar_comprobante",
    tipo_de_comprobante=NubeFact.TipoComprobante.FACTURA,  # or BOLETA, NOTA_CREDITO, NOTA_DEBITO
    serie="FFF1",  # Use FFF1 for test account
    numero=1,
    # ... other required fields
)

response = client.generar_comprobante(comprobante)
```

### 2. Query Documents

Check the status of existing documents:

```python
from nubefact import ComprobanteConsultar

consulta = ComprobanteConsultar(
    operacion="consultar_comprobante",
    tipo_de_comprobante=NubeFact.TipoComprobante.FACTURA,
    serie="FFF1",  # Use FFF1 for test account
    numero=1,
)

response = client.consultar_comprobante(consulta)
```

### 3. Generate Cancellations

Cancel existing documents:

```python
from nubefact import AnulacionGenerar

anulacion = AnulacionGenerar(
    operacion="generar_anulacion",
    tipo_de_comprobante=NubeFact.TipoComprobante.FACTURA,
    serie="FFF1",  # Use FFF1 for test account
    numero=1,
    motivo="Error en el sistema",
)

response = client.generar_anulacion(anulacion)
```

### 4. Query Cancellations

Check cancellation status:

```python
from nubefact import AnulacionConsultar

consulta = AnulacionConsultar(
    operacion="consultar_anulacion",
    tipo_de_comprobante=NubeFact.TipoComprobante.FACTURA,
    serie="FFF1",  # Use FFF1 for test account
    numero=1,
)

response = client.consultar_anulacion(consulta)
```

### 5. Generate Guía de Remisión

Create shipping guides (Guías de Remisión):

```python
from nubefact import GuiaGenerar, GuiaItem

# Create guide items
items = [
    GuiaItem(
        unidad_de_medida="NIU",
        codigo="PROD001",
        descripcion="Laptop Dell Inspiron 15",
        cantidad=1.0
    )
]

# Create Guía de Remisión Remitente
guia = GuiaGenerar(
    operacion="generar_guia",
    tipo_de_comprobante=NubeFact.TipoComprobante.GUIA_REMITENTE,
    serie="TTT1",  # Must start with 'T' for Guía Remitente
    numero=1,
    cliente_tipo_de_documento=NubeFact.ClienteTipoDocumento.RUC,
    cliente_numero_de_documento="20600695771",
    cliente_denominacion="EMPRESA DESTINATARIO SAC",
    cliente_direccion="AV. EJEMPLO 123 - LIMA",
    fecha_de_emision="23-09-2025",
    observaciones="Entrega programada",
    motivo_de_traslado=NubeFact.GuiaRemision.MotivoTraslado.VENTA,
    peso_bruto_total=5.0,
    peso_bruto_unidad_de_medida=NubeFact.GuiaRemision.UnidadMedidaPeso.KILOGRAMOS,
    numero_de_bultos=2,
    tipo_de_transporte=NubeFact.GuiaRemision.TipoTransporte.PRIVADO,
    fecha_de_inicio_de_traslado="23-09-2025",
    transportista_placa_numero="ABC444",
    conductor_documento_tipo=NubeFact.ClienteTipoDocumento.DNI,  # DNI
    conductor_documento_numero="12345678",
    conductor_nombre="JORGE",
    conductor_apellidos="LOPEZ",
    conductor_numero_licencia="Q87654321",
    punto_de_partida_ubigeo="150101",
    punto_de_partida_direccion="AV. PARTIDA 456 - LIMA",
    punto_de_llegada_ubigeo="150203",
    punto_de_llegada_direccion="CALLE LLEGADA 789 - MIRAFLORES",
    items=items
)

response = client.generar_guia(guia)
```

### 6. Query Guía de Remisión

Check Guía de Remisión status:

```python
from nubefact import GuiaConsultar

consulta = GuiaConsultar(
    operacion="consultar_guia",
    tipo_de_comprobante=NubeFact.TipoComprobante.GUIA_REMITENTE,
    serie="TTT1",  # Use TTT1 for test account
    numero=1,
)

response = client.consultar_guia(consulta)
```

### 7. Generate Percepción

Create Percepción (Perception) documents:

```python
from nubefact import PercepcionGenerar, PercepcionItem

# Create Percepción items (related documents)
items = [
    PercepcionItem(
        documento_relacionado_tipo=NubeFact.DocRelacionadoTipo.FACTURA,  # "01"
        documento_relacionado_serie="F001",
        documento_relacionado_numero=1,
        documento_relacionado_fecha_de_emision="26-10-2021",
        documento_relacionado_moneda=NubeFact.Moneda.SOLES,
        documento_relacionado_total=1000.00,
        cobro_fecha="26-10-2021",
        cobro_numero=1,
        cobro_total_sin_percepcion=1000.00,
        tipo_de_cambio=3.421,
        tipo_de_cambio_fecha="26-10-2021",
        importe_percibido=20.00,  # 2% of 1000
        importe_percibido_fecha="26-10-2021",
        importe_cobrado_con_percepcion=1020.00
    )
]

# Create Percepción document
percepcion = PercepcionGenerar(
    operacion="generar_percepcion",
    serie="PPP1",  # Must start with 'P'
    numero=1,
    cliente_tipo_de_documento=NubeFact.ClienteTipoDocumento.RUC,  # Must be RUC
    cliente_numero_de_documento="20131312955",
    cliente_denominacion="SUNAT",
    cliente_direccion="LIMA",
    fecha_de_emision="26-10-2021",
    moneda=NubeFact.Moneda.SOLES,  # Must be Soles
    tipo_de_tasa_de_percepcion=NubeFact.PercepcionTasa.PORCIENTO_2,  # 2%
    total_percibido=20.00,
    total_cobrado=1020.00,
    items=items
)

response = client.generar_percepcion(percepcion)
```

### 8. Query Percepción

Check Percepción status:

```python
from nubefact import PercepcionConsultar

consulta = PercepcionConsultar(
    operacion="consultar_percepcion",
    serie="PPP1",
    numero=1
)

response = client.consultar_percepcion(consulta)
```

### 9. Generate Percepción Reversion

Reverse a Percepción document:

```python
from nubefact import PercepcionReversionGenerar

reversion = PercepcionReversionGenerar(
    operacion="generar_reversion_percepcion",
    serie="PPP1",
    numero=1
)

response = client.generar_reversion_percepcion(reversion)
```

### 10. Query Percepción Reversion

Check Percepción reversion status:

```python
from nubefact import PercepcionReversionConsultar

consulta = PercepcionReversionConsultar(
    operacion="consultar_reversion_percepcion",
    serie="PPP1",
    numero=1,
    motivo="Error en datos"
)

response = client.consultar_reversion_percepcion(consulta)
```

### 11. Generate Retención

Create Retención (Retention) documents:

```python
from nubefact import RetencionGenerar, RetencionItem

# Create Retención items (related documents)
items = [
    RetencionItem(
        documento_relacionado_tipo=NubeFact.DocRelacionadoTipo.FACTURA,  # "01"
        documento_relacionado_serie="F001",
        documento_relacionado_numero=1,
        documento_relacionado_fecha_de_emision="26-10-2021",
        documento_relacionado_moneda=NubeFact.Moneda.SOLES,
        documento_relacionado_total=1000.00,
        pago_fecha="26-10-2021",
        pago_numero=1,
        pago_total_sin_retencion=1000.00,
        tipo_de_cambio=3.421,
        tipo_de_cambio_fecha="26-10-2021",
        importe_retenido=30.00,  # 3% of 1000
        importe_retenido_fecha="26-10-2021",
        importe_pagado_con_retencion=970.00
    )
]

# Create Retención document
retencion = RetencionGenerar(
    operacion="generar_retencion",
    serie="RRR1",  # Must start with 'R'
    numero=1,
    cliente_tipo_de_documento=NubeFact.ClienteTipoDocumento.RUC,  # Must be RUC
    cliente_numero_de_documento="20131312955",
    cliente_denominacion="SUNAT",
    cliente_direccion="LIMA",
    fecha_de_emision="26-10-2021",
    moneda=NubeFact.Moneda.SOLES,  # Must be Soles
    tipo_de_tasa_de_retencion=NubeFact.RetencionTasa.PORCIENTO_3,  # 3%
    total_retenido=30.00,
    total_pagado=970.00,
    items=items
)

response = client.generar_retencion(retencion)
```

### 12. Query Retención

Check Retención status:

```python
from nubefact import RetencionConsultar

consulta = RetencionConsultar(
    operacion="consultar_retencion",
    serie="RRR1",
    numero=1
)

response = client.consultar_retencion(consulta)
```

### 13. Generate Retención Reversion

Reverse a Retención document:

```python
from nubefact import RetencionReversionGenerar

reversion = RetencionReversionGenerar(
    operacion="generar_reversion_retencion",
    serie="RRR1",
    numero=1,
    motivo="Error en datos"
)

response = client.generar_reversion_retencion(reversion)
```

### 14. Query Retención Reversion

Check Retención reversion status:

```python
from nubefact import RetencionReversionConsultar

consulta = RetencionReversionConsultar(
    operacion="consultar_reversion_retencion",
    serie="RRR1",
    numero=1
)

response = client.consultar_reversion_retencion(consulta)
```

## Data Models

### Document Types

```python
NubeFact.TipoComprobante.FACTURA        # 1 - Invoice
NubeFact.TipoComprobante.BOLETA         # 2 - Receipt
NubeFact.TipoComprobante.NOTA_CREDITO   # 3 - Credit Note
NubeFact.TipoComprobante.NOTA_DEBITO    # 4 - Debit Note
NubeFact.TipoComprobante.GUIA_REMITENTE      # 7 - Guía de Remisión Remitente
NubeFact.TipoComprobante.GUIA_TRANSPORTISTA  # 8 - Guía de Remisión Transportista
```

### SUNAT Transaction Types

```python
NubeFact.SunatTransaction.VENTA_INTERNA                 # 1 - Internal sale
NubeFact.SunatTransaction.EXPORTACION                   # 2 - Export
NubeFact.SunatTransaction.VENTA_INTERNA_ANTICIPOS       # 4 - Internal sale with advances
NubeFact.SunatTransaction.VENTA_NO_DOMICILIADOS         # 29 - Non-resident sales
NubeFact.SunatTransaction.DETRACCION                    # 30 - Withholding
NubeFact.SunatTransaction.PERCEPCION                    # 34 - Perception
```

### Percepción and Retención Constants

```python
# Percepción Rates
NubeFact.PercepcionTasa.PORCIENTO_2    # 1 - 2% (Percepción Venta Interna)
NubeFact.PercepcionTasa.PORCIENTO_1    # 2 - 1% (Percepción Combustible)
NubeFact.PercepcionTasa.PORCIENTO_0_5  # 3 - 0.5% (Tasa Especial)

# Retención Rates
NubeFact.RetencionTasa.PORCIENTO_3     # 1 - 3%
NubeFact.RetencionTasa.PORCIENTO_6     # 2 - 6%

# Related Document Types for Percepción/Retención
NubeFact.DocRelacionadoTipo.FACTURA    # "01" - Invoice
NubeFact.DocRelacionadoTipo.BOLETA     # "03" - Receipt
NubeFact.DocRelacionadoTipo.NOTA_CREDITO  # "07" - Credit Note
NubeFact.DocRelacionadoTipo.NOTA_DEBITO   # "08" - Debit Note
```

### Client Document Types

```python
NubeFact.ClienteTipoDocumento.RUC          # 6 - RUC
NubeFact.ClienteTipoDocumento.DNI          # 1 - DNI
NubeFact.ClienteTipoDocumento.VARIOS       # 0 - Various (minor sales)
NubeFact.ClienteTipoDocumento.CARNET_EXTRANJERIA  # 4 - Foreigner ID
NubeFact.ClienteTipoDocumento.PASAPORTE    # 7 - Passport
```

### Currencies

```python
NubeFact.Moneda.SOLES            # 1 - Peruvian Soles
NubeFact.Moneda.DOLARES          # 2 - US Dollars
NubeFact.Moneda.EUROS            # 3 - Euros
NubeFact.Moneda.LIBRA_ESTERLINA  # 4 - British Pounds
```

### IGV Types (for items)

```python
NubeFact.TipoIGV.GRAVADO_OPERACION_ONEROSA    # 1 - Taxable operation
NubeFact.TipoIGV.EXONERADO_OPERACION_ONEROSA  # 8 - Exempt operation
NubeFact.TipoIGV.INAFECTO_OPERACION_ONEROSA   # 9 - Non-taxable operation
NubeFact.TipoIGV.EXPORTACION_ITEM             # 16 - Export
```

### Guía de Remisión Constants

```python
# Transfer Reasons
NubeFact.GuiaRemision.MotivoTraslado.VENTA                           # "01" - Sale
NubeFact.GuiaRemision.MotivoTraslado.COMPRA                          # "02" - Purchase
NubeFact.GuiaRemision.MotivoTraslado.VENTA_CON_ENTREGA_TERCEROS      # "03" - Sale with third-party delivery
NubeFact.GuiaRemision.MotivoTraslado.TRASLADO_ENTRE_ESTABLECIMIENTOS # "04" - Transfer between establishments
NubeFact.GuiaRemision.MotivoTraslado.CONSIGNACION                    # "05" - Consignment
NubeFact.GuiaRemision.MotivoTraslado.DEVOLUCION                      # "06" - Return
NubeFact.GuiaRemision.MotivoTraslado.OTROS                           # "13" - Others

# Transport Types
NubeFact.GuiaRemision.TipoTransporte.PUBLICO    # "01" - Public transport
NubeFact.GuiaRemision.TipoTransporte.PRIVADO    # "02" - Private transport

# Weight Units
NubeFact.GuiaRemision.UnidadMedidaPeso.KILOGRAMOS     # "KGM" - Kilograms
NubeFact.GuiaRemision.UnidadMedidaPeso.TONELADAS      # "TNE" - Tons

# Related Document Types
NubeFact.GuiaRemision.DocumentoRelacionado.FACTURA           # 1 - Invoice
NubeFact.GuiaRemision.DocumentoRelacionado.BOLETA            # 3 - Receipt
NubeFact.GuiaRemision.DocumentoRelacionado.GUIA_REMITENTE    # 9 - Guía Remitente
NubeFact.GuiaRemision.DocumentoRelacionado.GUIA_TRANSPORTISTA # 31 - Guía Transportista
```

## Helper Methods for UI Integration

The library provides helper methods to get lists of available options for UI selects and convert user selections back to API constants.

### Get Available Categories

```python
from nubefact import get_categories

categories = get_categories()
print(categories)
# ['tipo_de_comprobante', 'sunat_transaction', 'cliente_tipo_de_documento', 'moneda', 'tipo_de_igv', ...]
```

### Get Options for a Category

```python
from nubefact import get_options

# Get text options for UI selects
options = get_options('tipo_de_comprobante')
print(options)
# ['FACTURA', 'BOLETA', 'NOTA DE CRÉDITO', 'NOTA DE DÉBITO', 'GUÍA DE REMISIÓN REMITENTE', 'GUÍA DE REMISIÓN TRANSPORTISTA']

# Get options for other categories
moneda_options = get_options('moneda')
# ['SOLES', 'DÓLARES', 'EUROS', 'LIBRA ESTERLINA']

igv_options = get_options('tipo_de_igv')
# ['GRAVADO - OPERACIÓN ONEROSA', 'GRAVADO – RETIRO POR PREMIO', ...]
```

### Convert Text to Constant

```python
from nubefact import get_constant

# Convert user selection back to API constant
constant = get_constant('tipo_de_comprobante', 'FACTURA')
print(constant)  # 1

# Use the constant in your document
comprobante = ComprobanteGenerar(
    tipo_de_comprobante=constant,
    # ... other fields
)
```

### Get All Options as Dictionary

```python
from nubefact import get_all_options

all_options = get_all_options()
print(all_options['moneda'])  # ['SOLES', 'DÓLARES', 'EUROS', 'LIBRA ESTERLINA']
print(all_options['cliente_tipo_de_documento'])  # ['RUC - REGISTRO ÚNICO DE CONTRIBUYENTE', 'DNI - DOC. NACIONAL DE IDENTIDAD', ...]
```

### Available Categories

The helper methods support 18 different categories:

- `tipo_de_comprobante` - Document types
- `sunat_transaction` - SUNAT transaction types
- `cliente_tipo_de_documento` - Client document types
- `moneda` - Currencies
- `tipo_de_igv` - IGV tax types
- `percepcion_tipo` - Perception types
- `retencion_tipo` - Retention types
- `tipo_de_nota_de_credito` - Credit note types
- `tipo_de_nota_de_debito` - Debit note types
- `motivo_de_traslado` - Shipping reasons
- `peso_bruto_unidad_de_medida` - Weight units
- `tipo_de_transporte` - Transport types
- `sunat_envio_indicador` - Shipping indicators
- `tipo_de_tasa_de_percepcion` - Perception rates
- `documento_relacionado_tipo` - Related document types
- `tipo_de_tasa_de_retencion` - Retention rates
- `documento_relacionado_tipo_guia` - Guide related document types

## Error Handling

The library raises `NubeFactError` exceptions for API errors:

```python
from nubefact import NubeFactError

try:
    response = client.generar_comprobante(comprobante)
except NubeFactError as e:
    print(f"Error {e.code}: {e.message}")
```

Common error codes:
- `10`: Authentication failed
- `11`: Invalid route/URL
- `20`: Invalid file format
- `21`: Operation failed
- `24`: Document not found

## Using Context Manager

The client supports context manager usage for automatic cleanup:

```python
with NubeFact.create_client(ruta, token) as client:
    response = client.generar_comprobante(comprobante)
    # Client automatically closed when exiting the context
```

## Examples

See the `examples/` directory for complete working examples:

- `basic_usage.py` - Basic invoice creation and queries
- `advanced_usage.py` - Credit notes, cancellations, export invoices
- `guia_remision.py` - Guía de Remisión (Shipping Guide) creation and queries
- `percepcion_retencion.py` - Percepción and Retención document creation and queries

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/nubefact-python.git
cd nubefact-python

# Install dependencies
pip install -e .[dev]

# Run tests
pytest

# Run linters
black .
ruff .
mypy .
```

### Project Structure

```
nubefact-python/
├── nubefact/                 # Package source
│   ├── __init__.py          # Package exports
│   ├── client.py            # Main client class
│   └── models.py            # Data models
├── tests/                   # Test suite
│   └── test_nubefact.py
├── examples/                # Usage examples
│   ├── basic_usage.py
│   └── advanced_usage.py
├── pyproject.toml          # Project configuration
└── README.md
```

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Create an issue on GitHub
- Contact NubeFact support for API-related questions

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for your changes
4. Submit a pull request

## Changelog

### v0.3.0
- Added Percepción (Perception) document support
- Added Retención (Retention) document support
- Support for all 4 Percepción operations (generate, query, reversion)
- Support for all 4 Retención operations (generate, query, reversion)
- New models: PercepcionGenerar, PercepcionItem, RetencionGenerar, RetencionItem, etc.
- Complete examples and documentation for Percepción and Retención

### v0.2.0
- Added Guía de Remisión (Shipping Guide) support
- Support for both Guía Remitente and Guía Transportista
- New models: GuiaGenerar, GuiaConsultar, GuiaItem, DocumentoRelacionado, etc.
- Complete examples and documentation for shipping guides

### v0.1.0
- Initial release
- Support for all 4 main API operations
- Comprehensive data models with validation
- Error handling and type hints
- Examples and documentation