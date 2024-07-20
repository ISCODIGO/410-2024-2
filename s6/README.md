# Semana 6

## Cap. 12: Network
- **webserver**: `server.py` es un servidor web simple.
- **request**: Diversos programas que permiten extraer datos a través del protocolo TCP/IP utilizando sockets, y a través del protocolo HTTP utilizando URLLib.
- **chat**: aplicación para usar sockets e intercambiar mensajes entre el cliente y el servidor. El servidor es un programa que está esperando "escuchar" a un cliente que se conecte a un puerto definido.


## Virtual Environment

### Creación de Virtual Environment
Para crear un entorno virtual, utiliza el siguiente comando:
```sh
python -m venv .venv
```
Este comando crea una carpeta denominada `.venv`, aunque puedes nombrarla de cualquier otra forma. Dentro de este directorio se almacenarán los paquetes de terceros instalados.

### Activación
Para usar el entorno virtual, es necesario activarlo. Los comandos para activarlo varían según el sistema operativo:

- **Windows**:
```sh
.venv\Scripts\activate.bat
```
  O si estás usando PowerShell:
```sh
.venv\Scripts\Activate.ps1
```

- **macOS y Linux**:
```sh
source .venv/bin/activate
```

Activar el entorno virtual permite instalar y usar paquetes en el entorno aislado, sin afectar la instalación global de Python.

### Desactivación
Para desactivar el entorno virtual y volver al entorno global de Python, usa el siguiente comando:
```sh
deactivate
```

### Instalación de Paquetes
Una vez que el entorno virtual esté activado, puedes instalar paquetes usando `pip`:
```sh
pip install nombre_del_paquete
```

### Almacenar dependencias
Para guardar las dependencias en un archivo `requirements.txt`, ejecuta:
```sh
pip freeze > requirements.txt
```

### Cargar Dependencias
Para instalar todas las dependencias listadas en un archivo `requirements.txt`:
```sh
pip install -r requirements.txt
```
