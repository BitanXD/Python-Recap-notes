# INNER WORKING OF PYTHON

Compile to byte code - low level and platform independent
byte code runs faster
.pyc - compiled python (frozen binaries)
**pycache** source change and python version uses a difference change algorithm
works only for imported files
not for top level files

# Python Virtual Machine PVM

code loop to iterate byte code
run time engine
also known as python interpreter
byte code is not machine code - python specific interpretation
machine code is direct instruction for the computer hardware intel, ryzen, apple chips

# Python shell concepts

can import custom files and programs

suppose there is changes made in the file that has been imported it will not get
updated on the terminal we need to reload the imported file using from importlib import reload
then run the command reload(bitan_sarkar)

a = 5

b = 2

a = a + 2 // 7

what happened above

calculation is done a = 5 + 2

a = 7

first 7 object is created and then a variable reference is pointed to 7

> > > mylistone = [1,2,3]

> > > mylisttwo = mylistone

> > > mylisttwo
> > > //
> > > [1, 2, 3]

> > > mylistone[0] = 22

> > > mylistone
> > > //
> > > [22, 2, 3]

> > > mylisttwo
> > > //
> > > [22, 2, 3]

untill the above both mylistone and mylisttwo had the same reference to the [22,2,3]

> > > mylistone = 'pudding'

> > > mylistone
> > > //
> > > 'pudding'

> > > mylisttwo
> > > //
> > > [22, 2, 3]

> > > mylistone = [22,2,3]
> > > mylistone
> > > //
> > > [22, 2, 3]

> > > mylisttwo
> > > //
> > > [22, 2, 3]

> > > mylistone[1] = 11

> > > mylistone
> > > //
> > > [22, 11, 3]

> > > mylisttwo
> > > //
> > > [22, 2, 3]

since list is mutable so on creating a new variable with the same value a new reference is created in the memory and tho it may seem that both the variables are
havind the same reference to the value but they are having different references in case of mutable type data

> > > h1 = [1,2,3]

> > > h2 = h1[:]

when we slice then it makes a new reference

> > > h1[0] = 55

> > > h1
> > > //
> > > [55, 2, 3]

> > > h2
> > > //
> > > [1, 2, 3]

> > > m = [1,2,3]

> > > m = n

Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined

> > > n = m

> > > m
> > > //
> > > [1, 2, 3]

> > > n
> > > //
> > > [1, 2, 3]

> > > m == n
> > > //
> > > True

> > > m is n
> > > //
> > > True

since both m and n has same reference, it is true

> > > n = [1,2,3] // now n is defined explicitly

although m and n has same value hence true but their reference is different hence false

> > > m == n
> > > //
> > > True

> > > m is n
> > > //
> > > False

username = "bitan"

> > > username
> > > //
> > > 'bitan'

> > > username = "sonia"

> > > username
> > > //
> > > 'sonia'

> > > num1 = 10

> > > num2 = num1

> > > num1
> > > //
> > > 10

> > > num2
> > > //
> > > 10

> > > num1 = 20

> > > num1
> > > //
> > > 20

> > > num2
> > > //
> > > 10

mutable and immutable

username = "bitan" // nothing is pointing to this variable so garbage collector deletes it automatically

username = "pudding"

here the reference changes for the variable username to pudding

x = 10 // reference get changed to 20
y = x // still reference is same to 10
x = 20 // new reference is set to 20

in python everything is treated as object

data/object types in python

- numbers : 1231, 3.123, 3+4j, 0b111, Decimal(), Fraction()
- string : 'spam', "bob's"
- list : [1,2,3, 'three', [4,5],7,8], list(range(10))
- tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- dictionary : {'food': 'chicken', 'taste': 'yummy'}, dict(hours = 10)
- set : set('abc') , {'a','b','c'} unique data storage
- file : open('file.txt'), open('C:\ham.bin', 'wb')

# OPERATORS

1 == 2 < 3 // return false
it is read as if( 1 == 2 and 2 < 3 )
so it returns false

> > > 2 + 3j \* 4
> > > //
> > > (2+12j)

> > > (2 + 3j) \* 4
> > > //
> > > (8+12j)

> > > 1001
> > > //
> > > 1001

> > > 0o20
> > > //
> > > 16

> > > 0xFF
> > > //
> > > 255

> > > 0b1001
> > > //
> > > 9

> > > 0b1000
> > > //
> > > 8

> > > oct(64)
> > > //
> > > '0o100'

> > > hex(64)
> > > //
> > > '0x40'

> > > bin(64)
> > > //
> > > '0b1000000'

> > > 0.1 + 0.1 + 0.1 - 0.3
> > > //
> > > 5.551115123125783e-17

> > > Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
> > > //
> > > Decimal('0.0')

> > > from fractions import Fraction

> > > myFrac = Fraction(2,7)

> > > myFrac
> > > //
> > > Fraction(2, 7)

# STRING

repr() provides a string representation suitable for debugging,
str() provides a more user-friendly string representation,
and
print() is a function for outputting text or values to the console, typically using str() for the conversion.

> > > string = "bitan"

> > > string
> > > //
> > > 'bitan'

> > > string[-1:-6:-1]
> > > //
> > > 'natib'

> > > string[::2]
> > > //
> > > 'btn'

this is how we can convert a string to list type

> > > family = "bitan, sonia, pudding"  
> > > family.split(", ")
> > > //
> > > ['bitan', 'sonia', 'pudding']

> > > family = "bitan"

> > > newFamily = "sonia"

> > > fullFamily = "{} and {} are together"

> > > print(fullFamily)
> > > //
> > > {} and {} are together

> > > print(fullFamily.format(family, newFamily))  
> > > //
> > > bitan and sonia are together

this is how we can convert a list to string type

> > > family = ["bitan", "sonia", "pudding"]
> > > family
> > > //
> > > ['bitan', 'sonia', 'pudding']

> > > print(", ".join(family))
> > > //
> > > bitan, sonia, pudding

raw string is used to avoid unicode characters

family_path = "c:\bitan\sonia\pudding"
error

family_path = r"c:\bitan\sonia\pudding"
no error prints the correct output
