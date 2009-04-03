import clr
clr.AddReferenceByPartialName("System.Windows.Forms")
clr.AddReferenceByPartialName("System.Drawing")

from System.Windows import Forms

import PygmentsCodeSource 

class WriterMock(Forms.Form):
  def __init__(self):
    self.Text = "Mock Writer"
    self.Click += self.OnClick
    
  def OnClick(sender, args):
    reload(PygmentsCodeSource)
    PygmentsCodeSource.CreateContent(sender, None)
    

Forms.Application.Run(WriterMock())