import machine
import time

led_vermelho = machine.Pin(14, machine.Pin.OUT)
led_verde = machine.Pin(18, machine.Pin.OUT)
led_amarelo = machine.Pin(27, machine.Pin.OUT)
botao = machine.Pin.PULL_UP


while True:
    led_vermelho.value(1)
    time.sleep(5)
    led_vermelho.value(0)
    time.sleep(0.1)

    led_verde.value(1)
    time.sleep(3)
    led_verde.value(0)
    time.sleep(0.1)

    led_amarelo.value(1)
    time.sleep(1.5)
    led_amarelo.value(0)
    time.sleep(0.1)

