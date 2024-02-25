object Main {
  def main(args: Array[String]): Unit = {
    
    var n1: Int = scala.io.StdIn.readInt();
    var n2: Int = scala.io.StdIn.readInt();

    var arr = new Array[Int](20);

    for(i <- 0 until arr.length){
      if(i%2 == 0)
        arr(i) = i*n1;
      else
        arr(i) = i*n2;
    }

    for(i <- 0 until arr.length){
      println("arr("+i+"): "+arr(i))
    }
  }
}