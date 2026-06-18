import os
import requests
import json

def main():
    handle = os.environ.get('CF_HANDLE')
    if not handle:
        print("Error: CF_HANDLE no configurada.")
        return

    print(f"Buscando entregas para el usuario: {handle}")
    url = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count=100"
    
    try:
        response = requests.get(url).json()
    except Exception as e:
        print(f"Error al conectar con Codeforces: {e}")
        return

    if response.get("status") != "OK":
        print("Error en la respuesta de la API de Codeforces.")
        return

    submissions = response.get("result", [])
    
    for sub in submissions:
        # Solo nos interesan los problemas aceptados (OK)
        if sub.get("verdict") == "OK":
            problem = sub["problem"]
            contest_id = problem.get("contestId")
            index = problem.get("index") # Ej: 'A', 'B'
            name = problem.get("name")
            
            if not contest_id or not index:
                continue
                
            # Definir extensión básica según el lenguaje de programación
            lang = sub.get("programmingLanguage", "").lower()
            ext = "cpp"
            if "py" in lang: ext = "py"
            elif "java" in lang: ext = "java"
            elif "c#" in lang: ext = "cs"
            
            # Formatear nombre de la carpeta y archivo
            folder_name = f"Concurso_{contest_id}/{index} - {name}".replace(" ", "_")
            file_name = f"{index}.{ext}"
            
            # Crear la estructura si no existe
            os.makedirs(folder_name, exist_ok=True)
            file_path = os.path.join(folder_name, file_name)
            
            # Como la API pública estándar no da el código fuente exacto por privacidad, 
            # generamos un archivo estructurado listo para que metas tu código o lleves tu registro.
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"// Problema: {name}\n")
                    f.write(f"// Enlace: https://codeforces.com/contest/{contest_id}/problem/{index}\n")
                    f.write(f"// Lenguaje: {sub.get('programmingLanguage')}\n\n")
                    f.write("// [Inserta tu solución aquí o automatiza con un CLI local]\n")
                print(f"Añadido nuevo registro: {folder_name}")

if __name__ == "__main__":
    main()
