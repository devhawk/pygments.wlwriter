using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using WindowsLive.Writer.Api;

namespace DevHawk
{
    public partial class PygmentsCodeSidebar : SmartContentEditor
    {
        public PygmentsCodeSidebar(IEnumerable<PygmentLanguage> languages, IEnumerable<string> styles)
        {
            InitializeComponent();

            foreach (var lang in languages)
                language_selector.Items.Add(lang);

            foreach (var style in styles)
                style_selector.Items.Add(style);
        }

        private void edit_code_button_Click(object sender, EventArgs e)
        {
            var form = new CodeInsertForm();
            form.Code = SelectedContent.Properties["code"];
            var result = form.ShowDialog(this);

            if (result == DialogResult.OK)
            {
                SelectedContent.Properties["code"] = form.Code;
                SelectedContent.Properties.Remove("html");
                OnContentEdited();
            }
        }

        private void language_selector_SelectionChangeCommitted(object sender, EventArgs e)
        {
            var lang = (PygmentLanguage)language_selector.SelectedItem;
            SelectedContent.Properties["language"] = lang.LookupName;
            SelectedContent.Properties.Remove("html");
            OnContentEdited();
        }

        private void style_selector_SelectionChangeCommitted(object sender, EventArgs e)
        {
            var style = (string)style_selector.SelectedItem;
            SelectedContent.Properties["style"] = style;
            SelectedContent.Properties.Remove("html");
            OnContentEdited();
        }
    }
}
