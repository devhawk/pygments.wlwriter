import clr
clr.AddReference("pygments")

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

def generate_html(code, lexer_name, style_name):
  from pygments import highlight
  from pygments.lexers import get_lexer_by_name
  from pygments.styles import get_style_by_name
  from devhawk_formatter import DevHawkHtmlFormatter

  if not lexer_name: lexer_name = "text"
  if not style_name: style_name = "default"
  lexer = get_lexer_by_name(lexer_name)
  return highlight(code, lexer, DevHawkHtmlFormatter(style=style_name))