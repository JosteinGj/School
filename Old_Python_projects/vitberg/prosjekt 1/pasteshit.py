import numpy as np
from wav_file_loader import read_wavefiles

paths = ['audio/mix_1.wav', 'audio/mix_2.wav', 'audio/mix_3.wav',"vitberg aids.wav"]
data, sampling_rate = read_wavefiles(paths)
num_signals = data.shape[0]