import sqlite3 as lite

def db_1():
    con = lite.connect('test.sqlite') # connect to database
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    #print(data)  # print sqlite version: 3.14.2

    # drop and create table
    cur.execute('drop table if exists Phonebook')
    cur.execute("create table Phonebook (\
        phone char(10) primary key, \
        address text,\
        name text unique, \
        age int not null)")

    # insert data
    cur.execute("INSERT INTO Phonebook (phone, address,name, age) values (\
                '0911111111', \
                'United State', \
                'JhonDoe', \
                53)")
    cur.execute("select * from Phonebook")
    data = cur.fetchall()
    print(data)
    con.close()

def insert_dataframe_to_db():
    import pandas
    employee = [{'name': 'mary', 'age': 23, 'gender': 'F'}, {'name': 'john', 'age': 30, 'gender': 'M'}]
    df = pandas.DataFrame(employee)

    # insert dataframe to sqlite
    with lite.connect('test.sqlite') as db:
        df.to_sql(name='employee', index=False, con=db, if_exists='replace')
    con = lite.connect('test.sqlite')
    cur = con.cursor()
    cur.execute('select * from employee')
    data = cur.fetchall()
    print(data)
    con.close()

insert_dataframe_to_db()

#def read_db_data_to_dataframe():
