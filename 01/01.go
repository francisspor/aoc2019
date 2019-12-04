package main

	
import (
//    "io"
    "bufio"
    "fmt"
    "log"
    "os"
    "strconv"
)


// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
	lines, err := readLines("./input.txt")
    if err != nil {
        log.Fatalf("readLines: %s", err)
    }

    sum := 0

    for i, line := range lines {
        val, err := strconv.Atoi(line)
        if err == nil {
            val = (val / 3) - 2
            for val > 0 {
                sum = sum + val
                val = (val / 3.0) - 2
            }
        }

        fmt.Println(i, line)
    }

    fmt.Println(sum)
}