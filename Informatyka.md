Ilość bitów informacji niesiona przez zdarzenie o prawdopodobieństwie p wynosi:  
$$
l(p)=\log_2\frac{1}{p}
$$ 
Entropia źródła informacji: 
$$
H=\sum_{i=1}^Np_il(p_i),
$$
Warunek Fano: żaden pojedynczy kod nie może być początkiem innego pojedynczego kodu

Algorytm Shannona-Fano:
- Podzielić zbiór komunikatów na dwie grupy o możliwe równych sumach prawdopodobieństw
- Do aktualnych kodów elementów z pierwszej grupy dodać pierwszy znak kodowania,  do elementów z drugiej grupy - drugi
- Kontynuować dzielenie grup aż do uzyskania grup jednoelementowych

Algorytm Huffmana:
- Zbudować drzewo binarne elementów przez łączenie ze sobą węzłów o najniższych prawdopodobieństwach, prawdopodobieństwo danego węzła rodzica ma być sumą prawdopodobieństw węzłów potomnych
- Przechodząc przez drzewo od korzenia do liści, dodawać pierwszy znak do kodu danego elementu, gdy przechodzi się w lewo, aby do niego dojść, a drugi znak, gdy przechodzi się w prawo
- W ten sposób elementy bardziej prawdopodobne mają krótkie kody, bo są dołączone późno (czyli blisko korzenia), a elementy o niskim prawdopodobieństwie są połączone wcześnie, czyli daleko od korzenia

Konwersja liczby całkowitej do systemu innego niż dziesiętny:
- Podzielić liczbę przez podstawę systemu
- Reszta jest pierwszą cyfrą nowej reprezentacji
- Wynik jest dzielony dalej, żeby uzyskać kolejne cyfry, aż wynik osiągnie 0

Konwersja liczny ułamkowej do systemu innego niż dziesiętny:
- Pomnożyć liczbę przez podstawę systemu
- Część całkowita jest pierwszą cyfrą nowe reprezentacji
- Część ułamkowa jest mnożona dalej, żeby uzyskać kolejne cyfry, aż wynik osiągnie 0

Sposoby kodowania stałopozycyjnego
- Znak-moduł prosty: skomplikowana arytmetyka, nie nadaje się do praktycznego zastosowania
- Kodowanie odwrotnościowe:
- Pierwszy bit to znak (0 to liczba dodatnia, 1 to liczba ujemna)
- Na kolejnych pozycjach dla liczby ujemnej dana cyfra kodu jest uzupełnieniem danej cyfry liczby do największej cyfry systemu, w systemie binarnym oznacza to odwrócenie bitu
- Dodawanie w ogólności: dodać kody, a w przypadku przepełnienia powiększyć wynik o najmniejszą możliwą liczbę dodatnią

Kodowanie uzupełnieniowe:
- Uzupełnić każdą cyfrę do największej cyfry systemu i dodać 1 na najmniej znaczącej pozycji
- Dodawanie w ogólności: dodać kody

Kodowanie nadmiarowe:
- Dodać do każdej liczby stałą, tak żeby kody były tylko "dodatnie", najczęściej podstawy systemu do potęgi ilości cyfr całkowitych
- Dodawanie w ogólności: dodać kody i odjąć 1 od cyfry znaku

Pierwiastek kwadratowy z x:
$$
\begin{split}
a_0 =&1,\\
a_{n+1}=&\frac{1}{2}\left(a_n+\frac{x}{a_n}\right)
\end{split}
$$
###### IEEE-754
Mantysa kodowana jako znak-moduł prosty, znormalizowana do całości, bez optymalizacji, cecha kodowana nadmiarowo:
- Single: 32 bity, 24 na mantysę
- Double: 64 bity, 53 na mantysę
Negacja liczby zmiennoprzecinkowej: `XOR` z `-0.0`

Algorytm Euklidesa bazuje na tym, że jeżeli a = m b + r, to NWD(a, b) = NWD(b, r)

Definicja poprawności algorytmu:
- Algorytm A ma własność określoności obliczeń, względem warunku a, jeśli dla każdych danych spełniających warunek a działanie algorytmu A nie zostanie zerwane
- Algorytm A ma własność stopu względem warunku a, jeśli dla każdych danych spełniających warunek a działanie algorytmu A nie ciągnie się w nieskończoność
- Algorytm A jest częściowo poprawny względem warunku początkowego a oraz warunku końcowego b, gdy dla każdych danych spełniających warunek początkowy a, jeżeli działanie algorytmu A dochodzi do końca, wyniki spełniają warunek końcowy b
- Algorytm A jest całkowicie poprawny (semantycznie poprawny) względem warunku początkowego a oraz warunku końcowego b, jeśli ma wartość określoności obliczeń względem warunku a, ma własność stopu względem warunku a oraz jest częściowo poprawny względem warunku a i warunku b.

