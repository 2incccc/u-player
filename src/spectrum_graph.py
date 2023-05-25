import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

## TODO 声谱图生成
def plot_and_display_spectrogram(audio_path, offset, duration):
    # 加载音频文件并限制时间段
    y, sr = librosa.load(audio_path, offset = offset, duration = duration)

    # 计算短时傅里叶变换（STFT）
    D = librosa.stft(y, n_fft=2048, hop_length=512)
    # 转换为分贝尺度
    S_db = librosa.amplitude_to_db(abs(D), ref=np.max)

    # 显示声谱图
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')

    # 生成输出路径
    audio_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_path = f'./resource/spectrogram/{audio_name}_{offset}_{duration}.png'

    # 保存声谱图为静态图像(防止计算坐标过程中电脑卡死)
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close()
    # 读取保存的图像文件
    image = Image.open(output_path)
    # 创建 Matplotlib 图像窗口
    fig, ax = plt.subplots()
    # 显示图像
    ax.imshow(image)
    # 隐藏坐标轴
    ax.axis('off')
    # 展示图像
    plt.show()



