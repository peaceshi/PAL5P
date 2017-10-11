from xml_parser import *

path_string = '\Data'

files = get_file_names(set_dir(path_string))

load_xml_document_files(files)
