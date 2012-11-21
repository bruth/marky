"""Hashtag extension for Markdown.

To create a hashtag, simply start with a pound sign and the tag itself
without any spaces included in the text.

Examples:

>>> import markdown
>>> md = markdown.Markdown(extensions=['hashtag'])
>>> md.convert('Coding is fantastic !code !life')
u'<p>Coding is fantastic <tag>#code</tag> <tag>#life</tag></p>'
"""

import markdown

# Global Vars
HASHTAG_RE = r'!([\w-]+)'

class HashtagPattern(markdown.inlinepatterns.Pattern):
    """ Return a hashtag Element: `#code' """
    def handleMatch(self, m):
        text = '#' + m.group(2)
        el = markdown.util.etree.Element('tag')
        el.text = markdown.util.AtomicString(text)
        return el

class HashtagExtension(markdown.Extension):
    """ Hashtag Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        """ Replace subscript with HashtagPattern"""
        md.inlinePatterns['hashtag'] = HashtagPattern(HASHTAG_RE, md)

def makeExtension(configs=None):
    return HashtagExtension(configs=configs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
