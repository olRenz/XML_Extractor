def add_template(file, def_name, stat_base):
    file.write(
        '    <Operation Class="PatchOperationAdd">\n'
        f'        <xpath>Defs/ThingDef[defName="{def_name}"]/statBases</xpath>\n'
        '        <value>\n'
        f'           <{stat_base}>TBD</{stat_base}>\n'
        '        </value>\n'
        '    </Operation> \n'
        '\n'
        )


def replace_template(file, def_name, stat_base):
    file.write(
        '    <Operation Class="PatchOperationReplace">\n'
        f'        <xpath>Defs/ThingDef[defName="{def_name}"]/statBases/{stat_base}</xpath>\n'
        '        <value>\n'
        f'           <{stat_base}>TBD</{stat_base}>\n'
        '        </value>\n'
        '    </Operation> \n'
        '\n'
        )

def weight_template(file, def_name):
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
    
def ranged_weapon_template():
    pass

def Melee_weapon_template():
    pass