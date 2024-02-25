package main

import (
	"fmt"
  "math"
)
func main() {
  var a,b,c float64
  var delta float64
  
  fmt.Println("Entre com 3 números:")
  fmt.Scan(&a,&b,&c)

  delta = (b*b - 4*a*c)

  if delta < 0 {
  fmt.Println("Sem raízes reais")
    
  } else if delta > 0 {
  var x1 = (-b + math.Sqrt(delta))/(2*a)
  var x2 = (-b - math.Sqrt(delta))/(2*a)
  fmt.Println("Raízes: ", x1, x2)
  fmt.Println("Tem raízes reais")
    
  } else {
  var x1 = (-b + math.Sqrt(delta))/(2*a)
  fmt.Println("Raíz: ", x1)}
}
