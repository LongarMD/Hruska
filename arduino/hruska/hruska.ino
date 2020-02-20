int incomingByte = 0; // for incoming serial data
#define pump1 8
#define pump2 9
#define pump3 10
#define pump4 11

bool pumps[4] = { false, false, false, false};

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  // send data only when you receive data:
  while(Serial.available() > 0){
      // read the incoming byte:
   // incomingByte = Serial.read();

    // say what you got:
   
    String currentLine  = Serial.readStringUntil('\n');

 //1 0 1 0
   for (int i = 0; i<4; i++){
      pumps[i] = currentLine[2*i] == '1';
       Serial.println("pumpa "+(String)i+" je: "+(String)pumps[i]);
      digitalWrite(8+i,pumps[i]);
    }
   
   
}
}
