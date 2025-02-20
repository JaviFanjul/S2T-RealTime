import sys
audiopath = sys.argv[1]
chunkpath = "../audiochunks_volume"
chunk_length_ms = 5000
logpath  ="../audiotranscription_volume/audio_transcription.log"

prompt_inicial = (
    "Esta es una conversación telefónica entre un cliente y un teleoperador de una compañía de servicios móviles. "
    "El cliente hace preguntas sobre su factura, planes de datos y problemas técnicos con la red. "
    "El teleoperador responde de manera educada y profesional, proporcionando información y soluciones. "
    "La conversación incluye términos como factura, plan de datos, cobertura, servicio al cliente y soporte técnico. "
    "Términos frecuentes en la conversación:\n"
    "factura, cargo extra, saldo, megas, gigas, datos móviles, roaming, cobertura, señal, "
    "llamadas internacionales, plan prepago, plan pospago, cambio de plan, descuento, promoción, "
    "atención al cliente, servicio técnico, soporte, renovación de contrato, número de teléfono, "
    "código de verificación, tarjeta SIM, activación, suspensión de línea.\n"

    "Historial de la conversación previa:\n"
)

whisper_model = "small"