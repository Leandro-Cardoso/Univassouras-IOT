import serial
import time
import random

# CONFIGURAÇÃO
PORTA_SIMULADA = 'COM10' # Deve ser a primeira porta do par virtual
BAUDRATE = 9600
INTERVALO = 5.0 # Envia dados a cada 5 segundos

def simular_arduino():
    print(f"Iniciando simulador Arduino na porta {PORTA_SIMULADA}...")
    try:
        # Abre a porta COM10, que está ligada à COM11 (onde o Django vai ler)
        ser = serial.Serial(PORTA_SIMULADA, BAUDRATE, timeout=1)
        time.sleep(2) # Espera a conexão estabilizar
        print("Simulador conectado e pronto para enviar dados.")

        while True:
            # Geração de dados simulados (valores flutuantes)
            temperatura = 20.0 + random.uniform(-2.0, 5.0)
            umidade = 50.0 + random.uniform(-10.0, 10.0)

            # Formato de saída (EXATAMENTE como o Django espera: "temp,umid\n")
            dados_enviados = f"{temperatura:.2f},{umidade:.2f}\n"

            ser.write(dados_enviados.encode('utf-8')) # Envia os dados
            print(f"Enviado: {dados_enviados.strip()}")
            
            time.sleep(INTERVALO) # Atraso entre os envios

    except serial.SerialException as e:
        print(f"Erro serial (Verifique a porta e se ela está livre): {e}")
    except KeyboardInterrupt:
        print("Simulador encerrado.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == '__main__':
    simular_arduino()
