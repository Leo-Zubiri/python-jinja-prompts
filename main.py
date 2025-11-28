from prompt_manager import render_from_file, render_from_string
from templates.prompts import soporte_tecnico


def main():
    print("\nPROMPTS DINÁMICOS CON JINJA2\n")

    # 1. Desde archivo .j2
    print("="*60)
    print("--- DESDE ARCHIVO ---")
    print("="*60)
    context = {
        "agent_name": "Ana",
        "company_name": "TechSupport",
        "customer_name": "Juan",
        "call_reason": "Problema de conexión",
        "instructions": ["Verificar router", "Reiniciar equipo"],
        "tone": None
    }
    print(render_from_file("soporte_tecnico.j2", context))

    # 2. Desde string en memoria (archivo .py)
    print("\n\n","="*60)
    print("--- DESDE MEMORIA ---")
    print("="*60,"\n")
    context = {
        "agent_name": "Carlos",
        "company_name": "TechSupport",
        "customer_name": "María",
        "call_reason": "Reseteo de contraseña",
        "instructions": ["Verificar cuenta", "Enviar código"],
        "tone": "profesional"
    }
    print(render_from_string(soporte_tecnico, context))

    # 3. Ejemplo con valores None (no muestra secciones)
    print("\n\n","="*60)
    print("--- EJEMPLO CON None (sin secciones opcionales) ---")
    print("="*60,"\n")
    context = {
        "agent_name": "Laura",
        "company_name": "TechSupport",
        "customer_name": "Pedro",
        "call_reason": None,  # Mostrará "desconocido"
        "instructions": None,  # No mostrará sección INSTRUCCIONES
        "customer_id": None,
        "customer_tier": None,
        "priority": None,
        "tone": None  # Usará default "profesional y amable"
    }
    print(render_from_file("soporte_tecnico.j2", context))

    # 4. Ejemplo completo con todos los campos
    print("\n\n","="*60)
    print("--- EJEMPLO COMPLETO (todos los campos) ---")
    print("="*60,"\n")
    context = {
        "agent_name": "Roberto",
        "company_name": "TechSupport Premium",
        "customer_name": "Ana García",
        "customer_id": "CUST-98765",
        "customer_tier": "VIP",
        "call_reason": "Error crítico en sistema de pagos",
        "priority": "ALTA",
        "call_duration": "30 minutos máximo",
        "instructions": [
            "Revisar logs de transacciones",
            "Verificar estado de la API de pagos",
            "Contactar al equipo de infraestructura si persiste"
        ],
        "tone": "muy empático y urgente",
        "additional_context": "El cliente reporta pérdidas económicas. Manejar con máxima prioridad."
    }
    print(render_from_string(soporte_tecnico, context))


if __name__ == "__main__":
    main()
