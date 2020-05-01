from monkeycli.monkeycli import MonkeyCLI


learning_rates = ["0.01", "0.02", "0.03", "0.05"]

for rate in learning_rates:
    monkey = MonkeyCLI()
    monkey.run("python mnist.py --learning-rate {}".format(rate))