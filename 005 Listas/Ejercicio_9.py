#Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
segundo_cliente = compras[1]
indice_fideos = segundo_cliente.index("fideos")
segundo_cliente[indice_fideos:indice_fideos+1] = ["tallarines"]
primer_cliente = compras[0]
primer_cliente.remove("pan")
print(compras)