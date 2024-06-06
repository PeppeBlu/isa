import pytest

# from isa.isa import Operation
import isa.isa as isa


 
class TestUnit:
    def test_mae_0(self):
        p = [1, 2, 5]
        e = [1, 2, 5]
        expected_result = 0
        op = isa.Operation(predicted=p, expected=e, metrics="MAE")
        computed_value = op.compute_metrics()
        assert computed_value == expected_result
    
    #@pytest.mark.skip(reason="Not implemented yet")
    def test_mae_1(self):
        p = [1, 2, 5]
        e = [1, 2, 4]
        expected_result = 0.333333

        op = isa.Operation(predicted=p, expected=e, metrics="MAE")
        computed_value = op.compute_metrics()

        assert pytest.approx(computed_value) == expected_result

    def test_mse(self):
        p = [1, 2, 5]
        e = [1, 2, 5]

        op = isa.Operation(predicted=p, expected=e, metrics="MSE")
        res = op.compute_metrics()
        assert res == 0

    def test_raise_exception(self):
        with pytest.raises(ValueError):
            p = [1, 2, 5, 6]
            e = [1, 2, 5]
            op = isa.Operation(predicted=p, expected=e, metrics="MSE")
            op.compute_metrics()

    #questo non è un test, solo un assert
    def test_non_test(self):
        p = [1, 2, 5]
        e = [1, 2, 5]
        excepted_result = 0
        op = isa.Operation(predicted=p, expected=e, metrics="MAE")
        computed_value = op.compute_metrics()

        #return computed_value == excepted_result

        #try:
            #assert computed_value == excepted_result
        #except:
            #assert True

    @pytest.mark.parametrize("p, e, m, r", [
        ([1, 2, 5], [1, 2, 5], "MSE",0),
        ([1, 2, 5], [1, 2, 5], "RMSE",0)
    ])
    def test_parametrized(self, p, e, m, r):
        #expected_result = 0
        op = isa.Operation(predicted=p, expected=e, metrics=m)
        computed_value = op.compute_metrics()
        assert computed_value == r
    
    
    def test_rmse(self, monkeypatch):
        p = [1, 2, 5]
        e = [1, 2, 5]
        expected_result = 0
        op = isa.Operation(predicted=p, expected=e, metrics="RMSE")
        #RMSE non è ancora implementata quindi la simulo

        monkeypatch.setattr(op, "compute_metrics", lambda: 0)

        res = op.compute_metrics()
        assert res == expected_result


    def test_rmse_0(self):
        p = [1, 2, 5]
        e = [1, 2, 5]
        expected_result = 0
        op = isa.Operation(predicted=p, expected=e, metrics="RMSE")
        #RMSE adesso è implementata

        res = op.compute_metrics()
        assert res == expected_result


    def test_rmse_1(self):
        import math
        p = [1, 2, 5]
        e = [1, 2, 4]
        expected_result = math.sqrt(1/3)
        op = isa.Operation(predicted=p, expected=e, metrics="RMSE")
        #RMSE adesso è implementata

        res = op.compute_metrics()
        assert pytest.approx(res) == expected_result