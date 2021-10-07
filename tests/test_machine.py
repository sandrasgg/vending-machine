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
	assert product.stock == 0 


def test_should_not_buy_product_if_not_enough_cash():
	# given
	machine = Machine()
	machine.valid_coins = 0

	product = Product(1, 'Coke', 1, 1)

	# when
	machine.buy_product(product)

	# then
	assert machine.valid_coins == 0
	assert machine.remaining_cash == 0
	assert product.stock == 1 


def test_should_check_valid_coin_successfully():
	# given
	machine = Machine()
	machine.inserted_coins = 0.05

	# when
	result = machine.check_coins()

	# then
	assert result == True


def test_check_coins_should_return_invalid():
	# given
	machine = Machine()
	machine.inserted_coins = 0.30

	# when
	result = machine.check_coins()

	# then
	assert result == False


def test_should_return_true_if_product_is_available():
	# given
	machine = Machine()
	product = Product(1, 'Coke', 1, 1)

	machine.products.append(product)

	# when
	result = machine.is_product_available('Coke')

	# then
	assert result == True


def test_should_return_false_if_product_is_unavailable():
	# given
	machine = Machine()
	product = Product(1, 'Coke', 1, 1)

	machine.products.append(product)

	# when
	result = machine.is_product_available('Some product')

	# then
	assert result == False


def test_should_return_false_if_product_is_out_of_stock():
	# given
	machine = Machine()
	product = Product(1, 'Coke', 1, 0)

	machine.products.append(product)

	# when
	result = machine.is_product_available('Coke')

	# then
	assert result == False


def test_should_return_false_if_is_not_empty():
	# given
	machine = Machine()
	product1 = Product(1, 'Coke', 1, 2)
	product2 = Product(2, 'Fanta', 1, 0)

	machine.products.append(product1)
	machine.products.append(product2)

	# when
	result = machine.is_empty()

	# then
	assert result == False



def test_should_return_true_if_empty_machine():
	# given
	machine = Machine()
	product1 = Product(1, 'Coke', 1, 0)
	product2 = Product(2, 'Fanta', 1, 0)

	machine.products.append(product1)
	machine.products.append(product2)

	# when
	result = machine.is_empty()

	# then
	assert result == True


def test_returns_beverage_correctly():
	# given
	machine = Machine()
	product = Product(1, 'Fanta', 2.50, 3)
	machine.products.append(product)
	chosen_beverage = 'Fanta'

	# when
	result = machine.select_product(chosen_beverage)

	# then
	assert result == product
	assert result.order == 1
	assert result.name == 'Fanta'
	assert result.price == 2.50
	assert result.stock == 3


def test_does_not_return_beverage_if_not_present():
	# given
	machine = Machine()
	chosen_beverage = 'Coke'

	# when
	result = machine.select_product(chosen_beverage)

	# then
	assert result == None












