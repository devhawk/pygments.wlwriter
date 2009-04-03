import clr
clr.AddReference('System.Windows.Forms')

from System.Windows.Forms import DialogResult

def CreateContent(dialogOwner, newContent):
  return DialogResult.OK
  
def CreateEditor(editorSite):
  return None
  
def GeneratePublishHtml(content, publishingContext):
  return "<pre>spam, spam, spam, baked beans and spam</pre>"
  