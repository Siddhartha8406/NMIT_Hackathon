/*
SDA - 10
SCK - 13
MOSI - 11
MISO - 12
GND - GND
RST - 9
3.3V - 3.3V
*/

#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

#define SS_PIN 10
#define RST_PIN 9

int servoPin = A4;
Servo Servo1;

MFRC522 rfid(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;

String tag;
String old_id;
void setup(){
  Serial.begin(115200);

  Servo1.attach(servoPin);

  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522
}

void loop(){
  delay(1000);
  if ( ! rfid.PICC_IsNewCardPresent())
    return;
  if ( ! rfid.PICC_ReadCardSerial())
    return;

  for (byte i = 0; i < 4; i++) {
    tag += rfid.uid.uidByte[i];
  }

  if (old_id != tag){
    Serial.println(tag);
    validate(tag);
  }
  tag = "";
}

void validate(String tag){
  String cor_id = "24923324875";

  if(tag == cor_id){
    Serial.println("Successfully Unlocked");
    Servo1.write(90);
    delay(5000);
    Servo1.write(0);
    Serial.println("Locked");
  }
  else{
    Serial.println("Wrong Key");
    delay(2000);
    Serial.println("Try again");
  }
}
