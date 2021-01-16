## pyaudio 설치

```
pip install pipwin
pipwin install pyaudio
```

하면 됩니다.

## matplotlib 설치

```
pip install matplotlib
```



## audio.py

audio.py는 pyaudio를 이용해 pcm 데이터를 출력하는 모듈입니다.



## convert_to_pcm.py

convert_to_pcm.py는 -2^15 ~ 2^15 의 숫자 리스트를 받아 16비트 little endian pcm data로 변환하는 모듈입니다.



## signal_generator.py

signal_generator.py는 기본파를 합성하는 신디사이저입니다. 또한 generate함수를 이용해 소리를 주어진 길이만큼 반복해서 생성할 수 있습니다.



## 실습1

raw.py를 실행시켜서 generate된 파동의 파형을 확인하고, FFT 결과를 확인하세요.

## 실습 2

filtered.py를 실행시켜서 IIR필터의 임펄스 응답의 모양을 확인하고 (주어진 필터는 로우 패스 필터입니다. 그러니까 sinc 함수가 잘 나타나는지 확인해 보세요.) 이를 적용한 음원에서 cutoff frequency $f_c$ 보다 큰 성분이 잘 제거되었는지 확인해 보세요.