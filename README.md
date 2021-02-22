# SteamGamesRecommender

**Número da Lista**: 15<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0028685  |  Victor Samuel dos Santos Lucas |
| 18/0029177  |  Wagner Martins da Cunha |

## Sobre 
Este projeto tem como objetivo ser um guia de relações entre jogos da plataforma [Steam](https://store.steampowered.com/?l=portuguese), que por meio do uso de Grafos e do algorítmo BFS (Busca em Largura), realiza análises de semelhanças baseando-se em critérios de Categorias, Gêneros e Desenvolvedores. 


## Screenshots

### A aplicação
    ![Counter Strike - GO](img/csgoFront.jpg)
    ![Red Dead Redemption 2](img/reddeadredemption2Front.jpg)

### Funcionamento no BackEnd
    ![Grafo](img/getGraphBack.jpg)
    ![Busca](img/csgoBack.jpg)

## Instalação 
#### Linguagem: 
* BackEnd: [Python](https://www.python.org/)
* FrontEnd: [JavaScript](https://www.javascript.com/)

#### Framework:
* BackEnd: [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* FrontEnd: [React](https://pt-br.reactjs.org/)


### :warning: Como rodar o projeto?
Ter instalado as seguintes dependências
 
```
Pytyon: Versão 3+
Node: Versão 12+
Npm: Versão 6+
```
Clonar este repositório

```
git clone https://github.com/projeto-de-algoritmos/Grafos1_SteamGamesRecommender.git
```
Acessar a pasta raiz do repositório 

```
cd ../../Grafos1_SteamGamesRecommender
```
#### Configurando o BackEnd
Acessar a pasta raiz do BackEnd

```
cd ../../Grafos1_SteamGamesRecommender/backend
```
Para executar o backend, utilize o ambiente virtual venv:

```
python3 -m venv venv
```
Para executar o ambiente(em um linux), digite na raís desta pasta.

```
source ./venv/bin/activate
```
e por fim dê o comando

```
activate
```
Com o ambiente virtual ativado, instale as bibliotecas:

```
pip3 install -r requirements.txt
```
Por fim defina a variável de ambiente do flask e execute o mesmo:

```
export FLASK_APP=src/app.py
flaskrun
```
#### Configurando o FrontEnd
Acessar a pasta raiz do FrontEnd

```
cd ../../Grafos1_SteamGamesRecommender/frontend
```
Realize a instalação das dependências

```
npm install
```
Execute a aplicação no modo de desenvolvimento

```
npm start
```
##### :warning: Observações
Nesta última etapa a aplicação será aberta na porta  http://localhost:3001, logo se faz necessário que a mesma esteja livre para uso. 

## Uso 
Após a aplicação dos comandos citados nos tópicos anteriores, o projeto irá abrir no seu navegador padrão. 

* Para realizar o uso do projeto é muito simples, basta inserir o nome do jogo que em questão no campo de busca e apertar "Search", após isso, o grafo com as relações entre os jogos irá aparecer no campo à direita do seu navegador. 
## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.




