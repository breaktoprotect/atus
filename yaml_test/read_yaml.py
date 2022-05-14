"""
Author  : Jeremy Soh @breaktoprotect
Date    : 14 May 2022
What    : Test yaml in python
"""
import yaml

#* Read YAML file
with open("example.yaml", 'rb') as yaml_file:
    example = yaml.load(yaml_file, Loader=yaml.FullLoader)

    print("'Example' object type:", type(example))
    print("Print 'example' yaml object as is: ", example)