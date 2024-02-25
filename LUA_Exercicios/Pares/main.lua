local pares = 0
local numeros = {}

for i = 0, 100, 1 do
  numeros[i] = math.random(0,100)
end

for i in pairs(numeros) do
  if numeros[i] % 2 == 0 then
    pares = pares + 1
  end
end

print("numeros pares: "..pares)