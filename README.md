
# Projeto de Estudo - Pesquisa e Manipulação de Planilhas com Flask

## Descrição

Este é um projeto desenvolvido com o propósito de estudar e aplicar conceitos de **Python**, **Flask** e **manipulação de planilhas Excel** no contexto de automação de tarefas de trabalho. O objetivo principal deste projeto é permitir a busca por um nome específico dentro de vários arquivos `.xlsx` e retornar os arquivos que contêm o nome pesquisado.

O projeto foi desenvolvido para facilitar a análise de grandes volumes de dados armazenados em planilhas, sem a necessidade de abrir cada uma manualmente. Esse tipo de automação pode ser aplicado em diversas áreas da empresa, como pesquisa de clientes, dados financeiros, e muito mais.

## Funcionalidades

- **Upload de arquivos Excel (.xlsx)**: Permite o envio de múltiplos arquivos `.xlsx` via interface web.
- **Busca por nome**: O usuário pode inserir um nome e o sistema irá procurar por ele em todas as planilhas dos arquivos carregados.
- **Exibição dos resultados**: Retorna a lista de arquivos que contêm o nome pesquisado.

## Tecnologias Utilizadas

- **Python** (com a biblioteca `Flask`): Backend da aplicação web.
- **Pandas**: Para leitura e manipulação dos dados das planilhas Excel.
- **HTML/CSS**: Para estruturação e estilo da interface do usuário.
- **Flask**: Framework web utilizado para criar a aplicação.

## Como Rodar o Projeto Localmente

Para rodar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório** para o seu computador:
   ```bash
   git clone https://github.com/SEU_USUARIO/PROJETO-NOME.git
   cd PROJETO-NOME
````

2. **Instale as dependências**:
   Dentro do diretório do projeto, execute:

   ```bash
   pip install -r requirements.txt
   ```

3. **Rodando o Flask**:
   Para rodar o servidor localmente, execute o seguinte comando:

   ```bash
   python app.py
   ```

   O servidor Flask será iniciado e você poderá acessar a aplicação no seu navegador pelo endereço:

   ```
   http://127.0.0.1:5000/
   ```

4. **Usando a aplicação**:

   * Faça o upload de arquivos `.xlsx`.
   * Insira o nome que deseja buscar.
   * O sistema exibirá os arquivos que contêm o nome pesquisado.

### Estrutura do Projeto

O projeto é organizado da seguinte maneira:

```
/busca_py
│
├── app.py                 # Arquivo principal onde o Flask é configurado e executado
├── /static                # Arquivos estáticos como CSS e imagens
│   └── styles.css         # Estilos CSS para a interface
├── /templates             # Arquivos HTML
│   ├── index.html         # Página principal
│   └── resultado.html     # Página que exibe os resultados da busca
└── README.md              # Este arquivo com informações do projeto
```

## Dependências

O projeto utiliza as seguintes bibliotecas:

* **Flask**: Para criar a aplicação web.
* **Pandas**: Para manipulação e análise dos dados das planilhas.
* **openpyxl**: Para leitura de arquivos Excel `.xlsx`.

Para instalar as dependências, você pode usar o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Contribuindo

Este é um projeto de estudo, mas contribuições são bem-vindas. Se você deseja adicionar funcionalidades, corrigir erros ou melhorar a documentação, siga os passos abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch para sua funcionalidade (`git checkout -b minha-feature`).
3. Faça as modificações necessárias e faça commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin minha-feature`).
5. Abra um pull request.

## Licença

Este projeto está sob a **Licença MIT**. Consulte o arquivo `LICENSE` para mais informações.

## Aplicação no Trabalho

O projeto foi desenvolvido como parte de um estudo sobre automação de tarefas dentro da empresa. A aplicação pode ser utilizada para:

* **Analisar dados de clientes**: Pesquisar nomes de clientes em diversas planilhas de vendas, contratos, e comunicações.
* **Controle de inventário**: Buscar dados de produtos ou registros em grandes arquivos Excel de controle de estoque.
* **Análise financeira**: Buscar informações específicas em relatórios financeiros armazenados em múltiplos arquivos Excel.

Este tipo de automação facilita a consulta rápida de informações e reduz o tempo de processamento manual de dados.

---

Se tiver dúvidas ou precisar de ajuda, não hesite em entrar em contato!

```

### Explicação das Seções:

- **Descrição**: Explica o objetivo do projeto e como ele pode ser utilizado, tanto para estudo quanto para aplicações no trabalho.
- **Funcionalidades**: Lista as principais funcionalidades que o projeto oferece.
- **Tecnologias Utilizadas**: Enumera as principais ferramentas e bibliotecas usadas.
- **Como Rodar o Projeto Localmente**: Instruções detalhadas de como configurar e executar o projeto na máquina local.
- **Estrutura do Projeto**: Descrição da estrutura de pastas e arquivos no seu projeto.
- **Dependências**: Lista de bibliotecas externas que o projeto utiliza.
- **Contribuindo**: Explica como outras pessoas podem contribuir para o projeto.
- **Licença**: Informação sobre a licença do código (aqui, usei a licença MIT como exemplo).
- **Aplicação no Trabalho**: Mostra como esse projeto pode ser útil na empresa, aplicando-o em situações práticas do dia a dia.

