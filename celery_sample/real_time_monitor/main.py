import tasks

print('<first task>')
# ここでタスク起動　(runタスク)
worker = tasks.run.delay()
# 終わらぬなら終わるまで待とうホトトギス
while not worker.ready():
    pass
#　返り値をだす
print(worker.result)

print('<second task>')
# ここでタスク起動　(calcタスク)
worker = tasks.calc.delay(100, 200)
# 終わらぬなら終わるまで待とうホトトギス
while not worker.ready():
    pass
#　返り値をだす
print(worker.result)

