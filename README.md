# Marky

Marky is simple Django app that provides a single view and template for
live editing Markdown documents. Copy in existing Markdown into the textarea
or just start typing to see how the document will be rendered.

#### Install package

```bash
pip install marky
```

#### Add to `INSTALLED_APPS`

`django.contrib.staticfiles` is also required if the supplied template is used.

```python
INSTALLED_APPS = (
    ...
    'django.contrib.staticfiles',
    'marky',
)
```

#### Create a `base.html`

Here is a starter template:

```django
<!doctype html>
<html>
    <head>
        {% block styles %}{% endblock %}
    </head>
    <body>
        {% block content %}
        {% endblock %}
        {% block scripts %}
        {% endblock %}
    </body>
</html>
```

Define a `{% block content %}`, `{% block scripts %}`, and `{% block styles %}`
(should be in the `<head>`). If you prefer different named blocks, copy the
[marky template](https://github.com/bruth/marky/blob/master/marky/templates/marky/preview.html)
and rename the blocks to your preferences. Make sure the new template comes
first on the template lookup path.

_More a more complete base HTML template, I recommend using
[HTML5 Boilerplate](http://html5boilerplate.com)._

#### Add it to `urls.py`

```python
urlpatterns = patterns('',
    ...
    # ..or whatever endpoint you want
    url(r'', include('marky.urls')),
)
```

#### Enjoy
