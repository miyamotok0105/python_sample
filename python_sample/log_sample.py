import logging

logging.basicConfig(level=logging.DEBUG, 
    filename="log_sample.log",
    format="%(asctime)s %(levelname)-7s %(message)s")

logger = logging.getLogger("logger")    #logger名loggerを取得
logger.setLevel(logging.DEBUG)  #loggerとしてはDEBUGで

#handler1を作成
handler1 = logging.StreamHandler()
handler1.setFormatter(logging.Formatter(
    "H1, %(asctime)s %(levelname)8s %(message)s"))

#handler2を作成
handler2 = logging.StreamHandler()
handler2.setLevel(logging.WARN)     #handler2はLevel.WARN以上
handler2.setFormatter(logging.Formatter(
    "H2, %(asctime)s %(levelname)8s %(message)s"))

#loggerに2つのハンドラを設定
logger.addHandler(handler1)
logger.addHandler(handler2)

#出力処理
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
