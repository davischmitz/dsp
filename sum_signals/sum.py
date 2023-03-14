# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:07:03 2019

@author: jeans
"""

import matplotlib.pyplot as plt
import numpy as np
import wave as fw

arqff = './sin_100Hz_1s.wav';
arquivoWav = fw.open(arqff, 'r');

print("Número canais: ", arquivoWav.getnchannels());
print("Número bytes: ", arquivoWav.getsampwidth());
print("Taxa de amostragem: ", arquivoWav.getframerate());
print("Número de frames: ", arquivoWav.getnframes());
print("Compactação: ", arquivoWav.getcompname());

tipos = np.uint8;
Damp = 256;
if arquivoWav.getsampwidth()>1:
    tipos = np.int16;
    Damp = 32760;

frames = arquivoWav.readframes(-1);
Amplitude = np.fromstring(frames, tipos)/Damp;
fim = np.size(Amplitude);
fim2 = round(fim/2 - 1);

dt = 1.0 / arquivoWav.getframerate();
tempo = np.arange(0, arquivoWav.getnframes() * dt, dt);
arquivoWav.close();


arqff2 = './sin_10000Hz_1s.wav';
arquivoWav2 = fw.open(arqff2, 'r');

print("Número canais: ", arquivoWav2.getnchannels());
print("Número bytes: ", arquivoWav2.getsampwidth());
print("Taxa de amostragem: ", arquivoWav2.getframerate());
print("Número de frames: ", arquivoWav2.getnframes());
print("Compactação: ", arquivoWav2.getcompname());

tipos2 = np.uint8;
Damp2 = 256;
if arquivoWav2.getsampwidth()>1:
    tipos2 = np.int16;
    Damp2 = 32760;

frames2 = arquivoWav2.readframes(-1);
Amplitude2 = np.fromstring(frames2, tipos2)/Damp2;

dt2 = 1.0 / arquivoWav2.getframerate();
tempo2 = np.arange(0, arquivoWav2.getnframes() * dt2, dt2);
arquivoWav2.close();

plt.plot(tempo + tempo2, Amplitude + Amplitude2); plt.grid();
plt.title("sum");

plt.show();


