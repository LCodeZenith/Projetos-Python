# 🐍 Projetos Python

Coleção de projetos em Python, cada um com um tema diferente: criptografia, jogos e aplicativos com interface gráfica. Cada projeto fica na sua própria pasta, com o código e um README próprio explicando como usar.

> Repositório de estudo e prática. Os projetos evoluem com o tempo, e alguns são experimentos rápidos.

---

## 📚 Projetos

| Projeto | Descrição | Tecnologias | Status |
|---------|-----------|-------------|--------|
| [🔐 Cifra de César](./cifra-de-cesar) | Criptografa qualquer mensagem usando a cifra de César | Python | ✅ Funcional |
| [🎲 Jogo de Martingale](./jogo-martingale) | Jogo em Python baseado na estratégia de apostas Martingale | Python | ✅ Funcional |
| [🧮 Calculadora](./calculadora-tkinter) | Calculadora completa e funcional, com interface gráfica | Python, tkinter | ✅ Funcional |

*(Novos projetos entram nesta tabela conforme forem sendo adicionados.)*

**Legenda de status:** ✅ Funcional · 🚧 Em desenvolvimento · 🧪 Experimento · 💤 Pausado

---

## 🔎 Sobre os projetos

### 🔐 Cifra de César
Programa que criptografa qualquer mensagem com a cifra de César, uma das cifras mais antigas que existem: cada letra do texto é trocada por outra, deslocada um número fixo de posições no alfabeto. Por exemplo, com deslocamento 3, `A` vira `D`, `B` vira `E`, e assim por diante.

> ⚠️ A cifra de César é um método clássico, ótimo para aprender os conceitos de criptografia, mas **não é segura** para proteger informações reais.

### 🎲 Jogo de Martingale
Jogo feito em Python baseado no Martingale, uma estratégia de apostas em que o jogador dobra o valor da aposta depois de cada perda, na esperança de recuperar o prejuízo com uma vitória. O projeto serve para entender como essa estratégia se comporta na prática.

> ⚠️ É um jogo de estudo, e a estratégia Martingale não garante lucro: uma sequência longa de derrotas pode consumir a banca rapidamente.

### 🧮 Calculadora
Calculadora completa e funcional, com interface gráfica feita em **tkinter**, a biblioteca de janelas que já vem com o Python.

---

## ▶️ Como rodar um projeto

**Requisitos gerais:** Python 3 instalado ([python.org](https://www.python.org/downloads/)). Os projetos são desenvolvidos com Python 3, e cada um informa no seu README se precisa de algo a mais.

1. Clique em **Code → Download ZIP** nesta página e extraia o arquivo (ou clone o repositório com o Git).
2. Abra um terminal **dentro da pasta do projeto** que você quer rodar. No Windows, uma forma fácil é abrir a pasta no Explorador de Arquivos, clicar na barra de endereço, digitar `powershell` e apertar Enter.
3. Rode o programa:

```bash
python nome_do_arquivo.py
```

O nome do arquivo principal está no README de cada projeto.

> A calculadora usa o tkinter. No Windows e no macOS ele já vem com o Python, mas no Linux às vezes vem separado. Se der erro de importação, instale com `sudo apt install python3-tk`.

### Projetos com bibliotecas externas

Quando um projeto tiver um arquivo `requirements.txt`, instale as dependências antes de rodar. O ideal é usar um ambiente virtual, para que um projeto não interfira nos outros:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux / macOS

pip install -r requirements.txt
```

---

## 📁 Organização do repositório

Cada projeto segue o mesmo padrão, em uma pasta própria:

```
projetos-python/
├── README.md                  # este arquivo
├── cifra-de-cesar/
├── jogo-martingale/
├── calculadora-tkinter/
└── nome-do-projeto/
    ├── README.md              # o que faz, como rodar, exemplos
    ├── main.py                # arquivo principal
    └── requirements.txt       # só se usar bibliotecas externas
```

---

## ➕ Adicionando um novo projeto

1. Crie uma pasta com o nome do projeto, em minúsculas e com hífens (`gerador-de-senhas`).
2. Coloque dentro o código e um `README.md` com: o que o projeto faz, como rodar e um exemplo de uso.
3. Se usar bibliotecas externas, inclua um `requirements.txt` (gere com `pip freeze > requirements.txt` dentro do ambiente virtual do projeto).
4. Acrescente uma linha na tabela de projetos deste README.

---

## 📦 Executáveis (.exe)

Os projetos podem ser convertidos em executável para Windows com o [PyInstaller](https://pyinstaller.org) (ou com a interface gráfica [Auto Py To Exe](https://pypi.org/project/auto-py-to-exe/)):

```powershell
python -m pip install --upgrade pyinstaller
python -m PyInstaller --onefile --windowed arquivo.py
```

Use `--windowed` para programas com janela, como a calculadora, e tire essa opção para programas de terminal, como a cifra de César e o jogo de Martingale (se rodarem no terminal). Os executáveis **não ficam versionados nas pastas**, porque são arquivos grandes. Quando existirem, ficam disponíveis na aba **Releases**. Antivírus e SmartScreen costumam marcar executáveis do PyInstaller como suspeitos (falso positivo comum).

---

## 🤝 Sugestões

Achou um erro ou tem uma ideia de melhoria? Abra uma **Issue** na aba do repositório.
