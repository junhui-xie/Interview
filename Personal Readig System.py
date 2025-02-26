import os
import json

# 定义图书管理类
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"书名: {self.title}, 作者: {self.author}, 出版年份: {self.year}"

# 定义图书管理系统类
class BookManager:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = []
        self.load_books()

    # 加载图书数据
    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.books = [Book(**book_data) for book_data in json.load(f)]

    # 保存图书数据
    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([book.__dict__ for book in self.books], f, ensure_ascii=False, indent=4)

    # 添加图书
    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()
        print("图书添加成功！")

    # 删除图书
    def delete_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        self.save_books()
        print(f"图书'{title}'已删除。")

    # 查找图书
    def search_books(self, search_term):
        found_books = [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
        return found_books

    # 显示所有图书
    def display_books(self):
        if not self.books:
            print("没有找到任何图书。")
        else:
            for book in self.books:
                print(book)

# 主程序
def main():
    book_manager = BookManager()

    while True:
        print("\n--- 图书管理系统 ---")
        print("1. 添加图书")
        print("2. 删除图书")
        print("3. 查找图书")
        print("4. 显示所有图书")
        print("5. 退出系统")

        choice = input("请输入选择的操作: ")

        if choice == '1':
            title = input("请输入图书标题: ")
            author = input("请输入图书作者: ")
            year = input("请输入图书出版年份: ")
            book_manager.add_book(title, author, year)

        elif choice == '2':
            title = input("请输入要删除的图书标题: ")
            book_manager.delete_book(title)

        elif choice == '3':
            search_term = input("请输入要查找的图书标题或作者: ")
            found_books = book_manager.search_books(search_term)
            if found_books:
                for book in found_books:
                    print(book)
            else:
                print("未找到匹配的图书。")

        elif choice == '4':
            book_manager.display_books()

        elif choice == '5':
            print("感谢使用图书管理系统！")
            break

        else:
            print("无效的操作，请重新选择。")

# 运行程序
if __name__ == "__main__":
    main()