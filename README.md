# API REST - Gerenciamento de Livros

Uma API RESTful simples desenvolvida em Python utilizando o framework Flask para o gerenciamento de um inventário de livros. 

Este projeto foi construído para demonstrar conceitos fundamentais de desenvolvimento backend, como criação de rotas, manipulação de métodos HTTP (CRUD), persistência local de dados e implementação de algoritmos de estrutura de dados do zero.

Tentei fazer a maior parte do código em inglês, já que o dominio dele é apreciado e tambem preciso para ler documentações.
## 🚀 Funcionalidades

* **Cadastrar (POST):** Adiciona um novo livro ao inventário, gerando um ID sequencial automaticamente.
* **Consultar (GET):** Retorna a lista completa de livros ou um livro específico baseado em seu ID.
* **Atualizar (PUT):** Permite alterar as informações de um livro já existente.
* **Deletar (DELETE):** Remove um livro do inventário pelo ID de forma segura.

## 🧠 Destaques Técnicos

* **Busca Binária:** Implementação manual de um algoritmo de busca binária para localizar livros pelo ID, evidenciando conhecimento sólido em algoritmos sem dependência de funções prontas.
* **Persistência em JSON:** Utilização de arquivos `.json` para simular um banco de dados *in-memory*, com separação de responsabilidades (I/O isolado do roteamento).
* **Boas Práticas de Código:**
  * Uso de *Context Managers* (`with open`) para manipulação segura de arquivos, prevenindo vazamento de memória.
  * Tratamento correto de *Edge Cases* (como IDs inválidos ou fora de escopo).
  * Respeito às convenções do protocolo HTTP, retornando os Status Codes adequados (ex: `404 Not Found`, `200 OK`).
  * Tipagem estática em rotas Flask para maior segurança (`<int:id>`).

## 🛠️ Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* Módulo `json` (Standard Library)

## ⚙️ Como Executar

1. **Clone o repositório:**
   ```bash
  git clone https://github.com/Cavalcante62/api_rest.git
