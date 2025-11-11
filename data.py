CUENCA_NODES = {
    "Catedral Nueva": {"lat": -2.8975, "lon": -79.005, "descripcion": "Centro histórico de Cuenca"},
    "Parque Calderón": {"lat": -2.89741, "lon": -79.00438, "descripcion": "Corazón de Cuenca"},
    "Puente Roto": {"lat": -2.90423, "lon": -79.00142, "descripcion": "Monumento histórico"},
    "Museo Pumapungo": {"lat": -2.90607, "lon": -78.99681, "descripcion": "Museo de antropología"},
    "Terminal Terrestre": {"lat": -2.89222, "lon": -78.99277, "descripcion": "Terminal de autobuses"},
    "Mirador de Turi": {"lat": -2.92583, "lon": -79.0040, "descripcion": "Vista panorámica"},
    "Mercado 10 de Agosto": {"lat": -2.8991, "lon": -79.0025, "descripcion": "Mercado tradicional"},
    "Universidad de Cuenca": {"lat": -2.9028, "lon": -79.0211, "descripcion": "Campus universitario"},
    "Parque de la Madre": {"lat": -2.9003, "lon": -79.0117, "descripcion": "Parque recreativo"},
    "Museo Remigio Crespo": {"lat": -2.9017, "lon": -79.0093, "descripcion": "Museo cultural"}
}

GRAPH_EDGES = {
    "Catedral Nueva": ["Parque Calderón", "Puente Roto", "Mercado 10 de Agosto"],
    "Parque Calderón": ["Catedral Nueva", "Terminal Terrestre", "Puente Roto", "Mercado 10 de Agosto"],
    "Puente Roto": ["Catedral Nueva", "Parque Calderón", "Museo Pumapungo", "Mirador de Turi"],
    "Museo Pumapungo": ["Puente Roto", "Terminal Terrestre", "Museo Remigio Crespo"],
    "Terminal Terrestre": ["Parque Calderón", "Museo Pumapungo", "Mirador de Turi"],
    "Mirador de Turi": ["Puente Roto", "Terminal Terrestre"],
    "Mercado 10 de Agosto": ["Catedral Nueva", "Parque Calderón", "Parque de la Madre"],
    "Universidad de Cuenca": ["Parque de la Madre", "Museo Remigio Crespo"],
    "Parque de la Madre": ["Mercado 10 de Agosto", "Universidad de Cuenca"],
    "Museo Remigio Crespo": ["Museo Pumapungo", "Universidad de Cuenca"]
}
