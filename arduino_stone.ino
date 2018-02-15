#include<Servo.h>
Servo x,y;
int a;
void setup() {
  // put your setup code here, to run once:
x.attach(2);
y.attach(11);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0)
  {
     a=Serial.read();
    if(a=='1'){
stone();
Serial.println("Do you even know what is stone paper and scissors");
//delay(1000);
    }
    else if(a=='2')
    {
paper();
Serial.println("bloody looser");
//delay(1000);
    }
    else if(a=='3')
    {
scissor();
Serial.println("You don't have enough abilities to beat me at this");
//delay(1000);
    }
  }



}


void stone()
{
  x.write(110);
  y.write(67);
  delay(15);
  }
  void paper()
  {
  x.write(0);
  y.write(175);
  delay(15);
  }
void scissor()
{
  x.write(110);
  y.write(175);
  delay(15);
  }

