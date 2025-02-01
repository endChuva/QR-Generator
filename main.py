import qrcode
import os
from termcolor import colored

def start_code():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(
        '''
         e88 88e   888 88e      e88'Y88                                           d8                    
        d888 888b  888 888D    d888  'Y   ,e e,  888 8e   ,e e,  888,8,  ,"Y88b  d88    e88 88e  888,8, 
       C8888 8888D 888 88"    C8888 eeee d88 88b 888 88b d88 88b 888 "  "8" 888 d88888 d888 888b 888 "  
        Y888 888P  888 b,      Y888 888P 888   , 888 888 888   , 888    ,ee 888  888   Y888 888P 888    
         "88 88"   888 88b,     "88 88"   "YeeP" 888 888  "YeeP" 888    "88 888  888    "88 88"  888    
             b                                                                                          
             8b,                                                                                                                              

        endChuva.github.io/Profile/

      --------------------------------------------------------------------------------------------------
        ''', "light_red"))

def criar_pasta_qrcodes():
    if not os.path.exists("QRcodes"):
        os.makedirs("QRcodes")

def gerar_qrcode(texto, nome_arquivo):
    criar_pasta_qrcodes()
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4, 
    )

    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    caminho_arquivo = os.path.join("QRcodes", nome_arquivo + ".png")
    img.save(caminho_arquivo)
    print(colored(f"        QR Code salvo em {caminho_arquivo}", "light_green"))

def gerar_qrcode_wifi(ssid, senha, tipo_seguranca="WPA", nome_arquivo="wifi_qrcode.png"):
    criar_pasta_qrcodes()
    wifi_config = f"WIFI:S:{ssid};T:{tipo_seguranca};P:{senha};;"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)

    img = qr.make_image(fill_color="darkblue", back_color="white")

    caminho_arquivo = os.path.join("QRcodes", nome_arquivo + ".png")
    img.save(caminho_arquivo)
    print(colored(f"        QR Code de Wi-Fi salvo em {caminho_arquivo}", "light_green"))

if __name__ == "__main__":
    while True:
        start_code()

        print(colored("        Escolha uma opção:", "light_blue"))
        print(colored("        1 - Gerar QR Code normal", "light_blue"))
        print(colored("        2 - Gerar QR Code de Wi-Fi", "light_blue"))
        escolha = input("        Digite o número da opção desejada: ")

        if escolha == "1":
            texto = input("        Enter the text or URL to generate the QR Code: ")
            nome_arquivo = input("        Enter the output file name: ")
            gerar_qrcode(texto, nome_arquivo)
        elif escolha == "2":
            ssid = input("        Digite o nome da rede Wi-Fi (SSID): ")
            senha = input("        Digite a senha da rede Wi-Fi: ")
            tipo_seguranca = input("        Digite o tipo de segurança (WPA, WEP, ou nopass): ")
            nome_arquivo = input("        Digite o nome do arquivo de saída (ex: wifi_qrcode.png): ")
            gerar_qrcode_wifi(ssid, senha, tipo_seguranca, nome_arquivo)
        else:
            print(colored("        Opção inválida! Tente novamente.", "light_red"))

        continuar = input(colored("        Do you want to generate another QR Code? (y/n): ", "light_blue"))
        if continuar.lower() != 'y':
            break
