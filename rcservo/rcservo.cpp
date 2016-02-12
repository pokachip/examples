#include <stdlib.h>
#include <wiringPi.h>
#include "softServo.h"

#define RCSERVO1  23


int main(void)
{
  if (wiringPiSetupGpio() == -1)
    return 1 ;

  softServoSetup(RCSERVO2,-1,-1,-1,-1,-1,-1,-1);
  
  softServoWrite(RCSERVO1, -250);
  delay(2000);
  softServoWrite(RCSERVO1,  500);
  delay(2000);
  softServoWrite(RCSERVO1, 1250);
  delay(2000);
}
