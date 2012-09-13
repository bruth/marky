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

def convert_markdown(text):
    markdown.reset()
    return markdown.convert(text)
