import os
import Template

class xml_maker:
    def __init__(self, xml_data):
        self.xml_dict = xml_data
        self.make_directory()
        self.parse_dictionary()
        
    def make_directory(self):
         if not os.path.exists("Output"):
             os.makedirs("Output")

    def parse_dictionary(self):
        for file_name, defs in self.xml_dict.items():
            file = open("Output\\" + f"{file_name}", 'w')
            file.write('<?xml version="1.0" encoding="utf-8"?>\n')
            file.write('<Patch>\n')
            for def_name, stat_bases in defs.items():
                file.write(f'\n <!-- ============== {def_name} =============== --> \n' + '\n')
                Template.weight_template(file, def_name)

                if "StuffEffectMultiplierArmor" not in stat_bases:
                    Template.add_template(file, def_name, "StuffEffectMultiplierArmor")

                for stat_base in stat_bases:
                    if stat_base == "StuffEffectMultiplierArmor" or stat_base == "ArmorRating_Sharp" or stat_base == "ArmorRating_Blunt":
                        Template.replace_template(file, def_name, stat_base)

            file.write('</Patch>')

