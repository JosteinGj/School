.thumb
.syntax unified

.include "gpio_constants.s"     // Register-adresser og konstanter for GPIO
.include "sys-tick_constants.s" // Register-adresser og konstanter for SysTick

.text
	.global Start
	
Start:

    
    /*
        Skal bli en Klokke som teller med 10-dels oppløsnings. 
        bruk sysTick,
        freq/10 == 0.1 sec
        Interupt=sysTick_Handler
        set opp interrupt slik at 10-dels sekund oppdateres hvert tick
        sekund skal oppdateres hver 10tick
        minutt skal oppdateres hver 60 sec
        
        Ha noe gående i bakgrunnen 
     */
sysTick_Handler:
    

NOP // Behold denne på bunnen av fila

