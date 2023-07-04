from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available(self):
        ice = IceCreamStand('Glacial', 'Sorveteria', ['Morango', 'Chocolate'])
        result_expected = "No momento temos os seguintes sabores de sorvete disponíveis:\nMorango\nChocolate"
        result = ice.flavors_available()

        assert result_expected == result

    def test_find_flavor(self):
        ice = IceCreamStand('Glacial', 'Sorveteria', ['Morango', 'Chocolate', 'Baunilha'])
        result_expected = "Não temos no momento Cupuaçu!"
        result = ice.find_flavor('Cupuaçu')

        assert result_expected == result

    def test_add_flavor(self):
        ice = IceCreamStand('Glacial', 'Sorveteria', ['Morango', 'Chocolate', 'Cupuaçu'])
        result_expected = 'Pistache adicionado ao estoque!'
        result = ice.add_flavor('Pistache')

        assert result_expected == result
