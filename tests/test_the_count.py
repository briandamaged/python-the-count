
from the_count import TheCount

def test_len_returns_number_of_unique_keys():
  c = TheCount()
  for _ in xrange(3):
    c.tally("foo")

  assert len(c) == 1

  for _ in xrange(2):
    c.tally("bar")

  assert len(c) == 2

  for _ in xrange(2):
    c.tally("foo")

  assert len(c) == 2


def test_it_counts_stuff():
  c = TheCount()

  assert set(c.keys()) == set()

  for _ in xrange(3):
    c.tally("foo")

  assert set(c.keys()) == set(["foo"])
  assert c["foo"] == 3

  for _ in xrange(2):
    c.tally(10)

  assert set(c.keys()) == set(["foo", 10])
  assert c["foo"] == 3
  assert c[10] == 2

  for _ in xrange(2):
    c.tally("foo")

  assert set(c.keys()) == set(["foo", 10])
  assert c["foo"] == 5
  assert c[10] == 2


def test_counts_can_be_aggregated():
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

  assert set(orlok.keys()) == set(["one", 2, "THREE", 4.0])
  assert orlok["one"] == 2
  assert orlok[2] == 3
  assert orlok["THREE"] == 2
  assert orlok[4.0] == 2

