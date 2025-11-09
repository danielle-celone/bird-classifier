import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import os
'''data augementation script'''

#add noise within one standard deviation of the base signal on a gaussian, scaled by a noise factor
def add_noise(signal, noise_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented = signal + noise*noise_factor
    return augmented

#pitch shift
def pitch_shift(signal, sr, num_steps):
    return librosa.effects.pitch_shift(signal, sr=sr, n_steps=num_steps)


#time stretching
def time_stretch(signal, stretch_factor):
    return librosa.effects.time_stretch(signal, rate=stretch_factor)


def augment_clips(directory):
    for filename in os.listdir(directory):
        print(filename[-4:])
        if filename[-4:] == '.wav':
            with open(os.path.join(directory,filename), 'br') as f:
                stripped_filename = filename[:(len(filename)-3)]
                print(stripped_filename)
                signal, sr = librosa.load(f)
                noise_signal = add_noise(signal,0.1)
                pitch_signal=pitch_shift(signal,sr,0.5)
                stretch_signal=time_stretch(signal,0.2)
                sf.write(f'{directory}/augmented/{stripped_filename}_noise.wav', noise_signal, sr)
                sf.write(f'{directory}/augmented/{stripped_filename}_pitch.wav', pitch_signal, sr)
                sf.write(f'{directory}/augmented/{stripped_filename}_stretch.wav', stretch_signal, sr)


if __name__ == '__main__':

    #chickadees
    directory_bcc = '../data/raw/bcc'
    augment_clips(directory_bcc)

    #northern flickers
    directory_nf = '../data/raw/nf'
    augment_clips(directory_nf)

    #spotted towhees
    directory_st = '../data/raw/st'
    augment_clips(directory_st)

    #steller's jay
    directory_sj = '../data/raw/sj'
    augment_clips(directory_sj)

