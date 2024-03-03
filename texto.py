email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver %(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponivéis!

Preço promocional %(preco).2f
"""

clientes = ["Maria", "Cirilo", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "tinta",
            "texto": "Pinta muito bem",
            "link": "https://tintas.com",
            "quantidade": 20,
            "preco": 45.5,
        }
    )