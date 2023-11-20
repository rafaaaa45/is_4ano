import os

class Xml_Save:
    def __init__(self, xml_content, save_path, file_name):
        self.xml_content = xml_content
        self.save_path = save_path
        self.file_name = file_name

    def save_to_file(self):
        file_path = os.path.join(self.save_path, self.file_name)
        with open(file_path, 'w', encoding='utf-8') as xml_file:
            xml_file.write(self.xml_content)
        return file_path
