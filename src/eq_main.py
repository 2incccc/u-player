from eq import eq

if __name__ == "__main__":
    input_mp3 = "D:\\DESKTOP\\WANGHAO\\WORKSPACE\\u-player-for-comprehensive-experiment-of-programming\\单相思.mp3"
    freq_range = [100, 400]
    gain = 2
    output_dir = "./resource/media/eq"

    eq(input_mp3, freq_range, gain, output_dir)
