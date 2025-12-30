from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
import uselect
import usys

# 1. Configuración de Hardware
hub = PrimeHub()
motor_l = Motor(Port.D)
motor_r = Motor(Port.B)
dist_sensor = UltrasonicSensor(Port.E)

# 2. SEÑAL DE INICIO (Sonido y Display)
# Mostramos la 'M' de "Motor" o "Maestro"
hub.display.char('M')

# Melodía característica de encendido (Frecuencia en Hz, Duración en ms)
hub.speaker.beep(frequency=440, duration=100) # Nota La
wait(50)
hub.speaker.beep(frequency=880, duration=200) # Nota La (octava superior)

# 3. Configuración de comunicación
poll = uselect.poll()
poll.register(usys.stdin, uselect.POLLIN)

hub.light.on(Color.BLUE) # Azul para indicar "Modo Servidor Activo"
print("Servidor M iniciado y listo")

while True:
    # Aseguramos que la 'M' se mantenga (por si otra función la borra)
    hub.display.char('M')

    # --- Lógica de Seguridad (Autónoma) ---
    distancia = dist_sensor.distance()
    
    if distancia < 150:
        motor_l.stop()
        motor_r.stop()
        hub.light.on(Color.RED) # Rojo si hay peligro
    else:
        hub.light.on(Color.BLUE) # Azul si está despejado

    # --- Escucha de comandos (Cliente PC) ---
    if poll.poll(10):
        # Solo procesamos si no hay un objeto demasiado cerca
        cmd = usys.stdin.read(1)
        
        if distancia >= 150:
            if cmd == 'F':
                motor_l.run(800); motor_r.run(-800)
            elif cmd == 'B':
                motor_l.run(-800); motor_r.run(800)
            elif cmd == 'L':
                motor_l.run(-500); motor_r.run(-500)
            elif cmd == 'R':
                motor_l.run(500); motor_r.run(500)
            elif cmd == 'S':
                motor_l.stop(); motor_r.stop()
        else:
            # Si intentas moverte y hay obstáculo, hace un pequeño pitido de error
            hub.speaker.beep(frequency=100, duration=50)
            
    wait(20)