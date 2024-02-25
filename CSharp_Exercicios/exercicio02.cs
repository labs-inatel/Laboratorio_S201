using System;

class Cachorro
{
  public string nome;
  public int idade;
 
  public void showNome(){
     Console.WriteLine("O nome do cachorro é: " + nome);
  }
  public void showIdade(){
     Console.WriteLine("A idade do cachorro é: " + idade);
  }
}

class CachorroGrande : Cachorro
{
  public string tamanho;
  
  public void showTamanho(){
     Console.WriteLine("O tamanho do cachorro grande é: " + tamanho);
  }

  public new void showIdade(){
     Console.WriteLine("A idade do cachorro grande é: " + idade);
  }
}

class CachorroPequeno : Cachorro
{
  public new void showIdade()
  {
     Console.WriteLine("A idade do cachorro pequeno é: " + idade);
  }
}

class Program
{
  static void Main(string[] args)
  {
     Cachorro c = new Cachorro();
     c.nome = "Bolinha";
     c.idade = 5;
     c.showNome();
     c.showIdade();

     CachorroGrande cg = new CachorroGrande();
     cg.nome = "Rex";
     cg.idade = 3;
     cg.tamanho = "Grande";
     cg.showNome();
     cg.showTamanho();
     cg.showIdade();

     CachorroPequeno cp = new CachorroPequeno();
     cp.nome = "Pipoca";
     cp.idade = 2;
     cp.showNome();
     cp.showIdade();
  }
}