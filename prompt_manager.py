"""
Gestor de prompts dinámicos usando Jinja2.
Soporta carga desde archivos y desde strings en memoria.
"""
from jinja2 import Environment, FileSystemLoader


def render_from_file(template_name: str, context: dict, templates_dir: str = "templates") -> str:
    """
    Renderiza una plantilla desde un archivo.

    Args:
        template_name: Nombre del archivo (ej: "soporte_tecnico.j2")
        context: Variables para la plantilla
        templates_dir: Directorio de plantillas

    Returns:
        Prompt renderizado
    """
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = env.get_template(template_name)
    return template.render(**context)


def render_from_string(template_string: str, context: dict) -> str:
    """
    Renderiza una plantilla desde un string.

    Args:
        template_string: Contenido de la plantilla Jinja2
        context: Variables para la plantilla

    Returns:
        Prompt renderizado
    """
    env = Environment(trim_blocks=True, lstrip_blocks=True)
    template = env.from_string(template_string)
    return template.render(**context)
