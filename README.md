# TheCount #

TheCount loves to count things!

## Installation ##

```shell
pip install the_count
```

## Usage ##

```python
from the_count import TheCount

c = TheCount()

c.tally("foo")
c.tally("foo")
c.tally("bar")
c.tally(4)

print(c["foo"])        # Prints: 2
print(c["bar"])        # Prints: 1
print(c["quux"])       # Throws: KeyError

print(c.total("foo"))  # Prints: 2
print(c.total("bar"))  # Prints: 1
print(c.total("quux")) # Prints: 0

print(c.grand_total()) # Prints: 4

# TheCount supports most (all?) of the iteration functions
# that are available to the dict type:
for k, v in c.iteritems():
  print("%s: %s" % (k, v))


# Create a new TheCount instance that only contains the
# key/value pairs that satisfy the condition:
d = c.select(lambda k, v: v > 1)
print(d.keys())   # Prints: ["foo"]


# Create a new TheCount instance that only contains the
# key/value pairs that fail to satisfy the condition:
d = c.reject(lambda k, v: v > 1)
print(d.keys())   # Prints: ["bar", 4]


# Use the + operator to aggregate results
dracula = TheCount()

dracula.tally("one")
dracula.tally(2)
dracula.tally(2)
dracula.tally("THREE")

chocula = TheCount()

chocula.tally("one")
chocula.tally(2)
chocula.tally("THREE")
chocula.tally(4.0)
chocula.tally(4.0)

orlok = dracula + chocula

print(orlok.total("one"))   # Prints: 2
print(orlok.total(2))       # Prints: 3
print(orlok.total(5))       # Prints: 0

```

