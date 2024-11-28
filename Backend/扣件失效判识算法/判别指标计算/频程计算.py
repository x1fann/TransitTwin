import pandas as pd
import numpy as np

#三分之一倍频程
def third_octave_levels(x, fs, ref=2e-5):
    '''计算信号的三分之一倍频程级别'''
    nfft = 2 ** 15
    Y = np.fft.fft(x, n=nfft)
    f = np.fft.fftfreq(nfft, 1 / fs)

    YE = np.abs(Y[:nfft // 2]) * 2 / nfft  # 频域中的能量
    L_a = 20 * np.log10(YE / ref)  # 计算频谱声压级

    # 三分之一倍频程
    f_bo_middle = np.array([1, 1.25, 1.6, 2, 2.5, 3.15, 4, 5, 6.3, 8, 10,
                            12.5, 16, 20, 25, 31.5, 40, 50, 63, 80, 100,
                            125, 160, 200, 250, 315, 400, 500])  # 给出的中心频率
    Sxx_bo = np.zeros(len(f_bo_middle))  # 三分之一倍频功率

    for i_bo, fc in enumerate(f_bo_middle):  # 对应 MATLAB 代码中的 fc
        f_start = fc / 2 ** (1 / 6)
        f_stop = fc * 2 ** (1 / 6)
        f_idx = np.where((f >= f_start) & (f <= f_stop))[0]
        # 逆傅里叶变换
        mask = np.zeros(nfft, dtype=bool)
        mask[(f_idx,)] = True
        mask[(-f_idx,)] = True        
        cc = np.fft.ifft(Y * mask)
        # 按照 MATLAB 代码中的做法计算能量
        Sxx_bo[i_bo] = np.sqrt(np.var(cc.real))

    # 避免0值，如果值为0则替换为一个小的正数
    Sxx_bo_div_ref = np.where(Sxx_bo == 0, 1e-12, Sxx_bo)
    L_bo = 20 * np.log10(Sxx_bo_div_ref / ref)  # 转成 dB

    return f_bo_middle, L_bo


input_file = 'E:/数字孪生/扣件失效数据/原始数据/35m失效转置.csv'
output_file = 'E:/数字孪生/扣件失效数据/原始数据/35m频程.csv'

df = pd.read_csv(input_file)

df_third_octave = pd.DataFrame()


for i, col in enumerate(df.columns[1:]):
    signal = df[col].values
    fs = 1000.0
    f_bo_middle, L_bo = third_octave_levels(signal, fs)

    if i == 0:
        df_third_octave['Frequency (Hz)'] = f_bo_middle
        df_third_octave[col] = L_bo
    else:
        df_third_octave[col] = L_bo



df_third_octave.to_csv(output_file, index=False)