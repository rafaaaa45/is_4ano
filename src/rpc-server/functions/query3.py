import psycopg2

def query3():
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="localhost",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()
        cursor.execute("SELECT xpath('//Player[@age > 25]/@name', xml_column) AS player_names FROM imported_documents")
        result = cursor.fetchall()
        return result

    finally:
        if connection:
            cursor.close()
            connection.close()
