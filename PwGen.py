import random

cMax = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cMin = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
cEsp = "!@#$%¨&*()"

estrutura = cMax + cMin + num + cEsp
digito = 15 

senha1 = "".join(random.sample(estrutura,digito))
senha2 = "".join(random.sample(estrutura,digito))
senha3 = "".join(random.sample(estrutura,digito))

print("======= Escolha a senha que desejar =======")

print("Senha: " + senha1)
print("Senha: " + senha2)
print("Senha: " + senha3)