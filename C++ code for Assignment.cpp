const uint8_t l = 10;
uint8_t pins[l] = {
27,//1
25,//2
33,//3
21,//4
26,//5
23,//6
22,//7
12,//8
19,//9
13 //10
};

void setup(){
    for (int i=0; i<10; i++){
        pinMode(pins[i], OUTPUT);
    }
}
void loop() {
     for (int i = 0; i < 5; i++) {
    digitalWrite(pins[i], HIGH); 
  }
  delay(1000);
  
  // Example: Turn off all LEDs
  for (int i = 0; i < 10; i++) {
    digitalWrite(pins[i], LOW);  
  }
  delay(1000);
}