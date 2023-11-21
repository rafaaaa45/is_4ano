import csv
import os
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader
from entities.nation import Nation
from entities.club import Club
from entities.player import Player
from entities.country import Country

def read_entities(path):
    reader = CSVReader(path)

    countries = reader.read_entities(
        attr="Nation",  
        builder=lambda row: Nation(row["Nation"])
    )

    clubs = reader.read_entities(
        attr="Club",
        builder=lambda row: Club(row["Club"])
    )

    def after_creating_player(player, row):
        club = clubs[row["Club"]]
        country = countries[row["Nation"]]

        if country not in club.players_by_country:
            club.players_by_country[country] = []

        club.players_by_country[country].append(player)

    reader.read_entities(
        attr="Name",
        builder=lambda row: Player(
            # ... (atributos do jogador)
        ),
        after_create=after_creating_player
    )

    for country in countries.values():
        coordinates = country.get_geoloc(country.get_name())
        country.set_geoloc(coordinates[0], coordinates[1])

    return countries, clubs

def generate_xml(countries, clubs):
    root_el = ET.Element("Football")

    clubs_el = ET.Element("Clubs")

    for club in clubs.values():
        club_el = ET.SubElement(clubs_el, "Club", name=club._name)
        countries_el = ET.SubElement(club_el, "Countries") 
        for country, players in club.players_by_country.items():
            country_el = ET.SubElement(countries_el, "Country", name=country.get_name(), Coordenadas=f"{country._lat}, {country._lon}")
            players_el = ET.SubElement(country_el, "Players")
            for player in players:
                players_el.append(player.to_xml())

    root_el.append(clubs_el)

    return root_el

def to_xml_str(root_el):
    xml_str = ET.tostring(root_el, encoding='utf8', method='xml').decode()
    dom = md.parseString(xml_str)
    return dom.toprettyxml()

def save_to_file(xml_content, save_path, file_name):
    file_path = os.path.join(save_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_content)
    return file_path

def import_file(path, save_path, file_name):
    countries, clubs = read_entities(path)
    xml_root = generate_xml(countries, clubs)
    xml_str = to_xml_str(xml_root)
    file_path = save_to_file(xml_str, save_path, file_name)
    return file_path

# Exemplo de chamada
def converter():
    imported_file_path = import_file("caminho/para/seu/arquivo.csv", "caminho/para/salvar", "arquivo.xml")
    print(f"Arquivo importado e salvo em: {imported_file_path}")


