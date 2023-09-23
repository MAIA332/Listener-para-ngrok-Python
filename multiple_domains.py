import subprocess
import time
import requests
import json
import threading

ngrok_processes = {} 

def start_ngrok(domain, port):
    command = ['ngrok', 'http', str(port)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ngrok_processes[domain] = process

def get_ngrok_tunnel_info(domain):
    try:
        response = requests.get(f"http://localhost:4040/api/tunnels/{domain}")
        data = response.json()
        return data['public_url'], data['public_url'].split('//')[1]
    except Exception as e:
        print(f"Failed to fetch Ngrok tunnel info for {domain}: {str(e)}")
        return None, None

def ngrok_process_thread(domain, port):
    start_ngrok(domain, port)
    print(f"Ngrok process started for {domain} on port {port}")

if __name__ == "__main__":
 
    domain_port_mapping = {
        "dominio1.com": 5000,
        "dominio2.com": 6000,
       
    }

    for domain, port in domain_port_mapping.items():
  
        threading.Thread(target=ngrok_process_thread, args=(domain, port)).start()

    try:
        while True:
            for domain in domain_port_mapping.keys():
                public_url, ip_address = get_ngrok_tunnel_info(domain)
                if public_url and ip_address:
                    print(f"Ngrok Public URL for {domain}: {public_url}")
                    print(f"Ngrok IP Address for {domain}: {ip_address}")
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        for process in ngrok_processes.values():
            process.terminate()
