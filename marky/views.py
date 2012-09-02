from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
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

@csrf_protect
def preview(request):
    if request.method == 'POST':
        markup = request.POST.get('markup', '')
        markdown.reset()
        return HttpResponse(markdown.convert(markup))
    return render(request, 'marky/preview.html')

