from __future__ import with_statement

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('WindowsLive.Writer.Api')

from System.Windows import Forms
from System import Drawing
from WindowsLive.Writer.Api import SmartContentEditor

from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles, get_style_by_name

from pygments.formatter import Formatter

class DevHawkHtmlFormatter(Formatter):
  def __init__(self, **options):
        Formatter.__init__(self, **options)

        # create a dict of (start, end) tuples that wrap the
        # value of a token so that we can use it in the format
        # method later
        self.styles = {}

        # we iterate over the `_styles` attribute of a style item
        # that contains the parsed style values.
        for token, style in self.style:
            start = end = ''
            # a style item is a tuple in the following form:
            # colors are readily specified in hex: 'RRGGBB'
            if style['color']:
                start += '<span style="color:#%s">' % style['color']
                end = '</span>' + end
            if style['bold']:
                start += '<b>'
                end = '</b>' + end
            if style['italic']:
                start += '<i>'
                end = '</i>' + end
            if style['underline']:
                start += '<u>'
                end = '</u>' + end
            self.styles[token] = (start, end)


  def format(self, tokensource, outfile):
        # lastval is a string we use for caching
        # because it's possible that an lexer yields a number
        # of consecutive tokens with the same token type.
        # to minimize the size of the generated html markup we
        # try to join the values of same-type tokens here
        lastval = ''
        lasttype = None

        # wrap the whole output with <pre>
        outfile.write('<div style="font-family: consolas, lucida console, courier, monospace">\n')

        for ttype, value in tokensource:
            value = value.replace(' ', '&#160;')
            value = value.replace("<", '&lt;')
            value = value.replace(">", '&gt;')
            value = value.replace('\n', '<br/>\n')
            # if the token type doesn't exist in the stylemap
            # we try it with the parent of the token type
            # eg: parent of Token.Literal.String.Double is
            # Token.Literal.String
            while ttype not in self.styles:
                ttype = ttype.parent
            if ttype == lasttype:
                # the current token type is the same of the last
                # iteration. cache it
                lastval += value
            else:
                # not the same token as last iteration, but we
                # have some data in the buffer. wrap it with the
                # defined style and write it to the output file
                if lastval:
                    stylebegin, styleend = self.styles[lasttype]
                    outfile.write(stylebegin + lastval + styleend)
                # set lastval/lasttype to current values
                lastval = value
                lasttype = ttype

        # if something is left in the buffer, write it to the
        # output file, then close the opened <pre> tag
        if lastval:
            stylebegin, styleend = self.styles[lasttype]
            outfile.write(stylebegin + lastval + styleend)
        outfile.write('</div>\n')

class LexerItem(object):
  def __init__(self, lang_tuple):
    self.longname = lang_tuple[0]
    self.lookup = lang_tuple[1][0]
    
  def __str__(self):
    return self.longname
    
  def ToString(self):
    return self.longname

lexers = [LexerItem(l) for l in get_all_lexers()]
lexers.sort(key=lambda l: l.longname)
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
  def __init__(self, editorSite): 
    self.editor_site = editorSite
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
    
    self.lexer_selector.SelectionChangeCommitted += self.LexerSelectionChangeCommitted
    self.lexer_selector.SelectionChangeCommitted += self.StyleSelectionChangeCommitted
    
    with LayoutCtxMgr(self):
      self.Text = "Pygmented Code"
      self.Controls.Add(self.panel)
      
      self.panel.Controls.Add(self.label)
      self.panel.Controls.Add(self.lexer_selector)
      self.panel.Controls.Add(self.style_selector)
      self.panel.Controls.Add(self.lexer_label)
      self.panel.Controls.Add(self.style_label)
            
    self.panel.Size = self.Size

  def LexerSelectionChangeCommitted(self, sender, args):
    self.SelectedContent.Properties["lexer"] = self.lexer_selector.SelectedItem.lookup
    self.OnContentEdited()

  def StyleSelectionChangeCommitted(self, sender, args):
    self.SelectedContent.Properties["style"] = self.style_selector.SelectedItem
    self.OnContentEdited()
  
def CreateContent(dialogOwner, newContent):
  frm = CodeInsertForm()
  result = frm.ShowDialog(dialogOwner)
  if result == Forms.DialogResult.OK:
    newContent.Properties["code"] = frm.Code
  return result
    
def CreateEditor(editorSite):
  return PygmentedCodeEditor(editorSite)
  
def GeneratePublishHtml(content, publishingContext):
  Forms.MessageBox.Show("GeneratePublishHtml")
  code = content.Properties["code"]
  try:
    lexer = get_lexer_by_name(content.Properties["lexer"])
  except:
    lexer = get_lexer_by_name("text")
  
  if content.Properties["style"]:
    formatter = DevHawkHtmlFormatter(style=content.Properties["style"])
  else:
    formatter = DevHawkHtmlFormatter()
    
  return highlight(code, lexer, formatter)
