import sqlite3

test = sqlite3.connect('test.db')

t = test.cursor()

# t.execute('''CREATE TABLE stocks
#                 (date text, trans text, symbol text, qty real, price real)''')
#
# t.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35.15)")
#
# test.commit()
#
# test.close()

# This is the correct method for assembling queries, put your values into python objects and use the ? placeholder
# followed by the argument that includes the object you're trying to enter

# singular example
s = ('RHAT',)

t.execute('SELECT * from stocks where symbol=?', s)
print(t.fetchone())

# many values example
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

t.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

for row in t.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)