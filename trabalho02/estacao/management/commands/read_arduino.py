from django.core.management.base import BaseCommand
from estacao.models import Data
import serial
import time

class Command(BaseCommand):
    help = 'Lê dados do Arduino pela porta serial e salva no banco de dados.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--port',
            type=str,
            default='COM3',
            help='Porta serial do Arduino (ex: COM3 no Windows ou /dev/ttyUSB0 no Linux)'
        )
        parser.add_argument(
            '--baudrate',
            type=int,
            default=9600,
            help='Taxa de transmissão (baudrate) da comunicação serial.'
        )
        parser.add_argument(
            '--interval',
            type=float,
            default=5.0,
            help='Intervalo em segundos entre cada leitura.'
        )

    def handle(self, *args, **options):
        port = options['port']
        baudrate = options['baudrate']
        interval = options['interval']

        self.stdout.write(self.style.SUCCESS(f'Conectando à porta {port} ({baudrate} bps)...'))

        try:
            arduino = serial.Serial(port=port, baudrate=baudrate, timeout=1)
            self.stdout.write(self.style.SUCCESS("Conectado com sucesso!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro ao abrir porta serial: {e}"))
            return

        try:
            while True:
                line = arduino.readline().decode().strip()
                print(line, "<- AQUI") # TODO: REMOVER

                if line:
                    try:
                        temperature, humidity = map(float, line.split(','))

                        Data.objects.create(
                            temperature = temperature,
                            humidity = humidity
                        )

                        self.stdout.write(self.style.SUCCESS(f"Salvo: {temperature}°C | {humidity}%"))
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Formato inválido: '{line}'"))

                time.sleep(interval)

        except KeyboardInterrupt:
            self.stdout.write(self.style.NOTICE("Leitura interrompida pelo usuário."))

        finally:
            arduino.close()

            self.stdout.write(self.style.SUCCESS("Conexão serial encerrada."))
