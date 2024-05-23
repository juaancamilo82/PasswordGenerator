import random
import string
import os
import pyperclip

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += '!@$*().,?'

    if not characters:
        raise ValueError("Debe seleccionar al menos un tipo de carácter para generar la contraseña.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Bienvenido al generador de contraseñas")

    try:
        number = int(input('Cantidad de contraseñas a generar: '))
        length = int(input('Cantidad de caracteres de la contraseña: '))
    except ValueError:
        print("Por favor ingrese un número válido.")
        return

    use_upper = input('¿Incluir letras mayúsculas? (s/n): ').lower() == 's'
    use_lower = input('¿Incluir letras minúsculas? (s/n): ').lower() == 's'
    use_digits = input('¿Incluir números? (s/n): ').lower() == 's'
    use_special = input('¿Incluir caracteres especiales? (s/n): ').lower() == 's'

    save_to_file = input('¿Desea guardar las contraseñas en un archivo? (s/n): ').lower() == 's'
    copy_to_clipboard = input('¿Desea copiar la primera contraseña generada al portapapeles? (s/n): ').lower() == 's'

    if save_to_file:
        file_path = input('Ingrese la el nombre del archivo para guardar las contraseñas (ej. contraseñas.txt): ')

    print('\nAquí están las contraseñas:')

    passwords = []
    for _ in range(number):
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        passwords.append(password)
        print(password)

    if save_to_file:
        with open(file_path, 'w') as file:
            for password in passwords:
                file.write(password + '\n')
        print(f"Contraseñas guardadas en {file_path}")

    if copy_to_clipboard and passwords:
        pyperclip.copy(passwords[0])
        print("La primera contraseña generada ha sido copiada al portapapeles.")

if __name__ == "__main__":
    main()
