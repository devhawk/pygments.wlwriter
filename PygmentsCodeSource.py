import clr
clr.AddReference('System.Windows.Forms')

from System.Windows.Forms import Form, DialogResult

class CodeInsertForm(Form):
  def __init__(self):
    self.Text = "Insert Code to Pygmentize"

def CreateContent(dialogOwner, newContent):
  frm = CodeInsertForm()
  return frm.ShowDialog(dialogOwner)
  
def CreateEditor(editorSite):
  return None
  
def GeneratePublishHtml(content, publishingContext):
  return "<pre>spam, spam, spam, baked beans and spam</pre>"
  