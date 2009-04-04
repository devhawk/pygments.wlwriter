import clr
clr.AddReference('pygments')

code = '''import os

def get_all_files(folder):
  files = []
  for (dirpath, dirnames, filenames) in os.walk(folder):
    for file in filenames:
       files.append(os.path.join(dirpath, file))
  return files

pygments_files = get_all_files(
  os.path.join(os.getcwd(), 'pygments'))
     
import clr
clr.CompileModules("pygments.dll", *pygments_files)'''

from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles, get_style_by_name

from devhawk_formatter import DevHawkHtmlFormatter

def get_lexers(): 
  return get_all_lexers()

def get_styles(): 
  return get_all_styles()

def generate_html(code, lexer_name, style_name):
  if not lexer_name: lexer_name = "text"
  if not style_name: style_name = "default"
  lexer = get_lexer_by_name(lexer_name)
  return highlight(code, lexer, DevHawkHtmlFormatter(style=style_name))
  
lexers = get_lexers()
styles = get_styles()

html = generate_html(code, 'python', 'tango')
