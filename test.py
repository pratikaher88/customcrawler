import psycopg2

# hostname = 'localhost'
# username = 'postgres' # the username when you create the database
# password = '***' #change to your password
# database = 'quotes'

def queryQuotes( conn ) :
    cursor = conn.cursor()
    # cursor.execute("""SELECT table_name FROM information_schema.tables
    #        WHERE table_schema = 'public'""")

    cursor.execute("SELECT * from main_quote")
    for r in cursor.fetchall():
        print(r[0],r[1],r[2],r[3])


    # query =  "INSERT INTO main_quote (text, author) VALUES (%s, %s);"
    # data = ("Hello", "Author")
    #
    # cursor.execute(query,data)
    #
    # conn.commit()
    #
    # cursor.execute("SELECT * from main_quote")
    # for r in cursor.fetchall():
    #     print(r[0],r[1],r[2])

    # cursor.execute("truncate table main_url_details")
    # cursor.execute("truncate table main_quote")
    # cursor.execute("truncate table main_timetocrawl")

    # conn.commit()
    # cursor.close()

    # cursor.execute("Select * FROM main_timetocrawl LIMIT 0")
    # colnames = [desc[0] for desc in cursor.description]
    #
    # print(colnames)

    # for table in cursor.fetchall():
    #     print(table[0])

conn = psycopg2.connect("postgres://oycwhsjvhddhcl:f2e09305580a6190aaad8b8190cee847cf9e543734495f23639a0e64df5f4153@ec2-174-129-255-7.compute-1.amazonaws.com:5432/d6hilf2cnuv69l")
queryQuotes( conn )
conn.close()

# d2c5re4ar3rrqv

# current_DB










