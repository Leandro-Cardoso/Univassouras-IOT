# TRABALHO - Estação Meteorologica

[**<- VOLTAR**](https://github.com/Leandro-Cardoso/Univassouras-IOT)

Trabalho realizado como P2 da disciplina de **Internet das Coisas** do 5º período de **Engenharia de Software** da Univassouras, ministrada pelo professor Dr. Altemar Sales.

## Descrição:

O projeto tem o objetivo de através de uma placa **Arduino** e sensores, obter dados de temperatura e humidade do ar no decorrer do tempo.

Também está previsto armazenar esses dados em um banco de dados **SQLite**.

E um FrontEnd simples, desenvolvido em **Python** e **Django**, para a visualização dos dados e graficos relacionados.

## Requisitos:

### Funcionais:

01. RF - Ler os dados dos sensores utilizados.

01. RF - Registrar dados de data e hora da medição periodicamente.

02. RF - Registrar dados de temperatuda periodicamente.

03. RF - Registrar dados de humidade do ar periodicamente.

04. RF - Consultar dados de temperatuda por histórico de datas.

05. RF - Consultar dados de humidade por histórico de datas.

### Não Funcionais:

01. RNF - Utilizar Arduino.

02. RNF - Utilizar no mínimo dois sensores.

03. RNF - Os sensores devem ter relação um com o outro.

04. RNF - Utilizar um banco de dados para armazenamento dos dados.

05. RNF - Uma Interface intuitiva, funcional e eficaz para interação com o usuário.

## Diagramas:

### Classe e Relacionamento:

<img src="diagrama-classe-relacionamento.png" alt="Diagrama de Classe e Relacionamento">

### Casos de Usos:

<img src="diagrama-casos-de-usos.png" alt="Diagrama de Casos de Usos">

## Arduino:

### Componentes:

* Arduino Uno
* LiquidCrystal I2C
* DHT 22

<img src="arduino.png" alt="Arduino">

### Código:

<pre><code>
#include < LiquidCrystal_I2C.h>
#include < DHT.h>

#define LCD_ADDR 0x27
#define LCD_COLLUNS 16
#define LCD_ROWS 2

#define DHTPIN 7
#define DHTTYPE DHT22

LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLLUNS, LCD_ROWS);

DHT dht (DHTPIN, DHTTYPE);

float humidity;
float temperature;

void setup() {
  // put your setup code here, to run once:

  lcd.begin(16, 2);
  lcd.init();
  lcd.backlight();

  dht.begin();

  lcd.setCursor(3, 0);
  lcd.print("Humidity");

  lcd.setCursor(2, 1);
  lcd.print("Temperature");

}

void loop() {
  // put your main code here, to run repeatedly:

  delay(2000);

  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  lcd.setCursor(0, 0);
  lcd.print("Humi: ");
  lcd.print(humidity);
  lcd.print(" %");

  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.print(temperature);
  lcd.print(" C");

}
</code></pre>

## Instruções do Trabalho:

1. Os itens básicos exigidos na P1, mais um sensor. Ou seja, ao todo o projeto deve ter no mínimo dois sensores. Os sensores devem ter relação um com o outro.

2. Uma Interface (Front End en Java, Pytho, PHP...) intuitiva, funcional e eficaz para interação com o usuário, permitindo ler os dados dos sensores e outros elementos visuais gráficos e textuais do projeto.

3. Uma lista de requisitos funcionais e não funcionais, Diagrama de casos de uso, Diagrama de Classes e o Modelo Relacional de Dados.

4. Armazenamento eficiente e correto dos dados recebidos para fins históricos em um Banco de dados relacional (PostgreSQL, MySQL...).

5. Consultas por histórico de datas, pelo menos.

6. Código bem estruturado, com comentários, organização, e documentação correta dos arquivos.

## Entrega do Trabalho:

* O projeto deve conter fotos ou um breve vídeo do arduino, sensores, resistores...

* As instruções estão em anexo.

* Não esqueça de enviar o código do arduino.

* Os arquivos podem ser enviados em um único arquivo doc, pdf ou zip.

* Favor seguir o padrão  a seguir para o nome do arquivo, antes de enviar pelo AVA:

    * Nome_Completo_do_Aluno_matricula.zip
    <br>(Exemplo: Altemar_Sales_de_Oliveira_125567.zip)

[**<- VOLTAR**](https://github.com/Leandro-Cardoso/Univassouras-IOT)
