import os
import numpy as np
import scipy.signal as signal
import librosa
import soundfile as sf

def eq( input_mp3, freq_range, gain, output_dir):
    # 加载输入的MP3文件
    audio, sr = librosa.load(input_mp3, sr=None, mono=False)  # 将mono参数设为False以保留多个通道的音频

    # 计算频率范围在采样率下的索引范围
    freq_start = freq_range[0]
    freq_end = freq_range[1]
    freq_range_idx = [int(freq_start * len(audio[0]) / sr), int(freq_end * len(audio[0]) / sr)]

    # 创建均衡器滤波器
    b, a = signal.butter(4, [freq_start/(sr/2), freq_end/(sr/2)], btype='band')
    w, h = signal.freqz(b, a)

    # 计算增益系数
    gain_db = np.interp(gain, [-10, 10], [-np.inf, np.inf])
    gain_linear = 10**(gain_db/20)

    # 应用滤波器并进行增益处理
    eq_audio = np.zeros_like(audio)
    for i in range(audio.shape[0]):  # 对每个通道进行处理
        filtered_audio = signal.lfilter(b, a, audio[i])
        eq_audio[i] = filtered_audio * gain_linear

    # 创建输出文件路径
    output_filename = os.path.join(output_dir, "output.mp3")

    # 保存均衡后的音频为MP3文件
    sf.write(output_filename, eq_audio.T, sr, format='mp3')  # 需要转置为(通道数, 采样点数)

    return output_filename
