import pyaudio
import PySimpleGUI as sg
import numpy as np
import wave
import sys
import random
import struct


fs = 16000
ch = 1
amp = 20000



def makeSineWave(freq, sec, amp, fs):
    n = np.arange(0, int(fs * sec), 1.0)
    data = amp * np.sin(2 * np.pi * freq * n / fs)
    return data.astype(np.int16)


def playMusic(data):
    binaryData = struct.pack("h" * len(data), *data)
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=int(fs), output=True)

    size = 1024
    current = 0
    buf = binaryData[current:current+size]
    while len(buf) != 0:
        stream.write(buf)
        current = current + size
        buf = binaryData[current:current+size]

    stream.close()
    audio.terminate()


def keyConvertToHz(num):
    freq = [220, 233, 246, 261, 277, 293, 311, 329, 349, 369, 391, 415]

    return freq[num]


def answerCheck(key, rnd):
    str = "asdfghjkl;:]"
    onkai = ["ラ", "ラ＃", "シ", "ド", "ド＃", "レ", "レ＃", "ミ", "ファ", "ファ＃", "ソ", "ソ＃"]

    index = str.find(key)

    print("あなたは"+onkai[index] + "と答えました")
    if str.find(key) == rnd:
        print("正解です")
    else:
        print("不正解です")
        print("答えは" + onkai[rnd] + "でした")


if __name__ == '__main__':

    print("絶対音感チェッカーへようこそ！！")
    print("ある音階の正弦波の音が再生されます")
    print("a:ラ,s:ラ＃,d:シ,f:ド,g:ド＃,h:レ,j:レ＃,k:ミ,l:ファ,;ファ＃,:ソ,]ソ＃")
    print("つまり，キーボード中段(asdfghjkl;:])に音階がラ・・・・というように対応しているので再生された音に対応するキーを1つだけ入力しよう！")
    print("その前に!!! お使いのパソコンの音量を調整してください!!!!(イヤホンを使用しているなら小さめがおすすめです)")
    input("調整が終わったらenterを押してください:")

    rnd = int(random.random()*12)

    # print(rnd)

    Hz = keyConvertToHz(rnd)
    #print(str(Hz) + "Hz" + "を再生します")
    print("音を再生します")
    playMusic(makeSineWave(Hz, 2, amp, fs))

    answerCheck(input("答えを入力してください:"), rnd)






