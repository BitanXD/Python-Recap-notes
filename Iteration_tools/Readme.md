## How to open files and get their reference stored in a variable

> > > f = open("test.py")

> > > f.readline()

> > > 'import math\n'

> > > f.readline()

> > > 'print(math.floor(3.25))\n'

> > > f.readline()

> > > 'name = "Bitan"\n'

> > > f.readline()

> > > 'print(name)'

> > > f.readline()

> > > ''

## with the **next** function it is a raw way to get each line of the file, upon reaching the end of the file it throws a error as StopIteration to indicate the end of file

> > > f = open("test.py")

> > > f.__next__()

> > > 'import math\n'

> > > f.__next__()

> > > 'print(math.floor(3.25))\n'

> > > f.__next__()

> > > 'name = "Bitan"\n'

> > > f.__next__()

> > > 'print(name)'

> > > f.__next__()

> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > StopIteration

## other ways to read / open a file using loops

> > > f = open("test.py")

> > > while True:

> > > ... line = f.readline()

> > > ... if not line:

> > > ... break

> > > ... print(line, end="")

> > > ...
> > > import math
> > > print(math.floor(3.25))
> > > name = "Bitan"
> > > print(name)>>>

## testing the string value

> > > test = "bitan"

> > > if not test: // not empty

> > > ... print("pudding")

> > > ...

> > > test = ""

> > > if not test:  // empty

> > > ... print("pudding")

> > > ...

> > > pudding


>>> mylist = [1,2,3,4,5]

>>> I = iter(mylist) // reference variable of the list

>>> I
<list_iterator object at 0x000001F154F04130> 
>>> I.__next__()
1
>>> I.__next__()
2
>>> I
<list_iterator object at 0x000001F154F04130> // reference is same ie it still points to the first item in the list

>>> f = open("test.py")

>>> iter(f) is f
//
True

>>> iter(mylist) is mylist
//
False