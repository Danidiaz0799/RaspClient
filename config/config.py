# Configuracion de la red Wi-Fi
SSID = 'Stev7'
PASSWORD = 'hola12345'

CLIENT_ID = 'mushroom123'  # Identificador único del cliente

SERVER = 'raspserver.local'  # IP del servidor MQTT (Raspberry Pi)

# Nuevos tópicos basados en el ID de cliente
TOPIC_PREFIX = f'clients/{CLIENT_ID}/'
TOPIC_REGISTER = f'{TOPIC_PREFIX}register'
TOPIC_FAN = f'{TOPIC_PREFIX}fan'
TOPIC_LIGHT = f'{TOPIC_PREFIX}light'
TOPIC_HUMIDIFIER = f'{TOPIC_PREFIX}humidifier'
TOPIC_MOTOR = f'{TOPIC_PREFIX}motor'
TOPIC_SHT3X = f'{TOPIC_PREFIX}sensor/sht3x'