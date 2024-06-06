import pytest
import isa.isa as isa

class TestIntegration:
    
    def test_integration_arguments(self,monkeypatch):
        import argparse

        #definisco la funzione che restituisce il valore
        def return_value():
            return argparse.Namespace(predicted=[1.0,2.0,3.0], expected=[1.0,2.0,3.0], metrics="MAE")
        
        #testa il main
        monkeypatch.setattr(isa, "setup_parser", return_value)
                            
        assert isa.main(isa.setup_parser()) == 0.0    