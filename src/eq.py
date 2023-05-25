import os
import librosa
import numpy as np
import soundfile as sf

## TODO 简单滤波算法
def eq(input_file, freq_range, gain_factor, output_dir):
    # 加载音频文件
    y, sr = librosa.load(input_file)

    # 计算频率范围在频谱中的索引范围
    freq_bins = np.fft.fftfreq(len(y), 1/sr)
    start_idx = np.argmax(freq_bins >= freq_range[0])
    end_idx = np.argmax(freq_bins >= freq_range[1])

    # 设置均衡增益
    gain = 10 ** (gain_factor / 20)  # 将增益因子转换为幅度倍数

    # 应用均衡增益
    for i in range(start_idx, end_idx+1):
        y[i] *= gain

    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)

    # 构建输出文件名
    file_name = os.path.splitext(os.path.basename(input_file))[0]  # 获取输入文件名（不包含扩展名）
    freq_info = f'{freq_range[0]}-{freq_range[1]}Hz'  # 频率范围信息
    gain_info = f'{gain_factor}dB'  # 增益信息
    output_file = os.path.join(output_dir, f'{file_name}_{freq_info}_{gain_info}.mp3')

    # 将音频数据保存到文件
    sf.write(output_file, y, sr)