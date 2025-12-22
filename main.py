# main

import os
import work_with_file

def organizar_descargas(descargas):
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop") # arma la ruta
    files = os.listdir(descargas)

    for file in files:
        ruta_origen = os.path.join(descargas, file) # ruta + nombre. STRING, bien armado

        if os.path.isfile(ruta_origen):
          
          name, extension = os.path.splitext(file) #tupla
          print(extension)
          type_of_file = work_with_file.see_type(extension)
          print(type_of_file)

          # 1. Determinar carpeta destino
          ruta_destino_carpeta = os.path.join(escritorio, type_of_file)
          os.makedirs(ruta_destino_carpeta, exist_ok=True) # Crea la carpeta si no existe

          # 2. Generar nombre con fecha
          prefix = work_with_file.see_prefix(type_of_file,name)
          timestamp = os.path.getmtime(ruta_origen)
          date = work_with_file.see_date(timestamp)
          suggested_name = work_with_file.rename(prefix,date,extension)
          #os.rename(nombre,new_name)

          # 3. Tratar repetidos
          final_name = work_with_file.unic_name(ruta_destino_carpeta,suggested_name)
          ruta_final= os.path.join(ruta_destino_carpeta,final_name)

          try:
              # 4. MOVER
              os.rename(ruta_origen, ruta_final)
              print(f"✅ Movido: {file} -> {type_of_file}/{final_name}")
          except Exception as e:
              print(f"❌ No se pudo mover {file}: {e}")
          


# quiero obtener la ruta a la carpeta Descargas del usuario

home = os.path.expanduser("~") #Carpeta personal del usuario
descargas = os.path.join(home, "Downloads") #string bien armado

print(descargas)

organizar_descargas(descargas)
