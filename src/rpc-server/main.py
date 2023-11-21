import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from functions.converter import converter
from functions.string_length import string_length
from functions.string_reverse import string_reverse
from functions.xml_validator import validator
from functions.importer import importFile
from functions.query1 import query1
from functions.query2 import query2
from functions.query3 import query3


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)


    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    server.register_function(string_reverse)
    server.register_function(string_length)
    server.register_function(converter)
    server.register_function(validator)
    server.register_function(importFile)
    server.register_function(query1)
    server.register_function(query2)
    server.register_function(query3)

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
