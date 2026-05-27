import os
import subprocess

# Configuramos las rutas relativas a la arquitectura
ORIGEN_UI = os.path.join('presentation', 'ui')
DESTINO_PY = os.path.join('presentation', 'ui')

def automatizar_qt():
    if not os.path.exists(DESTINO_PY):
        os.makedirs(DESTINO_PY)

    archivos_ui = [f for f in os.listdir(ORIGEN_UI) if f.endswith('.ui')]
    
    for archivo in archivos_ui:
        nombre = os.path.splitext(archivo)[0]
        input_path = os.path.join(ORIGEN_UI, archivo)
        output_path = os.path.join(DESTINO_PY, f"ui_{nombre}.py")
        
        print(f"🛠️  Generando adaptador de UI: {archivo}...")
        subprocess.run(['pyside6-uic', input_path, '-o', output_path], check=True)

if __name__ == "__main__":
    automatizar_qt()
    print("✨ Infraestructura de UI actualizada.")