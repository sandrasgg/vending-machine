from machine import Machine
from product import Product



def test_add_product():
	# given
	machine = Machine()
	product = 'some product'

	# when
	machine.add_product(product)

	# then
	assert len(machine.products) == 1



def test_should_buy_product_successfully_if_enough_cash():
	# given
	machine = Machine()
	machine.valid_coins = 2

	product = Product(1, 'Coke', 1, 1)

	# when
	machine.buy_product(product)

	# then
	assert machine.valid_coins == 1
	assert machine.remaining_cash == 1 
