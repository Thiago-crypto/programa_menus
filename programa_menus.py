def menu_programas():
    while True:
        print("\n--- Menú PROGRMAS  ---")
        print("\n--- DE SANTIAGO MUNGUIA ---")
        print("1. CALCULADORA")
        print("2. lICENCIA")
        print("3. CALIFICACION ")
        print("4.IMC ")
        print("5.HORAS DE TRABAJO ")
        print("6. PASTELES")
        print("7. TABLAS DE MULTIPLICAR DEL 1-10")
        print("8. CONTRASEÑA")
        print("9.PALABRA 10 VECES")
        print("10. NUMERO PRIMO")
        print("11. SALIR")
        opcion = input("eliga una opcion:")

        if opcion == "1":

            def menu_calculadora():
                while True:
                    print("\n--- Menú Calculadora  ---")
                    print("\n--- DE SANTIAGO MUNGUIA ---")
                    print("1. Suma")
                    print("2. Resta")
                    print("3. Multiplicación")
                    print("4. División")
                    print("5-.Potencia")
                    print("6. Salir")

                    op = input("Selecciona una opción (1-6): ")

                    if op == "6":
                        print("Hasta pronto, Adiós.")
                        break

                    try:
                        numero_1 = float(input("Ingresa el primer número: "))
                        numero_2 = float(input("Ingresa el segundo número: "))
                    except ValueError:
                        print("Por favor, ingresa valores numéricos válidos.")
                        continue

                    if op == "1":
                        print(
                            f"El resultado de la suma es: {numero_1 + numero_2}"
                        )
                    elif op == "5":
                        print(
                            f"El resultado de la potencia es: {numero_1 ** numero_1}"
                        )
                    elif op == "2":
                        print(
                            f"El resultado de la resta es: {numero_1 - numero_2}"
                        )
                    elif op == "3":
                        print(
                            f"El resultado de la multiplicación es: {numero_1 * numero_2}"
                        )
                    elif op == "4":
                        if numero_2 != 0:
                            print(
                                f"El resultado de la división es: {numero_1 / numero_2}"
                            )
                        else:
                            print("Error: No se puede dividir entre cero.")
                    else:
                        print("Opción no válida. Intenta de nuevo.")

            menu_calculadora()

        elif opcion == "2":
            edad = int(input("Ingresa la edad: "))
            lincencia = input("¿Tienes licencia? ")
            if edad >= 18 and lincencia == "Si":
                print("Puede conducir")
            else:
                print("No puedes conducir")
        elif opcion == "3":
            try:
                calificacion = float(
                    input("Ingrese la calificación del estudiante: "))
                if calificacion >= 9:
                    print("Tu calificación es: A ¡Excelente trabajo!")
                elif calificacion >= 8:
                    print("Tu calificación es: B ¡Buen trabajo!")
                elif calificacion >= 7:
                    print("Tu calificación es: C ¡Aprobado!")
                else:
                    print(
                        "¡Ánimo! Con más estudio podrás mejorar tu calificación."
                    )
            except ValueError:
                print("Por favor, ingresa una calificación válida.")

        elif opcion == "4":
            try:
                peso = float(input("Ingrese su peso en kg: "))
                estatura = float(input("Ingrese su estatura en metros: "))
                imc = peso / (estatura**2)
                print(f"Tu índice de masa corporal es {imc:.2f}")
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos")
        elif opcion == "5":
            try:
                horas = float(input("Ingrese el número de horas trabajadas: "))
                costo_hora = float(input("Ingrese el coste por hora: "))
                paga = horas * costo_hora
                print(f"La paga que le corresponde es: ${paga:.2f}")
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos")
        elif opcion == "6":

            def menu_pasteleria():
                while True:
                    print("P A S T E L E R I A ")
                    ingredientes = ["Chispas de chocolate", "Estrellas"]

                    try:
                        tipo_cupcake = input(
                            "¿Desea un cupcake sencillo? (Si/No): ").lower()

                        if tipo_cupcake == "si":
                            print(
                                "\nCoberturas disponibles para cupcake sencillo:"
                            )
                            print("1. Fondant")
                            print("2. Queso crema")

                            cobertura = input(
                                "Seleccione el número de cobertura (1-2): ")
                            if cobertura == "1":
                                ingredientes.append("Fondant")
                            elif cobertura == "2":
                                ingredientes.append("Queso crema")
                            else:
                                print("Opción no válida")
                                continue

                        elif tipo_cupcake == "no":
                            print("\nTipos de Buttercream disponibles:")
                            print("1. Buttercream de merengue suizo")
                            print("2. Buttercream de merengue italiano")
                            print("3. Buttercream de merengue francés")

                            buttercream = input(
                                "Seleccione el tipo de buttercream (1-3): ")
                            buttercreams = {
                                "1": "Buttercream de merengue suizo",
                                "2": "Buttercream de merengue italiano",
                                "3": "Buttercream de merengue francés"
                            }

                            if buttercream in buttercreams:
                                ingredientes.append(buttercreams[buttercream])
                            else:
                                print("Opción no válida")
                                continue
                        else:
                            print("Respuesta no válida")
                            continue

                        print("\n--- Resumen del Pedido ---")
                        print(
                            f"Tipo de cupcake: {'Sencillo' if tipo_cupcake == 'si' else 'Elaborado'}"
                        )
                        print("Ingredientes:")
                        for i, ingrediente in enumerate(ingredientes, 1):
                            print(f"{i}. {ingrediente}")

                        salir = input(
                            "\n¿Desea hacer otro pedido? (Si/No): ").lower()
                        if salir == "no":
                            break

                    except ValueError:
                        print("Por favor, ingrese una opción válida")

            menu_pasteleria()
        elif opcion == "7":
            print("\n--- Tablas de Multiplicar del 1 al 10 ---")
            for i in range(1, 11):
                print(f"\nTabla del {i}:")
                for j in range(1, 11):
                    resultado = i * j
                    print(f"{i} x {j} = {resultado}")
        elif opcion == "8":
            contrasena_correcta = "secreto123"
            while True:
                intento = input("Introduce la contraseña: ")
                if intento == contrasena_correcta:
                    print("¡Contraseña correcta! Acceso permitido.")
                    break
                else:
                    print("Contraseña incorrecta. Intenta de nuevo.")
        elif opcion == "9":
            palabra = input("Introduce una palabra: ")
            for i in range(10):
                print(palabra)
        elif opcion == "10":
            try:
                numero = int(input("Introduce un número entero: "))
                if numero > 1:
                    es_primo = True
                    for i in range(2, int(numero**0.5) + 1):
                        if numero % i == 0:
                            es_primo = False
                            break
                    if es_primo:
                        print(f"{numero} es un número primo")
                    else:
                        print(f"{numero} no es un número primo")
                else:
                    print("El número debe ser mayor que 1")
            except ValueError:
                print("Por favor, introduce un número entero válido")
        elif opcion == "11":
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")


menu_programas()
