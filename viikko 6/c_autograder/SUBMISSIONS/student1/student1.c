// Viikkotehtävä 7 - Hammad Atif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Tehtävä 1
void tehtava1() {
 char name[50];
 printf("Tehtävä 1: Syötä nimesi: ");
 scanf("%49s", name);
 FILE *f = fopen("name.txt", "w");
 fprintf(f, "%s", name);
 fclose(f);
 printf("Nimi tallennettu tiedostoon name.txt\n\n");
}
// Tehtävä 2
void tehtava2() {
 char ch;
 FILE *source = fopen("source.txt", "r");
 FILE *target = fopen("target.txt", "w");
 while ((ch = fgetc(source)) != EOF) {
 if (ch == ',') ch = ';';
 fputc(ch, target);
 }
 fclose(source);
 fclose(target);
 printf("Pilkut korvattu puolipisteillä target.txt-tiedostossa\n\n");
}
// Tehtävä 3
void tehtava3() {
 int lines = 0, words = 0;
 char c;
 FILE *f = fopen("source.txt", "r");
 while ((c = fgetc(f)) != EOF) {
 if (c == ' ') words++;
 if (c == '\n') {
 lines++;
 words++;
 }
 }
 fclose(f);
 printf("Rivejä: %d\nSanoja: %d\n\n", lines, words);
}
// Tehtävä 4,5
struct Student {
 int ID;
 char name[50];
 int age;
};
void tehtava4_5() {
 struct Student students[5];
 int save;
 for (int i = 0; i < 5; i++) {
 printf("Syötä opiskelija %d ID: ", i+1);
 scanf("%d", &students[i].ID);
 printf("Syötä opiskelija %d nimi: ", i+1);
 scanf("%49s", students[i].name);
 printf("Syötä opiskelija %d ikä: ", i+1);
 scanf("%d", &students[i].age);
 }
 printf("\nOpiskelijat:\n");
 for (int i = 0; i < 5; i++)
 printf("ID: %d, Nimi: %s, Ikä: %d\n", students[i].ID, students[i].name, students[i].age);
 printf("\nHaluatko tallentaa tiedot (Kyllä=1 / Ei=2)? ");
 scanf("%d", &save);
 if (save == 1) {
 FILE *f = fopen("c:/temp/students_data.txt", "w");
 for (int i = 0; i < 5; i++)
 fprintf(f, "%d,%s,%d\n", students[i].ID, students[i].name, students[i].age);
 fclose(f);
 printf("Tiedot tallennettu c:/temp/students_data.txt\n\n");
 }
}
// Tehtävä 6
void tehtava6() {
 int id, fileID, age, found = 0;
 char name[50];
 FILE *f;
 printf("Tehtävä 6: Syötä etsittävä opiskelijan ID: ");
 scanf("%d", &id);
 f = fopen("c:/temp/students_data.txt", "r");
 if (f == NULL) {
 printf("Tiedostoa ei löydy!\n");
 return;
 }
 while (fscanf(f, "%d,%49[^,],%d", &fileID, name, &age) == 3) {
 if (fileID == id) {
 printf("ID: %d, Nimi: %s, Ikä: %d\n", fileID, name, age);
 found = 1;
 break;
 }
 }
 if (!found)
 printf("Antamaasi id:tä ei löydy\n");
 fclose(f);
}
int main() {
 tehtava1();
 tehtava2();
 tehtava3();
 tehtava4_5();
 tehtava6();
 return 0;
}