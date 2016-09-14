#include <Synapse.h>

unsigned int dataPoints = 6;
long baudRate = 115200;
Synapse dataLink(Serial);
int ledPin = 13;

void setup() {
    pinMode(ledPin, OUTPUT);
    digitalWrite(13, LOW);
    Serial.begin(baudRate);
}

void loop() {
    float setPointArray[dataPoints];
    float positionArray[dataPoints] = {10.0,11.1,12.2,13.3,14.4,15.5};
    while(!Serial.available());
    char command = Serial.read();
    switch(command) {
        case 's':
            dataLink.readSetPoints(&setPointArray[0]);
            if(setPointArray[0]==10.0 && setPointArray[1]==11.1 && setPointArray[2]==12.2 && setPointArray[3]==13.3 && setPointArray[4]==14.4 && setPointArray[5]==15.5) {
                digitalWrite(ledPin, HIGH);
            }
            else if(setPointArray[0]==10.0 && setPointArray[1]==0.0 && setPointArray[2]==0.0 && setPointArray[3]==0.0 && setPointArray[4]==0.0 && setPointArray[5]==0.0) {
                digitalWrite(ledPin, LOW);
            }
            break;
        case 'r':
            datalink.writeDataArray(&positionArray[0]);
            break;
    }
}
