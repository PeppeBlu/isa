# parent image
FROM python

#impostiamo la working directory 
#(all'interno dell'immagine, e quindi del container)
WORKDIR /home/isa

# copio il file di build nel container
#punto finale copia il file nella cartella corrente
#specificata nella workdir

#se non specifico la workdir viene copiato
#nella root
COPY dist/isa-0.0.1-py3-none-any.whl .

#dopo aver copiato il file eseguo il run del file che mi interessa
#con sinstassi exec o bash
RUN ["python", "-m", "pip", "install", "isa-0.0.1-py3-none-any.whl"]

#imposto il comando che viene eseguito appena runnato il container
#ENTRYPOINT ["isa", "--predicted"; "1", "2", "3", "--expected", "1", "2", "4", "--metrics", "MAE"]

#se la chiamo così mi da l'errore che è sena argomenti
#li posso passare tramite il terminale stesso con la chiamata run
ENTRYPOINT [ "isa" ]