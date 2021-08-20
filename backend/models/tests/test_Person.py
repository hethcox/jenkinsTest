
from models.classes.Person import Person


def test_name():
    p1 = Person("John", 36)
    assert p1.name == 'John'
    assert p1.age == 36
