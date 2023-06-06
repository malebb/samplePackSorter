import os;
import argparse
from argparse import RawTextHelpFormatter
import shutil
from enum import Enum

class SampleTypes(Enum):
    KICK = 0
    SNARE = 1
    BASS = 2
    CLAP = 3
    HAT = 4
    PERC = 5
    FX = 6
    BELL = 7
    OTHER = 8

# Parse program's arguments
parser = argparse.ArgumentParser(description="This program helps you sort your sample pack.\nIt uses the sample names to perform the sorting.", formatter_class=RawTextHelpFormatter)
parser.add_argument("path", help="Path toward the directory containing your samples.")
parser.add_argument("dest", help="Path where the sorted sample pack will be added.")
parser.add_argument("name", help="Name of the created sample pack after sorting.")
args = parser.parse_args()

# Create sorted sample pack folder
path_to_sorted_pack = os.path.join(args.dest, args.name)
if (not os.path.exists(path_to_sorted_pack)):
    os.mkdir(path_to_sorted_pack)

# Look for a category in the sample name
def get_sample_type(sample):
    for sample_type_id in range(len(SampleTypes) - 1):
        sample_type = SampleTypes(sample_type_id).name.lower()
        if (sample.lower().find(sample_type) != -1):
            return SampleTypes(sample_type_id)
    return SampleTypes.OTHER

# Create a new sample category folder if never created
def create_categorie_dir(sample_categorie):
    categorie_path = os.path.join(path_to_sorted_pack, sample_categorie.name.lower())
    if (not os.path.exists(categorie_path) and sample_categorie):
        os.mkdir(categorie_path)
    return (categorie_path)

# Loop through each sample to sort them into the right category
def sort_sample_pack():
    for root, dirs, samples in os.walk(args.path, topdown=True):
        for sample in samples:
            sample_type = get_sample_type(sample);
            sample_dest = create_categorie_dir(sample_type)
            shutil.copy(os.path.join(root, sample), sample_dest)

sort_sample_pack()
