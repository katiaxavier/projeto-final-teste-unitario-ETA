from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            ### print("\nNo momento temos os seguintes sabores de sorvete disponíveis:") --- Coloquei na linha 22
            ###for flavor in self.flavors:

            sorvet = '\n'.join(self.flavors)
            return f"No momento temos os seguintes sabores de sorvete disponíveis:\n{sorvet}"   ### print(f"\t-{flavor}")
        else:
            return "Estamos sem estoque atualmente!"    ###print("Estamos sem estoque atualmente!")

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento o sabor {flavor}!"      ### Adicionando o return, trocando self.flavors para flavor
            else:
                return f"Não temos no momento o sabor {flavor}!"          ### Estava self.flavors, Trocando para flavor e adicionando o return
        else:
            return "Estamos sem estoque atualmente!"            # Adicionando o return

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                return "Sabor já disponivel!"                   ###print("\nSabor já disponivel!")
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"       ###print(f"{flavor} adicionado ao estoque!")
        else:
            return "Estamos sem estoque atualmente!"            ###print("Estamos sem estoque atualmente!")
