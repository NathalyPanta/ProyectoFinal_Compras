# from config.wsgi import *
from django.template.loader import get_template
from weasyprint import HTML


def printRegistro():
    template = get_template('pregistro.html')
    context= {"name": "NSPV"}
    html_template = template.render(context)
    HTML(string=html_template).write_pdf(target="RegistroCompras.pdf")

printRegistro()