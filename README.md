# Marky

## Install

**Install package**

```bash
pip install marky
``

**Add to `INSTALLED_APPS`**

Also required if the supplied template is used is `django.contrib.staticfiles`.

```python
INSTALLED_APPS = (
    ...
    'django.contrib.staticfiles',
    'marky',
)
```

**Create a `base.html`**

_I recommend using [HTML5 Boilerplate](http://html5boilerplate.com)._

Define a `{% block content %}`, `{% block scripts %}`, and `{% block styles %}`
(should be in the `<head>`). If you prefer different named blocks, copy the
[marky template](https://github.com/bruth/marky/blob/master/marky/templates/preview.html)
and rename the blocks to your preferences. Make sure the new template comes
first on the template lookup path.

**Add it to `urls.py`

```python
urlpatterns = patterns('',
    ...
    # ..or whatever endpoint you want
    url(r'', include('marky.urls')),
)
```

**Enjoy**
