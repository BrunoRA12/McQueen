from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
import uselect
import usys

# Configuración de Hardware
hub = PrimeHub()
motor_l = Motor(Port.D)
motor_r = Motor(Port.B)
dist_sensor = UltrasonicSensor(Port.E) # Sensor de distancia

# Configuración de comunicación
poll = uselect.poll()
poll.register(usys.stdin, uselect.POLLIN)

hub.light.on(Color.GREEN) # Luz verde = Listo y Autónomo
print("Servidor Autónomo Iniciado")

while True:
    # --- PARTE 1: Lógica Autónoma (Prioridad Alta) ---
    # Si detecta algo a menos de 15cm, se detiene por seguridad
    if dist_sensor.distance() < 150:
        motor_l.stop()
        motor_r.stop()
        hub.light.on(Color.RED) # Alerta visual
    else:
        hub.light.on(Color.GREEN)

    # --- PARTE 2: Escucha de comandos del Cliente (PC) ---
    # Revisamos si hay órdenes externas, pero solo si el camino está despejado
    if poll.poll(10) and dist_sensor.distance() >= 150:
        cmd = usys.stdin.read(1)
        
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
            
    wait(20) # Pequeña pausa para no saturar el procesador