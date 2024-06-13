from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_luiz = Restaurante("Restaurante do luiz", "Gourmet")
bebida_suco = Bebida("Suco de melacia", 20, "500ml")
bebida_suco.aplicar_desconto()
prato_pao = Prato("Árabe", 2, "Pão árabe")
prato_pao.aplicar_desconto()
restaurante_luiz.adicionar_no_cardapio(bebida_suco)
restaurante_luiz.adicionar_no_cardapio(prato_pao)
sobremesa_gelada = Sobremesa("Sobremesa Gelada", 200, "Limão")
restaurante_luiz.adicionar_no_cardapio(sobremesa_gelada)


def main():
    restaurante_luiz.exibir_no_cardapio

if __name__ == "__main__":
    main()