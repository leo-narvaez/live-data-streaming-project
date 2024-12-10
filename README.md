# End to End - Proyecto de Subasta en Tiempo Real 
![kafka-live-stream](https://github.com/user-attachments/assets/538b6dfa-ad54-4678-a91c-886921547b85)

## 1. Crear un entorno virtual

Para crear un entorno virtual en Python, primero navega a la carpeta de tu proyecto. Luego, crea un entorno virtual con el nombre que prefieras (por ejemplo, `venv`). El entorno virtual contendrá todos los paquetes necesarios para tu proyecto y se mantendrá aislado de otros proyectos.
```bash
python3 -m venv venv
```

## 2. Activar el entorno virtual

Una vez creado el entorno virtual, debes activarlo para empezar a usarlo. La activación varía dependiendo de tu sistema operativo:


- **En Windows**, debes ejecutar el comando de activación específico para este sistema.
```bash
venv\Scripts\activate
```
- **En macOS o Linux**, la activación también tiene un comando diferente.
```bash
source venv/bin/activate
```

Cuando el entorno esté activado, verás su nombre en la línea de comandos, indicando que todo lo que instales y ejecutes será dentro de este entorno aislado.

## 3. Instalar los requerimientos

Si tu proyecto tiene un archivo que lista las dependencias necesarias (como un archivo `requirements.txt`), puedes instalar todas las bibliotecas requeridas de manera automática. Esto asegura que tu proyecto tenga todas las herramientas necesarias para funcionar correctamente.
```bash
pip install -r requirements.txt
```

## 4. Ejecutar el proyecto

Ejecutar el proyecto Flask:  
```bash
flask run
```
Ejecutar los `writers` en diferentes terminales con:
```bash
python db_writer1.py
```

```bash
python db_writer2.py
```
Para escribir el archivo `csv` en otra terminal ejecuta:
```bash
python file_writer.py
```
## 5. PowerBI
- Abre el archivo de powerbi: `dashboard-livestream.pbix`

## 6. Desactivar el entorno virtual

Cuando termines de trabajar en el proyecto, puedes desactivar el entorno virtual para salir de él. Esto te devolverá a tu entorno de Python global.
```bash
deactivate
```
