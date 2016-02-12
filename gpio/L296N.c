#include <stdio.h>
#include <wiringPi.h> 

#define DIRL 17
#define PWML 27  
#define DIRR 23 
#define PWMR 24  
#define EN 18 

int main (void)
{
  if (wiringPiSetupGpio() == -1) 
    return 1;

  pinMode(DIRL, OUTPUT); 
  pinMode(PWML, OUTPUT);
  pinMode(DIRR, OUTPUT); 
  pinMode(PWMR, OUTPUT);
  pinMode(EN, OUTPUT); 

  digitalWrite(EN, 1);
  digitalWrite(DIRL, 1); 
  digitalWrite(DIRR, 1);
  digitalWrite(PWML, 1);
  digitalWrite(PWMR, 1); 
  delay(3000);
  digitalWrite(EN, 1);
  digitalWrite(DIRL, 0); 
  digitalWrite(DIRR, 0);
  digitalWrite(PWML, 1);
  digitalWrite(PWMR, 1); 
  delay(3000);
  digitalWrite(EN, 1);
  digitalWrite(DIRL, 0); 
  digitalWrite(DIRR, 1);
  digitalWrite(PWML, 1);
  digitalWrite(PWMR, 1); 
  delay(3000);
  digitalWrite(EN, 1);
  digitalWrite(DIRL, 1); 
  digitalWrite(DIRR, 0);
  digitalWrite(PWML, 1);
  digitalWrite(PWMR, 1); 
  delay(3000);
  digitalWrite(EN, 0);
}
