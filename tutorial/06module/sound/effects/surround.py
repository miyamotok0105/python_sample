

def run1():
    print("run1!")

def run_echo_echofilter():
    #相対インポート。このモジュールから見て同じ階層のecho.pyを読み込む
    from . import echo
    input = 1
    output = 2
    echo.echofilter(input, output, delay=0.7, atten=4)

