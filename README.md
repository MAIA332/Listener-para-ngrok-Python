# Projeto de gerenciamento de processos e portas do Ngrok

Este projeto consiste em um script Python para gerenciar a execução do Ngrok e obter o IP público para um determinado porta.

## Pré-requisitos

- Python 3.x
- Ngrok (https://ngrok.com/)
- Bibliotecas Python: `subprocess`, `requests`

## Como usar

1. Certifique-se de ter o Python 3.x instalado.

2. Faça o download e instale o Ngrok em seu sistema a partir do site oficial: [Ngrok - Download](https://ngrok.com/download)

3. Instale as bibliotecas Python necessárias usando pip:

4. Edite o código no arquivo index.py para especificar a porta que deseja expor através do Ngrok:

```
port = 5000  # Altere para a porta desejada
```
5. Execute o script Python:

```
python index.py
```

### É possível ainda gerenciar multiplos domínios usando a feature ```multiple_domains.py```

1. Edite o código para mapear os domínios e portas desejadas
```
domain_port_mapping = {
 "dominio1.com": 5000,
 "dominio2.com": 6000,
}
```


<p align="center">
  Feito com ❤️ por Lukas Maia
</p>
