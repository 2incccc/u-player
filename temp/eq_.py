import os
import numpy as np
import scipy.signal as signal
import soundfile as sf


# def eq(input_file, freq_range, gain_factor, output_dir):
# 加载音频文件
audio, sample_rate = sf.read("danxiangsi.mp3")

# 计算频率范围在频谱中的索引范围
freq_bins = np.fft.fftfreq(len(audio), 1 / sample_rate)
start_idx = np.argmax(freq_bins >= 0)
end_idx = np.argmax(freq_bins >= 500)

# 构造滤波器增益响应
filter_order = 5  # 滤波器阶数
filter_freqs = [0, 100, 500, sample_rate/2]  # 滤波器频率边界
gain_db = [0, 2, 2, 0]  # 滤波器增益
filter_gain = 10 ** (np.array(gain_db) / 20)  # 将增益因子转换为幅度倍数
filter_coeffs = signal.firwin2(filter_order, filter_freqs, filter_gain, fs=sample_rate)

# 应用滤波器增益
filtered_audio = signal.lfilter(filter_coeffs, 1, audio)

# 创建输出目录（如果不存在）
os.makedirs("./resource/media/eq", exist_ok=True)

# 构建输出文件路径
output_file = os.path.join("./resource/media/eq", os.path.basename("danxiangsi.mp3"))

# 将音频数据保存为MP3格式文件
sf.write(output_file, filtered_audio, sample_rate, subtype='PCM_16', format='WAV', endian='LITTLE')
