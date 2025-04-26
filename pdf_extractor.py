import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import PyPDF2
import zipfile
import io
import logging

# Set up logging
logging.basicConfig(
    filename='pdf_extractor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class HelpWindow:
    def __init__(self, parent):
        self.help_window = tk.Toplevel(parent)
        self.help_window.title("PDF Extractor Manual")
        self.help_window.geometry("600x400")
        self.help_window.resizable(True, True)
        manual_text = (
            "PDF Page Extractor - User Manual\n\n"
            "1. Select the PDF directory using the 'Browse' button.\n"
            "2. Enter the page numbers to extract (comma-separated, e.g., 1,2,3).\n"
            "3. Choose the output ZIP file location using the 'Browse' button.\n"
            "4. Click 'Start Extraction' to begin.\n\n"
            "Troubleshooting:\n"
            "- Ensure all fields are filled.\n"
            "- Page numbers must be valid integers.\n"
            "- Check the log file for errors."
        )
        text = tk.Text(self.help_window, wrap=tk.WORD, font=("Segoe UI", 11))
        text.insert(tk.END, manual_text)
        text.config(state=tk.DISABLED)
        text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

class PDFExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Page Extractor")
        self.root.geometry("600x320")
        self.root.minsize(500, 250)
        self.root.resizable(True, True)
        self.set_theme()

        self.pdf_path = tk.StringVar()
        self.output_zip_file = tk.StringVar()
        self.pages_to_extract = tk.StringVar(value="2,3")

        self.create_toolbar()
        self.create_widgets()

    def set_theme(self):
        style = ttk.Style(self.root)
        if "clam" in style.theme_names():
            style.theme_use("clam")
        style.configure("TLabel", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 11))
        style.configure("TEntry", font=("Segoe UI", 11))

    def create_toolbar(self):
        toolbar = ttk.Frame(self.root, padding=(5, 2))
        toolbar.grid(row=0, column=0, columnspan=3, sticky="ew")
        help_btn = ttk.Button(toolbar, text="Help", command=self.show_help)
        help_btn.pack(side=tk.RIGHT, padx=2)

    def show_help(self):
        HelpWindow(self.root)

    def create_widgets(self):
        content = ttk.Frame(self.root, padding=15)
        content.grid(row=1, column=0, sticky="nsew")
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(1, weight=1)

        # PDF Directory
        ttk.Label(content, text="PDF Directory:").grid(row=0, column=0, sticky="e", padx=5, pady=8)
        pdf_entry = ttk.Entry(content, textvariable=self.pdf_path)
        pdf_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=8)
        ttk.Button(content, text="Browse", command=self.browse_pdf).grid(row=0, column=2, padx=5, pady=8)

        # Pages to Extract
        ttk.Label(content, text="Pages (e.g., 1,2,3):").grid(row=1, column=0, sticky="e", padx=5, pady=8)
        pages_entry = ttk.Entry(content, textvariable=self.pages_to_extract)
        pages_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=8)
        
        # Output ZIP
        ttk.Label(content, text="Output ZIP:").grid(row=2, column=0, sticky="e", padx=5, pady=8)
        output_entry = ttk.Entry(content, textvariable=self.output_zip_file)
        output_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=8)
        ttk.Button(content, text="Browse", command=self.browse_output).grid(row=2, column=2, padx=5, pady=8)

        # Start Button
        start_btn = ttk.Button(content, text="Start Extraction", command=self.start_extraction)
        start_btn.grid(row=3, column=0, columnspan=3, pady=20)

    def browse_pdf(self):
        directory = filedialog.askdirectory()
        if directory:
            self.pdf_path.set(directory)
            logging.info(f"PDF directory selected: {directory}")

    def browse_output(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("ZIP files", "*.zip")]
        )
        if file:
            self.output_zip_file.set(file)
            logging.info(f"Output ZIP file selected: {file}")

    def start_extraction(self):
        try:
            pdf_dir = self.pdf_path.get()
            output_zip = self.output_zip_file.get()
            pages = [int(p.strip()) for p in self.pages_to_extract.get().split(',') if p.strip().isdigit()]

            if not pdf_dir or not output_zip or not pages:
                messagebox.showerror("Error", "Please fill in all fields")
                logging.error("Extraction failed: Not all fields filled in.")
                return

            logging.info(f"Starting extraction: Directory={pdf_dir}, Output={output_zip}, Pages={pages}")

            with zipfile.ZipFile(output_zip, 'w') as zip_file:
                for pdf_file in os.listdir(pdf_dir):
                    if pdf_file.lower().endswith('.pdf'):
                        pdf_path = os.path.join(pdf_dir, pdf_file)
                        logging.info(f"Processing file: {pdf_path}")
                        with open(pdf_path, 'rb') as file:
                            pdf_reader = PyPDF2.PdfReader(file)
                            pdf_writer = PyPDF2.PdfWriter()

                            for page_num in pages:
                                if 1 <= page_num <= len(pdf_reader.pages):
                                    pdf_writer.add_page(pdf_reader.pages[page_num - 1])
                                else:
                                    logging.warning(f"Page {page_num} out of range for file {pdf_file}")

                            output_filename = f"extracted_{pdf_file}"
                            pdf_bytes = io.BytesIO()
                            pdf_writer.write(pdf_bytes)
                            pdf_bytes.seek(0)
                            zip_file.writestr(output_filename, pdf_bytes.read())

            messagebox.showinfo("Success", "PDF pages extracted successfully!")
            logging.info("Extraction completed successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            logging.error(f"Extraction failed: {str(e)}")

def main():
    root = tk.Tk()
    app = PDFExtractorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
