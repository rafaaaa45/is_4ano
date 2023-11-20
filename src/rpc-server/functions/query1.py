import psycopg2

def query1():
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="localhost",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()
        cursor.execute("SELECT xpath('//Club[count(Countries/Country/Players/Player) > 20]/@name', xml_column) AS team_names FROM imported_documents")
        result = cursor.fetchall()
        return result

    finally:
        if connection:
            cursor.close()
            connection.close()
