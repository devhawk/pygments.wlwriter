  
from System import IO

def walk(folder):
  for file in IO.Directory.GetFiles(folder):
    yield file
  for folder in IO.Directory.GetDirectories(folder):
    for file in walk(folder): yield file
  

pygments_files = list(walk('pygments'))
pygments_dependencies = list(walk('pygments_dependencies'))

all_files = pygments_files + pygments_dependencies
all_files.append('devhawk_formatter.py')

import clr
clr.CompileModules("..\external\pygments.dll", *all_files)