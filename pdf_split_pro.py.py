import os
import re
import threading
import time
import datetime

import fitz
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


class PDFSplit:
    def __init__(self):
        self.root = tk.Tk()
    
    def extract_names_from_pdf(self, pdf_path: str, keywords: list[str]) -> list[str]:
        with fitz.open(pdf_path) as pdf_document:
            names = []
            keyword_pattern = '|'.join([re.escape(keyword.lower()) for keyword in keywords])

            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                page_text = page.get_text().lower()
                matches = re.finditer(keyword_pattern, page_text)

                for match in matches:
                    start_index = match.start()
                    end_index = page_text.find('\n', start_index)
                    if end_index == -1:
                        end_index = None
                    data = page_text[start_index:end_index]
                    names.append(data.strip())

            return names

    def separar_contracheques(self, pdf_path: str, keywords: list[str], progress_var: tk.DoubleVar, label_progress: ttk.Label, output_folder: str):
        try:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                if not output_folder:
                    output_folder = os.path.join(os.path.dirname(pdf_path), "PDFs")
                    os.makedirs(output_folder, exist_ok=True)

                names = self.extract_names_from_pdf(pdf_path, keywords)

                total_pages = len(pdf_reader.pages)
                for page_num in range(total_pages):
                    page = pdf_reader.pages[page_num]

                    if page_num < len(names):
                        name = names[page_num]
                        output_filename = os.path.join(output_folder, f"{name}.pdf")
                    else:
                        output_filename = os.path.join(output_folder, f"page_{page_num + 1}.pdf")

                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(page)

                    with open(output_filename, 'wb') as output_file:
                        pdf_writer.write(output_file)

                        progress = (page_num + 1) / total_pages * 100
                        progress_var.set(progress)
                        label_progress.config(text=f"Separando: {int(progress)}%")
                        self.root.update_idletasks()
                        time.sleep(0.1)

            messagebox.showinfo("Sucesso", "PDFs foram separados com sucesso!")
        except PyPDF2.errors.PdfReadError as e:
            messagebox.showerror("Erro no PDF", f"Ocorreu um erro ao ler o PDF: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

    def selecionar_arquivo_pdf(self) -> None:
        arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        if arquivo:
            self.entry_pdf_path.delete(0, tk.END)
            self.entry_pdf_path.insert(0, arquivo)

    def verificar_pdf(self, arquivo: str) -> bool:
        if not arquivo.lower().endswith('.pdf'):
            messagebox.showwarning("Arquivo inválido", "Por favor, selecionar um arquivo PDF.")
            return False
        return True

    def selecionar_diretorio_saida(self) -> None:
        diretorio = filedialog.askdirectory()
        if diretorio:
            self.entry_output_folder.delete(0, tk.END)
            self.entry_output_folder.insert(0, diretorio)

    def criar_historico(self, pdf_path: str, keywords: list[str], output_folder: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        historico = {
            'arquivo': pdf_path,
            'palavras-chave': " ".join(keywords),
            'diretorio_saida': output_folder,
            'data': timestamp
        }
        historico_path = os.path.join(os.path.expanduser("~"), ".historico_separacao.txt")
        with open(historico_path, "a") as file:
            file.write(str(historico) + "\n")

    def iniciar_separacao_thread(self):
        pdf_path = self.entry_pdf_path.get()
        keywords = self.entry_keywords.get().split()
        output_folder = self.entry_output_folder.get()

        if not pdf_path or not keywords:
            messagebox.showwarning("Entrada inválida", "Por favor, insira o caminho do PDF e palavras-chave.")
            return
        if not self.verificar_pdf(pdf_path):
            return

        self.progress_var.set(0)
        self.label_progress.config(text="Separando: 0%")
        threading.Thread(target=self.separar_contracheques, args=(pdf_path, keywords, self.progress_var, self.label_progress, output_folder)).start()
        self.criar_historico(pdf_path, keywords, output_folder)

    def window_tk(self):
        self.root.title("PDF Split Pro PDF - Wesley Alexsander")
        self.root.geometry("900x550")
        self.root.minsize(600, 400)
        self.root.config(bg="#f4f4f4")

        style = ttk.Style()
        style.configure('TButton', font=('Arial', 14), padding=12, relief='flat', background='#4CAF50', foreground='white', width=25)
        style.configure('TLabel', font=('Arial', 16), background='#f4f4f4', foreground='#4CAF50')
        style.configure('TEntry', font=('Arial', 14), padding=6, width=50)
        style.configure('TFrame', background='#f4f4f4')

        frame = ttk.Frame(self.root, padding="20", style="TFrame")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        label_title = ttk.Label(frame, text="Ferramenta de manipulação de PDF", font=("Arial", 18, "bold"), anchor="center")
        label_title.grid(row=0, column=0, columnspan=3, pady=20)

        ttk.Label(frame, text="Caminho do arquivo PDF:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.entry_pdf_path = ttk.Entry(frame, width=50)
        self.entry_pdf_path.grid(row=1, column=1, padx=10)
        ttk.Button(frame, text="Selecionar PDF", command=self.selecionar_arquivo_pdf).grid(row=1, column=2, padx=10)

        ttk.Label(frame, text="Palavras-chave (separadas por espaço):").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.entry_keywords = ttk.Entry(frame, width=50)
        self.entry_keywords.grid(row=2, column=1, pady=10)

        ttk.Label(frame, text="Diretório de saída (opcional):").grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.entry_output_folder = ttk.Entry(frame, width=50)
        self.entry_output_folder.grid(row=3, column=1, pady=10)
        ttk.Button(frame, text="Selecionar diretório", command=self.selecionar_diretorio_saida).grid(row=3, column=2, padx=10)

        self.progress_var = tk.DoubleVar()
        ttk.Progressbar(frame, variable=self.progress_var, maximum=100).grid(row=4, column=0, columnspan=3, pady=20)

        self.label_progress = ttk.Label(frame, text="Separando: 0%", font=("Arial", 14))
        self.label_progress.grid(row=5, column=0, columnspan=3)

        ttk.Button(frame, text="Separar", command=self.iniciar_separacao_thread).grid(row=6, column=0, columnspan=3, pady=10)

        self.root.mainloop()


if __name__ == "__main__":
    app = PDFSplit()
    app.window_tk()
