import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_safe, require_POST
from django.views.decorators.csrf import csrf_exempt
from markdown import Markdown

markdown = Markdown(output_format='html5', extensions=[
    'toc',
    'abbr',
    'nl2br',
    'tables',
    'urlize',
    'def_list',
    'footnotes',
    'superscript',
    'subscript',
    'sane_lists',
    'smart_strong',
    'fenced_code',
    'codehilite(css_class=highlight)',
])

@require_safe
def preview(request):
    return render(request, 'marky/preview.html')

@csrf_exempt
@require_POST
def api(request):
    response = HttpResponse()
    # TODO change this to check for registered hosts either as a setting
    # or database records
    response['Access-Control-Allow-Origin'] = '*'

    # Parse request body accordingly.. JSON, plain text and form data are
    # supported.
    content_type = request.META['CONTENT_TYPE']

    if 'application/json' in content_type:
        markup = json.loads(request.body).get('markup', '')
    elif 'text/plain' in content_type:
        markup = request.body
    else:
        markup = request.POST.get('markup', '')

    markdown.reset()
    response.content = markdown.convert(markup)
    return response
