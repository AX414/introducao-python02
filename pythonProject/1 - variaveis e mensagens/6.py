# Como determinar quantas casas após a virgula eu devo imprimir?
a = 3.1456
# Neste caso será duas casas,
# a formatação por si só acaba por arredondar o valor para cima
print("{:.2f}".format(a))