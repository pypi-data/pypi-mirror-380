from ..utils.template_loader import render_template
import os
from importlib import resources
from turbopdf.core import generate_pdf_from_string

class BaseFormAssembler:
    def __init__(self, context=None, total_pages=1):
        self.context = context or {}
        self.components = []
        self.total_pages = total_pages
        self.img_base = self._get_img_base()

    def _get_img_base(self):
        try:
            with resources.path('turbopdf', '__init__.py') as p:
                img_dir = p.parent / 'img'
                if img_dir.exists():
                    return f'file:///{img_dir.as_posix()}'
        except Exception:
            pass
        
        # Fallback
        import turbopdf
        turbopdf_path = os.path.dirname(turbopdf.__file__)
        img_dir = os.path.join(turbopdf_path, 'img')
        return f'file:///{img_dir.replace("\\", "/")}'

    def add_component(self, template_name, extra_context=None):
        full_context = {**self.context, 'img_base': self.img_base}
        if extra_context:
            full_context.update(extra_context)
        # ✅ Usa el renderizador interno, no Django
        rendered = render_template(template_name, full_context)
        self.components.append(rendered)
        return self

    def add_raw_html(self, html):
        self.components.append(html)
        return self

    def build(self):
        # Renderizar style.html con el mismo sistema
        head = render_template('sistema/style.html', {
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