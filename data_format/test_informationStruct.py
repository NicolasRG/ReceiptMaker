from informationStruct import Item, InformationStruct

item = Item("Tomatos", 4, 2)
other_item = Item("Carrot", 3, 1)
receipt = None


def test_item():
    assert item.getCost() == 8.00


def test_item_discount():
    item.setDiscount(.5)
    assert item.getCost() == 4.00


def test_informationStruct():
    receipt = InformationStruct([item])
    receipt.addItem(other_item)
    assert other_item in receipt.get_items()

def test_informationStruct_total():
    receipt = InformationStruct([item, other_item])
    assert receipt.getTotal() == 7.00
