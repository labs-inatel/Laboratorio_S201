function multiplica(num)
  for i = 1, 10, 1 do
    print(num.." x "..i.." = "..num * i)
  end
end

print("Digite um número:")
local num = io.read()
multiplica(tonumber(num))
