# test_knp.py -- testy

import knp

def test_vyhry():
    assert vyhodnot('kámen', 'papír') == 'Vyhrála jsi!'
    assert vyhodnot('papír', 'nůžky') == 'Vyhrála jsi!'
    assert vyhodnot('nůžky', 'kámen') == 'Vyhrála jsi!'