
from datetime import datetime
import os

def see_type(extension):
    # Definimos el mapeo de extensiones a categorías
    formatos = {
        ".txt": "Text", ".md": "Text",
        ".jar": "Java",
        ".png": "Image", ".jpg": "Image", ".jpeg": "Image", ".webp": "Image", ".jfif": "Image",
        ".exe": "Executable", ".lnk": "Executable",
        ".pdf": "PDF",
        ".bmp": "basura"
    }
    # .get() busca la extensión, si no la encuentra devuelve "Indetermined"
    return formatos.get(extension.lower(), "Undetermined")


def see_date(timestamp):
    fecha_ini = datetime.fromtimestamp(timestamp)
    fecha_lista = fecha_ini.strftime("%d-%m-%y")
    return fecha_lista

def see_prefix(type_of_file,name):
    prefix_ini = name.split("-")[0]

    if type_of_file == "Text":
        prefix = "text_" 
    elif type_of_file == "Java":
        prefix = "java_"
    elif type_of_file == "Image":
        prefix = "image_"
    elif (type_of_file == "Executable") or (type_of_file == "PDF"):
        prefix = prefix_ini+"_"
    else:
        prefix = "no_type_"
    return prefix

def unic_name(folder, name):
    base, extension = os.path.splitext(name)
    counter = 1
    new_name = name
    while os.path.exists(os.path.join(folder,new_name)):
        new_name= f"{base}_{counter}{extension}"
        counter += 1
    return new_name


def rename(prefix,date,extension):
    new_name = prefix + str(date) + extension
    return new_name
