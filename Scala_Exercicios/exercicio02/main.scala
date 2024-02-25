class Veiculo(nome:String, marca:String, fabricante:String,gasolina:Double){
  def printInfo() : Unit = println(s"$nome - $marca")
  
  def printInfo(nome:String) : Unit = println(s"$fabricante - $gasolina")
}

class Carro(nome:String, marca:String, fabricante:String,gasolina:Double, private val velocidade: Double) 
  extends Veiculo(nome,marca,fabricante,gasolina) {
  def teste() : Unit = println(nome)
}

class Aviao(nome:String, marca:String, fabricante:String,gasolina:Double)  extends Veiculo(nome,marca,fabricante,gasolina) {
  private var velocidade: Double = 0

  def setVelocidade(velocidade: Double) = {
    this.velocidade = velocidade
  }
  
  override def printInfo() : Unit = {
    super.printInfo()
    println("Vel: "+velocidade)
  }
}

object Main {
  def main(args: Array[String]): Unit = {
  
    val veic = new Veiculo("Uno", "Fiat", "Fabricante",14)
    veic.printInfo()
    val carro = new Carro("Uno 2", "Fiat 2", "Fabricante 2",14,90)
    carro.printInfo("a")
    val aviao = new Aviao("Uno 3", "Fiat 3", "Fabricante 3",14)
    aviao.setVelocidade(45)
    aviao.printInfo() 
  }
}
