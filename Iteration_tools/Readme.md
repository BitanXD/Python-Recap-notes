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


## with the __next__ function it is a raw way to get each line of the file, upon reaching the end of the file it throws a error as StopIteration to indicate the end of file
> > > f = open("test.py")

> > > f.**next**()

> > > 'import math\n'

> > > f.**next**()

> > > 'print(math.floor(3.25))\n'

> > > f.**next**()

> > > 'name = "Bitan"\n'

> > > f.**next**()

> > > 'print(name)'

> > > f.**next**()

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

> > > if not test:

> > > ... print("pudding")

> > > ...

> > > test = ""

> > > if not test:

> > > ... print("pudding")

> > > ...

> > > pudding
