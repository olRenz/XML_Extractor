import os
import xml.etree.cElementTree as ET

class Extractor():
    
    def __init__(self):
        self.xml_name = None
        self.mod_path = r"Mods"
        self.xml_dict = {}
        self.weapon_xml = []
        self.read_files()


    def read_files(self):
        for root, dirs, files in os.walk(self.mod_path):
            if "Languages" in dirs:
                dirs.remove("Languages")
            for file in files:
                if file.endswith(".xml"):
                    self.xml_name = file
                    xml_file = os.path.join(root, file)
                    if self.xml_name not in self.xml_dict:
                        self.xml_dict.update({self.xml_name: {}})
                    self.pull_def_name(xml_file)

        self.pull_weapon_data()    
                    
    
    def pull_def_name(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for thing_def in root.findall('ThingDef'):
            defname = thing_def.findtext('defName')
            if defname is None:
                continue

            weapon_tag = thing_def.find('weaponTags')
            if weapon_tag and xml_file not in self.weapon_xml:
                self.weapon_xml.append(xml_file)
                continue

            if defname not in self.xml_dict[self.xml_name]:
                self.xml_dict[self.xml_name][defname] = {}

            stat_bases = thing_def.find('statBases')
            if stat_bases is None:
                continue

            for subelement in stat_bases:
                if subelement.tag not in self.xml_dict[self.xml_name][defname]:
                    self.xml_dict[self.xml_name][defname].update({subelement.tag:subelement.text})
                    continue
                self.xml_dict[self.xml_name][defname].update({subelement.tag:subelement.text})


    def pull_weapon_data(self):
        return self.weapon_xml

        
    def get_dict(self):
        return self.xml_dict
