from django.shortcuts import render_to_response
from django.template.context import RequestContext


def configure(request, template_name="shipit_ascii_art/configure.html"):
    return render_to_response(template_name, RequestContext(request))
