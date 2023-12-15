from day_15 import calc_new_value, calc_value

class TestCalcNewValue:
    def test_returns_correct_value_starting_at_zero(self):
        assert calc_new_value(0, "H") == 200

    def test_returns_correct_value(self):
        assert calc_new_value(200, "A") == 153
        assert calc_new_value(153, "S") == 172
        assert calc_new_value(172, "H") == 52

class TestCalcValue:
    def test_calculates_value_for_sequence(self):
        assert calc_value("rn=1") == 30
        assert calc_value("cm-") == 253
        assert calc_value("qp=3") == 97
        assert calc_value("cm=2") == 47
        assert calc_value("qp-") == 14
        assert calc_value("pc=4") == 180
        assert calc_value("ot=9") == 9
        assert calc_value("ab=5") == 197
        assert calc_value("pc-") == 48
        assert calc_value("pc=6") == 214
        assert calc_value("ot=7") == 231
