import os
import subprocess 
from functools import lru_cache
from typing import Optional , Union

import numpy as np
import torch 
from torch.nn import functional as F

from .utils import exact_div

# 오디오 하이퍼파라미터
SAMPLE_RATE = 16000 
N_FFT = 400 # 빠른 푸리에 변환 . 파동 알고리즘

# 오디오 변환에서 FFT(Fast Fourier Transform)란 무엇일까요?
# FFT는 오디오 변환에서 중요한 역할을 하는 알고리즘입니다. 이 알고리즘은 시간 영역에서 표현되는 오디오 신호를 주파수 영역으로 변환하는 데 사용됩니다. 즉, 음악을 구성하는 각 주파수 성분의 강도를 분석할 수 있게 해줍니다.
# 샘플링: 오디오 신호를 일정한 간격으로 샘플링하여 이산적인 데이터 포인트 집합을 만듭니다.
# 윈도우 적용: 샘플링된 데이터에 윈도우 함수를 적용하여 불필요한 에너지 누출을 줄입니다.
# DFT 계산: 윈도우 적용된 데이터에 이산 푸리에 변환(DFT)을 계산하여 주파수 영역 데이터를 얻습니다.
# FFT 알고리즘: DFT 계산을 효율적으로 수행하기 위해 FFT 알고리즘을 사용합니다

HOP_LENGTH = 160 # stride?
CHUNK_LENGTH = 30 #
N_SAMPLES = CHUNK_LENGTH * SAMPLE_RATE  # 30초 청크 480,000샘플
N_FRAMES = exact_div(N_SAMPLES, HOP_LENGTH)  # 3000 frames in a mel spectrogram input

N_SAMPLES_PER_TOKEN = HOP_LENGTH * 2  # the initial convolutions has stride 2
FRAMES_PER_SECOND = exact_div(SAMPLE_RATE, HOP_LENGTH)  # 10ms per audio frame
TOKENS_PER_SECOND = exact_div(SAMPLE_RATE, N_SAMPLES_PER_TOKEN)  # 20ms per audio token
