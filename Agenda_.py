# ---------------------------------------------
# Clase Contacto
# Representa a UNA persona en la agenda
# ---------------------------------------------
class Contacto:
    def __init__(self, nombre, telefono1, telefono2, mail):
        """
        Constructor de la clase Contacto.
        'self' es la referencia al propio objeto.
        Guardamos los datos como atributos del objeto.
        """
        self.nombre = nombre
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.mail = mail

    def __str__(self):
        """
        Método especial que define CÓMO se mostrará el contacto
        cuando hagamos print(contacto) o str(contacto).

        Si no tuviéramos este método, Python mostraría algo como:
        <__main__.Contacto object at 0x0000...>

        Con __str__, devolvemos un texto amigable para humanos.
        """
        return (
            f"Nombre   : {self.nombre}\n"
            f"Teléfono1: {self.telefono1}\n"
            f"Teléfono2: {self.telefono2}\n"
            f"Mail     : {self.mail}"
        )


# ---------------------------------------------
# Clase Agenda
# Representa la agenda COMPLETA (lista de contactos)
# ---------------------------------------------
class Agenda:
    def __init__(self):
        """
        Constructor de la Agenda.
        Creamos una lista vacía donde guardaremos objetos Contacto.
        """
        self.contactos = []

    def agregar_contacto(self, contacto):
        """
        Agrega un objeto Contacto a la lista de contactos.
        """
        self.contactos.append(contacto)
        print("✔ Contacto agregado.\n")

    def buscar_por_nombre(self, nombre):
        """
        Busca un contacto por nombre.
        Recorre la lista de contactos y compara el nombre (case insensitive).

        Si lo encuentra, devuelve el objeto Contacto.
        Si no lo encuentra, devuelve None.
        """
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                return c
        return None

    def mostrar_contacto(self, nombre):
        """
        Muestra por pantalla la información del contacto con ese nombre.
        Internamente usa buscar_por_nombre.
        """
        contacto = self.buscar_por_nombre(nombre)
        if contacto:
            print("📇 Información del contacto:")
            # Gracias a __str__ se imprime bonito
            print(contacto)
        else:
            print("⚠ Contacto no encontrado.\n")

    def eliminar_contacto(self, nombre):
        """
        Elimina de la agenda el contacto con ese nombre, si existe.
        """
        contacto = self.buscar_por_nombre(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print("🗑 Contacto eliminado.\n")
        else:
            print("⚠ Contacto no encontrado.\n")


# ---------------------------------------------
# Función principal (main)
# Controla el menú y la interacción con el usuario
# ---------------------------------------------
def main():
    # Creamos una Agenda vacía
    agenda = Agenda()

    # Bucle principal del programa
    while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Mostrar información de un contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        # Opción 1: crear un nuevo contacto y agregarlo a la agenda
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono1 = input("Teléfono 1: ")
            telefono2 = input("Teléfono 2: ")
            mail = input("Mail: ")

            # Creamos el objeto Contacto con los datos ingresados
            nuevo = Contacto(nombre, telefono1, telefono2, mail)

            # Lo agregamos a la agenda
            agenda.agregar_contacto(nuevo)

        # Opción 2: buscar contacto y mostrarlo si existe
        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ")
            contacto = agenda.buscar_por_nombre(nombre)
            if contacto:
                print("✅ Contacto encontrado:")
                print(contacto)  # usa __str__
            else:
                print("⚠ Contacto no encontrado.")

        # Opción 3: mostrar info de un contacto usando el método de Agenda
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a mostrar: ")
            agenda.mostrar_contacto(nombre)

        # Opción 4: eliminar un contacto por nombre
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)

        # Opción 5: salir del programa
        elif opcion == "5":
            print("Saliendo de la agenda...")
            break

        # Cualquier otra opción no es válida
        else:
            print("Opción no válida, intente nuevamente.")


# ---------------------------------------------
# Punto de entrada del programa
# Solo se ejecuta main() si el archivo se corre directamente
# y NO cuando se importa como módulo desde otro archivo.
# ---------------------------------------------
if __name__ == "__main__":
    main()


