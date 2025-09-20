#include <LiquidCrystal_I2C.h>
#include <DHT.h>

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
