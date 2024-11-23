import os
import PyPDF2
import fitz
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import time 
import re
import threading
import datetime

def extract_names_from_pdf(pdf_path, keywords):
    pdf_document = fitz.open(pdf_path)
    names = []
    keyword_pattern = '|'.join([re.escape(keyword.lower()) for keyword in keyword])

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


    pdf_document.close()
    return names

def separar_contracheques(pdf_path, keywords, progress_var, label_progress, output_folder):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            if not output_folder:
                output_folder = os.path.join(os.path.dirname(pdf_path), "PDFs")
                os.makedirs(output_folder, exist_ok=True)

            names = extract_names_from_pdf(pdf_path, keywords)

            total_pages = len(pdf_reader.pages)
            for page_num in range(total_pages):
                page = pdf_reader.pages[page_num]

                if page_num < len(names):
                    name = names[page_num]
                    output_filename = os.path.join(output_folder, f"{name}.pdf")
                else:
                    output_filename = os.path.join(output_folder, f"page_{page_num + 1}.pdf")

                pdf_writer = PyPDF.PdfWriter()
                pdf_writer.add_page(page)

                with open(output_filename, 'wb') as output_file:
                    pdf_writer.write(output_file)

                    progress = (page_num + 1) / total_pages * 100
                    progress_var.set(progress)
                    label_progress.config(text=f"Separando: {int(progress)}%")
                    root.update_idletasks()
                    time.sleep(0.1)

        messagebox.showinfo("Sucesso", "PDFs foram separados com sucesso!")
    except PyPDF2.utils.PdfReadError as e:
        messagebox.showerror("Erro no PDF", f"Ocorreu um erro ao ler o PDF: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

def selecionar_arquivo_pdf():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if arquivo:
        entry_pdf_path.delete(0, tk.END)
        entry_pdf_path.insert(0, arquivo)

def verificar_pdf(arquivo):
    if not arquivo.lower().endswith('.pdf'):
        messagebox.showwarning("Arquivo inválido", "Por favor, selecionar um arquivo PDF.")
        return False
    return True

def selecionar_diretorio_saida():
    diretorio = filedialog.askdirectory()
    if diretorio:
        entry_output_folder.delete(0, tk.END)
        entry_output_folder.insert(0, diretorio)

def criar_historico(pdf_path, keywords, output_folder):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historico = {
        'arquivo': pdf_path,
        'palavras-chave': "".join(keywords),
        'diretorio_saida': output_folder,
        'data': timestamp

    }

    historico_path = os.path.expanduser("~/.historico_separacao.txt")
    with open(historico_path, "a") as file:
        file.write(str(historico) + "\n")

def iniciar_separacao_thread():
    pdf_path = entry_pdf_path.get()
    keywords = entry_keywords.get().split()
    output_folder = entry_output_folder.get()

    if not pdf_path or not keywords:
        messagebox.showwaring("Entrada inválida", "Por favor, insira o caminho do PDF e palavras-chave.")
        return
    if not verificar_pdf(pdf_path):
        return

    progress_var.set(0)
    label_progress.config(text="Separando: 0%")
    threading.Thread(target=separar_contracheques, args=(pdf_path, keywords, progress_var, label_progress, output_folder)).strat()

    criar_historico(pdf_path, keywords, output_folder)

root = tk.Tk()
root.title("PDF Split Pro PDF - Wesley Alexsander")
root.geometry("900x550")
root.minsize(600, 400)
root.config(bg="#f4f4f4")

style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=12, relief='flat', background='#4CAf50', foregrpund='white', width=25)
style.configure('TLabel', font=('Arial', 16), background='#f4f4f4', foreground='#4CAF50')
style.configure('TEntry', font=('Arial', 14), padding=6, width=50)
style.configure('TFrame', background='#f4f4f4')
style.configure('TLabelFrame', background='#f4f4f4')

frame = ttk.Frame(root, padding="20", style="TFrame")
frame.pack(padx=20, pady=20, fill="both", expand=True)

label_title = ttk.Label(frame, text="Ferramenta de manipulação de PDF", font=("Arial", 18, "bold"), anchor="center")
label_title.grid(row=0, column=0, columnspan=3, pady=20)

label_pdf_path = ttk.Label(frame, text="Caminho do arquivo PDF:")
label_pdf_path.grid(row=1, column=0, sticky="w", padx=10, pady=10)

entry_pdf_path = ttk.Entry(frame, width=50)
entry_pdf_path.grid(row=1, column=1, padx=10)

btn_selecionar_pdf = ttk.Button(frame, text="Selecionar PDF", command=selecionar_arquivo_pdf)
btn_selecionar_pdf.grid(row=1, column=2, padx=10)

label_keywords = ttk.Label(frame, text="Palavra-chave(separadas por espaço):")
label_keywords.grid(row=2, column=0, sticky="w", padx=10, pady=10)

entry_keywords = ttk.Entry(frame, width=50)
entry_keywords.grid(row=2, column=1, pady=10)

label_output_folder = ttk.Label(frame, text="Diretório de saída (opcional):")
label_output_folder.grid(row=3, column=0, sticky="w", padx=10, pady=10)

label_output_folder = ttk.Entry(frame, width=50)


entry_output_folder = ttk.Entry(frame, width=50)
entry_output_folder.grid(row=3, column=1, pady=10)

btn_selecionar_diretorio = ttk.Button(frame, text="Selecionar diretório", command=selecionar_diretorio_saida)
btn_selecionar_diretorio.grid(row=3, column=2, padx=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100)
progress_bar.grid(row=4, column=0, columnspan=3, pady=20)

label_progress = ttk.Label(frame, text="Separando: %0", font=("Arial", 14))
label_progress.grid(row=5, column=0, columnspan=3)

btn_separar = ttk.Button(frame, text="Separar", command=iniciar_separacao_thread)
btn_separar.grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()
