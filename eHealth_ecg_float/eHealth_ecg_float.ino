#include <eHealth.h>

// The setup routine runs once when you press reset:
void setup() {
  Serial.begin(115200);  
}

// The loop routine runs over and over again forever:
void loop() {

  float ECG = eHealth.getECG();
  serialFloatPrint(ECG); 
  Serial.println(); 
//  int ECGval = ECG * 1000; 
//  Serial.print("ECG value :  ");
//  Serial.print(ECG); 
//  Serial.print(" V"); 
//  Serial.println(""); 
//    Serial.write(ECGval); 


  delay(1);	// wait for a millisecond
}

void serialFloatPrint(float f) {
  byte * b = (byte *) &f;
  Serial.print("f:");
  for(int i=0; i<4; i++) {
    
    byte b1 = (b[i] >> 4) & 0x0f;
    byte b2 = (b[i] & 0x0f);
    
    char c1 = (b1 < 10) ? ('0' + b1) : 'A' + b1 - 10;
    char c2 = (b2 < 10) ? ('0' + b2) : 'A' + b2 - 10;
    
    Serial.print(c1);
    Serial.print(c2);
  }
}
