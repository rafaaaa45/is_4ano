import psycopg2

def query2():
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="localhost",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()
        cursor.execute("SELECT xpath('//Country/@name', xml_column) AS country_names, xpath('//Country/@Coordenadas', xml_column) AS coordinates FROM imported_documents")
        result = cursor.fetchall()
        return result

    finally:
        if connection:
            cursor.close()
            connection.close()
