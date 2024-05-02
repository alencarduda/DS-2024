from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(22),sda=Pin(21))

largura = 128
altura = 64

tela = ssd1306.ssd1306_I2C(largura, altura, i2c)

sentinela = 0

while True 
botao_verde.value
botao_azul1.value
botao_azul2.value
botao_vermelho.value

botao_verde = machine.Pin.PULL_UP
tela.text('Iluminacao', 0, 10)

botao_azul1 = machine.Pin.PULL_UP
tela.text('Ar-Condicionado', 0, 10)

botao_azul2 = machine.Pin.PULL_UP
tela.text('Portao Programatico', 0, 10)

botao_vermelho = machine.Pin.PULL_UP
tela.text('Camera', 0, 10)
tela.fill(0)
tela.show()
 
