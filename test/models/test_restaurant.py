from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        restaurante = Restaurant("Glacial", "Sorvete")
        expected = "Esse restaurante se chama Glacial e serve Sorvete." \
               f"Esse restaurante está servindo 0 consumidores desde que está aberto."

        result = restaurante.describe_restaurant()

        assert expected == result

    def test_open_restaurant(self):
        restaurante = Restaurant("Habaneiro", "Comida mexicana")
        expected = "Habaneiro agora está aberto!"

        result = restaurante.open_restaurant()

        assert expected == result

    def test_open_restaurant_opened(self):
        restaurante = Restaurant("Rei do churrasco", "Churrasco")
        expected = "Rei Do Churrasco já está aberto!"
        restaurante.open_restaurant()

        result = restaurante.open_restaurant()

        assert expected == result

    def test_close_restaurant(self):
        restaurante = Restaurant("Coco Bambu", "Comida nordestina")
        expected = "Coco Bambu agora está fechado!"
        restaurante.open_restaurant()

        result = restaurante.close_restaurant()

        assert expected == result

    def test_close_restaurant_closed(self):
        restaurante = Restaurant("Waku Sese", "Comida amazonense")
        expected = "Waku Sese já está fechado!"

        result = restaurante.close_restaurant()

        assert expected == result

    def test_set_number_served(self):
        restaurante = Restaurant("Allkasen", "Comida arabe")
        expected = 6
        restaurante.open_restaurant()

        result = restaurante.set_number_served(6)

        assert expected == result

    def test_set_number_served_closed(self):
        restaurante = Restaurant("Mc Donalds", "Hamburguer")
        expected = "Mc Donalds está fechado!"

        result = restaurante.set_number_served(4)

        assert expected == result

    def test_increment_number_served(self):
        restaurante = Restaurant("BK", "Hamburguer")
        expected = 13
        restaurante.open_restaurant()
        restaurante.set_number_served(7)

        result = restaurante.increment_number_served(6)

        assert expected == result

    def test_increment_number_served_closed(self):
        restaurante = Restaurant("China in box", "Sushi")
        expected = "China In Box está fechado!"

        result = restaurante.increment_number_served(5)

        assert expected == result
