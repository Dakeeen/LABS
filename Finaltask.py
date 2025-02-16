
class Blockchain:
    """ Базовый класс Блокчейна. """
    def __init__(self, name: str, tps: int): # tps - пропускная способность (trans per sec)
        self.name = name
        self.tps = tps

    def send_message(self, from_: str, to_: str, text: str): # отпправляет набранный текст from_ to_
        ...

    def convert(self, token: str, token_dest: str): # конвертирует один токен в другой
        ...

    def __str__(self):
        return f"Блокчейн {self.name}. Tps {self.tps}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.tps!r})"


class Solana(Blockchain):
    """ Блокчейн Solana рабоатет с NFT и стнадртными токенами. """
    def __init__(self, name: str, tps: int, nft: bool): #NFT - поддержка блокчейном NFT
        super().__init__(name, tps)
        self.nft = nft

    def convert(self, token: str, nft: str):  # конвертирует один токен в NFT, так как Солана может рабоать с нфт, а не только с токенами
        ...

    def __str__(self):
        return f"Книга {self.name}. Автор {self.nft}"




if __name__ == "__main__":
    # Write your solution here
    pass
