# 🌱 RaspClient: Sistema IoT para Monitoreo Ambiental

![RaspClient Logo](https://via.placeholder.com/600x200?text=RaspClient)

## 📋 Índice
- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación Rápida](#instalación-rápida)
- [Configuración](#configuración)
- [Conexión con RaspServer](#conexión-con-raspserver)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Componentes Principales](#componentes-principales)
- [Solución de Problemas](#solución-de-problemas)

## 📝 Descripción

**RaspClient** es un sistema IoT basado en Raspberry Pi que monitorea condiciones ambientales (temperatura, humedad, presión, luz) y controla diferentes actuadores (ventiladores, luces, humidificadores). Se comunica mediante MQTT con un servidor central para la gestión remota.

## 📋 Requisitos

### Hardware
- Raspberry Pi (3B+ o posterior recomendado)
- Sensores: SHT3x, BMP280, GY302
- Actuadores: Relés para ventilador (GPIO 19), luz (GPIO 26), humidificador (GPIO 13), motor (GPIO 6)
- Pantalla OLED SSD1306 (I2C)

### Software
- Raspbian OS Lite (o similar)
- Python 3.7+
- Dependencias principales: paho-mqtt, RPi.GPIO, adafruit-sht31d, adafruit-bmp280, adafruit-ssd1306, Pillow, smbus

## 🛠️ Instalación Rápida

1. **Preparar la Raspberry Pi:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y git python3-pip python3-venv i2c-tools
   sudo pip3 install --upgrade setuptools
   ```

2. **Habilitar interfaces necesarias:**
   ```bash
   sudo raspi-config
   ```
   Navegar a `Interfacing Options` → Habilitar I2C y GPIO

3. **Obtener el código:**
   ```bash
   git clone https://github.com/tu-usuario/RaspClient.git
   cd RaspClient
   ```

4. **Configurar entorno virtual e instalar dependencias:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt
   ```

5. **Instalar como servicio de sistema:**
   ```bash
   sudo cp projectClient.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable projectClient.service
   sudo systemctl start projectClient.service
   ```

## ⚙️ Configuración

La configuración principal se realiza en el archivo `config/config.py`:

```python
# Wi-Fi
SSID = 'TuRedWiFi'
PASSWORD = 'TuPassword'

# Identificación única del cliente
CLIENT_ID = 'dispositivo123'  # Debe ser único para cada RaspClient

# Servidor MQTT
SERVER = '192.168.1.100'  # IP del RaspServer
```

## 🔄 Conexión con RaspServer

### Configurar la conexión al servidor

1. **Editar la configuración MQTT:**
   Ajusta la variable `SERVER` en el archivo `config/config.py` con la dirección IP del RaspServer:
   ```bash
   nano config/config.py
   ```

2. **Asegúrate que cada cliente tenga un ID único:**
   Modifica `CLIENT_ID` en `config/config.py` para que sea distinto para cada dispositivo RaspClient.

3. **Verificar la conectividad:**
   ```bash
   ping [IP-DEL-SERVIDOR]
   ```

### Flujo de comunicación

1. **Registro inicial:** 
   - Al iniciar, RaspClient se registra automáticamente enviando su ID al tópico `clients/[CLIENT_ID]/register`
   - El servidor reconoce el dispositivo y comienza a recibir datos

2. **Envío de datos:**
   - Los datos de sensores se publican periódicamente en sus tópicos correspondientes
   - Ejemplo: datos SHT3x → `clients/[CLIENT_ID]/sensor/sht3x`

3. **Recepción de comandos:**
   - RaspClient está suscrito a tópicos de control como:
     - `clients/[CLIENT_ID]/fan`
     - `clients/[CLIENT_ID]/light`
     - `clients/[CLIENT_ID]/humidifier`
     - `clients/[CLIENT_ID]/motor`

## 📁 Estructura del Proyecto

```
RaspClient/
├── boot.py               # Punto de entrada principal
├── actuators/            # Control de dispositivos
├── config/               # Configuraciones
└── sensors/              # Interfaces de sensores
```

## 🧩 Componentes Principales

### Sensores
- **SHT3x:** Temperatura y humedad (I2C: 0x44)
- **BMP280:** Presión y temperatura (I2C: 0x76)
- **GY302:** Nivel de luz (I2C: 0x23)

### Actuadores
- **Ventilador:** Control por relé (GPIO 19)
- **Luz:** Control por relé (GPIO 26)
- **Humidificador:** Control por relé (GPIO 13)
- **Motor:** Control por relé (GPIO 6)
- **Pantalla OLED:** Visualización de datos (I2C: 0x3c)

## ⚡ Gestión del Servicio

```bash
# Iniciar el servicio
sudo systemctl start projectClient.service

# Detener el servicio
sudo systemctl stop projectClient.service

# Ver estado
sudo systemctl status projectClient.service

# Ver logs
sudo journalctl -u projectClient.service -f
```

## 🚀 Ejecución Manual

Si prefieres ejecutar el sistema manualmente:

```bash
cd ~/RaspClient
source myenv/bin/activate
python boot.py
```

## ❓ Solución de Problemas

### Problemas con WiFi
- Verifica la configuración en `config/config.py`
- Comprueba que la red esté disponible: `iwlist wlan0 scan`
- Intenta conectarte manualmente: `sudo nmcli d wifi connect SSID password PASSWORD`

### Problemas con sensores
- Verifica conexiones usando `i2cdetect -y 1`
- Comprueba la alimentación de los sensores
- Verifica los logs para mensajes de error específicos

### Problemas con MQTT
- Verifica que el servidor esté en línea: `ping [IP-SERVIDOR]`
- Comprueba la conexión MQTT: `mosquitto_sub -h [IP-SERVIDOR] -t '#' -v`
- Revisa los logs: `sudo journalctl -u projectClient.service`

---

Desarrollado para monitoreo ambiental automatizado.
