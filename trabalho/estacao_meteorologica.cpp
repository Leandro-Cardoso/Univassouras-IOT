#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

const int dht_pin = 2;
const int interval = 2000;

DHT dht(dht_pin, DHT22);
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // put your setup code here, to run once:

  lcd.init();
  lcd.backlight();

  dht.begin();

}

void loop() {
  // put your main code here, to run repeatedly:

  delay(interval);

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperature);
  lcd.print((char)223);
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("Umid: ");
  lcd.print(humidity);
  lcd.print(" %");

}
