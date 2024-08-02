import csv
#Se obtienen los datos de la lista de verificación y vox1_meta
with open("veri_test2.txt", "r") as verification_file:
    verification_list = verification_file.read().splitlines()


metadata = {}
with open("vox1_meta.csv", "r") as metadata_file:
    csv_reader = csv.reader(metadata_file, delimiter='\t')
    next(csv_reader)
    for row in csv_reader:
        voxceleb_id, _, gender, _, _ = row
        metadata[voxceleb_id] = gender.lower()

#Se obtienen tres listas con pares m-m,f-f,m-f/f-m
man_man_pairs = []
woman_woman_pairs = []
man_woman_pairs = []

for line in verification_list:
    print(line)
    label, path1, path2 = line.split()
    voxceleb_id_1 = path1.split("\\")[0]
    voxceleb_id_2 = path2.split("\\")[0]
    
    gender_1 = metadata.get(voxceleb_id_1)
    gender_2 = metadata.get(voxceleb_id_2)

    if gender_1 == "m" and gender_2 == "m":
        man_man_pairs.append(line)
    elif gender_1 == "f" and gender_2 == "f":
        woman_woman_pairs.append(line)
    else:
        man_woman_pairs.append(line)

# Se crean las tres listas de verificación con los datos empleados
with open("man_man_pairs.txt", "w") as man_man_file:
    man_man_file.write("\n".join(man_man_pairs))

with open("woman_woman_pairs.txt", "w") as woman_woman_file:
    woman_woman_file.write("\n".join(woman_woman_pairs))

with open("man_woman_pairs.txt", "w") as man_woman_file:
    man_woman_file.write("\n".join(man_woman_pairs))
