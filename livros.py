from datetime import datetime

# Classe Livro
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def __str__(self):
        status = "Disponível" if self.available else "Emprestado"
        return f"'{self.title}' por {self.author} ({self.year}) - {status}"

# Classe Biblioteca
class Library:
    def __init__(self):
        self.books = []
        self.loan_history = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Livro '{title}' adicionado com sucesso.")

    def list_books(self):
        if not self.books:
            print("A biblioteca não possui livros no momento.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                self.loan_history.append(
                    {"title": book.title, "action": "Emprestado", "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                )
                print(f"Você emprestou o livro '{book.title}'.")
                return
        print("Desculpe, este livro não está disponível ou não existe na biblioteca.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                self.loan_history.append(
                    {"title": book.title, "action": "Devolvido", "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                )
                print(f"Você devolveu o livro '{book.title}'.")
                return
        print("Este livro não foi emprestado ou não existe na biblioteca.")

    def view_loan_history(self):
        if not self.loan_history:
            print("Nenhum histórico de empréstimo encontrado.")
        else:
            for record in self.loan_history:
                print(f"{record['action']} - '{record['title']}' em {record['date']}")

# Menu principal
def main():
    library = Library()
    while True:
        print("\nSistema de Gestão de Biblioteca")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Visualizar Histórico de Empréstimos")
        print("6. Sair")

        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            title = input("Título do Livro: ")
            author = input("Autor do Livro: ")
            year = input("Ano de Publicação: ")
            library.add_book(title, author, year)
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            title = input("Título do Livro para Emprestar: ")
            library.borrow_book(title)
        elif choice == '4':
            title = input("Título do Livro para Devolver: ")
            library.return_book(title)
        elif choice == '5':
            library.view_loan_history()
        elif choice == '6':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()