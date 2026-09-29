# Automação de Cadastro de Produtos com Python

## Sobre o projeto

Este projeto consiste em uma automação desenvolvida em **Python** para realizar o cadastro automático de produtos em um sistema web.

A aplicação utiliza **PyAutoGUI** para controlar teclado e mouse, simulando as ações que normalmente seriam realizadas manualmente por um usuário.

Os dados dos produtos são lidos automaticamente de um arquivo CSV utilizando **Pandas**. Em seguida, o programa percorre cada registro da base e preenche os campos correspondentes no sistema.

O objetivo principal do projeto é demonstrar como tarefas repetitivas de cadastro podem ser automatizadas utilizando Python.

---

## Objetivo

Automatizar um processo manual composto pelas seguintes etapas:

1. Abrir o navegador.
2. Acessar o sistema da empresa.
3. Realizar login.
4. Ler uma base de produtos.
5. Percorrer os registros da base.
6. Preencher automaticamente os campos do formulário.
7. Salvar cada produto.
8. Repetir o processo até finalizar todos os registros.

---

## Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas
- CSV
- Automação de interface gráfica (GUI Automation)

---

# Funcionamento da automação

O fluxo do programa pode ser representado da seguinte forma:

```text
Arquivo CSV
    ↓
Pandas
    ↓
Leitura dos produtos
    ↓
Loop pelos registros
    ↓
PyAutoGUI
    ↓
Preenchimento automático do sistema
    ↓
Cadastro dos produtos
```

---

# 1. Abrindo o sistema

Inicialmente o programa utiliza o PyAutoGUI para abrir o navegador.

```python id="kw5t7p"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
```

Depois, o endereço do sistema é digitado:

```python id="oq9vze"
link = "URL_DO_SISTEMA"

pyautogui.write(link)
pyautogui.press("enter")
```

Uma pausa é adicionada para garantir que a página tenha tempo de carregar:

```python id="7meolr"
time.sleep(3)
```

---

# 2. Login automático

Após acessar o sistema, a automação identifica o campo de login através de coordenadas da tela.

```python id="w3fqiz"
pyautogui.click(x=786, y=376)
```

Em seguida, preenche as informações necessárias utilizando teclado e comandos de navegação:

```python id="mtqst2"
pyautogui.write("usuario")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
```

> Em uma aplicação real, credenciais não devem ficar diretamente no código. O recomendado é utilizar variáveis de ambiente.

---

# 3. Leitura da base de dados

Os produtos são armazenados em um arquivo CSV.

O Pandas é utilizado para importar essa base:

```python id="xbg8vd"
import pandas as pd

tabela_produtos = pd.read_csv("produtos.csv")
```

A tabela contém informações como:

- código;
- marca;
- tipo;
- categoria;
- preço unitário;
- custo;
- observações.

---

# 4. Percorrendo os produtos

A automação utiliza um loop para percorrer todas as linhas do DataFrame:

```python id="sk7p67"
for linha in tabela_produtos.index:
```

A cada repetição, o programa acessa os dados correspondentes ao produto atual.

Exemplo:

```python id="fs83gd"
codigo = tabela_produtos.loc[linha, "codigo"]
marca = tabela_produtos.loc[linha, "marca"]
tipo = tabela_produtos.loc[linha, "tipo"]
```

---

# 5. Preenchimento automático do formulário

Após acessar cada informação do DataFrame, o PyAutoGUI é utilizado para preencher os campos do sistema.

Exemplo:

```python id="78s1uz"
pyautogui.write(str(codigo))
pyautogui.press("tab")

pyautogui.write(str(marca))
pyautogui.press("tab")

pyautogui.write(str(tipo))
pyautogui.press("tab")
```

O uso da tecla `Tab` permite navegar entre os campos sem precisar clicar individualmente em cada posição.

---

# Dados cadastrados

Durante o processo, são preenchidos automaticamente os seguintes campos:

```text
Código
Marca
Tipo
Categoria
Preço unitário
Custo
Observação
```

Cada valor é retirado diretamente da linha correspondente da base de dados.

---

# Tratamento de valores vazios

A coluna de observações pode possuir valores vazios.

Por isso, antes de preencher o campo, o programa verifica se existe uma observação válida.

No código original:

```python id="qkdwmt"
if obs != "nan":
    pyautogui.write(str(obs))
```

