using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace DevHawk
{
    public partial class CodeInsertForm : Form
    {
        public CodeInsertForm()
        {
            InitializeComponent();
        }

        public string Code
        {
            get { return this.code_text_box.Text; }
            set { this.code_text_box.Text = value; }
        }
    }
}
