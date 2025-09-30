# src/turbopdf/assemblers/base.py
from django.template.loader import render_to_string
from turbopdf.core import generate_pdf_from_string
import turbopdf
import os
from importlib import resources

class BaseFormAssembler:
    def __init__(self, context=None, total_pages=1):
        self.context = context or {}
        self.components = []
        self.img_base = self._get_img_base()
        self.total_pages = total_pages

    def _get_img_base(self):
        # ✅ Forma moderna y segura de obtener la ruta de los recursos
        try:
            # Intenta obtener la ruta como directorio (modo editable)
            with resources.path(turbopdf, '__init__.py') as p:
                turbopdf_path = p.parent
                img_dir = turbopdf_path / 'img'
                if img_dir.exists():
                    return f'file:///{img_dir.as_posix()}'
        except Exception:
            pass

        # Fallback: modo tradicional (solo funciona en desarrollo)
        turbopdf_path = os.path.dirname(turbopdf.__file__)
        img_dir = os.path.join(turbopdf_path, 'img')
        return f'file:///{img_dir.replace("\\", "/")}'

    def add_page_break(self):
        """Agrega un salto de página."""
        self.components.append('<div style="page-break-before: always;"></div>')
        return self

    def add_component(self, template_name, extra_context=None, wrapper_html=None):
        """Agrega un componente HTML desde la librería."""
        full_context = {
            **self.context,
            'img_base': self.img_base,
            **(extra_context or {})
        }
        rendered = render_to_string(f'sistema/{template_name}', full_context)
        if wrapper_html:
            rendered = wrapper_html.replace('{{component}}', rendered)
        self.components.append(rendered)
        return self

    def add_raw_html(self, html):
        """Agrega HTML crudo."""
        self.components.append(html)
        return self

    def build(self):
        head = render_to_string('sistema/style.html', {
            **self.context,
            'img_base': self.img_base
        })
        body = "\n".join(self.components)

        html_final = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Formulario</title>
            <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            {head}
        </head>
        <body style="font-family: 'Roboto', sans-serif; margin: 0; padding: 0;">
            {body}
        </body>
        </html>
        """
        return generate_pdf_from_string(html_final)