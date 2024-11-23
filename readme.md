# PDF Split PRO

**Autor**: Wesley Alexsander  
**Licença**: MIT  
**Linguagem**: Python  

## 📖 Sobre a Ferramenta

O **PDF Split PRO** é uma ferramenta simples e eficaz para separar páginas de um arquivo PDF, nomeá-las automaticamente com base em palavras-chave presentes no conteúdo e salvar cada página como um arquivo PDF individual. 

Essa ferramenta foi desenvolvida para resolver um problema que enfrentei como jovem aprendiz na área administrativa. Durante esse período, precisei usar uma ferramenta chamada **PDF24**, onde era necessário enviar, manualmente, uma página por vez de contracheques para separar, nomear e encaminhar aos colaboradores. O processo era demorado e repetitivo.

Após ser efetivado, decidi criar essa ferramenta para ajudar os colegas do setor de Recursos Humanos da empresa a realizarem a mesma tarefa de forma mais ágil, automatizada e confiável. O **PDF Split PRO** automatiza a separação e o nomeamento das páginas dos PDFs, tornando o processo mais eficiente.

---

## 🚀 Funcionalidades

1. **Separar Páginas do PDF**: Divide um arquivo PDF em várias páginas individuais.
2. **Nomeação Automática**: Usa palavras-chave no conteúdo das páginas para nomear os arquivos PDF gerados.
3. **Diretório Personalizado**: Salva os PDFs gerados em um diretório de saída configurável.
4. **Interface Gráfica Intuitiva**: Fácil de usar com campos para selecionar arquivos, palavras-chave e diretório de saída.
5. **Criação de Histórico**: Registra detalhes sobre cada operação realizada, incluindo o arquivo processado, palavras-chave usadas e data/hora.
6. **Barra de Progresso**: Indica visualmente o progresso do processo de separação.
7. **Sistema Responsivo**: Não trava durante a execução, mesmo em arquivos PDF grandes.

---

## 📂 Para que usar?

- Automatizar a separação de contracheques em um PDF consolidado.
- Nomear páginas individualmente com base em informações específicas contidas em cada uma.
- Facilitar a gestão de documentos PDF no setor de RH ou administrativo.

---

## 📦 Bibliotecas Necessárias

Antes de usar a ferramenta, é necessário instalar as seguintes bibliotecas:

- **PyPDF2**: Manipulação de arquivos PDF.
- **PyMuPDF (fitz)**: Extração de texto de arquivos PDF.
- **tkinter**: Criação da interface gráfica.
- **threading**: Para tornar o programa mais responsivo.

### Como instalar as dependências no Linux:

```bash
pip install PyPDF2 pymupdf tk

