import asyncio
from pyppeteer import launch

ip = None  # Variável para armazenar o endereço IP

async def navegador():
    browser = await launch(headless=False)  # Iniciar uma instância do navegador Chromium em modo não "headless" (com interface gráfica)
    page = await browser.newPage()  # Criar uma nova página no navegador
    await page.goto('http://127.0.0.1:4040')  # Navegar para a URL especificada
    classcss = await page.querySelector("[class='tunnels']")  # Encontrar um elemento com a classe CSS 'tunnels'
    text = await page.evaluate('(element) => element.textContent', classcss)  # Obter o conteúdo de texto desse elemento
    global ip
    ip = text  # Armazenar o endereço IP da variável 'text' na variável 'ip'
    await browser.close()  # Fechar o navegador

asyncio.get_event_loop().run_until_complete(navegador())  # Chamar a função 'navegador' para obter o endereço IP

if ip is not None:
    print(ip)
else:
    print("IP não encontrado.")
