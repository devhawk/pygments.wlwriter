from __future__ import with_statement
import sys
sys.path.append(r'C:\Program Files\Windows Live\Writer')

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

import PygmentsCodeSource 

from System.Windows import Forms
from System import Drawing

from System.Collections.Generic import Dictionary


class LayoutCtxMgr(object):
  def __init__(self, ctl):
    self.ctl = ctl
    
  def __enter__(self):
    self.ctl.SuspendLayout()
    
  def __exit__(self, t, v, tr):
    self.ctl.ResumeLayout(False)
    self.ctl.PerformLayout()
    
class SmartContentMock(object):
  __slots__ = ['Properties']
  def __init__(self):
    self.Properties = Dictionary[str,str]() 

class WriterMock(Forms.Form):
  def __init__(self):
    
    self.show_plugin_menu_item = Forms.ToolStripMenuItem(
      Text = "Show Writer Plugin"
      )
    self.edit_content_menu_item = Forms.ToolStripMenuItem(
      Text = "Edit Content Plugin"
      )
    self.show_plugin_menu_item.Click += self.ShowPlugin
    self.edit_content_menu_item.Click += self.EditContent      
    self.menustrip = Forms.MenuStrip()
    self.menustrip.Items.Add(self.show_plugin_menu_item)    
    self.menustrip.Items.Add(self.edit_content_menu_item)
    
    self.html_view = Forms.TextBox(
      Dock = Forms.DockStyle.Fill,
      Multiline = True,
      WordWrap = False,
      ReadOnly = True,
      ScrollBars = Forms.ScrollBars.Both
      )
      
    self.splitter = Forms.SplitContainer(
      Dock = Forms.DockStyle.Fill,
      )
    
    self.splitter.Panel1.Controls.Add(self.html_view)
    
    with LayoutCtxMgr(self):
      self.Text = "Mock Writer"
      self.ClientSize = Drawing.Size(640,480)
      self.Controls.Add(self.splitter)
      self.Controls.Add(self.menustrip)
    
    self.splitter.SplitterDistance = self.splitter.Size.Width / 2
  
  def EditContent(self, sender, args):
    reload(PygmentsCodeSource)

    print PygmentsCodeSource.CreateEditor(None)
    
  def ShowPlugin(self, sender, args):
    reload(PygmentsCodeSource)
    
    content = SmartContentMock()
    if PygmentsCodeSource.CreateContent(self, content) == Forms.DialogResult.OK:
      html = PygmentsCodeSource.GeneratePublishHtml(content, None)
      self.html_view.Text = html

Forms.Application.Run(WriterMock())