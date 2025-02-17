# AGENDA
# el siguiente programa: guarda contactos, agrega contactos, muestra contactos, carga contactos.
# los datos se guardan en un archivo JSON

import json 

# Función para guardar los contactos en un archivo JSON
def agregar_contactos(nombre,telefono,email,agenda):
    contactos = {
        'nombre' : nombre,
        'telefono' : telefono,
        'email': email
    }
    agenda.append(contactos)
    print('contacto agregado correctamente')

# Función para guardar los contactos en un archivo JSON
def guardar_contactos(agenda,archivo):
    with open(archivo, 'w') as write:
        json.dump(agenda, write)
    print('contactos agregados perfectamente')

#funcion para mostrar los contactos desde un archivo json
    
def mostrar_contactos(agenda):
    if not agenda:
        print('la agenda está vacia')
    else:
        print('contactos en la agenda')
        for contactos in agenda:
             print(f"""
                   
                   nombre:   {contactos['nombre']},
                   teléfono: {contactos['telefono']},
                   email:    {contactos['email']}

                    """)

            
def cargar_contactos(archivo):
    try:
        with open(archivo, 'r') as read:
            agenda = json.load(read)
        print('contactos cargados')

        return agenda 
    except FileNotFoundError:
        print('el archivo no existe')
        return []

def main():
    agenda = []
    archivo = 'contactos.json'

    while True:
        print("\n1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Guardar contactos")
        print("4. Cargar contactos")
        print("5. Salir")

        opcion = input('Seleccione una opcion: ')

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            email = input("Ingrese el email del contacto: ")
            agregar_contactos(nombre,telefono,email,agenda)
        
        elif opcion == "2":
            mostrar_contactos(agenda)

        elif opcion == "3":
            guardar_contactos(agenda,archivo)

        elif opcion == "4":
            agenda = cargar_contactos(archivo)

        elif opcion == "5":
            print('Saliendo de la agenda, ¡Hasta Luego!')
            break
        
        else:
            print('Opcion Invalida, por favor seleccione otra')

if __name__ == '__main__':
    main()