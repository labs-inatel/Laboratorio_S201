squareAndAdd :: [Int] -> [Int]

squareAndAdd xs = reverse (map (\x -> (x + 2)^2) xs)
-- Aplica a função que a cada elemento da lista, eleva o resultado ao quadrado, inverte a lista e retorna o resultado

main :: IO ()
main = do
  
  let numbers = [1..30]
  -- Criando lista de números de 1 a 30 e atribui à numbers
  
  let modifiedList = squareAndAdd numbers -- recebendo resultado da função e atribui à modifiedList
  
  putStrLn $ "Primeiro elemento da lista modificada: " ++ show (head modifiedList)
  -- Imprime o primeiro elemento da lista convertido para String