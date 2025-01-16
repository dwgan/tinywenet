import wenet
from record import record

record("record.wav", time=4)  # modify time to how long you want

model = wenet.load_model('chinese')
result = model.transcribe('record.wav')
print(result['text'])