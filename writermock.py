from __future__ import with_statement
import sys
sys.path.append(r'C:\Program Files\Windows Live\Writer')

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("WindowsLive.Writer.Api")
import PygmentsCodeSource 

from System.Windows import Forms
from System import Drawing

from System.Collections.Generic import Dictionary
from WindowsLive.Writer.Api import ISmartContent, IProperties

class LayoutCtxMgr(object):
  def __init__(self, ctl):
    self.ctl = ctl
    
  def __enter__(self):
    self.ctl.SuspendLayout()
    
  def __exit__(self, t, v, tr):
    self.ctl.ResumeLayout(False)
    self.ctl.PerformLayout()
    
class SmartContentMock(ISmartContent):
  class PropertiesMock(IProperties):
    def __init__(self):
      self._props = Dictionary[str,str]() 
    
    def Contains(self, name):
      return self._props.ContainsKey(name)
      
    def __getitem__(self, key):
      return self._props[key]
      
    def __setitem__(self, key, value):
      self._props[key] = value
    
  def __init__(self):
    self.Properties = SmartContentMock.PropertiesMock()
  
  def Contains(self, name):
    return self.Properties.ContainsKey(name)

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
    
    self.content = SmartContentMock()
    if PygmentsCodeSource.CreateContent(self, self.content) == Forms.DialogResult.OK:
      html = PygmentsCodeSource.GeneratePublishHtml(self.content, None)
      editor = PygmentsCodeSource.CreateEditor(None)
      editor.SelectedContent = self.content
      self.splitter.Panel2.Controls.Add(editor)
      self.html_view.Text = html

Forms.Application.Run(WriterMock())