import pydaasiot
from pydaasiot import DDO, IDaasApiEvent, DaasWrapper

class HandlerBidirezionale(IDaasApiEvent):
    
    def __init__(self, nodo):
        super().__init__()
        self.nodo = nodo

    def ddoReceivedEvent(self, dimensione_payload, typeset, din_sorgente):
        print(f"Messaggio ricevuto da: {din_sorgente}, dimensione: {dimensione_payload}, typeset: {typeset}")

        result, ddo = self.nodo.wrapper.pull(din_sorgente)
        print(f"DEBUG pull() -> result = {result} , ddo = {ddo}")

        if result == pydaasiot.daas_error_t.ERROR_NONE and ddo is not None:
            
            payload = ddo.getPayloadAsBinary()

            try:
                msg = payload.decode('utf-8')
                print(f"Messaggio: {msg}")
            except Exception:
                print(f"Messaggio: {payload}")
        else:
            print(f"Pull non riuscito con errore {result}")
            
    def dinAcceptedEvent(self, din): 
        print(f"DIN {din} accettato")
        

    def nodeStateReceivedEvent(self, din): pass
    def frisbeeReceivedEvent(self, din): pass
    def atsSyncCompleted(self, din): pass
    def frisbeeDperfCompleted(self, din, p, s): pass


class NodoBidirezionale:
    def __init__(self, sid, din, ip_locale, porta_locale, din_remoto, ip_remoto,
                 porta_remota):
        
        self.sid = sid
        self.din = din
        self.ip_locale = ip_locale
        self.porta_locale = porta_locale
        self.din_remoto = din_remoto
        self.ip_remoto = ip_remoto
        self.porta_remota = porta_remota
        
        self.handler = HandlerBidirezionale(self)
        self.wrapper = DaasWrapper("",self.handler)
        self.handler.nodo = self   
        self.running = False

    def chat_interattiva(self):
        """Interfaccia chat interattiva"""
        print("CHAT ATTIVA - Scrivi un messaggio per il nodo remoto")
        print("    Scrivi: '!quit' per interrompere")
        print("    Scrivi: '!status' per lo stato")

        while self.running:
            try:
                messaggio = input("> ")

                if not messaggio:
                    continue 

                if messaggio.lower() == '!quit':
                    break

                if messaggio.lower() == '!status':
                    print(f"Nodo ativo - DIN: {self.din}")
                    continue

                self.invia_messaggio(messaggio)
            except KeyboardInterrupt:
                break
            except Exception as e:
               print(f"Errore Input: {e}")

    def inizializza_mio_nodo(self):
        """Inizializzo nodo"""
        print("Inizializzo nodo locale")

        nodo = self.wrapper.doInit(self.sid, self.din)
        if nodo != pydaasiot.daas_error_t.ERROR_NONE:
            print("Errore inizializzazione")
            return False
        print("Nodo inizializzato")
        return True 
        
    def configura_miei_driver(self):
        print("Configuro Driver nodo locale")
        uri_locale = f"{self.ip_locale}:{self.porta_locale}"
        driver = self.wrapper.enableDriver(pydaasiot.link_t._LINK_INET4, uri_locale)
        if driver != pydaasiot.daas_error_t.ERROR_NONE:
            print("Errore Driver!")
            return False
        print("Driver configurati")
        return True
        
    def mappa_nodo_remoto(self):
        uri_remoto = f"{self.ip_remoto}:{self.porta_remota}"
        nodo_remoto = self.wrapper.map(self.din_remoto, pydaasiot.link_t._LINK_INET4,
                                       uri_remoto)
        
        if nodo_remoto != pydaasiot.daas_error_t.ERROR_NONE:
            print("Errore mappatura nodo remoto")
            return False
        print("Mappatura nodo remoto completata")
        return True

    def invia_messaggio(self, messaggio):
        ddo = DDO()
        ddo.setOrigin(self.din)
        ddo.setTypeset(1)
        ddo.allocatePayload(len(messaggio))
        ddo.appendPayloadData(messaggio.encode('utf-8'))
        

        invio = self.wrapper.push(self.din_remoto, ddo)
        if invio == 0:
            print(f"Messaggio inviato a: {self.din_remoto}")
            return True
        else:
            print("Invio messaggio non riuscito")
            return False
        
    def start(self):
        self.running = True
        avvio = self.wrapper.doPerform(pydaasiot.performs_mode_t.PERFORM_CORE_THREAD)
        if avvio != pydaasiot.daas_error_t.ERROR_NONE:
            print("Avvio non riuscito")
            return False
        print("Esecuzione nodo avviata")
        return True
    
    def stop(self):
        self.running = False
        self.wrapper.doEnd()
        print("Esecuzione nodo arrestata")

    
def main():
    SID = 100
    MIO_DIN = int(input("Inserisci il tuo DIN: ").strip())
    MIO_IP = input("Inserisci il tuo IP: ").strip() 
    MIA_PORTA = int(input("Inserisci la tua porta").strip())

    DIN_REMOTO = int(input("Inserisci il DIN remoto").strip())
    IP_REMOTO = input("Inserisci IP remoto").strip()
    PORTA_REMOTA = int(input("Inserisci la porta remota").strip())

    nodo = NodoBidirezionale(sid=SID, din=MIO_DIN, ip_locale=MIO_IP, 
                                porta_locale=MIA_PORTA, din_remoto=DIN_REMOTO,
                                ip_remoto=IP_REMOTO,
                                porta_remota=PORTA_REMOTA)
        
    if not nodo.inizializza_mio_nodo():
        return
        
    if not nodo.configura_miei_driver():
        return
        
    if not nodo.mappa_nodo_remoto():
        return 
        
    if not nodo.start():
        return
        
    try:
        nodo.chat_interattiva()
    except KeyboardInterrupt:
        print("Interruzione da tastiera...")
    finally:
            nodo.stop()

if __name__ == "__main__":
    main()