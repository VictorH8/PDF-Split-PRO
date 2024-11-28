# PDF Split PRO

**Autor**: Wesley Alexsander  
**Licença**: GPL v3  
**Linguagem**: Python  

---

## 🔧 **Tecnologias Usadas**: 

<div align="center">
  <img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" alt="Python Logo" width="60" height="60"/>
  <img src="https://icongr.am/devicon/vim-original.svg?size=128&color=currentColor" alt="Vim Logo" width="60" height="60"/>
</div>

---

## 📖 Sobre a Ferramenta

O **PDF Split PRO** é uma ferramenta poderosa, simples e eficaz, projetada para automatizar o processo de separação de páginas de arquivos PDF e nomeação automática dessas páginas com base em palavras-chave extraídas do conteúdo do documento. 

Essa ferramenta foi criada para resolver um problema pessoal que enfrentei como jovem aprendiz na área administrativa. Durante meu trabalho, precisei usar uma ferramenta chamada **PDF24**, onde o processo de separação de contracheques envolvia o upload manual de uma página por vez. Além de ser extremamente demorado e repetitivo, o processo demandava muito tempo e atenção. 

Quando fui efetivado, decidi criar uma solução para ajudar os colegas do setor de Recursos Humanos a realizar essa tarefa de maneira mais rápida, eficiente e automatizada. O **PDF Split PRO** facilita a separação, nomeação e organização de documentos, tornando o processo muito mais ágil e confiável.

---

## 🚀 Funcionalidades

✨ **Separação de Páginas**: Divida um arquivo PDF em várias páginas individuais, extraindo o conteúdo conforme necessário.  
🖋️ **Nomeação Automática**: Utilize palavras-chave presentes no conteúdo das páginas para nomear os arquivos PDF gerados, com base nas informações extraídas.  
📁 **Diretório Personalizado**: Escolha onde deseja salvar os PDFs gerados, com a opção de definir um diretório de saída personalizado.  
🔧 **Interface Gráfica Intuitiva**: A interface foi construída com **Tkinter**, oferecendo uma maneira fácil de selecionar arquivos, inserir palavras-chave e escolher o diretório de saída.  
📝 **Criação de Histórico**: Todos os processos realizados são registrados, incluindo detalhes sobre o arquivo processado, palavras-chave usadas e data/hora da execução.  
⏳ **Barra de Progresso**: Acompanhe visualmente o progresso da separação de páginas com a barra de progresso em tempo real.  
⚙️ **Sistema Responsivo**: A ferramenta continua funcional e não trava, mesmo ao processar arquivos grandes.  

---

## 📂 Para que usar?

O **PDF Split PRO** é ideal para quem precisa:

- **Automatizar o processo de separação de contracheques** ou outros documentos em um único arquivo PDF consolidado.  
- **Nomear automaticamente páginas de um PDF** com base em informações extraídas de palavras-chave específicas em cada página.  
- **Facilitar a gestão de documentos** no setor de **RH**, administrativo ou em qualquer área que lide com documentos em PDF e precise de uma forma ágil e prática para organizar e distribuir informações.  

---

## 📦 Bibliotecas Necessárias

Antes de rodar a ferramenta, instale as seguintes dependências utilizando o **pip**:

- **PyPDF2**: Biblioteca para manipulação e extração de dados de arquivos PDF.  
- **PyMuPDF (fitz)**: Usado para extrair texto das páginas de um PDF e realizar a busca por palavras-chave.  
- **tkinter**: Ferramenta para criar interfaces gráficas de maneira simples e funcional.  
- **threading**: Para garantir que a ferramenta permaneça responsiva durante o processo de separação de páginas, especialmente em arquivos grandes.

---

## 🛠 Como Instalar

1. Clone o repositório para o seu computador:

   ```bash
   git clone https://github.com/WesleyA0101/PDF-Split-Pro.git
