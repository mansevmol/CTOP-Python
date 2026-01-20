# Ejercicio 1
productos = ["manzana", "pan", "leche", "huevo", "arroz"]
print("Lista completa:", ", ".join(productos))
print("Primer producto:", productos[0])
print("Último producto:", productos[-1])
productos.append("queso")
print("Lista actualizada:", ", ".join(productos))

# Ejercicio 2
productos.sort()
print("Lista ordenada:", ", ".join(productos))
productos.remove("pan")
print("Lista después de eliminar 'pan':", ", ".join(productos))

# Ejercicio 3
stock = {
  "arroz": 15,
  "huevo": 30,
  "leche": 8,
  "manzana": 20,
  "queso": 5
}

def total_productos(stock):
    return sum(stock.values())

def productos_con_stock_mayor(stock, cantidad):
    return [producto for producto, cantidad_stock in stock.items() if cantidad_stock > cantidad]

print("Total de productos disponibles:", total_productos(stock))
print("Productos con stock mayor a 10:", ", ".join(productos_con_stock_mayor(stock, 10)))

# Ejercicio 4
productos_t = tuple(productos)
print("Tupla de productos:", ", ".join(productos_t))

# Ejercicio 5
almacen = {
  "arroz": {"nombre": "arroz", "precio": 1.5, "stock": 15},
  "huevo": {"nombre": "huevo", "precio": 0.2, "stock": 30},
  "leche": {"nombre": "leche", "precio": 0.8, "stock": 8},
  "manzana": {"nombre": "manzana", "precio": 0.5, "stock": 20},
  "queso": {"nombre": "queso", "precio": 3.0, "stock": 5}
}

print("Precio del queso:", almacen["queso"]["precio"])
print("Productos con stock < 10:", ", ".join([p["nombre"] for p in almacen.values() if p["stock"] < 10]))

valor_total = sum(p["precio"] * p["stock"] for p in almacen.values())
print("Valor total del stock:", valor_total)
