import pymysql
from settings import *


def connection_database():
    try:
        connection = pymysql.connect(host='localhost',user='root',password='1234',database='python_data_analysis_projects')
        cur = connection.cursor()
        # print("Database Connection successfully")
        return connection,cur
    except Exception as ex:
        print(f'Error: {ex}')
        raise ValueError(ex)
        

def add_book_table(book_title,author_name,book_cp,book_sp,book_MRP,book_inventory):
    connection, cur = connection_database()
    veiw_book = f"select book_id from bookstore_books where book_title = '{book_title}'"
    cur.execute(veiw_book)
    book_id = cur.fetchall()
    if len(book_id):
        book_id = book_id[0][0]
    else:
        add_new_book = f"insert into bookstore_books (book_title,author_name,cost_price,selling_price,MRP,inventory) values('{book_title}','{author_name}',{book_cp},{book_sp},{book_MRP},{book_inventory});"
        cur.execute(add_new_book)
        connection.commit()
        print(f"new book {book_title} added successfully")
        veiw_book = f"select book_id from bookstore_books where book_title = '{book_title}'"
        cur.execute(veiw_book)
        book_id = cur.fetchall()
        if len(book_id):
            book_id = book_id[0][0]
    connection.close()
    return book_id
        

def add_author_table(author_name):
    connection, cur = connection_database()
    veiw_author = f"select author_id from bookstore_author where author_name = '{author_name}'"
    cur.execute(veiw_author)
    author_id = cur.fetchall()
    if len(author_id):
        author_id = author_id[0][0]
    else:
        add_new_author = f"insert into bookstore_author (author_name) values('{author_name}');"
        cur.execute(add_new_author)
        connection.commit()
        print(f"new author {author_name} added successfully")
        veiw_author = f"select author_id from bookstore_author where author_name = '{author_name}'"
        cur.execute(veiw_author)
        author_id = cur.fetchall()
        if len(author_id):
            author_id = author_id[0][0]
    connection.close()
    return author_id
        

# def view_cat_id():
#     # connection, cur = connection_database()
#     category_id_list = list()
#     veiw_category = f"select category_id from bookstore_category where category_name = '{category}'"
#     cur.execute(veiw_category)
#     category_id = cur.fetchall()[0][0]
#     # if category_id:
#     #     category_id_list.append(category_id)
#     #     return category_id_list

def add_category_table(category):
    connection, cur = connection_database()
    category = category.split(',')
    category_id_list = list()
    for i in category:
        veiw_category = f"select category_id from bookstore_category where category_name = '{i}'"
        cur.execute(veiw_category)
        category_id = cur.fetchall()
        if len(category_id):
            category_id_list.append(category_id[0][0])
        else:
            add_new_category = f"insert into bookstore_category (category_name) values('{i}');"
            cur.execute(add_new_category)
            connection.commit()
            print(f"new category {i} added successfully")
            veiw_category = f"select category_id from bookstore_category where category_name = '{i}'"
            cur.execute(veiw_category)
            category_id = cur.fetchall()
            if len(category_id):
                category_id_list.append(category_id[0][0])
    connection.close()
    return category_id_list

# def add_books_category_table(book_id,category_id_list):
#     for i in range(len(category_id_list)):

    
    


    


def bookstore_options():
    print("""Bookstore Management System with Sales Analysis
---------------------------------------------
1. Manage inventory
2. Record sales
3. Edit sales records
4. View sales reports
5. Identify bestselling books and authors
6. Quit""")
    
    choice = input('Enter your choice: ')
    return choice

def add_book():
    book_title = input('Enter Book Title[*]: ').strip().title()
    author_name = input('Enter Author name[*]: ').strip().title()
    category = input('Enter Book category[*]: ').strip().title()
    book_cp = input('Enter Book cost price: ')
    if book_cp == '':
        book_cp = 0
    book_sp = input('Enter Book Selling price: ')
    if book_sp == '':
        book_sp = 0
    book_MRP = input('Enter Book MRP[*]: ')
    book_inventory = input('Enter Book stock[*]: ')

    if book_title == '' or book_title == '0' or author_name == '' or author_name == '0' or category == '' or category == '0' or book_MRP == '' or book_MRP == '0' or book_inventory == '':
        print("Mandatory field can't be blank or 0")
        add_book()
    else:
        book_id = add_book_table(book_title,author_name,book_cp,book_sp,book_MRP,book_inventory)
        author_id = add_author_table(author_name)
        category_id_list = add_category_table(category)

        print(book_id,author_id,category_id_list)

        
    

