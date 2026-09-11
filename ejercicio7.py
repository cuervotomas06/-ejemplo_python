def validar_email(email):
    # Paso 1: exactamente un @
    if email.count("@") != 1:
        return False

    # Paso 2: separar
    usuario, dominio = email.split("@")

    # Paso 3: algo antes del @
    if len(usuario) == 0:
        return False

    # Paso 4: al menos un punto en el dominio
    if "." not in dominio:
        return False

    # Paso 5: no empieza/termina con @ o .
    if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):
        return False

    # Paso 6: extensión de al menos 2 caracteres
    extension = dominio.split(".")[-1]
    if len(extension) < 2:
        return False

    return True


email = input("Ingrese un email: ")
if validar_email(email):
    print("VÁLIDO (OK)")
else:
    print("INVÁLIDO")