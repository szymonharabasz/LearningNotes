Struktury danych wykorzystywane w komunikacji sieciowej realizowanej na gniazdach BSD (definicje w `netinet/in.h`):

```C
struct sockaddr { 
	unsigned short sa _family; // rodzina adresów (AF_xxx), my uzywamy AF_INET
	char sa_data [14]; // adres (interpretacja zalezy od rodziny)
};
```
Struktura ta reprezentuje adresy, które wykorzystywane sa w operacjach na gniazdach. Nie musza to być adresy IP, zależy to od stosowanej rodziny adresów (np. `AF_UNIX` - tzw. Unix sockets), my jednak skupimy się na adresach rodziny `AF_INET`, czyli adresach IP.
```C
struct sockaddr_in {
	short sin_family; // rodzina adresów (AF_INET)
	unsigned short sin_port; // numer portu
	struct in_addr sin_addr; // adres
	unsigned char sin_zero [8]; // nieuzywane (nalezy zerowaé!)
};
```
Wskaźniki tej struktury można przekazywać wszędzie tam, gdzie wymagane as wskaźniki na `struct sockaddr` (struktura ta ułatwia operowanie na zawartości pola `sa_data` struktury `sockaddr`).
```C
struct unsigned in_addr { 
	long s_addr; // adres IP w formacie sieci
};
```
Funkcje wykorzystywane w operacjach na gniazdach:

- `int socket (int namespace, int style, int protocol (sys/socket.h)` Tworzy gniazdo i zwraca jego deskryptor lub -1 w przypadku błędu. Parametr `namespace` określa rodzaj adresów (w naszym przypadku `AF_INET` lub `PF_INET` - stałe te mają tę samą wartość). Parametr `style` określa rodzaj gniazda. My będziemy używać gniazd rodzaju `SOCK_STREAM` (protokół TCP) i `SOCK_DGRAM` (protokół UDP). Parametr `protocol` zawsze będzie miał wartość 0 - jest to domyślny protokół dla danego rodzaju gniazda.
- `int bind(int socket, struct sockaddr *addr, socklen_t length) (sys/socket.h)` Przypisuje gniazdu socket adres addr o długości (rozmiarze struktury) length. Zwraca 0 jeśli operacja powiodła się lub -1 w przypadku błędu (np. zażądano przypisania portu, który jest juz wykorzystywany przez inny proces). Najczęściej wykorzystywana do łączenia gniazda nasłuchującego z konkretnym numerem portu i interfejsem sieciowym hosta.
- `int listen(int socket, unsigned int backlog) (sys/socket.h)` Umożliwia wykorzystanie podanego gniazda do nasłuchiwania w oczekiwaniu na nadchodzące połączenia (musi mu być wcześniej przypisany adres za pomoicą `bind`). Parametr `backlog` określa ile maksymalnie połączeń może być kolejkowanych (w przypadku, gdy połączenie w danym momencie nawiązuje więcej niż jeden klient). Funkcja zwraca 0 (sukces) lub -1 (błąd). Funkcja wykorzystywana tylko w przypadku protokolu TCP.
- `int accept(int socket, struct sockaddr *inaddr, socklen_t *len_ptr) (sys/socket.h)` Funkcja rozpoczyna oczekiwanie na połączenie. Jest blokująca, tzn. sterowanie opuszcza program do momentu nawiązania połączenia przez jakiś proces. W momencie nawiązania połączenia następuje powrót i funkcja zwraca nowy deskryptor gniazda, który następnie używany jest do wymiany danych z konkretnym klientem. Gniazdo takie należy później normalnie zamknąć przy użyciu `close`. Dodatkowo adres "rozmówcy" umieszczany jest w strukturze wskazywanej przez `inaddr`, a jego długość w zmiennej wskazywanej przez `len_ptr`. Funkcja używana tylko w przypadku protokołu TCP.
- `int recv(int socket, void *buffer, size_t nbytes, int flags) (sys/socket.h)` Odpowiednik funkcji `read` dla gniazd. Powoduje odczytanie co najwyżej `nbytes` bajtów z połączenia reprezentowanego przez `socket` i umieszczenie ich w obszarze pamięci wskazywanym przez `buffer`. Zwraca liczbę faktycznie odczytanych bajtów lub -1 w przypadku błędu. Parametr `flags` ma zwykle wartość 0, a umożliwia określenie pewnych szczególnych zachowań funkcji `recv`. Dla przykładu, podanie `MSG_PEEK` jako `flags` powoduje sprawdzenie, czy są jakieś dane do odczytania jednak nie zostaną one faktycznie odczytane.
- `int connect (int socket, struct sockaddr *adr, socklen_t addrlen) (sys/socket.h)` Nawiązuje połączenie przy użyciu podanego gniazda z gniazdem nasłuchującym, którego adres (host, protokół i port) określa `adr`. W parametrze `addrlen` podajemy wielkość struktury wskazywanej przez `addr`. Funkcja zwraca 0 jeśli udało się nawiązaé połączenie lub -1 w przypadku błędu.
- `int send(int socket, void *buffer, size_t nbytes, int flags) (sys/socket.h)` Odpowiednik funkcji `write`. Powoduje wysłanie `nbytes` bajtów z obszaru wskazywanego przez `buffer` poprzez gniazdo `socket`. Parametr `flags` ma zwykle wartość 0 i przydaje się jedynie w bardzo szczególnych sytuacjach (podobnie jak w przypadku `recv`). Funkcja zwraca liczbę faktycznie wysłanych bajtów.