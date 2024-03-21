# ISA instestazione

-- Descrizione testiuale di cosa fa la mia applicazione --
Date due liste di interi calcola diverse metriche di errore:
- MAE (mean absolute error)
- MSE (mean square error)

Esempio:
predicted = [1,2,3]
expected = [1,2,4]

MAE = 1/len(l1) * somma(|l1[i]-l2[i]|)

    = (|1-1|+|2-2|+|3-4|)/3

Voglio eseguire il mio programma al terminale:
$ ISA --predicted 1 2 3 --expected 1 2 4 --metrics MAE


