import os
import xml.etree.cElementTree as ET

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
            file.write('<Patch>\n')
            for def_name, stat_bases in defs.items():
                self.patch_add_weight_template(file, def_name)
                for stat_base in stat_bases:
                    if stat_base == "StuffEffectMultiplierArmor" or stat_base == "ArmorRating_Sharp" or stat_base == "ArmorRating_Blunt":
                        self.patch_replace_template(file, def_name, stat_base)

                file.write('\n ============================= \n' + '\n')
            file.write('</Patch>')


    def patch_add_template(self, file, def_name, stat_base):
        file.write(
            '    <Operation Class="PatchOperationAdd">\n'
            f'        <xpath>Defs/ThingDef[defName="{def_name}"]/statBases</xpath>\n'
            '        <value>\n'
            f'           <{stat_base}>TBD</{stat_base}>\n'
            '        </value>\n'
            '    </Operation> \n'
            '\n'
            )


    def patch_replace_template(self, file, def_name, stat_base):
        file.write(
            '    <Operation Class="PatchOperationReplace">\n'
            f'        <xpath>Defs/ThingDef[defName="{def_name}"]/statBases/{stat_base}</xpath>\n'
            '        <value>\n'
            f'           <{stat_base}>TBD</{stat_base}>\n'
            '        </value>\n'
            '    </Operation> \n'
            '\n'
            )

    def patch_add_weight_template(self, file, def_name):
        file.write(
            '    <Operation Class="PatchOperationAdd">\n'
            f'        <xpath>Defs/ThingDef[defName="{def_name}"]/statBases</xpath>\n'
            '        <value>\n'
            '            <Bulk>TBD</Bulk>\n'
            '            <WornBulk>TBD</WornBulk>\n'
            '        </value>\n'
            '    </Operation> \n'
            '\n'
            )