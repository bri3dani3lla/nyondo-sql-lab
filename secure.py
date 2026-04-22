import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def is_valid_name(name):
    if not isinstance(name, str) or len(name) < 2:
        return False
    if '<' in name or '>' in name or ';' in name:
        return False
    return True

def is_valid_username(username):
    if not isinstance(username, str) or username == "":
        return False
    if " " in username:
        return False
    return True

def is_valid_password(password):
    if not isinstance(password, str) or len(password) < 6:
        return False
    return True


def search_product_safe(name):
    if not is_valid_name(name):
        print("Error: Invalid product name")
        return None

    query = "SELECT * FROM products WHERE name LIKE ?"
    param = f"%{name}%"
    rows = conn.execute(query, (param,)).fetchall()
    return rows


def login_safe(username, password):
    if not is_valid_username(username):
        print("Error: Invalid username")
        return None

    if not is_valid_password(password):
        print("Error: Invalid password")
        return None

    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    return row


print("Test 1:", search_product_safe('cement'))          
print("Test 2:", search_product_safe(''))                
print("Test 3:", search_product_safe('<script>'))        

print("Test 4:", login_safe('admin', 'admin123'))        
print("Test 5:", login_safe('admin', 'ab'))              
print("Test 6:", login_safe('ad min', 'pass123'))        

conn.close()
