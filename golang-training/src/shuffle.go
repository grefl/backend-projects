package main

import (
  "fmt"
  "math/rand"
  "time"
)




func ShuffleInt(list []int) {
  random := rand.New(rand.NewSource(time.Now().UnixNano()))
  for i := 1; i < len(list); i +=1 {
    j := random.Intn(i)

    temp := list[i]
    list[i] = list[j]
    list[j] = temp
  }
}

func ShuffleString(list []string) {
  random := rand.New(rand.NewSource(time.Now().UnixNano()))
  for i := 1; i < len(list); i +=1 {
    j := random.Intn(i)

    temp := list[i]
    list[i] = list[j]
    list[j] = temp
  }
}

func main() {
  array_int := []int{1,2,3,4,5,6}
  array_string := []string{"Go", "Rust", "PHP"}
  ShuffleInt(array_int)
  ShuffleString(array_string)
  fmt.Println(array_int)
  fmt.Println(array_string)
}
