# Fruit Stand

### v1.0.0

Fruit Stand generates lists or dictionaries of fruits to streamline to demonstration of Python fundumentals involving the two data types.

## Installation

`pip install fruit_stand`

## Usage

`import fruit_stand`

Fruit Stand contains four functions:

1.  `all_fruits()`
    > This returns a list of all the fruits that Fruit Stand has.

2. `shopping_list(n = 10)`
   > Returns a list of `n` fruit names. 

3. `fruit_prices(n = 10)`
    > Returns a dictionary containing `n` number of fruits as keys and random float values between 0.0 and 1.0 representing their price.

4. `fill_basket(n = 10)`
    > Returns a dictionary containing `n` number of fruits with dictionaries as values. These nested dictionaries contain:

    * `quantity` - Random integer value between 1 and 10 representing how many of this item are in the basket
    * `price_per` - A random float value between 0.0 and 1.0 representing the price per item.
    * `item_total` - The product of multiplying `quantity` by `price_per`

If no value for `n` is passed to these functions, they will return 10 items each by default.

If anything other than an integer is passed to these functions, a TypeError will be raised, and `None` will be returned.