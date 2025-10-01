import pydaasiot



class MyHandler(pydaasiot.IDaasApiEvent):
    def dinAcceptedEvent(self, din):
        print(f"[EVENT] DIN accepted: {din}")

    def ddoReceivedEvent(self, payload_size, typeset, din):
        print(f"[EVENT] DDO received (sender side)")

    def frisbeeReceivedEvent(self, din):
        print(f"[EVENT] FRISBEE")

    def nodeStateReceivedEvent(self, din):
        print(f"[EVENT] Node state received")

    def atsSyncCompleted(self, din):
        print(f"[EVENT] ATS sync completed")

    def frisbeeDperfCompleted(self, din, packets_sent, block_size):
        print(f"[EVENT] Frisbee dperf completed")

handler = MyHandler()

# Inizializza il wrapper con config e handler
node = pydaasiot.DaasWrapper("config.json", handler)

# SID e DIN del nodo sender
node.doInit(100, 102)

# Abilita il driver di rete sulla porta 2223 (per il sender)
node.enableDriver(pydaasiot.link_t._LINK_INET4, "127.0.0.1:2223")

# Mappa il receiver (DIN 101) sulla porta 2222
node.map(101, pydaasiot.link_t._LINK_INET4, "127.0.0.1:2222")

# Avvia il thread interno
node.doPerform(pydaasiot.performs_mode_t.PERFORM_CORE_THREAD)

# Creiamo un DDO da inviare
ddo = pydaasiot.DDO()
ddo.setOrigin(102)
ddo.setTypeset(1)  # puoi cambiare il typeset a seconda del test
ddo.allocatePayload(32)
ddo.appendPayloadData(b"Hello from sender!")

# Esegui push verso il nodo 101
err = node.push(101, ddo)
print(f"Push result: {err}")

input("Press Enter to exit...\n")
