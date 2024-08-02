import os
import random
import shutil
import csv


directory = 'C:\\Users\\julen\\OneDrive\\Escritorio\\TFG Electro\\TFG\\TFG\\Datasets\\VoxCeleb1_speaker_reduct\\dev\\wav'
ids_to_keep = list()

#Se escogen 150 carpetas aleatoriamente y se borra el resto
all_folders = [os.path.join(directory, spk_id) for spk_id in os.listdir(directory)]
folders_to_keep = random.sample(all_folders, 150)


for directory in folders_to_keep:
    id_keep = directory.split('\\')[len(directory.split('\\'))-1]
    ids_to_keep.append(id_keep)


folders_to_keep = [os.path.join(directory, spk_id) for spk_id in ids_to_keep]
for folder in all_folders:
    if folder.split('\\')[len(folder.split('\\'))-1] not in ids_to_keep:
        shutil.rmtree(folder)


### Hay que modificar los metadatos del .csv
vox_meta = 'C:\\Users\\julen\\OneDrive\\Escritorio\\TFG Electro\\TFG\\TFG\\Datasets\\VoxCeleb1_speaker_reduct\\vox1_meta.csv'

lines_to_keep = []

with open(vox_meta, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  
    for line in reader:
        first_column = line[0]  
        first_column_parts = first_column.split('\t')
        first_id = first_column_parts[0]  
        if first_id in ids_to_keep:
            lines_to_keep.append(line)

with open(vox_meta, 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')  
    writer.writerow(header)  
    writer.writerows(lines_to_keep)

    





