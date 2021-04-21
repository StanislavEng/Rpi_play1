#include <Wire.h>

const byte RED = 13;
const byte BLU = 7;
const byte YEL = 4;
const byte col[] = {YEL,BLU,RED};
const byte LEDMask = 14;
const byte ONOFFMask = 1;

void setup() {
  // put your setup code here, to run once:
  Wire.begin(0x8);
  Serial.begin(9600);
  
  Wire.onReceive(receiveEvent);

  for (byte i = 0; i < sizeof(col)/sizeof(col[0]);i++){
    byte LED = col[i];
    pinMode(LED,OUTPUT);
    digitalWrite(LED,LOW);
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
}

void receiveEvent(int howMany){
  while(Wire.available()){
    byte I2C = Wire.read();
    byte LED = I2C & LEDMask;
    byte ONOFF = I2C & ONOFFMask;
    switch (LED)
    {
      case 2: 
        digitalWrite(RED,ONOFF); 
        break;
      case 4:
        digitalWrite(BLU,ONOFF);
        break;
      case 8:
        digitalWrite(YEL,ONOFF); 
        break;
      default:
        Serial.println("Nope");
    }

    //digitalWrite(LED,c);  
  }
}
