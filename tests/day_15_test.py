from day_15 import calc_new_value

class TestCalcNewValue:
    def test_returns_correct_value_starting_at_zero(self):
        assert calc_new_value(0, "H") == 200

    def test_returns_correct_value(self):
        assert calc_new_value(200, "A") == 153
        assert calc_new_value(153, "S") == 172
        assert calc_new_value(172, "H") == 52
