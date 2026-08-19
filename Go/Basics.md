###### Go tools
Checking for shadowed variables
```shell
go vet -vettool=$(which shadow)
```
###### Iota
```go
const (
    StatusNew = iota       // 0
    StatusRunning          // 1
    StatusStopped          // 2
)
```
###### Overwriting variables with `:=`
With the `:=` operator, variables can be overwritten in the same block, but only if another *new* variable is defined in the same line:
```go
var varA = "Hello, "
varA, varB := "World", "foobar"
```
###### Copying slices
Only at most as many elements can be copied as the capacity of the target slice:
```go
slA := []int{1, 2, 3, 4}
slB := []int{5, 6}
n := copy(slB, slA)
fmt.Println(n, slB) // 2 [1 2]
```
###### Importing packages
When we want to avoid a compiler error of unused package (here `oa`), for example, when debug unfinished code:
```go
import ( 
	"fmt" 
	"math" 
	_ "os" 
	"strings" 
)
```
When we want to import the members of the imported package to the current namespace, so we do not need to prefix them with the imported package name:
```go
import ( 
	. "fmt" 
	. "math"
)
```
###### Maps
Adding element to uninitialized map initializes it. Getting non-existing element from a map return a zero-value.
###### Advanced IO
Input reader:
```go
reader := bufio.NewReader(os.Stdin) 
b, err := reader.ReadBytes('\n') // Input into `b`: Hello World!\n 
if err != nil {
	log.Fatal(err)
} fmt.Println(string(b)) 
s, err := reader.ReadString('d')
if err != nil { 
	log.Fatal(err) 
}
```
In the above examples, `\n` and 'd' are deliminers which are *included* in the read data.
Scanner (for reading line by line)
```go
scanner := bufio.NewScanner(os.Stdin)
for scanner.Scan() {
    line := scanner.Text() // Input: Sheldon Cooper 100 98 Physics\n
    fmt.Println(line)     // Output: Sheldon Cooper 100 98 Physics
}
```
Or by words, runes, bytes:
```go
wordScanner := bufio.NewScanner(os.Stdin)
wordScanner.Split(bufio.ScanWords)
// or ScanRunes, ScanBytes
for wordScanner.Scan() { // Input: Among Us ඞ\n
    fmt.Println(wordScanner.Text())
}
```
Or with a custom scan function (use `scanner.Split(scanBools))`:
```go
func ScanBools(data []byte, atEOF bool) (advance int, token []byte, err error) {
    advance, token, err = bufio.ScanWords(data, atEOF)
    if err == nil && token != nil {
        _, err = strconv.ParseBool(string(token))
    }
    return advance, token, err
}
```