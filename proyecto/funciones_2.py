import time

def presentation():
  """
  Esta función sin parámetros imprime la portada del juego 'El Ahorcado'.
  """

  print()

  texto = """
  ▒█▀▀▀ ▒█░░░ 　 ░█▀▀█ ▒█░▒█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▀▄ ▒█▀▀▀█ 
  ▒█▀▀▀ ▒█░░░ 　 ▒█▄▄█ ▒█▀▀█ ▒█░░▒█ ▒█▄▄▀ ▒█░░░ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ 
  ▒█▄▄▄ ▒█▄▄█ 　 ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄█
  """
  print(texto)

  e = " "*9
  mensaje = [f"{e}LOADING ...",f"{e}COMPLETE"]
  print()
  e1 = " "*23
  e2 = " "*22
  animation = [ "🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳      0 %",
                "🟩🔳🔳🔳🔳🔳🔳🔳🔳🔳      10 %",
                "🟩🟩🔳🔳🔳🔳🔳🔳🔳🔳      20 %",
                "🟩🟩🟩🔳🔳🔳🔳🔳🔳🔳      30 %",
                "🟩🟩🟩🟩🔳🔳🔳🔳🔳🔳      40 %",
                "🟩🟩🟩🟩🟩🔳🔳🔳🔳🔳      50 %",
                "🟩🟩🟩🟩🟩🟩🔳🔳🔳🔳      60 %",
                "🟩🟩🟩🟩🟩🟩🟩🔳🔳🔳      70 %",
                "🟩🟩🟩🟩🟩🟩🟩🟩🔳🔳      80 %",
                "🟩🟩🟩🟩🟩🟩🟩🟩🟩🔳      90 %",
                "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩      100 %"]

  for i in range(len(animation)):
      time.sleep(0.2)
      print("\r" + e1+animation[i], end = "")
      if i == len(animation)-1:
        print("\r" + mensaje[1], end = "")
      else: print("\r" + mensaje[0], end = "")

  print("\n")

  logo =f"""
    {e2}░░░░░░░░░░░░░░░
    {e2}░░    +---+  ░░
    {e2}░░    |   |  ░░
    {e2}░░    O   |  ░░
    {e2}░░   /|\  |  ░░
    {e2}░░   / \  |  ░░
    {e2}░░        |  ░░
    {e2}░░ ========= ░░
    {e2}░░░░░░░░░░░░░░░
  """
  print(logo)
  print("\n")
  print("PRESIONA CUALQUIER TECLA PARA CONTINUAR".rjust(51))
  input()