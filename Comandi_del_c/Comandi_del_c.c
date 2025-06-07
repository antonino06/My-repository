#include <stdio.h> 
#include <stdbool.h> // include i caratteri buleani

int main() // inizio
{
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
    printf("Hello World!");  // esecuzione
    return 0;
}
