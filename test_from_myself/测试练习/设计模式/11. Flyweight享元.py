# 11. Flyweight（享元）
# 运用共享技术有效地支持大量细粒度的对象。

import weakref

class Card(object):
    _CardPool = weakref.WeakValueDictionary()

    