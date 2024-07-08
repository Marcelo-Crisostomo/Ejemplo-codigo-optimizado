import json

def cargarClientes(archivo):
    try:
        with open(archivo, 'r') as leer:
            return json.load(leer)
    except FileNotFoundError:
        return []
    
def guardarCliente(archivo, biblioteca):
    with open(archivo, 'w') as f:
        json.dump(biblioteca, f, indent=4)

def agregarCliente(biblioteca, nombre, contacto, evento, menu, comensales):
    cliente = {
        "Nombre": nombre,
        "Contacto": contacto,
        "Tipo de evento": evento,
        "Tipo de menu": menu,
        "Cantidad de Comensales": comensales
    }
    biblioteca.append(cliente)

def mostrarCliente(biblioteca):
    for cliente in biblioteca:
        print(f"Nombre: {cliente['Nombre']}, Contacto: {cliente['Contacto']}, Tipo de evento: {cliente['Tipo de evento']}, Tipo de menu: {cliente['Tipo de menu']}, Cantidad de comensales: {cliente['Cantidad de Comensales']}\n")

def buscarPorGenero(biblioteca, menu):
    encontrados = [cliente for cliente in biblioteca if cliente['Tipo de menu'].lower() == menu.lower()]
    if encontrados:
        print(f"Clientes encontrados en el Menu '{menu}':")
        for cliente in encontrados:
            print(f"Nombre: {cliente['Nombre']}, Contacto: {cliente['Contacto']}, Tipo de evento: {cliente['Tipo de evento']}, Tipo de menu: {cliente['Tipo de menu']}, Cantidad de comensales: {cliente['Cantidad de Comensales']}\n")
    else:
        print(f"No se encontraron animes en el género '{menu}'.")

def main():
    archivo = "Clientes.json"
    biblioteca = cargarClientes(archivo)
    archivo_json = "ejemplo.json"

    while True:
        print("Menu")
        print("1 Ver Clientes")
        print("2 Agregar Clientes")
        print("3 Generar archivo de cliente")
        print("4 Buscar Clientes por Tipo de menu")
        print("5 Salir")
        
        opciones = input("Ingrese un número: ")

        if opciones == "1":
            mostrarCliente(biblioteca)
        elif opciones == "2":
            nombre = input("Nombre Completo: ")
            contacto = input("Ingrese su numero telefonico: ")
            evento = input("Tipo de evento: ")
            menu = input("Menu: ")
            comensales = input("Cantidad de comensales: ")
            agregarCliente(biblioteca, nombre, contacto, evento, menu, comensales)
            guardarCliente(archivo, biblioteca)
        elif opciones == "3":
            if biblioteca:
                cliente = biblioteca[-1] 
                # Creamos un archivo txt con la informacion detallada del cliente
                nombre_archivo_txt = f"Cliente_{cliente['Nombre'].replace(' ', '_')}.txt"
                with open(nombre_archivo_txt, "w") as archivo_txt:
                    archivo_txt.write("Detalles del Cliente:\n")
                    archivo_txt.write(f"Nombre del Cliente: {cliente['Nombre']}\n")
                    archivo_txt.write(f"Contacto:  {cliente['Contacto']}\n")
                    archivo_txt.write(f"Tipo de evento: {cliente['Tipo de evento']}\n")
                    archivo_txt.write(f"Tipo de menu: {cliente['Tipo de menu']}\n")
                    archivo_txt.write(f"Cantidad de comensales: {cliente['Cantidad de Comensales']}\n")
                print(f"Archivo de cliente generado: {nombre_archivo_txt}")

                # Creamos un archivo json
                with open(archivo_json, 'w') as archivo_json:
                    json.dump(cliente, archivo_json, indent=4)
                    print(f"Archivo JSON '{archivo_json}' creado correctamente.")
            else:
                print("No hay clientes para generar un archivo.")
        elif opciones == "4":
            menu = input("Ingrese el menu que desea buscar: ")
            buscarPorGenero(biblioteca,menu)
        elif opciones == "5":
            break
        else:
            print("Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()