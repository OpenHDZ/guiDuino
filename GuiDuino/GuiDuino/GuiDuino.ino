int entreeAna = 0; // définition de l'entrée analogique numero 0 de l'arduino
int voltage; // la variable ou nous mettrons la valeur à transmetre
             // a l'interface graphique

void setup()
{
  Serial.begin(9600); // Initialisation de la liaison série
  pinMode(entreeAna, INPUT); // Mettre la pin 0A en mode entrée 
}

void loop()
{
  voltage = (analogRead(entreeAna))/10.24; // lire la valeur analogique
                                           
  Serial.println(voltage); // l'envoi de la donnée 
  
  delay(1000);
  Serial.flush(); // vidé le buffer USB
}

