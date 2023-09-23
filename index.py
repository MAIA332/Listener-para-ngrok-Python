import requests
import json

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
    ngrok_ip = get_ngrok_ip()
    if ngrok_ip:
        print('IP do ngrok:', ngrok_ip)