Zamiana na odwrotną notację polską:
- Lewy nawias: odłożyć na stos
- Operand: wysłać na wyjście
- Operator: zdjąć ze stosu i wysłać na wyjście wszystkie operatory o priorytecie wyższym lub równym priorytetowi operatora wczytanego, a sam wczytany operator odłożyć na stos
- Prawy nawias: zdjąć ze stosu i wysłać na wyjście wszystkie operatory aż do pierwszego lewego nawiasu, a sam lewy nawias zdjąć ze stosu i odrzucić
- Po zakończeniu wejścia całą pozostałą zawartość stosu wysłać na wyjście

Ewaluacja odwrotnej notacji polskiej:
- Operand: położyć na stos
- Operator: zdjąć ze stosu ilość operandów odpowiadających krotności operatora, wykonać działanie, a wynik działania odłożyć na stos

###### Zapis w odwrotnej notacji polskiej elementarnych algorytmów strukturalnych:
Krótka instrukcja warunkowa:  
```
ONP(warunek)|n|SW|ONP(instrukcje)|…  
                                  n
```
Długa instrukcja warunkowa:  
```
ONP(warunek)|m|SW|ONP(instrukcje if)|n|SB|ONP(instrukcje else)|…  
                                          m                    n
```
Pętla dopóki:  
```
ONP(warunek)|n|SW|ONP(instrukcje)|m|SB|…  
m                                      n
```
Pętla powtórz:  
```
ONP(instrukcje)|ONP(warunek)|m|SW|…  
m
```
Liczby zmiennoprzecinkowe:
- Pojedyncza precyzja (single): 1 bit - znak | 8 bitów - wykładnik | 23 bity - mantysa
- Podwójna precyzja (double): 1 bit - znak | 11 bitów wykładnik | 52 bity - mantysa
- Mantysa zawiera cyfry po przecinku
- Liczba jest znormalizowana tak, że przed przecinkiem znajduje się jedynka, nie jest ona zapisywana w pamięci, tylko wstawiana domyślnie, dzięki czemu oszczędza się 1 bit
- Od wartości całkowitej zapisanej w bitach wykładnika odejmuje się 127 (single) albo 1023 (double)
- Wartości specjalne:

| **Wykładnik** | **Mantysa**  | **Znaczenie**           |
| ------------- | ------------ | ----------------------- |
| Same zera     | Same zera    | Zero                    |
| Same zera     | Inna wartość | Liczba zdenormalizowana |
| Same jedynki  | Same zera    | Nieskończoność          |
| Same jedynki  | Inna wartość | NaN                     |
Dla liczby zdenormalizowanej nie jest dodawana domyślna jedynka przed przecinkiem, pozwala to na zapisanie jeszcze mniejszych liczb
#### Rejestry procesora x86_64
###### Ogólnego przeznaczenia
- 64 bitowe:
  `rax - rdx, rsi, rdi, rbp, rsp, r8 - r15`
- 32 bitowe:
  `eax - edx, esi, edi, ebp, esp, r8d - r15d`
- 16 bitowe
  `ax - dx, si, di, bp, sp, r8w - r15w`
- Niższe 8 bitów rejestru 16-bitowego
  `al - dl`
- Wyższe 8 bitów rejestru 16-bitowego
  `ah - dh`
Kopiowanie wartości do rejestru 8-bitowego lub 16-bitowego **nie zeruje** górnych bitów rejestru 64-bitowego.
Kopiowanie wartości do rejestru 32-bitowego **zeruje** górne bity rejestru 64-bitowego
###### Rejestr flag `rflags`
- `CF` - przeniesienie - poprzednia instrukcja spowodowała przeniesienie
- `PF` - parzystość - ostatni bajt zawierał parzystą liczbę jedynek
- `AF` - korekcja - operacja BCD
- `ZF` - zero - wynikiem poprzedniej instrukcji było zero
- `SF` - znak - w wyniku poprzedniej instrukcji najbardziej znaczący bit został ustawioy na 1
- `DF` - kierunek - kierunek operacji łańcuchowych, zwiększanie lub zmniejszanie
- `OF` - przepełnienie - poprzednia instrukcja spowodowała przepełnienie
Typy danych w `section .data`:
- db - bajt
- dw - słowo (16 bitów)
- dd - podwójne słowo
- dq - poczwórne słowo
Bieżąca pozycja w pamięci : `$`
Użycie funkcji zewnętrznej
```asm
extern printf
; ... po umieszczeniu argumentów w odpowiednich rejestrach:
call printf
```
Prolog i epilog funkcji
```asm
push rpb
mov rpb,rsp
; ...
mov rsp,rpb
pop rpb
```
Wyjście z programu:
```assembler
mov rax, 60; 60 = wyjście
mov rdi, 0 ; wartość wyjściowa - 0 = sukces
syscall
```
albo
```asm
ret
```
###### Instrukcje
Umieszczenie w rejestrze wartości pod danym adresem
```asm
mov rsi, [radius]
```
Porównanie (ustawia odpowiednie flagi):
```
cmp rax, rbx
```
Skok bezwarunkowy:
```asm
jmp etykieta
```
Skoki warunkowe
- `je` - skok jeśli równe
- `jne` - skok jeśli nie równe
- `jg, jge, jl, jle` - skok jeśli większe, większe lun równe itd, ze znakiem
- `ja, jae, jb, jbe` - skok jeśli wyższe, wyższe lub równe itd, bez znaku