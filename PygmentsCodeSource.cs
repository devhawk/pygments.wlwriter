using System;
using System.Windows.Forms;
using WindowsLive.Writer.Api;

namespace DevHawk
{
    [WriterPlugin("2EC9848E-067D-4e79-BAB7-06CA927DB962", "Pygments.WLWriter",
    Description = "Code Colorizer using Python pygments package",
    PublisherUrl = "http://devhawk.net")]
    [InsertableContentSource("Insert Pygmented Code", SidebarText = "Pygmented Code")]
    public class PygmentsCodeSource : SmartContentSource
    {
        public override System.Windows.Forms.DialogResult CreateContent(IWin32Window dialogOwner, ISmartContent newContent)
        {
            throw new NotImplementedException();
        }

        public override SmartContentEditor CreateEditor(ISmartContentEditorSite editorSite)
        {
            throw new NotImplementedException();
        }

        public override string GeneratePublishHtml(ISmartContent content, IPublishingContext publishingContext)
        {
            throw new NotImplementedException();
        }

        public override string GenerateEditorHtml(ISmartContent content, IPublishingContext publishingContext)
        {
            throw new NotImplementedException();
        }
    }
}
