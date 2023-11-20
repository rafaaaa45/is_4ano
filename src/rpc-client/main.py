import xmlrpc.client

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

import xmlrpc.client

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://0.0.0.0:9000')

# Menu Display
while True:

    print(" 1 - Convert CSV file             ")
    print(" 2 - Validate XML file            ")
    print(" 3 - Import XML file              ")
    print(" 4 - Queries                      ")
    print(" 5 - Exit                         ")

    opc = str(input("Selecione a opçao desejada: "))

    if (opc == '1'):
        print("Convert CSV file")
        server.converter()

    elif (opc == '2'):
        print("Validate XML file")
        output = server.validator()
        print(output)

    elif (opc == '3'):
        print("Import XML file")
        result = server.importFile('../../../docker/volumes/data/csvtoxml.xml', input("Set Database file name: "))

    elif (opc == '4'):
        print(" 1 - Selecionar todas as equipas com mais de 20 jogadores")
        print(" 2 - Nome e coordenadas de todos os países")
        print(" 3 - Selecionar todos os jogadores com mais de 25 anos")

        opc2 = str(input("Selecione a opçao desejada: "))

        if (opc2 == '1'):
            query1 = server.query1()
            print(query1)

        elif (opc2 == '2'):
            query2 = server.query2()
            print(query2)


        elif (opc2 == '3'):
            query3 = server.query3()
            print(query3)


    elif (opc == '5'):
        print("Exiting")
        break

    else:
        print("Invalid option")
