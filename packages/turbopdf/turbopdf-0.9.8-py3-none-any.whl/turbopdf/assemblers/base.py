from django.template.loader import render_to_string
from turbopdf.core import generate_pdf_from_string
import os
import turbopdf

class BaseFormAssembler:
    def __init__(self, context=None, total_pages=1):
        self.context = context or {}
        self.components = []
        self.total_pages = total_pages
        self.img_base = self._get_img_base()


    def add_component(self, template_name, extra_context=None):
        full_context = {**self.context, 'img_base': self.img_base}
        if extra_context:
            full_context.update(extra_context)
        # ✅ Usa el sistema de templates de Django (pero con ruta completa)
        rendered = render_to_string(f'sistema/{template_name}', full_context)
        self.components.append(rendered)
        return self

    def add_raw_html(self, html):
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
            <title>Documento</title>
            <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            {head}
        </head>
        <body style="font-family: 'Roboto', sans-serif; margin: 0; padding: 0;">
            {body}
        </body>
        </html>
        """
        return generate_pdf_from_string(html_final)