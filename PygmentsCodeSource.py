from __future__ import with_statement
import clr
clr.AddReference('System.Windows.Forms')

from System.Windows import Forms
from System import Drawing

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
      
    


def CreateContent(dialogOwner, newContent):
  frm = CodeInsertForm()
  result = frm.ShowDialog(dialogOwner)
  if result == Forms.DialogResult.OK:
    newContent.Properties["code"] = frm.Code
  return result
    
def CreateEditor(editorSite):
  return None
  
def GeneratePublishHtml(content, publishingContext):
  return "<pre>\n" + content.Properties["code"] + "\n</pre>"
  