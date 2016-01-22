#include <wiringPi.h>

const ledPin = 18;
int main(){
   wiringPiSetupGpio();

   pinMode(ledPin, OUTPUT);

   
   digitalWrite(ledPin, HIGH);


return 0;
}
