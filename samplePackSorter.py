import os;
import argparse
from argparse import RawTextHelpFormatter

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
    NONE = 8

parser = argparse.ArgumentParser(description="This program helps you sort your sample pack.\nIt uses the sample names to perform the sorting.", formatter_class=RawTextHelpFormatter)
parser.add_argument("path", help="Path toward the directory containing your samples.")
parser.add_argument("dest", help="Path where the sorted sample pack will be added.")

parser.add_argument("name", help="Name of the created sample pack after sorting.")

args = parser.parse_args()

def getSampleType(sample):
    for sampleTypeId in range(len(SampleTypes) - 1):
        sampleType = SampleTypes(sampleTypeId).name.lower()
        if (sample.lower().find(sampleType) != -1):
            return SampleTypes(sampleTypeId)
    return SampleTypes.NONE

for root, dirs, samples in os.walk(args.path, topdown=True):
    for sample in samples:
        sampleType = getSampleType(sample);
        print(sampleType," " , sample);
