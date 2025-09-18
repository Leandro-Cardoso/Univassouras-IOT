const int led_pin = 13;
const int buzzer_pin = 8;
const int button_pin = 2;

void start_button_action() {

  digitalWrite(led_pin, HIGH);
  digitalWrite(buzzer_pin, HIGH);

}

void stop_button_action() {

  digitalWrite(led_pin, LOW);
  digitalWrite(buzzer_pin, LOW);

}

void setup() {
  // put your setup code here, to run once:

  pinMode(led_pin, OUTPUT);
  pinMode(buzzer_pin, OUTPUT);
  pinMode(button_pin, INPUT_PULLUP);

  stop_button_action();

}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (digitalRead(button_pin) == LOW) {
    
    start_button_action();

  }
  else {

    stop_button_action();

  }

}
