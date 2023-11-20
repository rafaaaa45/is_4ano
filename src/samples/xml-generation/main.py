from csv_to_xml_converter import CSVtoXMLConverter
import os
import cProfile
from xml_save import Xml_Save


if __name__ == "__main__":
    
    file_path = "C:/Users/crist/Downloads/IS_2024-master/IS_2024-master/docker/volumes/data/all_players.csv"
    
    # Verifique se o arquivo existe antes de criar o conversor
    if not os.path.exists(file_path):
        print(f"O arquivo '{file_path}' não foi encontrado.")
    else:
        converter = CSVtoXMLConverter(file_path)

        # Convert CSV to XML
        xml_str = converter.to_xml_str()

        # Configurações para salvar o arquivo XML
        save_path = r'C:\Users\crist\Downloads'
        file_name = 'csvtoxml.xml'

        # Criar uma instância do XMLImporter e salvar o XML no arquivo
        xml_importer = Xml_Save(xml_str, save_path, file_name)
        file_path_xml = xml_importer.save_to_file()

        print(f'O XML foi salvo em: {file_path_xml}')

        profiler = cProfile.Profile()
        profiler.enable()

        # Convert CSV to XML (novamente, se necessário)
        xml_str = converter.to_xml_str()

        profiler.disable()
        profiler.print_stats(sort="cumulative")