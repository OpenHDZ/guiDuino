#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600); // Initialisation de la liaison série
  dht.begin(); 
}

void loop()
{
  delay(2000);
  
  int h = dht.readHumidity();
                                           
  Serial.println(h); // l'envoi de la donnée 
  
  Serial.flush(); // vidé le buffer USB
}

