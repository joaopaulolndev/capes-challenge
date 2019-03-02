


<p align="center">
  <a href="https://github.com/joaopaulolndev/">
    <img alt="" src="https://scba.capes.gov.br/scba/img/logo-capes-full-hor.png">
  </a>
</p>

## Sobre Capes Challenge API Rest:

Neste desafio será avaliado os conhecimento em:
- Linguagens de programação;
- Testes automatizados;
- Análise e modelagem de dados;
- Arquitetura REST
- GIT
- Arquitetura de software
- Padrões de projeto

### Objetivo

Criar um microsserviço utilizando arquitetura REST em qualquer linguagem de programação e utilizando qualquer banco de dados

### Requisitos

- Criar um modelo de dados para a representação das seguintes entidades Pessoa e Endereço;
- Utilizar um banco de dados SQL embutido(SQLite por exemplo) ou NoSQL (MongoDB por exemplo); 
- Criar uma API REST para lidar com obtenção, criação e exclusão de Pessoas e seus endereços;
- Criar testes unitários;
- Publicar no seu github o fonte da implementação e enviar o link do mesmo por e-mail.

### Desejável

- Ter especificação da API testável, com o swagger por exemplo;
- Ter testes funcionais para a API;

## Requisitos:
   * Python 3.6
   * Flask Framework 1.0.2
   * flask-restplus 0.9.2
   * Flask-SQLAlchemy 2.1

   
<p align="center">
  <img alt="" src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg">
  <img src="https://img.shields.io/badge/size-76%20kB-green.svg" alt="">
  <img src="https://img.shields.io/badge/license-MIT-000.svg" alt="">
  <img src="https://img.shields.io/badge/Flask%20Framework-1.0.2-red.svg" alt="">
  <img src="https://img.shields.io/badge/platform-linux--64%20%7C%20win--32%20%7C%20osx--64%20%7C%20win--64-lightgrey.svg" alt="">
</p>
   
## Instalando Flask Framework

Instalando `Flask` from the `pip`

```
pip install Flask
```
    
## Run Instructions:
    Rode esse código local > python app.py 
    Open the Browser http://localhost:8888/api/
       

## @todo Build:

   Pode visualizar a aplicação nesse endereço. <br/>
   You can view the application at this address.

   [https://champions-league-challenge.herokuapp.com/api/champions-league/](https://champions-league-challenge.herokuapp.com/api/champions-league/)

## Recursos:


* GET /pessoa/enderecos/ 
<br/>Retorna a lista de endereços
* POST /pessoa/enderecos/ 
<br/>Cria novo endereço
* DELETE /pessoa/enderecos/{id} 
<br/>Apaga um endereço
* GET /pessoa/enderecos/{id} 
<br/>Retorna a lista de endereco com as pessoa
* PUT /pessoa/enderecos/{id} 
<br/>Altera um endereço

* GET /pessoa/pessoas/ 
<br/>Retorna a lista de pessoas
* POST /pessoa/pessoas/ 
<br/>Cria nova pessoa
* DELETE /pessoa/pessoas/{id} 
<br/>Apaga uma pessoa
* GET /pessoa/pessoas/{id} 
<br/>Retorna uma pessoa
* PUT /pessoa/pessoas/{id} 
<br/>Altera uma pessoa
   
## Padrões 
Utilizado para boas práticas de programação em Python o 
[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) como referência.  
    
## Referência:
   - [Desafio](https://github.com/harryssongilgamesh/selecao-2019)
   - [Flask Documentation](http://flask.pocoo.org/docs/1.0/)
   - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
   - [Postman](https://www.getpostman.com/)
   - [Git](https://git-scm.com/)
   - [PyCharm](https://www.jetbrains.com/pycharm/)
   - [Shields IO](https://shields.io/#/)

