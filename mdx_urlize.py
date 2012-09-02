import re
import markdown

PROTOCOL_MATCH = re.compile(r'^(news|telnet|nttp|file|http|ftp|https)')
URLIZE_RE = r'((?:(?:news|telnet|nttp|file|http|ftp|https)://)?(?:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|(?:[-A-Za-z0-9@]*\.)+[A-Za-z]+)(?::[0-9]+)?(?:[-A-Za-z0-9_\$\.\+!\*\(\),;:@&=?/~#%]*[A-Za-z0-9/])?)'

class UrlizePattern(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = text = m.groups()[1]

        if '@' in url and not '/' in url:
            url = 'mailto:' + url
        elif not PROTOCOL_MATCH.search(url):
            url = 'http://' + url

        el = markdown.util.etree.Element("a")
        el.set('href', url)
        el.text = markdown.util.AtomicString(text)
        return el

class UrlizeExtension(markdown.Extension):
    "Urlize Extension for Python-Markdown."

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['autolink'] = UrlizePattern(URLIZE_RE, md)

def makeExtension(configs=None):
    return UrlizeExtension(configs=configs)
