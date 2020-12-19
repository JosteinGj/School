// Eksempel kode for oppsett av timer-interrupt for en konstant samplingsfrekvens

#include <TimerOne.h>
/* Om du ikke har innstallert dette biblioteket
gå til Sketch -> Include library -> Manage Libraries
Søk opp TimerOne og innstaller*/

// Globale variaber
volatile int sample; // Holder siste sample
volatile float prevsample=0;
bool newSample; // Støtte varibel for å sjekke om ny sample er tatt
float lowpass=0;
float highpass=0;

float last_lowpass=0;
float last_highpass=0;

float sum_low=0;
float sum_high=0;

float mean_low=0;
float mean_high=0;

float alow=0.5;
float ahigh=0.5;

int k=20;
int count=0;

void setup() {
  // Oppsett av timer interrupt
  Timer1.initialize(500); // 500 mikrosekund mellom hver sample -> gir F_s = 2kHz
  // Argumentet i "attachInterrupt" bestemmer hvilken funskjon som er interrupt handler 
  Timer1.attachInterrupt(takeSample); 
  Serial.begin(115200);
  pinMode(0,INPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
}
void lowpassfilter(){
  lowpass=sample-prevsample + alow * last_lowpass;
  last_lowpass=lowpass;  
}

void highpassfilter(){
  highpass=sample-prevsample - ahigh* last_highpass;
  last_highpass=highpass;
}


void loop() {

   if(newSample){
    // Ny sample er tatt
    lowpassfilter();
    highpassfilter();
    sum_low+=abs(lowpass);
    sum_high+=abs(highpass);
    count++;
    
    if (count==k)
    {
      mean_low=sum_low/k;
      mean_high=sum_high/k;
      if (mean_low<k && mean_high<k)
      {digitalWrite(6,LOW);}
      else
      {digitalWrite(6,HIGH);}
      if (mean_low > mean_high)
        {digitalWrite(7,LOW);}
      else
        {digitalWrite(7,HIGH);}
      sum_low=0;
      sum_high=0;
      count=0;
      mean_low=0;
      mean_high=0;
    }
    prevsample=sample;
    newSample = false;
  }
}


// Interrupt-handler (denne kalles ved hvert interrupt)
void takeSample(void){
  sample = analogRead(0); // Sampler på A0
  newSample = true;
}
