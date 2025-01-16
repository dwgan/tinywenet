from pydub import AudioSegment


def convert_m4a_to_wav(input_path, output_path, target_rate=16000, channels=1):
    """
    将 m4a 格式的音频转换为 wav 格式。

    参数：
    - input_path: 输入 m4a 文件路径
    - output_path: 输出 wav 文件路径
    - target_rate: 目标采样率（默认 16000 Hz）
    - channels: 通道数（默认单声道）
    """
    try:
        # 读取 m4a 文件
        audio = AudioSegment.from_file(input_path, format="m4a")

        # 设置目标采样率和通道数
        audio = audio.set_frame_rate(target_rate).set_channels(channels)

        # 导出为 wav 格式
        audio.export(output_path, format="wav")
        print(f"转换成功！输出文件：{output_path}")
    except Exception as e:
        print(f"转换失败：{e}")


# 示例用法
input_m4a = "record.m4a"  # 替换为您的 m4a 文件路径
output_wav = "record.wav"  # 替换为期望的 wav 输出路径
convert_m4a_to_wav(input_m4a, output_wav, target_rate=16000, channels=1)
