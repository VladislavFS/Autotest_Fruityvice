import random


def random_fruit_class(group: str):
    """
    :param group: Принимает значения family, genus или order
    :return: Функция возвращает 1 случайный объект(str) из заданной группы
    """
    family = ['Clusiaceae', 'Betulaceae', 'Actinidiaceae', 'Moraceae', 'Vitaceae', 'Ericaceae', 'Bromeliaceae',
              'Cucurbitaceae', 'Ebenaceae', 'Sapindaceae', 'Solanaceae', 'Anacardiaceae', 'Myrtaceae', 'Lythraceae',
              'Passifloraceae', 'Malvaceae', 'Musaceae', 'Rutaceae', 'Caricaceae', 'Cactaceae', 'Grossulariaceae',
              'Lauraceae', 'Rosaceae']
    genus = ['Vitis', 'Rubus', 'Ananas', 'Selenicereus', 'Sellowiana', 'Citrus', 'Malus', 'Mangifera', 'Litchi',
             'Ribes', 'Artocarpus', 'Passiflora', 'Morus', 'Prunus', 'Carica', 'Apteryx', 'Garcinia', 'Musa',
             'Diospyros', 'Punica', 'Actinidia', 'Pyrus', 'Psidium', 'Fragaria', 'Ficus', 'Solanum', 'Durio', 'Corylus',
             'Cactaceae', 'Vaccinium', 'Persea', 'Cucumis', 'Citrullus']
    order = ['Zingiberales', 'Myrtales', 'Poales', 'Laurales', 'Cucurbitaceae', 'Malvales', 'Rosales', 'Vitales',
             'Ericales', 'Caricacea', 'Saxifragales', 'Solanales', 'Cucurbitales', 'Struthioniformes', 'Myrtoideae',
             'Caryophyllales', 'Malpighiales', 'Sapindales', 'Fagales']
    if group == 'family':
        return random.choice(family)
    elif group == 'genus':
        return random.choice(genus)
    elif group == 'order':
        return random.choice(order)
