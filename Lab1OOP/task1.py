# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Gun:
    def __init__(self, ammo_amount: int, mag_capacity: int):
        '''
        Создание магазина для оружия
        param: ammo_amount - кол-во патронов
        param: mag_capacity - вместимость магазина
        Пример:
        >>> gun = Gun(0,30)
        '''
    def fully(self) -> bool:
        '''
        Проверяет заряжен полностю магазин
        Пример:
        >>> mag = Gun(30, 30)
        >>> mag.fully()
        '''
        ...
    def reload(self, bullets: int) -> None:
        '''
        Перезарядка
        param: bullets - пули заряжаемые в магазин
        Пример:
        >>> new_mag = Gun(3, 30)
        >>> new_mag.reload(15)
        '''
        ...

class Ladya:
    def __init__(self, x_cord: str, y_cord: int):
        '''
        param: x_cord - координата по горизонатли на доске
        param: y_cord - координата по вертикали на доске
        Пример:
        >>> chess = Ladya('h', 1)
        '''
    def hod_x(self, x: str) -> str:
        '''
        Движение фигуры по горизонтали
        param: x - новая координата x
        Пример:
        >>> moveA = Ladya('h', 3)
        >>> moveA.hod_x('a')
        '''
        ...
    def hod_y(self, y: int) -> int:
        '''
        Движение фигуры по вертикали
        param: y - новая координата y
        Пример:
        >>> moveb = Ladya('h', 3)
        >>> moveb.hod_y(7)
        '''
        ...
class Engine:
    def __init__(self, power: int, model: str):
        '''
        Создает двигатель с определенной мощностью
        param: power - мощность кВт
        param: model - модель
        Пример:
        >>> lada = Engine(300, 'priora')
        '''
    def start(self) -> bool:
        '''
        Запуск двигателя
        Пример:
        >>> V8 = Engine(300, 'priora')
        >>> V8.start()
        '''
        ...
    def boost(self, buff: int) -> int:
        '''
        Увеличение мощности за счет тюнинга
        param: buff - добавочная мощность
        Пример:
        >>> turbo = Engine(300, 'priora')
        >>> turbo.boost(150)
        '''
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
