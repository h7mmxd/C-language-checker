#include <stdio.h>
#include <stdlib.h>

// Tehtava 1
void tulosta() {
    printf("Hei maailma!\n");
}

// Tehtava 2
int lue() {
    int numero;
    printf("Anna kokonaisluku: ");
    scanf("%d", &numero);
    return numero;
}

// Tehtava 3
void luvunTulostus(int luku) {
    printf("Annoit luvun: %d\n", luku);
}

// Tehtava 4
float kolmella() {
    float numero;
    printf("Anna desimaaliluku: ");
    scanf("%f", &numero);
    return numero * 3;
}

// Tehtava 5
void vertaile(int a, int b) {
    if (a > b) {
        printf("Suuruusjarjestys: %d %d\n", a, b);
    } else if (b > a) {
        printf("Suuruusjarjestys: %d %d\n", b, a);
    } else {
        printf("Luvut ovat samat: %d ja %d\n", a, b);
    }
}

// Tehtava 6
void nelioLasku(int sivunPituus) {
    printf("Nelion keha: %d\n", 4 * sivunPituus);
}

void ympyraLasku(int ympranSade) {
    printf("Ympyran keha: %.2f\n", 2 * 3.14 * ympranSade);
}

// Tehtava 7
void screen(char nimi[]) {
    printf("Merkkijono: %s\n", nimi);
}

int main() {
    // Tehtava 1
    tulosta();

    // Tehtava 2 ja 3
    int luku = lue();
    luvunTulostus(luku);

    // Tehtava 4
    float number = kolmella();
    printf("Kolmella kerrottuna: %.2f\n", number);

    // Tehtava 5
    int a, b;
    printf("Anna kaksi kokonaislukua: ");
    scanf("%d %d", &a, &b);
    vertaile(a, b);

    // Tehtava 6 (menu)
    int userchoice;
    do {
        printf("\nValikko:\n");
        printf("1. Nelion kehan pituus\n");
        printf("2. Ympyran kehan pituus\n");
        printf("9. Lopetus\n");
        printf("Valinta: ");
        scanf("%d", &userchoice);

        if (userchoice == 1) {
            int sivunPituus;
            printf("Anna sivun pituus: ");
            scanf("%d", &sivunPituus);
            nelioLasku(sivunPituus);
        } else if (userchoice == 2) {
            int ympranSade;
            printf("Anna ympyran sade: ");
            scanf("%d", &ympranSade);
            ympyraLasku(ympranSade);
        }

    } while (userchoice != 9);

    // Tehtava 7
    char nimi[] = "Hello";
    screen(nimi);

    // Tehtava 8
    char intStr[20];
    char doubleStr[20];

    printf("Anna kokonaisluku (merkkijonona): ");
    scanf("%s", intStr);

    printf("Anna desimaaliluku (merkkijonona): ");
    scanf("%s", doubleStr);

    int kokonaisluku = atoi(intStr);
    double desimaaliluku = atof(doubleStr);

    double summa = kokonaisluku + desimaaliluku;
    printf("Summa on: %.2f\n", summa);

    return 0;
}
