import os
import random
import shutil

directory = 'C:\\Users\\julen\\OneDrive\\Escritorio\\TFG Electro\\TFG\\TFG\\Datasets\\VoxCeleb1_utterance_reduct\\dev\\wav'

all_utterance_files = list()


# Se eligen 18580 archivos para guardar aleatoriamente
for speaker_folder in os.listdir(directory):
    speaker_path = os.path.join(directory, speaker_folder)
    for dirpath, _, filenames in os.walk(speaker_path):
        utterance_files = [os.path.join(dirpath, file) for file in filenames]
        all_utterance_files.extend(utterance_files)


num_to_keep = 18580
utterance_files_to_keep = random.sample(all_utterance_files, num_to_keep)


# Se borra el resto
for file in all_utterance_files:
    if file in utterance_files_to_keep:
        continue
    else:
        os.remove(file)





    

