import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

print("\n--- Query A: All products ---")
rows = cursor.execute('SELECT * FROM products').fetchall()
for r in rows:
    print(r)

print("\n--- Query B: Name and price ---")
rows = cursor.execute('SELECT name, price FROM products').fetchall()
for r in rows:
    print(r)

print("\n--- Query C: Product with id = 3 ---")
rows = cursor.execute('SELECT * FROM products WHERE id = 3').fetchall()
for r in rows:
    print(r)

print("\n--- Query D: Name contains 'sheet' ---")
rows = cursor.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall()
for r in rows:
    print(r)

print("\n--- Query E: Sorted by price (highest first) ---")
rows = cursor.execute('SELECT * FROM products ORDER BY price DESC').fetchall()
for r in rows:
    print(r)

print("\n--- Query F: Top 2 most expensive ---")
rows = cursor.execute('SELECT * FROM products ORDER BY price DESC LIMIT 2').fetchall()
for r in rows:
    print(r)

print("\n--- Query G: Update Cement price ---")
cursor.execute('UPDATE products SET price = 38000 WHERE id = 1')
conn.commit()

rows = cursor.execute('SELECT * FROM products').fetchall()
for r in rows:
    print(r)

conn.close()

