import random
import pandas as pd
# Diccionario con el menú de pizzas y sus precios base
menu_pizzas = {
    "margarita": {"mediano": 35000.0, "grande": 40000.0},
    "pepperoni": {"mediano": 37000.0, "grande": 42000.0},
    "vegetariana": {"mediano": 32000.0, "grande": 36000.0}
}

costo_delivery = 12000.0  # definir aquí costo estándar de delivery

def calcular_precio_total_sin_delivery(pizza_type, pizza_size):
    """
    Función que calcula el precio total de un pedido de pizza, incluyendo pizza, tamaño y toppings, excluyendo el costo de entrega.

    Args:
        pizza_type (str): El nombre de la pizza.
        pizza_size (str): El tamaño de la pizza.

    Returns:
        float: Precio total del pedido sin costo de entrega.
    """

    pizza_type = pizza_type.lower()
    pizza_size = pizza_size.lower()

    # Validar pizza y tamaño
    if pizza_type not in menu_pizzas or pizza_size not in menu_pizzas[pizza_type]:
        return None

    # Obtener el precio base de la pizza
    precio_pizza = menu_pizzas[pizza_type][pizza_size]

    return precio_pizza

def calcular_precio_total_con_delivery(pedido, direccion):
    """
    Función que calcula el precio total de un pedido de pizza con costo de entrega.

    Args:
        pedido (list): Lista de tuplas, donde cada tupla contiene (pizza, size, toppings).
        direccion (str): Dirección de entrega.

    Returns:
        tuple: (float, str) - Precio total del pedido con costo de entrega y mensaje de confirmación.
    """

    total_general = 0
    for pizza_type, pizza_size in pedido:
        total_pizza = calcular_precio_total_sin_delivery(pizza_type, pizza_size)
        if total_pizza is None:
            return None

        total_general += total_pizza

    total_general += costo_delivery

    numero_pedido = random.randint(100, 500)
    mensaje_pedido = f"Su pedido ha sido registrado con éxito, su número de pedido es {numero_pedido}, será entregado en un periodo de 40 a 60 minutos en la dirección ingresada."
    return total_general, mensaje_pedido

def obtener_informacion_cliente_delivery():
    direccion = input("Por favor, ingrese su dirección de entrega: ")
    return direccion

def mostrar_detalles_pizza(pizza_type, pizza_size):
    precio = menu_pizzas[pizza_type][pizza_size]
    print(f"Pizza: {pizza_type.capitalize()} - Tamaño: {pizza_size.capitalize()} - Precio: Gs. {precio:.2f}")

def main():
    print("Bienvenido a la pizzería, desea realizar un pedido de pickup (recoger del local) o delivery (entrega a domicilio)?")

    pedidos = []  # Lista para almacenar los pedidos
    #DataFrame para almacenar los detalles de las pizzas
    columnas = ["Pizza", "Tamaño", "Precio"]
    columnas = ["Pizza", "Tamaño", "Precio"]
    detalles_df = pd.DataFrame(columns=columnas)
    # Definir método de entrega
    tipo_pedido = input("¿Quiere Pickup o Delivery? ").lower()
    mensaje_pedido = ""

    if tipo_pedido == "delivery":
        delivery = "delivery"
        direccion = obtener_informacion_cliente_delivery()

    else:
        delivery = "pickup"

    # Bucle principal para agregar pizzas al pedido
    while True:
        pizza_type = input("Seleccione una pizza (pepperoni, margarita, vegetariana): ")
        pizza_size = input("Tamaño de pizza que desea (mediano, grande): ")

        # Validar pizza y tamaño antes de agregar al pedido
        if pizza_type.lower() in menu_pizzas and pizza_size.lower() in ["mediano", "grande"]:
            precio = calcular_precio_total_sin_delivery(pizza_type, pizza_size)
            pedidos.append((pizza_type, pizza_size))  # Agregar pizza al pedido sin toppings

            # Agregar detalles al DataFrame
            detalles_df = detalles_df.append({"Pizza": pizza_type.capitalize(), "Tamaño": pizza_size.capitalize(), "Precio": precio}, ignore_index=True)
        else:
            print("Pizza o tamaño no válidos. Por favor, seleccione una pizza y tamaño válidos.")
            continue  # Utiliza continue en lugar de break para continuar con la siguiente iteración
        otro_pedido = input("¿Desea agregar otro pedido? (si/no): ").lower()
        if otro_pedido != 'si':
            break

    if tipo_pedido == "delivery":
        resultado = calcular_precio_total_con_delivery(pedidos, direccion)
        if resultado is not None:
            total, mensaje_pedido = resultado
        else:
            print("Error en el cálculo del precio total del pedido.")
            return

    else:
        total = sum(calcular_precio_total_sin_delivery(pizza_type, pizza_size) for pizza_type, pizza_size in pedidos)
        numero_pedido = random.randint(100, 500)
        mensaje_pedido = f"Su pedido ha sido registrado con éxito, su número de pedido es {numero_pedido}, puede pasar a retirarlo al local en 20 minutos."

    # Imprimir resumen del pedido en caso de que se haya realizado alguno:
    if len(pedidos) > 0:
        print("\n|--------------------------------|\n")
        print("n\Resumen del pedido:")
        print(detalles_df)
        print(f"\nTotal a pagar Gs. {total:.2f}")
        print("\n|--------------------------------|")

if __name__ == "__main__":
    main()