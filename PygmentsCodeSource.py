import clr
clr.AddReference('System.Windows.Forms')

from System.Windows import Forms
from System import Drawing

class CodeInsertForm(Forms.Form):
  def __init__(self):
  
    self.panel1 = Forms.Panel(
      Dock = Forms.DockStyle.Bottom,
      Size = Drawing.Size(40, 40),
      )
      
    self.code_text_box = Forms.TextBox(
      AcceptsReturn = True,
      AcceptsTab = True,
      Font = Drawing.Font("Consolas", 10),
      Dock = Forms.DockStyle.Fill,
      Multiline = True,
      ScrollBars = Forms.ScrollBars.Both,
      )

    self.SuspendLayout()
    self.ClientSize = Drawing.Size(640,480)
    self.Controls.Add(self.code_text_box)
    self.Controls.Add(self.panel1)
    self.Text = "Insert Code to be Pygmented"
    self.ResumeLayout(False)
    self.PerformLayout()


def CreateContent(dialogOwner, newContent):
  frm = CodeInsertForm()
  return frm.ShowDialog(dialogOwner)
  
def CreateEditor(editorSite):
  return None
  
def GeneratePublishHtml(content, publishingContext):
  return "<pre>spam, spam, spam, baked beans and spam</pre>"
  