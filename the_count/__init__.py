
class TheCount(object):
  def __init__(self, sums = None):
    self.sums = sums or {}

  def tally(self, thing):
    self.sums[thing] = self.sums.get(thing, 0) + 1

  def keys(self):
    return self.sums.keys()

  def __getitem__(self, key):
    return self.sums[key]

  def get(self, key, *args):
    return self.sums.get(key, *args)

  def total(self, key):
    """
    Returns the number of times the key has occurred, or 0
    if the key was never encountered.
    """
    return self.get(key, 0)

  def __len__(self):
    return len(self.sums)

  def __add__(self, counter):
    keys = set(self.keys() + counter.keys())
    sums = {}
    for k in keys:
      sums[k] = self.total(k) + counter.total(k)

    return TheCount(sums)

  def __str__(self):
    return str(self.sums)

  __repr__ = __str__


