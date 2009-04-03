using System;
using System.Windows.Forms;
using WindowsLive.Writer.Api;
using Microsoft.Scripting.Hosting;
using IronPython.Runtime;
using System.IO;

namespace DevHawk
{
    [WriterPlugin("2EC9848E-067D-4e79-BAB7-06CA927DB962", "Pygments.WLWriter",
        Description = "Code Colorizer using Python pygments package", 
        ImagePath="icon_16.png",
        PublisherUrl = "http://devhawk.net")]
    [InsertableContentSource("Insert Pygmented Code", SidebarText = "Pygmented Code")]
    public class PygmentsCodeSource : SmartContentSource
    {
        static ScriptEngine _engine;
        static ScriptSource _source;

        ScriptScope _scope;
        PythonFunction _CreateContent;
        PythonFunction _CreateEditor;
        PythonFunction _GeneratePublishHtml;

        private void InitializeHosting()
        {
            var asm = System.Reflection.Assembly.GetAssembly(typeof(PygmentsCodeSource));
            var folder = Path.GetDirectoryName(asm.Location);
            
            _engine = IronPython.Hosting.Python.CreateEngine();
            _engine.SetSearchPaths(new string[] { folder });

            _source = _engine.CreateScriptSourceFromFile(Path.Combine(folder, "PygmentsCodeSource.py"));
        }

        public PygmentsCodeSource()
        {
            if (_engine == null)
                InitializeHosting();

            try
            {
                _scope = _engine.CreateScope();
                _source.Execute(_scope);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, ex.Source);
            }
        }

        public override DialogResult CreateContent(IWin32Window dialogOwner, ISmartContent newContent)
        {
            if (_CreateContent == null)
               _CreateContent = _scope.GetVariable<PythonFunction>("CreateContent");

            return (DialogResult)_CreateContent.Target.DynamicInvoke(dialogOwner, newContent);
        }

        public override SmartContentEditor CreateEditor(ISmartContentEditorSite editorSite)
        {
            if (_CreateEditor == null)
                _CreateEditor = _scope.GetVariable<PythonFunction>("CreateEditor");

            return (SmartContentEditor)_CreateEditor.Target.DynamicInvoke(editorSite);
        }

        public override string GeneratePublishHtml(ISmartContent content, IPublishingContext publishingContext)
        {
            if (_GeneratePublishHtml == null)
                _GeneratePublishHtml = _scope.GetVariable<PythonFunction>("GeneratePublishHtml");

            return (string)_GeneratePublishHtml.Target.DynamicInvoke(content, publishingContext);

        }
    }
}
