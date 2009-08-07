using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Reflection;

namespace DevHawk
{
    public partial class CodeInsertForm : Form
    {
        public CodeInsertForm()
        {
            InitializeComponent();

            this.Text += string.Format(" (v{0})", PygmentsCodeSource.AssemblyVersion);
        }

        public string Code
        {
            get { return this.code_text_box.Text; }
            set { this.code_text_box.Text = value; }
        }
    }
}
