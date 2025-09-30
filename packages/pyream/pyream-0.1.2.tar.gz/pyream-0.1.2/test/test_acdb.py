import pyream.acdb


def test_acdb_emerge_lru_driver_append():
    c = pyream.acdb.Emerge(pyream.acdb.LruDriver(4))
    c['1'] = 1
    c['2'] = 2
    c['3'] = 3
    c['4'] = 4
    c['5'] = 5
    assert not '1' in c
    assert c['5'] == 5


def test_acdb_emerge_lru_driver_change():
    c = pyream.acdb.Emerge(pyream.acdb.LruDriver(4))
    c['1'] = 1
    c['2'] = 2
    c['3'] = 3
    c['4'] = 4
    c['1'] = 5
    assert c['1'] == 5


def test_acdb_emerge_lru_driver_delete():
    c = pyream.acdb.Emerge(pyream.acdb.LruDriver(4))
    c['1'] = 1
    c['2'] = 2
    c['3'] = 3
    c['4'] = 4
    del c['2']
    assert not '2' in c
