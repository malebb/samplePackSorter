import os;
import argparse
from argparse import RawTextHelpFormatter
import shutil
from SampleTypes import sample_types

# Parse program's arguments
parser = argparse.ArgumentParser(description=
"Sample Pack Sorter helps you sort your sample pack.\n\
It uses your samples' name to perform the sorting."\
                                 , formatter_class=RawTextHelpFormatter)
parser.add_argument("path", help="Path toward the directory containing your samples.")
parser.add_argument("dest", help="Path where the sorted sample pack will be created.")
parser.add_argument("name", help="Name of the created sample pack after sorting.")
args = parser.parse_args()

# Create sorted sample pack folder
path_to_sorted_pack = os.path.join(args.dest, args.name)
if (not os.path.exists(path_to_sorted_pack)):
    os.makedirs(path_to_sorted_pack)

# Create a new sample category folder if never created
def create_categorie_dir(sample_name):
    sample_name = sample_name.lower()
    type_found = False
    type_path = ""
    for sample_type in sample_types:
        for type_match in sample_types[sample_type]:
            if (sample_name.find(type_match) != -1):
                type_found = True
                break
        if type_found:
            type_path = os.path.join(path_to_sorted_pack, sample_type)
            break
    if not type_found:
        type_path = os.path.join(path_to_sorted_pack, "others")
    if sample_name.find("loop") != -1:
        type_path = os.path.join(type_path, "loop")
    if (not os.path.exists(type_path)):
        os.makedirs(type_path)
    return (type_path)

# Loop through each sample to sort them into the right category
def sort_sample_pack():
    file_sorted_nb = 0
    for root, dirs, samples in os.walk(args.path, topdown=True):
        for sample_name in samples:
            sample_dest = create_categorie_dir(sample_name)
            shutil.copy(os.path.join(root, sample_name), sample_dest)
            file_sorted_nb += 1
    return file_sorted_nb

file_sorted_nb = sort_sample_pack()

print(file_sorted_nb, "files have been sorted successfully")
