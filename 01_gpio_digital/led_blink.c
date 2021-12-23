#include <stdio.h>
#include <wiringPi.h>
#define LED_PIN 4

int main (void){
    //wiringPisetup();
    wiringPiSetupGpio();
    pinMode (LED_PIN, OUTPUT);

    for (int i = 0; i < 5; i++){
        printf("LED ON\n");
        digitalWrite (LED_PIN, HIGH) ; delay(1000);
        
        printf("LED OFF\n");
        digitalWrite (LED_PIN, LOW) ; delay(1000);  
    }

    return 0;
}