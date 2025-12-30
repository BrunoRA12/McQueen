McQueen: Robot de transporte de materiales

McQueen es un proyecto que consiste en la simulación de la fase de transporte de minerales en un proceso minero. Se trata de un camión transportador construido y programado utilizando el set LEGO Spike,
diseñado con el objetivo de mejorar la seguridad de los trabajadores mediante la automatización del traslado de materiales en entornos controlados. El sistema permite el manejo remoto del vehículo a través de una interfaz gráfica personalizada.

Características

Transporte eficiente: Capacidad de carga mínima de 96 cm³ y soporte para mover pesos de hasta 50 gramos.


Movilidad precisa: Capacidad para desplazarse hacia adelante, retroceder y realizar giros con exactitud.


Superación de obstáculos: Diseñado para rodear obstáculos y subir rampas con una inclinación aproximada de 4°.


Control Remoto: Interfaz gráfica de usuario (GUI) desarrollada en Python que permite operar el robot de forma inalámbrica.


Conectividad: Comunicación en tiempo real mediante Bluetooth/BLE entre el cliente (GUI) y el servidor (Hub LEGO Spike).

Instalación
Para preparar el sistema y controlar el robot McQueen, siga estos pasos:

Requisitos previos

Sistema Operativo: Windows (para la programación y ejecución de la GUI).


Hardware: Set LEGO Spike Prime y un computador con conectividad Bluetooth.


Software: Tener instalado Python y el software de LEGO Spike.

Pasos de instalación
Clonar el repositorio desde GitHub:

Clonar el repositorio.
git clone https://github.com/BrunoRA12/McQueen

cambiar directorio a la carpeta McQueen.
cd McQueen

Asegurarse de que las dependencias necesarias para la comunicación Bluetooth y la GUI estén instaladas (por ejemplo, librerías como pybricks o similares utilizadas en el proyecto).

Uso básico
Siga estos pasos para operar el robot una vez completada la instalación:

Encendido: Encienda el Hub de LEGO Spike y asegúrese de que el Bluetooth del computador esté activo.


Conexión: Ejecute el script del cliente en su PC para abrir la interfaz gráfica.


Vinculación: Utilice el botón de conexión de la GUI para buscar y vincularse al Hub del robot McQueen.


Control: Use los botones direccionales de la interfaz (adelante, atrás, izquierda, derecha) para maniobrar el robot a través de la pista.


Nota: El robot se moverá mientras mantenga presionado el botón o la tecla correspondiente y se detendrá al soltarla.
