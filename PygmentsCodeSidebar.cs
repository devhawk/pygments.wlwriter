using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Text;
using System.Windows.Forms;
using WindowsLive.Writer.Api;

namespace DevHawk
{
    public partial class PygmentsCodeSidebar : SmartContentEditor
    {
        public PygmentsCodeSidebar(List<PygmentLanguage> languages)
        {
            InitializeComponent();

            foreach (var lang in languages)
            {
                language_selector.Items.Add(lang);
            }
        }

        private void language_selector_SelectedIndexChanged(object sender, EventArgs e)
        {
            var lang = (PygmentLanguage)language_selector.SelectedItem;
            SelectedContent.Properties["language"] = lang.LookupName;
            OnContentEdited();
        }

        private void edit_code_button_Click(object sender, EventArgs e)
        {
            var form = new CodeInsertForm();
            form.Code = SelectedContent.Properties["code"];
            var result = form.ShowDialog(this);

            if (result == DialogResult.OK)
            {
                SelectedContent.Properties["code"] = form.Code;
                OnContentEdited();
            }
        }
    }
}
