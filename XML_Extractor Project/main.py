from Extractor import Extractor
from xml_maker import xml_maker
from weapon_maker import weapon_maker

# IDEA make the input different folders that I manually set. 
# then the outputs will be correct and run a different function depending on the folder they open

def my_function():
	print("Function called")
	xml_data = Extractor().get_dict()
	weapon_data = Extractor().pull_weapon_data()
	xml_maker(xml_data)
	weapon_maker(weapon_data)

if __name__ == "__main__":
	print("Script executed directly")
	my_function()

else:
	print("Script imported as a module")
