import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

# CSV 파일 경로
BOOKS_FILE = 'books.csv'
LOANS_FILE = 'loans.csv'

def initialize_files():
    """CSV 파일들을 초기화합니다. 파일이 없으면 헤더와 함께 생성합니다."""
    try:
        with open(BOOKS_FILE, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'title', 'author', 'available'])
    except FileExistsError:
        pass

    try:
        with open(LOANS_FILE, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['book_id', 'borrower_name', 'borrow_date'])
    except FileExistsError:
        pass

def add_book():
    """책을 books CSV 파일에 추가합니다."""
    book_id = simpledialog.askstring("책 추가", "책 ID를 입력하세요:")
    title = simpledialog.askstring("책 추가", "책 제목을 입력하세요:")
    author = simpledialog.askstring("책 추가", "책 저자를 입력하세요:")
    
    with open(BOOKS_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author, 'yes'])
    messagebox.showinfo("성공", "책이 성공적으로 추가되었습니다.")

def list_books():
    """모든 책과 그 가용성을 목록화합니다."""
    with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 헤더 건너뛰기
        books = "\n".join([f"ID: {row[0]}, 제목: {row[1]}, 저자: {row[2]}, 가용성: {row[3]}" for row in reader])
        messagebox.showinfo("모든 책", books)

def list_available_books():
    """대출 가능한 모든 책을 목록화합니다."""
    with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 헤더 건너뛰기
        available_books = [row for row in reader if row[3] == 'yes']
        
        if available_books:
            books = "\n".join([f"ID: {row[0]}, 제목: {row[1]}, 저자: {row[2]}" for row in available_books])
            messagebox.showinfo("대출 가능한 책", books)
        else:
            messagebox.showinfo("대출 가능한 책", "현재 대출 가능한 책이 없습니다.")

def list_borrowed_books():
    """대출된 모든 책과 대출자를 목록화합니다."""
    with open(LOANS_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 헤더 건너뛰기
        borrowed_books = [row for row in reader]
        
        if borrowed_books:
            books = "\n".join([f"책 ID: {row[0]}, 대출자: {row[1]}, 대출일: {row[2]}" for row in borrowed_books])
            messagebox.showinfo("대출된 책", books)
        else:
            messagebox.showinfo("대출된 책", "현재 대출된 책이 없습니다.")

def borrow_book():
    """책이 대출 가능하면 대출합니다."""
    book_id = simpledialog.askstring("책 대출", "대출할 책 ID를 입력하세요:")
    borrower_name = simpledialog.askstring("책 대출", "이름을 입력하세요:")
    
    books = []
    book_found = False
    with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] == book_id:  # 해당 책을 찾음
                if row[3] == 'yes':  # available 필드가 'yes'이면
                    book_found = True
                    row[3] = 'no'  # 대출 상태로 변경
                else:
                    messagebox.showerror("오류", "책이 대출 불가능합니다.")  # 대출 불가능
            books.append(row)
    
    if book_found:
        with open(BOOKS_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(books)
        
        with open(LOANS_FILE, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([book_id, borrower_name, datetime.now().strftime('%Y-%m-%d')])
        
        messagebox.showinfo("성공", "책이 성공적으로 대출되었습니다.")
    else:
        if not book_found:
            messagebox.showerror("오류", "책을 찾을 수 없습니다.")

def return_book():
    """책을 반납하고 가용 상태를 업데이트합니다."""
    book_id = simpledialog.askstring("책 반납", "반납할 책 ID를 입력하세요:")
    
    books = []
    book_found = False
    with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] == book_id:
                if row[3] == 'no':
                    book_found = True
                    row[3] = 'yes'
                else:
                    messagebox.showerror("오류", "이 책은 대출되지 않았습니다.")
            books.append(row)
    
    if book_found:
        with open(BOOKS_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(books)
        
        update_loans_file(book_id)
        
        messagebox.showinfo("성공", "책이 성공적으로 반납되었습니다.")
    else:
        messagebox.showerror("오류", "책을 찾을 수 없습니다.")

def delete_book():
    """책 정보를 삭제합니다."""
    book_id = simpledialog.askstring("책 삭제", "삭제할 책 ID를 입력하세요:")
    
    books = []
    book_found = False
    with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] == book_id:
                book_found = True
            else:
                books.append(row)
    
    if book_found:
        with open(BOOKS_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(books)
        
        update_loans_file(book_id)
        
        messagebox.showinfo("성공", "책이 성공적으로 삭제되었습니다.")
    else:
        messagebox.showerror("오류", "책을 찾을 수 없습니다.")

def update_loans_file(book_id):
    """반납되거나 삭제된 책의 대출 기록을 제거합니다."""
    loans = []
    with open(LOANS_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] != book_id:
                loans.append(row)
    
    with open(LOANS_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(loans)

def main():
    """프로그램을 실행하는 메인 함수입니다."""
    initialize_files()
    
    root = tk.Tk()
    root.title("도서 관리 시스템")
    root.geometry("1200x800")  # 창 크기 설정
    
    button_width = 20  # 버튼 너비 설정
    
    tk.Button(root, text="책 추가", command=add_book, width=button_width).pack(pady=5, anchor='w')
    tk.Button(root, text="모든 책 보기", command=list_books, width=button_width).pack(pady=5, anchor='w')
    tk.Button(root, text="대출 가능한 책 보기", command=list_available_books, width=button_width).pack(pady=5, anchor='w')
    tk.Button(root, text="대출된 책 보기", command=list_borrowed_books, width=button_width).pack(pady=5, anchor='w')
    tk.Button(root, text="책 대출", command=borrow_book, width=button_width).pack(pady=5, anchor='w')
    tk.Button(root, text="책 반납", command=return_book, width=button_width).pack(pady=5, anchor='w')
    tk.Button(root, text="책 삭제", command=delete_book, width=button_width).pack(pady=5, anchor='w')
    
    root.mainloop()

if __name__ == "__main__":
    main()
