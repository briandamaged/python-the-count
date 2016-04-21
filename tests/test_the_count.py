
import random

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


def test_tally_counts_stuff():
  c = TheCount()

  assert set(c.keys()) == set()

  for _ in xrange(3):
    c.tally("foo")

  assert set(c.keys()) == set(["foo"])
  assert c["foo"] == 3

  for _ in xrange(2):
    c.tally(10, 2)

  assert set(c.keys()) == set(["foo", 10])
  assert c["foo"] == 3
  assert c[10] == 4

  for _ in xrange(2):
    c.tally("foo")

  assert set(c.keys()) == set(["foo", 10])
  assert c["foo"] == 5
  assert c[10] == 4



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


def test_total_returns_number_of_occurrences_when_key_was_tallied():
  c = TheCount()

  times = random.randint(3, 10)
  for _ in xrange(times):
    c.tally("foo")

  assert c.total("foo") == times


def test_get_returns_0_by_default():
  c = TheCount()

  times = random.randint(3, 10)
  for _ in xrange(times):
    c.tally("foo")

  assert c.get("foo") == times
  assert c.get("bar") == 0


def test_total_returns_0_when_no_keys_are_requested():
  c = TheCount()
  assert c.total() == 0


def test_total_returns_0_if_key_was_never_tallied():
  c = TheCount()

  times = random.randint(3, 10)
  for _ in xrange(times):
    c.tally("foo")

  assert c.total("foo") == times
  assert c.total("bar") == 0


def test_total_returns_the_sum_of_the_specified_keys():
  c = TheCount()

  foo_times = random.randint(3, 10)
  for _ in xrange(foo_times):
    c.tally("foo")

  bar_times = random.randint(3, 10)
  for _ in xrange(bar_times):
    c.tally("bar")

  assert c.total("foo") == foo_times
  assert c.total("bar") == bar_times
  assert c.total("foo", "bar") == foo_times + bar_times
  assert c.total("foo", "bar", "quux") == foo_times + bar_times

def test_iter_methods_work_as_expected():
  c = TheCount()
  c.tally("foo")
  c.tally("bar")
  c.tally("foo")
  c.tally(4.2)
  c.tally((1, 2, 3))

  assert set(iter(c)) == set(["foo", "bar", 4.2, (1, 2, 3)])
  assert set(c.iterkeys()) == set(["foo", "bar", 4.2, (1, 2, 3)])
  assert set(c.itervalues()) == set([2, 1])
  assert set(c.iteritems()) == set([("foo", 2), ("bar", 1), (4.2, 1), ((1, 2, 3), 1)])


def test_clear_resets_the_sums():
  c = TheCount()
  c.tally("foo")
  c.tally("bar")

  assert len(c) == 2

  c.clear()

  assert len(c) == 0


def test_grand_total_sums_everything_up():
  c = TheCount()

  for _ in xrange(5):
    c.tally("foo")

  for _ in xrange(2):
    c.tally("bar")

  for _ in xrange(4):
    c.tally(153)

  assert c.grand_total() == 11


def test_select_keeps_iteritems_such_that_func_returns_something_truthy():
  c = TheCount()
  for _ in xrange(6):
    c.tally("apple")

  for _ in xrange(2):
    c.tally("banana")

  for _ in xrange(10):
    c.tally("carrot")

  for _ in xrange(3):
    c.tally(42)

  d = c.select(lambda k, v: v > 3)
  assert set(d.keys()) == set(["apple", "carrot"])
  assert d["apple"] == 6
  assert d["carrot"] == 10


def test_reject_keeps_iteritems_such_that_func_returns_something_falsey():
  c = TheCount()
  for _ in xrange(6):
    c.tally("apple")

  for _ in xrange(2):
    c.tally("banana")

  for _ in xrange(10):
    c.tally("carrot")

  for _ in xrange(3):
    c.tally(42)

  d = c.reject(lambda k, v: v > 3)
  assert set(d.keys()) == set(["banana", 42])
  assert d["banana"] == 2
  assert d[42] == 3



def test_select_and_reject_do_not_modify_the_original_TheCount_instance():
  c = TheCount()
  for _ in xrange(6):
    c.tally("apple")

  for _ in xrange(2):
    c.tally("banana")

  for _ in xrange(10):
    c.tally("carrot")

  for _ in xrange(3):
    c.tally(42)

  d = c.select(lambda k, v: v > 3)
  assert set(c.keys()) == set(["apple", "banana", "carrot", 42])
  assert set(d.keys()) == set(["apple", "carrot"])

  e = c.reject(lambda k, v: v > 3)
  assert set(c.keys()) == set(["apple", "banana", "carrot", 42])
  assert set(e.keys()) == set(["banana", 42])
