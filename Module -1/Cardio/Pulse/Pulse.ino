
// Definition of variables
unsigned long time;
long int pulse;
int count;
int pouls;


void setup() {
  
  // Assigning initial values to the different variables
  count=0;
  pulse=0;
  pouls=0;
  Serial.begin(9600);

  // Diplay message at the start of the program
  Serial.println("Please wait for a moment");

  time = millis();

  //awaiting time for the results to be more accurate
  while((millis()-time)<5000){
    analogRead(0);
  }

  time = millis();

  //we display on the serial monitor for 5 seconds
  while((millis()-time)< 10000){
    if ((millis()-time)%100 == 0)
    
      //calculate average pulse rate part 1
      pulse=pulse+(((1000.0*60.0)/(analogRead(0)))-100);
      count=count+1;
      
      //assignment to the pulse variable the mean pulse(pouls)
      pouls = pulse / count;
      
      //serial port output for processing
      Serial.print(millis()-time);
      Serial.print('->');
      Serial.println(pouls);
   
  }
 
 
}


void loop() {


}
