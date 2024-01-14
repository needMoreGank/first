#define C4 262
//define creates a constant variable named C4 with value of 262 (C variable method)

int buzzer = 11;
int button = 5;

#define D4 294 //Re
#define E4 330 //Mi
#define F4 349 //Fa
#define G4 392 //Sol
#define A4 440 //La
#define B4 494 //Ti
#define C5  523 //Do

int tempo = 500;
int notes[] = {C4,D4,E4,F4,G4,A4,B4,C5};
byte nSize = sizeof(notes)/sizeof(notes[0]);

//these notes are integers=4 bytes each
//sizeof measures byte size
//sizeof(notes) = 8x4=32, sizeof(notes[0]) = 4
//32/4 = 8, list length
//C does not support len() for some reason

void setup() {
pinMode(buzzer, OUTPUT);
pinMode(button, INPUT);
}

void loop() {
if(digitalRead(button) == HIGH)
{
    for (int i=0; i < nSize ; i++) {
    tone(buzzer, notes[i], tempo);
    delay(500);
    }
    noTone(buzzer);
    delay(1000);
}
delay(1); //let Uno take some rest
}int buzzer = 11;
int button = 5;

#define C4 262 //Do
#define D4 294 //Re
#define E4 330 //Mi
#define F4 349 //Fa
#define G4 392 //Sol
#define A4 440 //La
#define B4 494 //Ti
#define C5  523 //Do

int tempo = 500;
int notes[] = {C4,D4,E4,F4,G4,A4,B4,C5};
byte nSize = sizeof(notes)/sizeof(notes[0]);

void setup() {
pinMode(buzzer, OUTPUT);
pinMode(button, INPUT);
}

void loop() {
if(digitalRead(button) == HIGH)
{
    for (int i=0; i < nSize ; i++) {
    tone(buzzer, notes[i], tempo);
    delay(500);
    }
    noTone(buzzer);
    delay(1000);
}
delay(1); //let Uno take some rest
}
