import json

def cargar_clientes(archivo):
    """Carga los datos de los clientes desde un archivo JSON."""
    try:
        with open(archivo, 'r') as leer:
            return json.load(leer)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON.")
        return []

def guardar_clientes(archivo, biblioteca):
    """Guarda los datos de los clientes en un archivo JSON."""
    try:
        with open(archivo, 'w') as f:
            json.dump(biblioteca, f, indent=4)
    except IOError:
        print("Error al guardar los datos en el archivo.")

def agregar_cliente(biblioteca, nombre, contacto, evento, menu, comensales):
    """Agrega un nuevo cliente a la biblioteca."""
    cliente = {
        "Nombre": nombre,
        "Contacto": contacto,
        "Tipo de evento": evento,
        "Tipo de menú": menu,
        "Cantidad de Comensales": comensales
    }
    biblioteca.append(cliente)

def mostrar_clientes(biblioteca):
    """Muestra los datos de todos los clientes en la biblioteca."""
    for cliente in biblioteca:
        print(f"Nombre: {cliente['Nombre']}, Contacto: {cliente['Contacto']}, Tipo de evento: {cliente['Tipo de evento']}, Tipo de menú: {cliente['Tipo de menú']}, Cantidad de comensales: {cliente['Cantidad de Comensales']}\n")

def buscar_por_menu(biblioteca, menu):
    """Busca clientes por tipo de menú y los muestra."""
    encontrados = [cliente for cliente in biblioteca if cliente['Tipo de menú'].lower() == menu.lower()]
    if encontrados:
        print(f"Clientes encontrados en el menú '{menu}':")
        for cliente in encontrados:
            print(f"Nombre: {cliente['Nombre']}, Contacto: {cliente['Contacto']}, Tipo de evento: {cliente['Tipo de evento']}, Tipo de menú: {cliente['Tipo de menú']}, Cantidad de comensales: {cliente['Cantidad de Comensales']}\n")
    else:
        print(f"No se encontraron clientes en el menú '{menu}'.")

def obtener_dato_valido(mensaje, tipo_dato=str, validacion=None, mensaje_error="Dato inválido."):
    """Obtiene un dato válido del usuario."""
    while True:
        dato = input(mensaje)
        try:
            dato = tipo_dato(dato)
            if validacion and not validacion(dato):
                raise ValueError()
            return dato
        except ValueError:
            print(mensaje_error)

def main():
    archivo = "Clientes.json"
    biblioteca = cargar_clientes(archivo)
    archivo_json = "ejemplo.json"

    while True:
        print("Menú")
        print("1 Ver Clientes")
        print("2 Agregar Clientes")
        print("3 Generar archivo de cliente")
        print("4 Buscar Clientes por Tipo de menú")
        print("5 Salir")
        
        opcion = input("Ingrese un número: ")

        if opcion == "1":
            mostrar_clientes(biblioteca)
        elif opcion == "2":
            nombre = obtener_dato_valido("Nombre Completo: ", str, lambda x: len(x) > 0, "El nombre no puede estar vacío.")
            contacto = obtener_dato_valido("Ingrese su número telefónico: ", str, lambda x: x.isdigit(), "El contacto debe ser solo números.")
            evento = obtener_dato_valido("Tipo de evento: ")
            menu = obtener_dato_valido("Menú: ")
            comensales = obtener_dato_valido("Cantidad de comensales: ", int, lambda x: x > 0, "La cantidad de comensales debe ser un número positivo.")
            agregar_cliente(biblioteca, nombre, contacto, evento, menu, comensales)
            guardar_clientes(archivo, biblioteca)
        elif opcion == "3":
            if biblioteca:
                cliente = biblioteca[-1] 
                nombre_archivo_txt = f"Cliente_{cliente['Nombre'].replace(' ', '_')}.txt"
                try:
                    with open(nombre_archivo_txt, "w") as archivo_txt:
                        archivo_txt.write("Detalles del Cliente:\n")
                        archivo_txt.write(f"Nombre del Cliente: {cliente['Nombre']}\n")
                        archivo_txt.write(f"Contacto: {cliente['Contacto']}\n")
                        archivo_txt.write(f"Tipo de evento: {cliente['Tipo de evento']}\n")
                        archivo_txt.write(f"Tipo de menú: {cliente['Tipo de menú']}\n")
                        archivo_txt.write(f"Cantidad de comensales: {cliente['Cantidad de Comensales']}\n")
                    print(f"Archivo de cliente generado: {nombre_archivo_txt}")

                    with open(archivo_json, 'w') as archivo_json:
                        json.dump(cliente, archivo_json, indent=4)
                        print(f"Archivo JSON '{archivo_json}' creado correctamente.")
                except IOError:
                    print("Error al generar el archivo de cliente.")
            else:
                print("No hay clientes para generar un archivo.")
        elif opcion == "4":
            menu = obtener_dato_valido("Ingrese el menú que desea buscar: ")
            buscar_por_menu(biblioteca, menu)
        elif opcion == "5":
            break
        else:
            print("Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
