from product import Product



def test_decrease_stock():
	# given
	product = Product(1, 'Coke', 2.50, 2)

	# when
	product.decrease_stock()

	# then
	assert product.stock == 1
