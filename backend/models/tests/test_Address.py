from models.classes.Address import Address
from models.classes.Person import Person

def test_Address():
    a1 = Address("17 W Nightingale", "Apopka", "FL", 32712)
    assert a1.street == '17 W Nightingale'
    assert a1.city == 'Apopka'
    assert a1.state == 'FL'
    assert a1.zip == 32712

def test_inhabitants():
    a1 = Address("17 W Nightingale", "Apopka", "FL", 32712)
    p1 = Person("John", 36)
    a1.addInhabitant(p1)
    assert len(a1.inhabitants) == 1
