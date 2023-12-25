import random


class ResponseModel:
    def __init__(self, status: str, response: dict = None):
        self.status = status
        self.json = response


class RegisterFruts:
    @staticmethod
    def random_body_fruts():
        genus_r = ['Ianhedgea', 'Ianthopappus', 'Iberidella', 'Iberis', 'Ibervillea', 'Ibicella', 'Icacina', 'Icaria',
                   'Ichnanthus', 'Ichnocarpus', 'Ichthyothere', 'Ichtyoselmis', 'Icianthus', 'Icosinia', 'Icuria',
                   'Idahoa', 'Idertia', 'Idesia', 'Idiopappus', 'Idiospermum', 'Idiothamnus', 'Ifloga', 'Ignurbia',
                   'Iguanura', 'Ihlenfeldtia', 'Ikonnikovia', 'Ildefonsia', 'Ilex', 'Iliamna', 'Iljinia', 'Illecebrum',
                   'Illicium', 'Illigera', 'Iltisia', 'Ilysanthes', 'Imeria', 'Imerinaea', 'Impatiens', 'Imperata',
                   'Incarum', 'Incarvillea', 'India', 'Indigastrum', 'Indigofera', 'Indocalamus', 'Indofevillea',
                   'Indopiptadenia', 'Indopoa', 'Indorouchera', 'Indosasa', 'Indoschulzia', 'Indosinia',
                   'Indotristicha', 'Inezia', 'Inga', 'Inhambanella', 'Inocarpus', 'Inti', 'Intsia', 'Inula',
                   'Inulanthera', 'Inuloides', 'Inulopsis', 'Inversodicraea', 'Io', 'Iochroma', 'Iodanthus', 'Iodes',
                   'Iogeton', 'Ionactis', 'Ionidium', 'Ionopsis', 'Iostephane', 'Iotasperma', 'Iphigenia', 'Iphiona',
                   'Iphionopsis', 'Ipomoea', 'Ipomopsis', 'Ipsea', 'Iranecio', 'Irenella', 'Iresine', 'Iriartea',
                   'Iriartella', 'Iridodictyum', 'Iridosma', 'Iris', 'Irlbachia', 'Irvingbaileya', 'Irvingia',
                   'Iryanthera', 'Isabelia', 'Isachne', 'Isandrina', 'Isanitella', 'Isatis', 'Ischaemum', 'Ischnea',
                   'Ischnogyne', 'Ischnolepis', 'Ischnosiphon', 'Ischyrolepis', 'Iseia', 'Iseilema', 'Isertia',
                   'Isgarum', 'Isidorea', 'Isidrogalvia', 'Iskandera', 'Islaya', 'Ismelia', 'Ismene', 'Isnardia',
                   'Isoberlinia', 'Isocarpha', 'Isochilus', 'Isocoma', 'Isodon', 'Isoetopsis', 'Isoglossa',
                   'Isolatocereus', 'Isolepis', 'Isoleucas', 'Isoloba', 'Isoloma', 'Isolona', 'Isomacrolobium',
                   'Isometrum', 'Isonandra', 'Isonema', 'Isophysis', 'Isopogon', 'Isopyrum', 'Isostigma', 'Isotheca',
                   'Isotoma', 'Isotria', 'Isotropis', 'Itasina', 'Itaya', 'Itea', 'Iteadaphne', 'Itoa', 'Ituterion',
                   'Itzaea', 'Iva', 'Ivesia', 'Ivodea', 'Ixanthus', 'Ixerba', 'Ixeridium', 'Ixeris', 'Ixia', 'Ixidium',
                   'Ixiochlamys', 'Ixiolaena', 'Ixiolirion', 'Ixoca', 'Ixocactus', 'Ixodia', 'Ixodonerium',
                   'Ixonanthes', 'Ixophorus', 'Ixora', 'Ixorhea']
        name_r = ['Абиу', 'Абрикос', 'Авокадо', 'Айва', 'Аки', 'Алиберция', 'Алыча', 'Амбарелла',
                  'Американский абрикос', 'Американский орех', 'Ананас', 'Аннона горная', 'Аннона колючая',
                  'Аннона сетчатая', 'Аннона черимола', 'Аннона чешуйчатая', 'Антильский крыжовник', 'Апельсин',
                  'Арабика', 'Араза', 'Арахис', 'Арбуз обыкновенный', 'Астрокариум колючий', 'Атимойя',
                  'Африканский колючий огурец', 'Африканский тамаринд', 'Бакау', 'Баклажан', 'Балия', 'Бананы',
                  'Баобаб', 'Барбадин (Большая гранадилла)', 'Барбадосская вишня', 'Бархатное яблоко', 'Баэль',
                  'Белая сапота', 'Бергамот', 'Билимби', 'Бирсонима', 'Блигия вкусная', 'Большой змеиный фрукт',
                  'Боярышник', 'Бразильский орех', 'Бычье сердце', 'Вампи', 'Вангерия', 'Ваниль', 'Виноград', 'Вишня',
                  'Воаванга', 'Водяное(восковое) яблоко', 'Гандария', 'Генипа', 'Гибискус съедобный', 'Гнетум гнемон',
                  'Голубиная слива', 'Голубой квандонг', 'Горлянка', 'Горький огурец', 'Гранадилла (Маракуйа)',
                  'Гранадилла большая (Барбадин)', 'Гранадилла сладкая', 'Гранат', 'Грейпфрут', 'Грумичама', 'Груша',
                  'Гуайява земляничная', 'Гуайява коста-риканская', 'Гуайява красная', 'Гуайява обыкновенная',
                  'Гуарана', 'Давидсония', 'Дамские пальчики', 'Деревянное яблоко', 'Десертный квандонг', 'Джекфрут',
                  'Древесная калебаса', 'Дуку', 'Дуриан', 'Дуриан цибетиновый', 'Дынная груша', 'Дынное дерево',
                  'Дыня обыкновенная', 'Евгения одноцветковая', 'Жаботикаба', 'Звездчатое яблоко', 'Земляничная груша',
                  'Земляничный томат', 'Земляной орех', 'Зизифус мавританский', 'Золотая слива', 'Золотистый апельсин',
                  'Индийские бобы', 'Индийский инжир', 'Индийский миндаль', 'Индийское розовое яблоко', 'Инжир',
                  'Кабачки', 'Каинито', 'Какао', 'Кактус инжировый', 'Каламондин', 'Калебаса', 'Калина',
                  'Канариум яйцевидный', 'Капский крыжовник', 'Карамбола', 'Кас', 'Квини', 'Квинслендский орех',
                  'Кепель', 'Кетамбилла', 'Кивано', 'Киви', 'Китайская калебаса', 'Клементин', 'Кокколоба ягодоносная',
                  'Кокос', 'Корилла', 'Кофейные деревья', 'Кранжи', 'Кумкват овальный', 'Купуасу', 'Курбарил',
                  'Кустовой горошек', 'Лайм настоящий', 'Лангсат', 'Лансиум домашний', 'Леуцена светлоголовчатая',
                  'Либерика', 'Ликания', 'Лимон грубокожистый', 'Лимон обыкновенный', 'Лимон Мейера', 'Лимонная осина',
                  'Личи', 'Лобия', 'Ложный мангустан', 'Лох узколистный', 'Лукума', 'Луло', 'Люффа остроребристая',
                  'Маболо', 'Мадагаскарская слива', 'Макадамия цельнолистная', 'Малабарская тыква',
                  'Малабарский апельсин', 'Малайское яблоко', 'Малуко', 'Мальпигия гранатолистная',
                  'Маммея американская', 'Мамончилло (Лайм испанский)', 'Манго благоухающее', 'Манго великолепное',
                  'Манго индийское', 'Манго резко пахнущее', 'Мангостан', 'Мангустан', 'Мандарин', 'Манилкара',
                  'Маракуйя', 'Мармеладный плод', 'Марула', 'Мауриция извилистая', 'Маш', 'Мексиканская земляная вишня',
                  'Мексиканский огурец', 'Мелинжо', 'Моква', 'Момбин желтый', 'Момбин красный', 'Момордика', 'Моринда',
                  'Мунду', 'Мускатный орех', 'Мушмула японская', 'Наранхилла', 'Ням-ням', 'Нектарин (подвид персика)',
                  'Обезьяний хлеб', 'Огурец', 'Огуречное дерево', 'Орех кешью', 'Пальма катеху', 'Пальма кокосовая',
                  'Пальма масличная африканская', 'Пальма персиковая', 'Пальчиковый лайм', 'Папайя', 'Папайя горная',
                  'Папеда', 'Паприка', 'Пара-гуайява', 'Паркия красивая', 'Пассифлора съедобная', 'Пекуи', 'Пепино',
                  'Перец', 'Перец кайенский', 'Перец стручковый', 'Персик', 'Перуанская вишня', 'Питайя', 'Питомба',
                  'Пиши', 'Помело', 'Померанец', 'Помидор', 'Помпельмус', 'Понцирус (несъедобный плод)',
                  'Приморский виноград', 'Путерия', 'Пуласан', 'Ракум-салакка', 'Рамбай', 'Рамбутан', 'Робуста',
                  'Розовое яблоко', 'Роллиния слизистая', 'Салакка', 'Салакка скученная', 'Саламандровое дерево',
                  'Сантол', 'Саподилла', 'Сатсума', 'Сахарное яблоко', 'Сахарный горошек', 'Свечное дерево', 'Свити',
                  'Сизигиум аквеум', 'Сизигиум малаккский', 'Сизигиум ямбоза', 'Сингапурский миндаль', 'Слива',
                  'Слива какаду', 'Слоновье яблоко', 'Сметанное яблоко', 'Сонсоя', 'Соя', 'Спаржевая фасоль',
                  'Страстоцвет', 'Суринамская вишня', 'Съедобный таитянский орех', 'Таитянское яблоко', 'Такако',
                  'Тамарилло', 'Тамаринд', 'Танжерин', 'Терминалия катаппа', 'Томат настоящий', 'Томатное дерево',
                  'Тукума', 'Тупа', 'Тыква бутылочная', 'Тыква восковая', 'Тыква мускатная', 'Тыква обыкновенная',
                  'Тыква фиголистная', 'Тыквенное дерево', 'Фейхоа', 'Ферония лимонная', 'Ферония слоновая',
                  'Физалис земляничный', 'Филиппинское розовое яблоко', 'Филлантус кислый', 'Финик', 'Флакурция',
                  'Хлебное дерево', 'Хлебные бобы', 'Хурма\xa0восточная (японская)', 'Цейлонский крыжовник',
                  'Циклантера', 'Цуккини', 'Чайот', 'Чампедак', 'Черешня', 'Черимойя', 'Черная гуайява',
                  'Черная сапота', 'Черная хурма', 'Черный тамаринд', 'Чили', 'Чилибуха колючая', 'Чупа',
                  'Шоколадное дерево', 'Яблоко', 'Яблоко-кажу', 'Яботикаба', 'Ямайская вишня', 'Ятоба']
        family_r = ['Brassicaceae', 'Compositae', 'Brassicaceae', 'Brassicaceae', 'Cucurbitaceae', 'Martyniaceae',
                    'Icacinaceae', 'Melastomataceae', 'Poaceae', 'Apocynaceae', 'Compositae', 'Papaveraceae',
                    'Brassicaceae', 'Malvaceae', 'Leguminosae', 'Brassicaceae', 'Ochnaceae', 'Salicaceae', 'Compositae',
                    'Calycanthaceae', 'Compositae', 'Compositae', 'Compositae', 'Arecaceae', 'Aizoaceae',
                    'Plumbaginaceae', 'Plantaginaceae', 'Aquifoliaceae', 'Malvaceae', 'Amaranthaceae',
                    'Caryophyllaceae', 'Schisandraceae', 'Hernandiaceae', 'Compositae', 'Linderniaceae', 'Compositae',
                    'Orchidaceae', 'Balsaminaceae', 'Poaceae', 'Araceae', 'Bignoniaceae', 'Orchidaceae', 'Leguminosae',
                    'Leguminosae', 'Poaceae', 'Cucurbitaceae', 'Leguminosae', 'Poaceae', 'Linaceae', 'Poaceae',
                    'Apiaceae', 'Ochnaceae', 'Podostemaceae', 'Compositae', 'Leguminosae', 'Sapotaceae', 'Leguminosae',
                    'Orchidaceae', 'Leguminosae', 'Compositae', 'Compositae', 'Compositae', 'Compositae',
                    'Podostemaceae', 'Compositae', 'Solanaceae', 'Brassicaceae', 'Icacinaceae', 'Compositae',
                    'Compositae', 'Violaceae', 'Orchidaceae', 'Compositae', 'Compositae', 'Colchicaceae', 'Compositae',
                    'Compositae', 'Convolvulaceae', 'Polemoniaceae', 'Orchidaceae', 'Compositae', 'Amaranthaceae',
                    'Amaranthaceae', 'Arecaceae', 'Arecaceae', 'Iridaceae', 'Simaroubaceae', 'Iridaceae',
                    'Gentianaceae', 'Stemonuraceae', 'Irvingiaceae', 'Myristicaceae', 'Orchidaceae', 'Poaceae',
                    'Leguminosae', 'Orchidaceae', 'Brassicaceae', 'Poaceae', 'Compositae', 'Orchidaceae', 'Apocynaceae',
                    'Marantaceae', 'Restionaceae', 'Convolvulaceae', 'Poaceae', 'Rubiaceae', 'Amaranthaceae',
                    'Rubiaceae', 'Melanthiaceae', 'Brassicaceae', 'Cactaceae', 'Compositae', 'Amaryllidaceae',
                    'Onagraceae', 'Leguminosae', 'Compositae', 'Orchidaceae', 'Compositae', 'Lamiaceae', 'Compositae',
                    'Acanthaceae', 'Cactaceae', 'Cyperaceae', 'Lamiaceae', 'Lentibulariaceae', 'Gesneriaceae',
                    'Annonaceae', 'Leguminosae', 'Gesneriaceae', 'Sapotaceae', 'Apocynaceae', 'Iridaceae', 'Proteaceae',
                    'Ranunculaceae', 'Compositae', 'Acanthaceae', 'Campanulaceae', 'Orchidaceae', 'Leguminosae',
                    'Apiaceae', 'Arecaceae', 'Iteaceae', 'Lauraceae', 'Salicaceae', 'Salvadoraceae', 'Convolvulaceae',
                    'Compositae', 'Rosaceae', 'Rutaceae', 'Gentianaceae', 'Strasburgeriaceae', 'Compositae',
                    'Compositae', 'Iridaceae', 'Santalaceae', 'Compositae', 'Compositae', 'Ixioliriaceae',
                    'Caryophyllaceae', 'Loranthaceae', 'Compositae', 'Apocynaceae', 'Ixonanthaceae', 'Poaceae',
                    'Rubiaceae', 'Boraginaceae']
        body = dict(genus=random.choice(genus_r), name=random.choice(name_r), family=random.choice(family_r),
                    order="Яблоня", nutritions={
                "carbohydrates": random.randrange(1, 10, 1),
                "protein": random.randrange(1, 10, 1),
                "fat": random.randrange(1, 10, 1),
                "calories": random.randrange(1, 100, 1),
                "sugar": random.randrange(1, 10, 1)
            })
        return body
