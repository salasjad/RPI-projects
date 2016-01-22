#include <wiringPi.h>

const ledPin = 18;
int main(){
   wiringPiSetupGpio();

   pinMode(ledPin, OUTPUT);

   while(1){
      
      digitalWrite(ledPin, HIGH);
      delay(1000);
      digitalWrite(ledPin, LOW);
      delay(1000);
   }

return 0;
}
