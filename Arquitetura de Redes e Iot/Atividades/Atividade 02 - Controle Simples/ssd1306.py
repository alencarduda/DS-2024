import machine
import time
import ssd1306

btn_vermelho = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
btn_verde = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
btn_cima = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
btn_baixo = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)


while True
  if btn_vermelho.value() == 0:
    print("Botão Vermelho OK")

  if btn_verde.value() == 0:
    print("Botão Verde OK")

  if btn_cima.value() == 0:
    print("Botão Cima OK")

  if btn_baixo.value() == 0:
    print("Botão Baixo OK")

    time.sleep(0.1)
