

import os
import work_with_file
from generate_report import add_to_report as addition
from datetime import datetime


def organizar_descargas(carpeta):

    lista_dicts = []
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop")

    # os.walk recorre TODO: carpetas, subcarpetas y archivos
    for root, dirs, files in os.walk(carpeta, topdown = False):
        print(f"\n📂 Estoy mirando en: {root}\n")

        for file in files:
            ruta_origen = os.path.join(root,file)
            name, extension = os.path.splitext(file) #tupla
            type_of_file = work_with_file.see_type(extension)
            print(f"Se llama {name} , es {extension} y de tipo {type_of_file}\n")

            # 1. Determinar carpeta destino
            if type_of_file == "Image":
                # Esto arma: C:/Users/Tu/Desktop/Fotos/Images
                ruta_destino_carpeta = os.path.join(escritorio, "Fotos", "Images")
            else:
                # El resto sigue igual: C:/Users/Tu/Desktop/Tipo
                ruta_destino_carpeta = os.path.join(escritorio, type_of_file)

            os.makedirs(ruta_destino_carpeta, exist_ok=True) # Crea la carpeta si no existe

            # 2. Generar nombre con fecha
            prefix = work_with_file.see_prefix(type_of_file,name)
            timestamp = os.path.getmtime(ruta_origen)
            date = work_with_file.see_date(timestamp)
            suggested_name = work_with_file.rename(prefix,date,extension)

            # 3. Tratar repetidos
            final_name = work_with_file.unic_name(ruta_destino_carpeta,suggested_name)
            ruta_final= os.path.join(ruta_destino_carpeta,final_name)

            try:
              # 4. MOVER
              os.rename(ruta_origen, ruta_final)
              print(f"✅ Movido: Fst name:{file} -> {type_of_file} / Final: {final_name}")
            except Exception as e:
              print(f"❌ No se pudo mover {file}: {e}")

            #carguemos info
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            diccio = {
                "Date n time" : date_time,
                "Original file": name,
                "Final desktop": os.path.relpath(ruta_destino_carpeta, escritorio),
                "New file name": final_name
            }
            print(f"{diccio}\n")
            lista_dicts.append(diccio)
            print(f"{lista_dicts}\n")

        # borrando empty folders
        if root != carpeta:
           try:
                os.rmdir(root)
                print(f"🗑️ Carpeta vacía eliminada: {root}")

           except OSError:
                # Si la carpeta tiene una subcarpeta adentro, os.rmdir dará error
                # # y simplemente no la borrará. Esto es BUENO y SEGURO.
                pass

    return lista_dicts

("----------------------------------------------------------------------------------------")



ruta_prueba = os.path.join(os.path.expanduser("~"), "Desktop", "prueba")
print(f"{ruta_prueba}\n")

info = organizar_descargas(ruta_prueba)
addition(info) #carga el csv