import clr
clr.AddReferenceByPartialName("System.Windows.Forms")
clr.AddReferenceByPartialName("System.Drawing")

import PygmentsCodeSource 

from System.Windows import Forms
from System.Collections.Generic import Dictionary

class SmartContentMock(object):
  __slots__ = ['Properties']
  def __init__(self):
    self.Properties = Dictionary[str,str]() 

class WriterMock(Forms.Form):
  def __init__(self):
    self.Text = "Mock Writer"
    self.Click += self.OnClick
    
  def OnClick(sender, args):
    reload(PygmentsCodeSource)
    
    content = SmartContentMock()
    if PygmentsCodeSource.CreateContent(sender, content) == Forms.DialogResult.OK:
      html = PygmentsCodeSource.GeneratePublishHtml(content, None)
      Forms.MessageBox.Show(html)

Forms.Application.Run(WriterMock())