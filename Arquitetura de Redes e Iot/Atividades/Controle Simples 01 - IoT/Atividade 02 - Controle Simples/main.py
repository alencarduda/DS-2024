import machine
import time
import ssd1306

# Botões de controle
btn_vermelho = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
btn_verde = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# Botões de navegação
btn_cima = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
btn_baixo = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)

# LED
led_desligado = machine.Pin(17, machine.OUT)
led_ligado = machine.Pin(18, machine.OUT)

# Tela
largura = 128
altura = 64
12c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
tela = ssd1306.SSD1306_I2C(largura, altura, i2c)

qual_tela = 1
status_iluminacao = "OFF"
status_arcondicionado = "OFF"
status_portalprincipal = "OFF"
status_camera = "OFF"


while True

print(qual_tela)

if qual_tela = 1

  if btn_vermelho.value() == 0:
    status_iluminacao = OFF
    print("Botão Vermelho OK")

  if btn_verde.value() == 0:
    status_arcondicionado = OFF
    print("Botão Verde OK")

  if btn_cima.value() == 0 and qual_tela >= 3:
    qual_tela -= 1
    status_portalprincipal
    print("Botão Cima OK")

  if btn_baixo.value() == 0 and qual_tela <= 3:
    qual_tela += 1
    status_camera
    print("Botão Baixo OK")

    
    print(qual_tela)

  
  if qual_tela = 1
    tela.fill(0)
    tela.text("ILUNIMACAO", 0, 0)
    # tela.text("Status:", 0, 25)
    if staus_iluminacao == "OFF" :
      led_desligado.value (1)
      led_ligado.value (0)
      elif status_iluminacao == "ON":
      tela.text("Status: ON;, 0, 25")
      led.desligado.value(0)
      led.ligado.value(1)
    tela.text("[1/4]", 0, 50)
    tela.show()

  elif qual_tela = 2
  tela.fill(0)
  tela.text("AR-CONDICIONADO", 0, 0)
    # tela.text("Status:", 0, 25)
  if status_arcondicionado == "OFF" :
      led_desligado.value (1)
      led_ligado.value (0)
      elif status_arcondicionado == "ON":
      tela.text("Status: ON;, 0, 25")
      led.desligado.value(0)
      led.ligado.value(1)
    tela.text("[2/4]", 0, 50)
    tela.show()


  elif qual_tela = 3
  tela.fill(0)
  tela.text("PORTAO PRINCIPAL", 0, 0)
    # tela.text("Status:", 0, 25)
  if status_portalprincipal == "OFF" :
      led_desligado.value (1)
      led_ligado.value (0)
      elif status_portalprincipal == "ON":
      tela.text("Status: ON;, 0, 25")
      led.desligado.value(0)
      led.ligado.value(1)
    tela.text("[3/4]", 0, 50)
    tela.show()

  elif qual_tela = 4
  tela.fill(0)
  tela.text("CAMERA", 0, 0)
    # tela.text("Status:", 0, 25)
  if status_camera == "OFF" :
      led_desligado.value (1)
      led_ligado.value (0)
      elif status_camera == "ON":
      tela.text("Status: ON;, 0, 25")
      led.desligado.value(0)
      led.ligado.value(1)
    tela.text("[4/4]", 0, 50)
    tela.show()
    
    time.sleep(0.1)