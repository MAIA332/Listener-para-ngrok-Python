import requests
import json
import subprocess
import time
import os

def start_ngrok(port):
    ngrok_process = subprocess.Popen(['ngrok', 'http', str(port)],shell=False,stdout=subprocess.DEVNULL)
    return ngrok_process

def get_ngrok_ip():
    try:
        response = requests.get('http://localhost:4040/api/tunnels')
        data = response.json()
        if 'tunnels' in data:
            for tunnel in data['tunnels']:
                if 'public_url' in tunnel:
                    return tunnel['public_url']
    except requests.exceptions.RequestException as e:
        print('Erro ao obter o IP do ngrok:', str(e))
        return None

if __name__ == '__main__':
    port = 5000  # Change this to your desired port

    ngrok_process = start_ngrok(port)
    
    try:
        while True:
            ngrok_ip = get_ngrok_ip()
            
            if ngrok_ip:
                os.system("cls")
                print('IP do ngrok:', ngrok_ip)
            time.sleep(5)

    except KeyboardInterrupt:
        pass
    finally:
        ngrok_process.terminate()
