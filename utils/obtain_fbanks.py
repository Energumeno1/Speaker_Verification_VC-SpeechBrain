import torch
import matplotlib.pyplot as plt
from speechbrain.dataio.dataio import read_audio
import torchaudio
from speechbrain.processing.features import STFT
from speechbrain.processing.features import spectral_magnitude
from speechbrain.processing.features import Filterbank
import numpy as np
from speechbrain.lobes.features import Fbank

# Se carga un audio específico
file_path = 'C:\\Users\\julen\\OneDrive\\Escritorio\\TFG Electro\\TFG\\TFG\\Datasets\\VoxCeleb1\\dev\\wav\\id10008\\58jhTekFbHk\\00003.wav'  
waveform, sr = torchaudio.load(file_path)

time = torch.arange(0, waveform.size(1)) / sr

# Se plotea la forma de la onda 
plt.figure(figsize=(10, 4))
plt.plot(time.numpy(), waveform.t().numpy())
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.show()

# Se calcula la DFT
fft = torch.fft.fft(waveform)
mag = torch.abs(fft)

# Se plotea la DFT
plt.figure(figsize=(6, 4))
half_point = mag.size(1) // 2
x_axis = torch.linspace(0, sr / 2, half_point)   
plt.plot(x_axis, mag[:, :half_point].t().numpy())
plt.xlabel('Frecuencia(Hz)')
plt.ylabel('Magnitud')
plt.show()

#Se plotea el espectrograma
signal = read_audio(file_path).unsqueeze(0) 
compute_STFT = STFT(sample_rate=16000, win_length=25, hop_length=10, n_fft=400) 
signal_STFT = compute_STFT(signal)
spectrogram = signal_STFT.pow(2).sum(-1) 
spectrogram = spectrogram.squeeze(0).transpose(0,1)
spectrogram_log = torch.log(spectrogram) 
plt.imshow(spectrogram_log.squeeze(0), cmap='hot', interpolation='nearest', origin='lower')
plt.xlabel('Chunk')
plt.ylabel('Frecuencia (Hz)')
plt.show()

#Se calculan los filter banks
compute_fbanks = Filterbank(n_mels=24)

STFT = compute_STFT(signal)
mag = spectral_magnitude(STFT)
fbanks = compute_fbanks(mag)

plt.imshow(fbanks.squeeze(0).t(), cmap='hot', interpolation='nearest', origin='lower')
plt.xlabel('Chunks')
plt.ylabel('Frecuencia')
plt.show()


