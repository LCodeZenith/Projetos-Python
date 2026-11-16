# 🐍 Projetos Python

Coleção de projetos em Python, cada um com um tema diferente: programas com interface gráfica, automações, ferramentas de linha de comando, jogos e experimentos. Cada projeto fica na sua própria pasta, com o código e um README próprio explicando como usar.

> Repositório de estudo e prática. Os projetos evoluem com o tempo, e alguns são experimentos rápidos.

---

## 📚 Projetos

| Projeto | Descrição | Tecnologias | Status |
|---------|-----------|-------------|--------|
| [🚗 AutoScan Carros](./autoscan-carros) | Consulta de carros com interface gráfica: mostra no que cada modelo e cor são bons e ruins, com busca tolerante a erros de digitação | Python, tkinter, difflib | ✅ Funcional |

*(Novos projetos entram nesta tabela conforme forem sendo adicionados.)*

**Legenda de status:** ✅ Funcional · 🚧 Em desenvolvimento · 🧪 Experimento · 💤 Pausado

---

## ▶️ Como rodar um projeto

**Requisitos gerais:** Python 3 instalado ([python.org](https://www.python.org/downloads/)). Os projetos são desenvolvidos com Python 3.14, e cada um informa no seu README se precisa de algo a mais.

1. Clique em **Code → Download ZIP** nesta página e extraia o arquivo (ou clone o repositório com o Git).
2. Abra um terminal **dentro da pasta do projeto** que você quer rodar. No Windows, uma forma fácil é abrir a pasta no Explorador de Arquivos, clicar na barra de endereço, digitar `powershell` e apertar Enter.
3. Rode o programa:

```bash
python nome_do_arquivo.py
```

O nome do arquivo principal está no README de cada projeto.

### Projetos com bibliotecas externas

Quando um projeto tiver um arquivo `requirements.txt`, instale as dependências antes de rodar. O ideal é usar um ambiente virtual, para que um projeto não interfira nos outros:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux / macOS

pip install -r requirements.txt
```

> No Linux, o tkinter às vezes vem separado do Python. Se um projeto com janela der erro de importação, instale com `sudo apt install python3-tk`.

---

## 📁 Organização do repositório

Cada projeto segue o mesmo padrão, em uma pasta própria:

```
projetos-python/
├── README.md                  # este arquivo
├── autoscan-carros/
│   ├── README.md
│   ├── AutoScanCarros.py
│   └── index.html
├── nome-do-projeto/
│   ├── README.md              # o que faz, como rodar, exemplos
│   ├── main.py                # arquivo principal
│   └── requirements.txt       # só se usar bibliotecas externas
└── ...
```

---

## ➕ Adicionando um novo projeto

1. Crie uma pasta com o nome do projeto, em minúsculas e com hífens (`gerador-de-senhas`).
2. Coloque dentro o código e um `README.md` com: o que o projeto faz, como rodar e um exemplo de uso.
3. Se usar bibliotecas externas, inclua um `requirements.txt` (gere com `pip freeze > requirements.txt` dentro do ambiente virtual do projeto).
4. Acrescente uma linha na tabela de projetos deste README.

---

## 📦 Executáveis (.exe)

Alguns projetos podem ser convertidos em executável para Windows com o [PyInstaller](https://pyinstaller.org) (ou com a interface gráfica [Auto Py To Exe](https://pypi.org/project/auto-py-to-exe/)):

```powershell
python -m pip install --upgrade pyinstaller
python -m PyInstaller --onefile --windowed arquivo.py
```

Use `--windowed` para programas com janela e tire essa opção para programas de terminal. Os executáveis **não ficam versionados nas pastas**, porque são arquivos grandes. Quando existirem, ficam disponíveis na aba **Releases**. Antivírus e SmartScreen costumam marcar executáveis do PyInstaller como suspeitos (falso positivo comum).

---

## 🤝 Sugestões

Achou um erro ou tem uma ideia de melhoria? Abra uma **Issue** na aba do repositório.
