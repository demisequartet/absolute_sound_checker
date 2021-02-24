import PySimpleGUI as sg
import random
import class1

onkai = ["ラ", "ラ＃", "シ", "ド", "ド＃", "レ", "レ＃", "ミ", "ファ", "ファ＃", "ソ", "ソ＃"]

fs = 16000
ch = 1
amp = 20000

def makeLayout():

    layout,temp = [],[]

    layout.append([sg.Submit(button_text="音を再生")])

    for i in onkai:
        temp.append(sg.Submit(button_text=i))

    layout.append(temp)
    layout.append([sg.Submit(button_text="終了")])

    return layout


if __name__=="__main__":
        #  セクション1 - オプションの設定と標準レイアウト
    sg.theme('Dark Blue 3')

    layout = makeLayout()

    print(layout)

    # セクション 2 - ウィンドウの生成
    window = sg.Window('絶対音感チェッカー', layout,size=(640,480),resizable=True)

    select = str()
    rnd = int(random.random()*12)

    print(rnd)

    # セクション 3 - イベントループ
    while True:
        event, values = window.read()

        if event is None or event == "終了":
            print('exit')
            break
        elif event == '音を再生':
            show_message = "再生ボタンが押されました"
            # ポップアップ
            sg.popup(show_message)
            Hz = class1.keyConvertToHz(rnd)
            #print(str(Hz) + "Hz" + "を再生します")
            print("音を再生します")
            class1.playMusic(class1.makeSineWave(Hz, 2, amp, fs))
        else:
            index = onkai.index(event)
            print(onkai[index])
            if rnd == index:
                sg.popup("あなたは"+onkai[index]+"と答えました" + "正解です")
            else:
                sg.popup("あなたは"+onkai[index]+"と答えました" + "不正解です" + "答えは" + onkai[rnd] + "でした")
            break;
                


    # セクション 4 - ウィンドウの破棄と終了
    window.close()