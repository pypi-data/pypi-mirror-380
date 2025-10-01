import pydaasiot

class MyHandler(pydaasiot.IDaasApiEvent):
    def dinAcceptedEvent(self,din):
        print(f"[EVENT] DIN accepted: {din}")
        
    def ddoReceivedEvent(self,payload_size,typeset,din):
        print(f"[EVENT] DDO received: din={din}, size={payload_size}, typeset={typeset}")

        
        err, ddo = self.node.pull(din)
        if err == pydaasiot.daas_error_t.ERROR_NONE and ddo is not None:
            
            data = ddo.getPayloadAsBinary()
            print(f"[PULL] Payload received from DIN {din}: {data}")
        else:
            print(f"[PULL] Pull failed with error {err}")
        
        
    def frisbeeReceivedEvent(self,din):
        print(f"[EVENT] FRISBEE")
        
    def nodeStateReceivedEvent(self,din):
        print(f"[EVENT] Node state received")
        
    def atsSyncCompleted(self,din):
        print(f"[EVENT] ATS sync completed")
        
    def frisbeeDperfCompleted(self,din,packets_sent,block_size):
        print(f"[EVENT] Frisbee dperf completed")
        
handler = MyHandler()

node = pydaasiot.DaasWrapper("config.json",handler)
handler.node = node
node.doInit(100,101)
node.enableDriver(pydaasiot.link_t._LINK_INET4,"127.0.0.1:2222")
node.map(102,pydaasiot.link_t._LINK_INET4,"127.0.0.1:2223")

node.doPerform(pydaasiot.performs_mode_t.PERFORM_CORE_THREAD)

input("Press Enter to exit...\n")

