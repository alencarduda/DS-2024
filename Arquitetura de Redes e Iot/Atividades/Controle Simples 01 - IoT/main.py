from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(22),sda=Pin(21) )

largura = 128
altura = 64

tela = ssd1306.ssd1306_I2C(largura, altura, i2c)
while True
red = botao.value ()
black = botao.value ()

  if red == 0
tela.text('A temperatura', 0, 0)
tela.text('do quarto e de', 0, 10)
tela.text('29C', 0, 20)

  if black == 0
tela.text('Sua tv esta', 0, 0)
tela.text('ligada e acessou', 0, 10)
tela.text('Netflix', 0, 20)
tela.fill(0)
tela.show()
 