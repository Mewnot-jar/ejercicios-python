carrito = [
    {"tipo": "Burger Pizza", "cantidad": 2, "precio": 12000}, 
    {"tipo": "Americana", "cantidad": 1, "precio": 10000}, 
    {"tipo": "Pepperoni", "cantidad": 3, "precio": 9000}
]
total_a_pagar = 0

for pizza in carrito:
    sub_total = pizza['precio'] * pizza['cantidad']
    total_a_pagar += sub_total

if total_a_pagar > 40000:
    total_a_pagar -= (total_a_pagar * 0.10)
print(total_a_pagar) 