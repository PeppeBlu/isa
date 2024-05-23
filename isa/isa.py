import argparse
import sys
import logging
import math

# creo classe che gestisce il calcolo delle metriche
class Operation():
    """Class to handle the metrics computations"""

    # questo metodo restituisce null (posso anche togliere -> Null ma è un TypeHint)
    def __init__(self,
            # argomento: tipo
            predicted: 'list[float]',
            expected: 'list[float]',
            metrics: str 
        ) -> None:

        self.predicted:  'list[float]' = predicted
        self.expected:  'list[float]' = expected
        self.metrics: str = metrics

        # controllo lunghezza liste
        if not self._is_consistent():
            #print("Predicted and expected should have same length")
            #logging.critical(print("Predicted and expected should have same length"))
            raise ValueError("Predicted and expected should have same length")
            #sys.exit()

    # con underscore davanti perchè è un metodo "interno", da non esporre all'ulizz
    def _is_consistent(self) -> bool:
        """Return true if the length of the two input are equal """
        return len(self.predicted) == len(self.expected)
    
    def _mae(self) -> float:
        """Calculate che MAE metric"""
        result: float = 0
        
        for p, e in zip(self.predicted, self.expected):
            result += abs(p -e)
        return result/len(self.predicted)

        #fn = lambda p, e: abs(p - e)
        #sum (list (map (fn, zip(self.predicted, self.expected))/len(self.predicted)))    

    

    def _mse(self) -> float:
        """
        Computes Mean Square Error
        """
        result: float = 0
        for i in range(0, len(self.predicted)):
            result += (self.predicted[i] - self.expected[i])**2
        return result/len(self.predicted)


    def _rmse(self) -> float:
        '''
        Computes the root means squared error
        '''
        return math.sqrt(self._mse())
    
    
    # in base alla metrica selezionata ho la funzione che calcola la metrica
    #senza underscore perchè è esposta all'utilizzatore
    def compute_metrics(self) -> float:
        """Calcola la metrica in base alla scelta"""
        if self.metrics == "MAE":
            return self._mae()
        elif self.metrics == "MSE":
            return self._mse()
        elif self.metrics == "RMSE":
            return self._rmse()
        else:
            return -1


def setup_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        #uso prog perchè
        prog="ISA",
        #uso description perchè 
        description="Computes error metrics"
    )

    # $ ISA --predicted 1 2 3 --expected 1 2 4 --metrics MAE
    parser.add_argument("--predicted", 
        type=float, 
        nargs='+', #una sorta di append del valori
        required=True, 
        help="Predicted Values"
    )

    parser.add_argument("--expected", 
        type=float, 
        nargs='+', #una sorta di append del valori
        required=True, 
        help="Predicted Values"
    )

    parser.add_argument("--metrics",
        type=str,
        required=True,
        help="Metrica da calcolare",
        choices=["MAE", "MSE"]
    )

    return parser.parse_args()





def main(arguments) -> float:

    """
    Main Function
    """
    # 1) interpretazione argomenti da linea di comando
    """ Main function"""
    
    logging.basicConfig(level=logging.WARNING)

    #arguments = parser.parse_args()
    logging.debug(arguments.predicted)
    
    logging.debug(arguments.predicted)
    
    logging.debug(arguments.expected)
    
    logging.debug(arguments.metrics)
    

    solver = Operation(arguments.predicted, arguments.expected, arguments.metrics)

    result = solver.compute_metrics()
    print(f"Result: {result}")

    return result


if __name__ == "__main__":
    result = main(setup_parser())
    #stampo il risultato
    print(f"Result: ", result)

# se ci sono istruzioni qui, vengono comunque eseguiti, quindi scrivo il main in fondo
#commento inutile
