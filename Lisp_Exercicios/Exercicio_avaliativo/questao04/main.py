# Criar Classe para simular uma Televisão
class Televisao:

    def __init__(self, modelo):
        self.__modelo = modelo
        self.__canal = 0
        self.__volume = 0

    def aumentar_volume(self, quantidade):
        self.__volume += quantidade

    def diminuir_volume(self, quantidade):
        self.__volume -= quantidade

    def trocar_canal(self, novo_canal):
        self.__canal = novo_canal

    def imprimir_info(self):
        print(f"Modelo: {self.__modelo} \nVolume: {self.__volume} \nCanal: {self.__canal}")

# Criar Classe SmartTV que herda da Classe Televisão e que simula uma SmartTV
class SmartTV(Televisao):
    def __init__(self, modelo, internet=False):
        super().__init__(modelo)
        self.__internet = internet

    def conectar_internet(self):
        self.__internet = True
        print("O dispositivo foi conectado a Rede!")

    def imprimir_net(self):
        print(f"Conexão com Internet: {self.__internet}")


# Imprimir informações da Televisão (ajustar  volume e trocar de canal)
tv = Televisao("Modelo 1")
tv.aumentar_volume(70)
tv.diminuir_volume(27)
tv.trocar_canal("Canal #1")
tv.imprimir_info()

# Imprimir informações da SmartTV (ajustar  volume, trocar de canal, verificar conexão com Internet)
smartTv = SmartTV("Smart Modelo 1")
smartTv.aumentar_volume(70)
smartTv.diminuir_volume(27)
smartTv.trocar_canal("Canal #1")
smartTv.imprimir_net()
smartTv.conectar_internet()
smartTv.imprimir_net()
