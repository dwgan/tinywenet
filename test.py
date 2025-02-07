import wenet
from record import record
from auto_record import auto_record

# record("record.wav", time=4)  # modify time to how long you want
auto_record(output_filename="record.wav", min_record_time=2, silence_timeout=0.5)
print('正在加载模型...')
model = wenet.load_model('chinese')
print('正在转文字...\n')
result = model.transcribe('record.wav')
print(result['text'])