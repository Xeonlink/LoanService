import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

# CSV 파일 경로
BOOKS_FILE = 'books.csv'
LOANS_FILE = 'loans.csv'
MEMBERSHIP_FILE = 'membership.csv'

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

    try:
        with open(MEMBERSHIP_FILE, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['member_id', 'name', 'phone_number'])
    except FileExistsError:
        pass

def add_book():
    """책을 books CSV 파일에 추가합니다."""
    book_id = simpledialog.askstring("책 추가", "책 ID를 입력하세요:")
    if not book_id:
        messagebox.showerror("오류", "책 ID를 입력해야 합니다.")
        return
    
    title = simpledialog.askstring("책 추가", "책 제목을 입력하세요:")
    if not title:
        messagebox.showerror("오류", "책 제목을 입력해야 합니다.")
        return
    
    author = simpledialog.askstring("책 추가", "책 저자를 입력하세요:")
    if not author:
        messagebox.showerror("오류", "책 저자를 입력해야 합니다.")
        return
    
    with open(BOOKS_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author, 'yes'])
    messagebox.showinfo("성공", "책이 성공적으로 추가되었습니다.")

def list_books():
    """모든 책과 그 가용성을 목록화합니다."""
    books = []
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if len(row) >= 4:
                    books.append(f"ID: {row[0]}, 제목: {row[1]}, 저자: {row[2]}, 가용성: {row[3]}")
    except Exception as e:
        messagebox.showerror("오류", f"책 목록을 불러오는 중 오류가 발생했습니다: {e}")
        return
    
    if books:
        books_list = "\n".join(books)
        messagebox.showinfo("모든 책", books_list)
    else:
        messagebox.showinfo("모든 책", "등록된 책이 없습니다.")

def list_available_books():
    """대출 가능한 모든 책을 목록화합니다."""
    available_books = []
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if len(row) >= 4 and row[3] == 'yes':
                    available_books.append(f"ID: {row[0]}, 제목: {row[1]}, 저자: {row[2]}")
    except Exception as e:
        messagebox.showerror("오류", f"대출 가능한 책 목록을 불러오는 중 오류가 발생했습니다: {e}")
        return
    
    if available_books:
        books = "\n".join(available_books)
        messagebox.showinfo("대출 가능한 책", books)
    else:
        messagebox.showinfo("대출 가능한 책", "현재 대출 가능한 책이 없습니다.")

def list_borrowed_books():
    """대출된 모든 책과 대출자를 목록화합니다."""
    with open(LOANS_FILE, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
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
            if row[0] == book_id:
                if row[3] == 'yes':
                    book_found = True
                    row[3] = 'no'
                else:
                    messagebox.showerror("오류", "책이 대출 불가능합니다.")
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

def search_books():
    """책 제목이나 저자로 검색합니다."""
    search_term = search_entry.get()
    if not search_term:
        messagebox.showerror("오류", "검색어를 입력해야 합니다.")
        return
    
    results = []
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # 헤더 건너뛰기
            for row in reader:
                if len(row) < 4:
                    continue  # 예상된 열 수가 부족한 경우 건너뜁니다
                if search_term.lower() in row[1].lower() or search_term.lower() in row[2].lower():
                    results.append(f"ID: {row[0]}, 제목: {row[1]}, 저자: {row[2]}, 가용성: {row[3]}")
    except Exception as e:
        messagebox.showerror("오류", f"검색 중 오류가 발생했습니다: {e}")
        print(f"Debug Info: {e}")  # 콘솔에 오류를 출력하여 디버깅에 도움을 줍니다
        return
    
    results_text = "\n".join(results) if results else "검색 결과가 없습니다."
    results_label.config(text=results_text)

def register_member():
    """새 회원을 등록합니다."""
    name = simpledialog.askstring("회원 가입", "이름을 입력하세요:")
    if not name:
        messagebox.showerror("오류", "이름을 입력해야 합니다.")
        return
    
    phone_number = simpledialog.askstring("회원 가입", "전화번호를 입력하세요:")
    if not phone_number:
        messagebox.showerror("오류", "전화번호를 입력해야 합니다.")
        return
    
    # 회원 번호를 부여하기 위해 현재 파일의 데이터 수를 파악합니다
    member_id = 1
    try:
        with open(MEMBERSHIP_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # 헤더 건너뛰기
            members = list(reader)
            if members:
                last_member_id = int(members[-1][0])
                member_id = last_member_id + 1
    except FileNotFoundError:
        pass
    except StopIteration:
        # 파일이 비어 있을 때 발생할 수 있는 StopIteration 예외 처리
        pass
    
    with open(MEMBERSHIP_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([member_id, name, phone_number])
    
    messagebox.showinfo("성공", f"회원 가입이 완료되었습니다. 회원 번호: {member_id}")

def main():
    """프로그램을 실행하는 메인 함수입니다."""
    initialize_files()
    
    root = tk.Tk()
    root.title("도서 관리 시스템")
    root.geometry("1200x800")
    
    button_width = 20
    button_height = 2
    
    button_frame = tk.Frame(root)
    button_frame.grid(row=0, column=0, sticky="nsw", padx=10, pady=(100, 10))
    
    tk.Button(button_frame, text="책 추가", command=add_book, width=button_width, height=button_height).grid(row=0, column=0, pady=5)
    tk.Button(button_frame, text="모든 책 보기", command=list_books, width=button_width, height=button_height).grid(row=1, column=0, pady=5)
    tk.Button(button_frame, text="대출 가능한 책 보기", command=list_available_books, width=button_width, height=button_height).grid(row=2, column=0, pady=5)
    tk.Button(button_frame, text="대출된 책 보기", command=list_borrowed_books, width=button_width, height=button_height).grid(row=3, column=0, pady=5)
    tk.Button(button_frame, text="책 대출", command=borrow_book, width=button_width, height=button_height).grid(row=4, column=0, pady=5)
    tk.Button(button_frame, text="책 반납", command=return_book, width=button_width, height=button_height).grid(row=5, column=0, pady=5)
    tk.Button(button_frame, text="책 삭제", command=delete_book, width=button_width, height=button_height).grid(row=6, column=0, pady=5)
    
    search_frame = tk.Frame(root)
    search_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    
    search_label = tk.Label(search_frame, text="검색 (제목/저자):")
    search_label.grid(row=0, column=0, pady=5)
    
    global search_entry
    search_entry = tk.Entry(search_frame, width=50)
    search_entry.grid(row=0, column=1, pady=5)
    
    search_button = tk.Button(search_frame, text="검색", command=search_books)
    search_button.grid(row=0, column=2, padx=5)
    
    global results_label
    results_label = tk.Label(search_frame, text="", justify="left", anchor="nw", wraplength=500)
    results_label.grid(row=1, column=0, columnspan=3, pady=5)
    
    # 회원 가입 버튼 추가
    register_button = tk.Button(root, text="회원 가입", command=register_member, width=15, height=2)
    register_button.grid(row=0, column=2, padx=10, pady=(100, 10), sticky="ne")
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()
