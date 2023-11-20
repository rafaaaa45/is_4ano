from lxml import etree


def validar(xml_path: str, xsd_path: str) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result


def validator() -> str:
    xml_path = '../../../docker/volumes/data/csvtoxml.xml'
    xsd_path = '../../../docker/volumes/data/all_players.xsd'

    if validar(xml_path, xsd_path):
        print("O XML criado é válido")
    else:
        print("O XML criado não é válido")


if __name__ == "__main__":
    validator()