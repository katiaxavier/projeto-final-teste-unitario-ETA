class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        ### Adicionando docstring
        """
        Inicialize os atributos do restaurante.
        """

        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        ### Ajustes docstring
        """
        Imprima uma descrição simples da instância do restaurante.

        :return: Um texto com o nome do restaurante, o que serve e o numero de consumidores no momento.
        """

        ###print(f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}.")    ### Corrigindo erros de grafia e trocando a primeira variavel
        ###print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")          ### Corrigindo erros de grafia

        return f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}." \
               f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        ### Ajustes docstring
        """
        Imprima uma mensagem indicando que o restaurante está aberto para negócios.

        :return: "restaurant_name agora está aberto!" ou "restaurant_name já está aberto!"
        """

        if not self.open:
            self.open = True                                        ### Estava False, Mudando para True (BUG)
            self.number_served = 0                                  ### Estava -2, Alterando para 0 (BUG)
            return f"{self.restaurant_name} agora está aberto!"     ###print(f"{self.restaurant_name} agora está aberto!")
        else:
            return f"{self.restaurant_name} já está aberto!"        ###print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        ### Ajustes docstring
        """
        Imprima uma mensagem indicando que o restaurante está fechado para negócios.

        :return: "restaurant_name agora está fechado!" ou "restaurant_name já está fechado!"
        """

        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"    ###print(f"{self.restaurant_name} agora está fechado!")
        else:
            return f"{self.restaurant_name} já está fechado!"       ###print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        ### Ajustes docstring
        """
        Defina o número total de pessoas atendidas por este restaurante até o momento.

        :param total_customers: Valor em numero inteiro
        :return: Number served ou "restaunt_name está fechado!"
        """

        if self.open:
            self.number_served = total_customers
            return self.number_served                           ### adicionando return da variavel self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"      ###print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        ### Ajustes docstring
        """
        Aumenta número total de clientes atendidos por este restaurante.

        :param more_customers: Valor em numero inteiro
        :return: number_served ou "restaurant_name está fechado!"
        """

        if self.open:
            self.number_served += more_customers                ###Adicionando o +, estava apenas com o = (BUG)
            return self.number_served                           ### adicionando return da variavel self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"      ###print(f"{self.restaurant_name} está fechado!")
