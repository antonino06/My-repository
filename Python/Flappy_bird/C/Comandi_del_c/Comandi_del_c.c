#include <stdio.h> 
#include <stdbool.h> // include i caratteri buleani
#include <math.h> // include la matematica

int main() // inizio
{
    /* tipi di dati
    int eta = 14; // specificatore %d // variabile
    const int N_MESI = 12; // costante 
    int a = 4; // occupa fino a 4 byte di numeri
    short b = 2; // occupa fino a 2 byte di numeri
    long c = 4; // occupa fino a 4 byte di numeri
    long long d = 8; // occupa fino a 8 byte di numeri
    float e = 0.55; // fino a sette numeri dopo la virgola
    double f = 0.9999; // specificatore %f // fino a qundici numeri dopo la virgola
    long double g = 0.896894; // fino a trenta numeri dopo la virgola
    char carattere = 'A'; // specificatore %c // caratteri
    bool isonline = true; // caratteri buleani
    */
    /* conversione implicita
    int x = 30; float y = x; aggiunge gli zeri dopo la virgola
    int x = 30.000f; toglie gli zeri dopo la virgola
    */
    /* conversione esplicita
    double x = 30.85069; int y = (int)x; trasforma x in un intero 
    */
    /* operazioni algebriche
    int x = 30 + 5; // somma
    int x = 30 - 5; // sottrazione  
    int x = 30 * 5; // moltiplicazione   
    int x = 30 / 5; // divisione
    int x = 30 % 5; // resto della divisione
    */
    /* operatore di incremento
    ++x o x++; // aggiunge un valore ad x   
    int x = 11; int y = ++x; // mandando a schermo x o y avremo sempre 12 come risultato, questa regola vale sono se viene assegnate ad una variabile
    int x = 11; int y = x++; // mandato a schermo la x avremo 12 come risultato mandanto la y avremo 11 come risultato, questa regola vale sono se viene assegnate ad una variabile
    */
    /* operatore di decremento  
    --x o x--; // toglie un volere ad x
    int x = 11; int y = --x; // mandando a schermo x o y avremo sempre 10 come risultato, questa regola vale sono se viene assegnate ad una variabile
    int x = 11; int y = x--; // mandato a schermo la x avremo 10 come risultato mandanto la y avremo 11 come risultato, questa regola vale sono se viene assegnate ad una variabile
    */
    /* operatori di assegnazione cobinata
    int x = 11; x += 5; // manda a schermo x sommata
    int x = 11; x -= 5; // manda a schermo x sottratta
    int x = 11; x *= 5; // manda a schermo x moltiplicata
    int x = 11; x /= 5; // manda a schermo x divisa
    int x = 11; x %= 5; // manda a schermo il resto della divione 
    */
    /* math.h
    x = pow(); // fa la potenza
    x = sqrt(); // fa la radice quadrata
    */
    /* operatori di comparazione 
    bool condizione = 5 < 10; // è vero cioè 1
    bool condizione = 5 > 10; // è falso cioè 0
    bool condizione = 10 == 10; // è 10 uguale a 10
    bool condizione = 11 != 10; // è 11diverso da 10
    */
    int x = 11;
    int y = 20;
    bool condizione = x < y;
    printf("%d", condizione);  // esecuzione
    return 0;
}
