# requirements:
# python, pytorch, numpy, simpleaudio
import os
import torch
import numpy as np
import simpleaudio as sa

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/ru_v3.pt', local_file)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

# Текст который будет озвучен
example_text = 'текст'
sample_rate = 48000
speaker = 'baya'

# Эта функция сохраняет WAV на диск
def save_wav(text, speaker, sample_rate):
    # ...

    # Преобразуй текст в массив байтов.
    bytes = text.replace(u"\u00A0", " ").encode("utf-8")

    # ...

save_wav(example_text, speaker, sample_rate)

# Эта часть запускает аудио на колонках. 
audio = model.apply_tts(text=example_text, speaker=speaker, sample_rate=sample_rate, )
audio = audio.numpy()
audio *= 32767 / np.max(np.abs(audio))
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
play_obj.wait_done()