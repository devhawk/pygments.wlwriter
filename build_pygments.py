import os

def get_all_files(folder):
  files = []
  for (dirpath, dirnames, filenames) in os.walk(folder):
    for file in filenames:
       files.append(os.path.join(dirpath, file))
  return files

pygments_files = get_all_files(
  os.path.join(os.getcwd(), 'pygments'))

pygments_files.append('devhawk_formatter.py')
pygments_files.append(r'C:\Program Files\IronPython 2.0.1\Lib\os.py')
pygments_files.append(r'C:\Program Files\IronPython 2.0.1\Lib\ntpath.py')
pygments_files.append(r'C:\Program Files\IronPython 2.0.1\Lib\stat.py')
pygments_files.append(r'C:\Program Files\IronPython 2.0.1\Lib\UserDict.py')
pygments_files.append(r'C:\Program Files\IronPython 2.0.1\Lib\StringIO.py')
pygments_files.append(r'C:\Program Files\IronPython 2.0.1\Lib\fnmatch.py')
pygments_files.append(r'C:\Program Files\IronPython 2.0.1\Lib\types.py')

import clr
clr.CompileModules("pygments.dll", *pygments_files)