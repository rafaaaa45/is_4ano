import psycopg2

connection = None
cursor = None

try:
    connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="is-db",
                                  port="5432",
                                  database="is")

    cursor = connection.cursor()

    file_path = '../../../docker/volumes/data/csvtoxml.xml'
    xml_name = 'csvtoxml.xml'

    with open(file_path, encoding='utf-8') as file:
        data = file.read()

        cursor.execute("INSERT INTO imported_documents(file_name,xml) VALUES(%s,%s)", (xml_name, data))
        connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Failed to fetch data", error)

finally:
    if connection:
        cursor.close()
        connection.close()
