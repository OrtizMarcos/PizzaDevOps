import random
import pandas as pd

# Crear el menú de pizzas como DataFrame
menu_pizzas_data = {
    "Pizza": ["margarita", "pepperoni", "vegetariana"],
    "Mediano": [35000.0, 37000.0, 32000.0],
    "Grande": [40000.0, 42000.0, 36000.0]
}
menu_pizzas_df = pd.DataFrame(menu_pizzas_data)

costo_delivery = 12000.0  # Definir aquí el costo estándar de delivery

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
    if pizza_type not in menu_pizzas_df["Pizza"].values or pizza_size.lower() not in ["mediano", "grande"]:
        return None

    # Obtener el precio base de la pizza
    precio_pizza = menu_pizzas_df.loc[menu_pizzas_df["Pizza"] == pizza_type, pizza_size.capitalize()].values[0]

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
    precio = calcular_precio_total_sin_delivery(pizza_type, pizza_size)
    print(f"Pizza: {pizza_type.capitalize()} - Tamaño: {pizza_size.capitalize()} - Precio: Gs. {precio:.2f}")

def main():
    global pedidos_df  # Referenciar la variable global

    print("Bienvenido a la pizzería, desea realizar un pedido de pickup (recoger del local) o delivery (entrega a domicilio)?")

    pedidos = []  # Lista para almacenar los pedidos

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
            pedidos.append((pizza_type, pizza_size))  # Agregar pizza al pedido sin toppings
        else:
            print("Pizza o tamaño no válidos. Por favor, seleccione una pizza y tamaño válidos.")

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
    if len(pedidos) == 0:
        print("No se realizaron pedidos.")
    else:
        print("\n|--------------------------------|\n")
        print(mensaje_pedido)
        print("Resumen del pedido:")
        for pizza_type, pizza_size in pedidos:
            mostrar_detalles_pizza(pizza_type, pizza_size)
        print(f"Total a pagar: Gs. {total:.2f}")
        print("\n|--------------------------------|")
    
    # Crear un DataFrame con el nuevo registro
    nuevo_registro = {
        "tipo_pedido": [delivery],
        "direccion_entrega": [direccion if delivery == "delivery" else None],
        "pedido": [pedidos],
        "costo_delivery": [costo_delivery if delivery == "delivery" else None],
        "costo_total": [total]
    }
    nuevo_df = pd.DataFrame(nuevo_registro)

    # Concatenar el DataFrame inicial con el nuevo registro
    pedidos_df = pd.concat([pedidos_df, nuevo_df], ignore_index=True)

if __name__ == "__main__":
    pedidos_df = pd.DataFrame(columns=["tipo_pedido", "direccion_entrega", "pedido", "costo_delivery"])
    main()
    print(pedidos_df)  # Mostrar el DataFrame después de ejecutar main()