from Extractor import Extractor
from xml_maker import xml_maker

def my_function():
  print("Function called")
  xml_data = Extractor().get_dict()
  xml_func = xml_maker(xml_data)

if __name__ == "__main__":
  print("Script executed directly")
  my_function()
else:
  print("Script imported as a module")