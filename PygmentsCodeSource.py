from __future__ import with_statement

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('WindowsLive.Writer.Api')

from System.Windows import Forms
from System import Drawing
from WindowsLive.Writer.Api import SmartContentEditor

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

lexers = [l[0] for l in get_all_lexers()]
lexers.sort()
styles = list(get_all_styles())
styles.sort()

class LayoutCtxMgr(object):
  def __init__(self, ctl):
    self.ctl = ctl
    
  def __enter__(self):
    self.ctl.SuspendLayout()
    
  def __exit__(self, t, v, tr):
    self.ctl.ResumeLayout(False)
    self.ctl.PerformLayout()

class CodeInsertForm(Forms.Form):
  
  @property
  def Code(self):
    return self.code_text_box.Text
  
  def __init__(self):
  
    self.bottom_panel = Forms.Panel(
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
      
    self.ok_button = Forms.Button(
      Anchor = Forms.AnchorStyles.Right,
      DialogResult = Forms.DialogResult.OK,
      Size = Drawing.Size(75,26),
      Text = "OK",
      )
      
    self.cancel_button = Forms.Button(
      Anchor = Forms.AnchorStyles.Right,
      DialogResult = Forms.DialogResult.Cancel,
      Size = Drawing.Size(75,26),
      Text = "Cancel",
      )

    with LayoutCtxMgr(self):
      self.ClientSize = Drawing.Size(640,480)
      self.Controls.Add(self.code_text_box)
      self.Controls.Add(self.bottom_panel)
      self.Text = "Insert Code to be Pygmented"

    with LayoutCtxMgr(self.bottom_panel):
      self.bottom_panel.Controls.Add(self.ok_button)
      self.bottom_panel.Controls.Add(self.cancel_button)
      
      vmargin = (self.bottom_panel.Size.Height - self.cancel_button.Size.Height) / 2
      cancel_left = self.bottom_panel.Size.Width - vmargin - self.cancel_button.Size.Width
      ok_left = cancel_left - vmargin - self.ok_button.Size.Width
      self.cancel_button.Location = Drawing.Point(cancel_left, vmargin)
      self.ok_button.Location = Drawing.Point(ok_left, vmargin)
      
class PygmentedCodeEditor(SmartContentEditor):
  def __init__(self): 
    self.panel = Forms.Panel(
      )
    self.label = Forms.Label(
      Text = "Pygmented Code",
      Location = Drawing.Point(3,0),
      )
    self.lexer_label = Forms.Label(
      Text = "Language Lexer",
      Location = Drawing.Point(3,29),
      )
    self.style_label = Forms.Label(
      Text = "Color Scheme",
      Location = Drawing.Point(3,69),
      )
    self.lexer_selector = Forms.ComboBox(
      DropDownStyle = Forms.ComboBoxStyle.DropDownList,
      Location = Drawing.Point(3, 45),
      Size = Drawing.Size(144, 21),
      )
    for lexer in lexers:
      self.lexer_selector.Items.Add(lexer)
      
    self.style_selector = Forms.ComboBox(
      DropDownStyle = Forms.ComboBoxStyle.DropDownList,
      Location = Drawing.Point(3, 85),
      Size = Drawing.Size(144, 21),
      )
    for style in styles:
      self.style_selector.Items.Add(style)
      
    with LayoutCtxMgr(self):
      self.Text = "Pygmented Code"
      self.Controls.Add(self.panel)
      
      self.panel.Controls.Add(self.label)
      self.panel.Controls.Add(self.lexer_selector)
      self.panel.Controls.Add(self.style_selector)
      self.panel.Controls.Add(self.lexer_label)
      self.panel.Controls.Add(self.style_label)
            
    self.panel.Size = self.Size

def CreateContent(dialogOwner, newContent):
  frm = CodeInsertForm()
  result = frm.ShowDialog(dialogOwner)
  if result == Forms.DialogResult.OK:
    newContent.Properties["code"] = frm.Code
  return result
    
def CreateEditor(editorSite):
  return PygmentedCodeEditor()
  
def GeneratePublishHtml(content, publishingContext):
  return "<pre>\n" + content.Properties["code"] + "\n</pre>"
  