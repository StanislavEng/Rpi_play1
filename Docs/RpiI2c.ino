#include <Wire.h>

const int LED = 13;

void setup() {
  // put your setup code here, to run once:
  Wire.begin(0x8);
  Serial.begin(9600);
  
  Wire.onReceive(receiveEvent);


  pinMode(LED,OUTPUT);
  digitalWrite(LED,LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
}
byte d;
void receiveEvent(int howMany){
  while(Wire.available()==0){
    byte d;
    byte c = Wire.read();
    switch (c)
    {
      case 1: 
      {
        while(Wire.available()==0){
          Serial.println("A");           
          d = Wire.read();
        }
        digitalWrite(LED,d); 
        break;
      }
      case 2:
      {
        while(Wire.available()==0){
          Serial.println("B"); 
          d = Wire.read();
        }
        digitalWrite(LED,d);
        break;
      }
      case 3:
      {
        while(Wire.available()==0){
          Serial.println("C"); 
          d = Wire.read();
        }
        digitalWrite(LED,d); 
        break;
      }
      default:
        Serial.println("Nope");
    }
    Serial.println("First");
    Serial.println(c);
    Serial.println("Second");
    Serial.println(d);
    //digitalWrite(LED,c);  
  }
}
