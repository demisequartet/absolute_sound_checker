import PySimpleGUI as sg
import random
import class1

onkai = ["ラ", "ラ＃", "シ", "ド", "ド＃", "レ", "レ＃", "ミ", "ファ", "ファ＃", "ソ", "ソ＃"]

fs = 16000
ch = 1
amp = 20000

def makeLayout():

    layout,temp = [],[]

    layout.append([sg.Submit(button_text="音を再生"),sg.Checkbox("チートモードを有効にする",default=False)])
    layout.append([sg.Text("音域の選択"),sg.Radio("mid1",group_id="a",default=True),sg.Radio("mid2",group_id="a"),sg.Radio("Hi",group_id="a")])
                  

    for i in onkai:
        temp.append(sg.Submit(button_text=i))

    layout.append(temp)
    layout.append([sg.Submit(button_text="終了")])

    return layout


def octaveChanger(values):
    if values[1]:
        octave = 0.5
    elif values[2]:
        octave = 1.0
    elif values[3]:
        octave = 2.0

    return octave


if __name__=="__main__":
        #  セクション1 - オプションの設定と標準レイアウト
    sg.theme('Dark Blue 3')

    layout = makeLayout()

    #print(layout)

    # セクション 2 - ウィンドウの生成
    window = sg.Window('絶対音感チェッカー', layout,size=(640,480),resizable=True)

    select = str()
    
    rnd = -9999


    # セクション 3 - イベントループ
    while True:
        event, values = window.read()

        print(values)

        if event is None or event == "終了":
            print('exit')
            break
        elif event == '音を再生':
            show_message = "音量調整してください．OKを押すと音を再生します"
            rnd = int(random.random()*12)
            # ポップアップ
            sg.popup(show_message)
            Hz = class1.keyConvertToHz(rnd,octaveChanger(values),flag = values[0])
            print("音を再生します")
            class1.playMusic(class1.makeSineWave(Hz, 2, amp, fs))
        else:
            index = onkai.index(event)
            print(onkai[index])
            if rnd == -9999:
                sg.popup("再生ボタンが押されていません")
            elif rnd == index:
                sg.popup("あなたは"+onkai[index]+"と答えました" + "正解です")
            else:
                sg.popup("あなたは"+onkai[index]+"と答えました" + "不正解です" + "答えは" + onkai[rnd] + "でした")
            value = sg.PopupYesNo("もう一度挑戦しますか?");

            print(value)

            if value == "No" or value is None:
                break;
                


    # セクション 4 - ウィンドウの破棄と終了
    window.close()