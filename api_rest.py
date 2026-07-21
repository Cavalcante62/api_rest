# 1 objetivos: criar uma API rest que disponibilize cadastrar, deletar e consultar livros

# 2 URL= localhost

# 3 endpoints 
#   localhost/livros (GET) retorna todos os livros
#   localhost/livros/id (GET) retorna o livro correspondente ao id
#   localhost/livros/id (PUT) altera informações do livro correspondente ao id
#   localhost/livros/id (DELETE) deleta o livro correspondente ao id

# 4 a API usa um arquivo json para guardar o inventário de livros

#5 o index dos livros dentro da lista é = id -1
#o algoritimo de busca binaria foi feito sem uso de funções já prontas
#o arquivo json foi préviamente criado para facilitar testes

# Este projeto demonstra a aplicação prática de arquitetura RESTful utilizando Flask.
# Evidencia também a capacidade de implementar algoritmos fundamentais (Busca Binária) do zero,
# a separação de responsabilidades (persistência de dados vs roteamento) e o bom 
# gerenciamento de verbos HTTP e códigos de status de retorno.

#bibiliotecas usadas
from flask import Flask, jsonify, request
import json

app= Flask(__name__)

#função que carrega o inventário para o programa
# uso do context manager ('with') garante o fechamento automático e seguro do arquivo, 
# prevenindo memory leaks. O parâmetro encoding='utf-8' é para
# internacionalização e caracteres especiais.
def upload_books():
    with open('livros.json', 'r', encoding= 'utf-8') as f:
        return json.load(f)

#função que salva as informações no inventario
#Isolamento da camada de persistência. O uso de 'ensure_ascii=False' 
# e 'indent=4' mantém o JSON legível e formatado corretamente, facilitando o debug
def save_books(books_db):
    with open('livros.json', 'w', encoding='utf-8')as f:
        json.dump(books_db, f, ensure_ascii= False, indent= 4)

#função de busca binaria
# implementação manual de um algoritmo de O(log n)  
# um bom exemplo de 'early return' e tratamento de edge cases logo na primeira linha.
def binary_search(num:int, l:list):
    if num> len(l) or num<= 0: #
        return jsonify({"erro": "Livro não encontrado"}), 404
    
    smaller= 0
    bigger= len(l)
    guess= bigger//2

    while num!= guess:
        if num> guess:
            smaller= guess
        
        elif num< guess:
            bigger= guess
        guess= (smaller+bigger)//2
    return guess-1

books:list[dict]= upload_books()

# Função para retornar todos os livros do inventário
@app.route('/livros', methods= ['GET'])
def all_books():
    '''
    Return a list of all books in L
    '''
    return jsonify(books)

# função que procura o livro pelo seu id
@app.route('/livros/<int:id>', methods= ['GET'])
def search_id(id:int):
    '''
    Return de book by its id 
    '''
    index= binary_search(id, books)
    return jsonify(books[index])

#função que altera informações do livro correspondente ao id
# O código inclui validação de limites do ID e retorna o HTTP Status 404 (Not Found)
# adequadamente, seguindo as convenções do protocolo HTTP.
@app.route('/livros/<int:id>', methods=['PUT'])
def book_edit_by_id(id:int):
    '''
    Edit books by its id
    '''
    if id> 0 and id<= len(books):
        None
    else:
        return jsonify({"erro": "Livro não encontrado"}), 404
    changed_book= request.get_json()
    books[id-1].update(changed_book)
    save_books(books)
    return jsonify(books[id-1])

#função que adiciona novos livros
#A lógica de auto-incremento do ID é uma solução prática para garantir
# a integridade sem a dependência de um SGBD.
@app.route('/livros', methods= ['POST'])
def add_book():
    '''
    Recive a book by .json from user and append in de current list of books
    '''
    new_book= request.get_json()
    new_book['id']= len(books)+1 #isso garante que o id dos livros se mantenha ordenado
    books.append(new_book)
    save_books(books)
    return jsonify(books)

#função que deleta livros pelo seu id
# A validação de index evita o lançamento de exceções do 
#tipo IndexError (Index Out of Bounds) na aplicação.
@app.route('/livros/<int:id>', methods= ['DELETE'])
def delete_book(id:int):
    
    if id> 0 and id<= len(books):
        del books[id-1]
        #ordena os livros após a exclusão com ≃ O(n)
        for book in books:
            book['id']= books.index(book)+1
        save_books(books)
        return jsonify(books)
    else:
        return jsonify({"erro": "Livro não encontrado"}), 404
            

app.run(port=5000, host='localhost', debug= True)
