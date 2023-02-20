import io
from django.template import Context
from django.template.loader import render_to_string
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import pdfkit


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


def to_pdf(template_, context_=None):
    if context_ is None:
        context_ = {}
    template = get_template(template_)
    context = Context(context_)
    # html = template.render(context_)
    html = render_to_string(template_, context_)
    result = io.BytesIO()
    # pdf = pisa.pisaDocument(io.BytesIO(html.encode('UTF-8')), result)
    # pdf = pisa.pisaDocument(io.BytesIO(html.encode('ISO-8859-1')), result)
    response = HttpResponse(content_type='application/pdf')
    # pdf = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    pdf = pdfkit.from_string(html, None)
    # if not pdf.err:
    #     # HttpResponse(result.getvalue(), content_type='application/pdf')
    #     return response
    # print(pdf.err)
    return HttpResponse(pdf, content_type='application/pdf')
