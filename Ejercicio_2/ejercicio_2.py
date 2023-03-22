def solicitar_prestamo(ingresos_anuales, deudas):
    """
    Función que recibe los ingresos anuales y deudas de un cliente
    y determina si es elegible para un préstamo bancario.

    Args:
        ingresos_anuales (float): Ingresos anuales del cliente
        deudas (float): Deudas actuales del cliente

    Returns:
        str: Si el cliente es elegible para un préstamo bancario
             o no.
    """
    if ingresos_anuales > 945200 and deudas == 0:
        return "Usted es elegible para un préstamo bancario."
    else:
        return "Lo siento, no es elegible para un préstamo bancario en este momento."