import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# ======================================= Confiuration ===============================================
model_path = "vosk-model-small-en-us-0.15"  
keywords_milk_coffee = ["milk coffee","hot milk coffee","cappuccino","macchiato","coffee with milk"]
keywords_coffee = ["coffee","cafe", "iced coffee", "espresso", "double espresso"]
keywords_milk_tea = ["milk tea", "classic milk tea", "brown sugar milk tea","tea with milk"]

# ======================================= Initialize =================================================
q = queue.Queue()

device_info = sd.query_devices(sd.default.device[0], 'input')
samplerate = int(device_info['default_samplerate'])

model = Model(model_path)
rec = KaldiRecognizer(model, samplerate)
rec.SetWords(True)

def callback(indata, frames, time, status):
    if status:
        print("Audio Error:", status)
    q.put(bytes(indata))

def contains_keywords(text, keywords):
    for kw in keywords:
        if kw in text:
            return True
    return False

# ======================================== Run =========================================
print(f"Listening... (sample rate = {samplerate})")
with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "").lower()
            if text:
                print("Speak:", text)

                if contains_keywords(text, keywords_milk_coffee):
                    print("Keyword Detect: milk coffee")
                elif contains_keywords(text, keywords_coffee):
                    print("Keyword Detect: coffee")
                elif contains_keywords(text, keywords_milk_tea):
                    print("Keyword Detect: milk tea")
                else:
                    print("Not Keyword Detect")
