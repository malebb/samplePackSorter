# 🎵 Sample pack sorter 🎵
This program helps you sort your sample packs.  
It uses your sample names to perform the sorting.
## Usage
```
python3 ./path/to/pack ./path/to/dest/ sorted_pack_name
```
**Where** :  

**./path/to/pack** : relative or absolute path toward your sample pack.  
**./path/to/dest** : relative or absolute path where the sorted sample pack will be created.  
**sorted_pack_name** : name of the sorted sample pack.  
## Basic Example
![example diagram](./sorting_example.jpg?raw=true "basic sorting example")

## How does it works ?
- Read each sample's name to find a category in each one of them.
- If the sample contains *loop* in its name, it'll be placed in a *loops/* sub directory.
- If the sample does not match any of the categories, it'll be place in the *others/* directory.
- Some categories owns sub categories (e.g instruments/ category owns pianos/ guitars/ flutes/ etc...)

## Sample pack format
Every structures of sample pack can be sorted including :
- Pack that contains other sub packs.
- Pack that contains only files without directory.
