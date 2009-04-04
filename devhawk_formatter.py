from pygments.formatter import Formatter

class DevHawkHtmlFormatter(Formatter):
  def __init__(self, **options):
        Formatter.__init__(self, **options)
        
        if "fonts" in options:
          self.fonts = ",".join(options["fonts"])
        else:
		  self.fonts = ",".join(['consolas', 'lucida console', 'courier', 'monospace'])

        # create a dict of (start, end) tuples that wrap the
        # value of a token so that we can use it in the format
        # method later
        self.styles = {}

        # we iterate over the `_styles` attribute of a style item
        # that contains the parsed style values.
        for token, style in self.style:
            start = end = ''
            # a style item is a tuple in the following form:
            # colors are readily specified in hex: 'RRGGBB'
            if style['color']:
                start += '<span style="color:#%s">' % style['color']
                end = '</span>' + end
            if style['bold']:
                start += '<b>'
                end = '</b>' + end
            if style['italic']:
                start += '<i>'
                end = '</i>' + end
            if style['underline']:
                start += '<u>'
                end = '</u>' + end
            self.styles[token] = (start, end)


  def format(self, tokensource, outfile):
        # lastval is a string we use for caching
        # because it's possible that an lexer yields a number
        # of consecutive tokens with the same token type.
        # to minimize the size of the generated html markup we
        # try to join the values of same-type tokens here
        lastval = ''
        lasttype = None

        # wrap the whole output with <pre>
        outfile.write('<div style="font-family:'+self.fonts+'">\n')

        for ttype, value in tokensource:
            value = value.replace(' ', '&#160;')
            value = value.replace("<", '&lt;')
            value = value.replace(">", '&gt;')
            value = value.replace('\n', '<br/>\n')
            # if the token type doesn't exist in the stylemap
            # we try it with the parent of the token type
            # eg: parent of Token.Literal.String.Double is
            # Token.Literal.String
            while ttype not in self.styles:
                ttype = ttype.parent
            if ttype == lasttype:
                # the current token type is the same of the last
                # iteration. cache it
                lastval += value
            else:
                # not the same token as last iteration, but we
                # have some data in the buffer. wrap it with the
                # defined style and write it to the output file
                if lastval:
                    stylebegin, styleend = self.styles[lasttype]
                    outfile.write(stylebegin + lastval + styleend)
                # set lastval/lasttype to current values
                lastval = value
                lasttype = ttype

        # if something is left in the buffer, write it to the
        # output file, then close the opened <pre> tag
        if lastval:
            stylebegin, styleend = self.styles[lasttype]
            outfile.write(stylebegin + lastval + styleend)
        outfile.write('</div>\n')