Uma alternativa mais robusta utilizando Pandas seria:

```python id="klrnw7"
if pd.notna(obs):
    pyautogui.write(str(obs))
```

Assim, a verificação é feita diretamente com as ferramentas do Pandas.

---

# 6. Salvando o produto

Depois que todos os campos são preenchidos, a automação confirma o cadastro:

```python id="b0tma8"
pyautogui.press("enter")
```

Em seguida, retorna ao início da página:

```python id="ckvgh4"
pyautogui.scroll(1000)
```

O processo então continua com o próximo produto.

---

# Controle da velocidade da automação

Para evitar que os comandos sejam executados rápido demais, foi configurado um intervalo entre as ações:

```python id="1q72vf"
pyautogui.PAUSE = 0.5
```

Isso adiciona uma pausa de 0,5 segundo entre os comandos executados pelo PyAutoGUI.

Também são utilizadas pausas maiores quando é necessário aguardar o carregamento de páginas:

```python id="mqox3b"
time.sleep(3)
```

---

# Estrutura do projeto

```text
AUTOMACAO_CADASTRO/
│
├── main.py
├── produtos.csv
├── requirements.txt
└── README.md
```

### `main.py`

Contém toda a lógica responsável pela automação.

### `produtos.csv`

Contém os produtos que serão cadastrados automaticamente.

### `requirements.txt`

Contém as bibliotecas necessárias para executar o projeto.

---

# Como executar

## 1. Clone o repositório

```bash id="nfiylm"
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash id="jcsi76"
cd AUTOMACAO_CADASTRO
```

---

## 2. Instale as dependências

```powershell id="r3zv23"
python -m pip install -r requirements.txt
```

Ou diretamente:

```powershell id="sm88a7"
python -m pip install pyautogui pandas
```

---

## 3. Configure os dados

Certifique-se de que o arquivo:

```text id="4kj895"
produtos.csv
```

esteja no diretório do projeto.

---

## 4. Ajuste as coordenadas

Como o PyAutoGUI utiliza posições absolutas da tela, algumas coordenadas podem precisar ser ajustadas de acordo com:

- resolução do monitor;
- tamanho da janela;
- navegador utilizado;
- escala do Windows.

Exemplo:

```python id="r7eq5j"
pyautogui.click(x=786, y=376)
```

---

## 5. Execute

```powershell id="fc3h9k"
python main.py
```

A partir desse momento, o programa realizará os cadastros automaticamente.

---

# Limitações

Como a automação utiliza coordenadas da tela, sua execução depende da posição dos elementos visuais.

Mudanças na interface do sistema, resolução do monitor ou posição da janela podem exigir novos ajustes.

Também é importante evitar utilizar o computador manualmente enquanto a automação estiver sendo executada.

---

# Possíveis melhorias futuras

O projeto pode evoluir com:

- utilização de variáveis de ambiente para login;
- validação dos dados antes do cadastro;
- logs de produtos cadastrados;
- registro automático de erros;
- captura de screenshots em caso de falha;
- tratamento de exceções;
- confirmação de cadastro realizado com sucesso;
- identificação de elementos por imagem com `pyautogui.locateOnScreen`;
- geração de relatório de execução;
- interface gráfica para selecionar o CSV;
- substituição da automação por coordenadas por Selenium ou Playwright.

---

# Conceitos praticados

Durante o desenvolvimento foram utilizados conceitos como:

- automação de tarefas;
- RPA;
- manipulação de arquivos CSV;
- DataFrames;
- loops;
- estruturas condicionais;
- manipulação de dados com Pandas;
- controle de teclado e mouse;
- automação de formulários;
- integração entre dados e interface gráfica.

---

# Competências demonstradas

Este projeto demonstra conhecimentos em:

**Python • PyAutoGUI • Pandas • Automação • RPA • Manipulação de Dados • CSV • Automação de Processos**

---

## Conclusão

O projeto demonstra como Python pode ser utilizado para automatizar tarefas administrativas repetitivas.

Ao combinar **Pandas** para leitura e manipulação dos dados com **PyAutoGUI** para interação com a interface gráfica, foi possível criar uma solução capaz de percorrer uma base de produtos e realizar os cadastros automaticamente.

Esse tipo de automação pode reduzir trabalho manual, tempo de execução e erros de digitação em processos repetitivos.
