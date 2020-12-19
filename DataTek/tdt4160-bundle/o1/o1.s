.thumb
.syntax unified

.include "gpio_constants.s"     // Register-adresser og konstanter for GPIO

.text
	.global Start
	
Start:
    // BUTTON ER AKTIV 
    // Skriv din kode her...
    
    LDR R0, =GPIO_BASE+(LED_PORT*PORT_SIZE)      // Set R0 til LED port
    LDR R1, =GPIO_BASE+(BUTTON_PORT*PORT_SIZE)  // set R1 til BUTTON porten
    ADD R2, R1, GPIO_PORT_DIN           // set R3 til DIN_REG Porten til button
 
    ADD R4, R0, GPIO_PORT_DOUTTGL // Set R4 til DOUTTGL_REG PORTEN til LED 
    LDR R5, =1 << 2
    Loop:
        AND R5, R3,0b100000000  // and med pin nr 9 på DIN_REG_BUTTON

        CMP R5, 0               // Sammenlikn verdi til PIN 9 men 0 med hvis de er ulike er knappen trykket inn
        BEQ Change               // Dersom de er ulike hopp til false
        B Loop                  // hopp opp til loop. 
    Change:

        LDR R4, [R5]       
        B Loop
    
    

    /*
        psudo kode for hva som skal skje
        While TRUE:
        READ DIN til Button
        if DIN_ BUTTON == 1
           DOUT_ LED== Not(DOUT_LED)
        
     */

NOP // Behold denne på bunnen av fila

