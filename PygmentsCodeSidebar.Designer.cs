namespace DevHawk
{
    partial class PygmentsCodeSidebar
    {
        /// <summary> 
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(PygmentsCodeSidebar));
            this.label1 = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.label2 = new System.Windows.Forms.Label();
            this.language_selector = new System.Windows.Forms.ComboBox();
            this.edit_code_button = new System.Windows.Forms.Button();
            this.style_selector = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Arial", 15.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(30, 78);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(113, 24);
            this.label1.TabIndex = 0;
            this.label1.Text = "Pygments";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(49, 0);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(75, 75);
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(3, 139);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(119, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "Programming Lanugage";
            // 
            // language_selector
            // 
            this.language_selector.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.language_selector.FormattingEnabled = true;
            this.language_selector.Location = new System.Drawing.Point(3, 155);
            this.language_selector.Name = "language_selector";
            this.language_selector.Size = new System.Drawing.Size(154, 21);
            this.language_selector.Sorted = true;
            this.language_selector.TabIndex = 3;
            this.language_selector.SelectionChangeCommitted += new System.EventHandler(this.language_selector_SelectionChangeCommitted);
            // 
            // edit_code_button
            // 
            this.edit_code_button.Location = new System.Drawing.Point(3, 239);
            this.edit_code_button.Name = "edit_code_button";
            this.edit_code_button.Size = new System.Drawing.Size(154, 23);
            this.edit_code_button.TabIndex = 4;
            this.edit_code_button.Text = "Edit Code";
            this.edit_code_button.UseVisualStyleBackColor = true;
            this.edit_code_button.Click += new System.EventHandler(this.edit_code_button_Click);
            // 
            // style_selector
            // 
            this.style_selector.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.style_selector.FormattingEnabled = true;
            this.style_selector.Location = new System.Drawing.Point(3, 195);
            this.style_selector.Name = "style_selector";
            this.style_selector.Size = new System.Drawing.Size(154, 21);
            this.style_selector.Sorted = true;
            this.style_selector.TabIndex = 6;
            this.style_selector.SelectionChangeCommitted += new System.EventHandler(this.style_selector_SelectionChangeCommitted);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(3, 179);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(73, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Color Scheme";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Arial", 15.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(11, 102);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(150, 24);
            this.label4.TabIndex = 7;
            this.label4.Text = "For WL Writer";
            // 
            // PygmentsCodeSidebar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.label4);
            this.Controls.Add(this.style_selector);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.edit_code_button);
            this.Controls.Add(this.language_selector);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.label1);
            this.Name = "PygmentsCodeSidebar";
            this.Size = new System.Drawing.Size(172, 500);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox language_selector;
        private System.Windows.Forms.Button edit_code_button;
        private System.Windows.Forms.ComboBox style_selector;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
    }
}
