import typer
import pydaasiot

app = typer.Typer(help="DaaS-IoT Python CLI")

# Nodo globale
node = None

class MyHandler(pydaasiot.IDaasApiEvent):
    """
    Gestore eventi per il nodo DaaS-IoT.
    Tutti i metodi definiti in IDaasApiEvent sono implementati qui
    e stampano le informazioni ricevute.
    """
    def __init__(self, node_ref=None):
        super().__init__()
        self.node = node_ref

    def dinAcceptedEvent(self, din: int):
        print(f"[EVENT] DIN accepted: {din}")

    def ddoReceivedEvent(self, payload_size: int, typeset: int, din: int):
        print(f"[EVENT] DDO available from DIN {din} (size={payload_size}, typeset={typeset})")
        if self.node is None:
            print("[ERROR] No node reference set in handler.")
            return
        # Pull immediato del DDO
        err, ddo = self.node.pull(din)
        if err == pydaasiot.daas_error_t.ERROR_NONE and ddo:
            data = ddo.getPayloadAsBinary()
            print(f"[PULL] Pulled data: {data}")
        else:
            print(f"[PULL] Pull failed with error {err}")

    def frisbeeReceivedEvent(self, din: int):
        print(f"[EVENT] FRISBEE from DIN {din}")

    def nodeStateReceivedEvent(self, din: int):
        print(f"[EVENT] Node state received for DIN {din}")

    def atsSyncCompleted(self, din: int):
        print(f"[EVENT] ATS sync completed for DIN {din}")

    def frisbeeDperfCompleted(self, din: int, packets_sent: int, block_size: int):
        print(f"[EVENT] Frisbee dperf completed for DIN {din} "
              f"(packets_sent={packets_sent}, block_size={block_size})")


@app.command()
def init(sid: int, din: int, config: str = typer.Option("config.json", help="Path to config file")):
    """
    Initialize a DaaS-IoT node with given SID and DIN.
    """
    global node
    handler = MyHandler()
    node = pydaasiot.DaasWrapper(config, handler)
    handler.node = node
    node.doInit(sid, din)
    typer.echo(f"Node initialized SID={sid} DIN={din}")

@app.command()
def enable_driver(link: str, uri: str):
    """
    Enable a driver on the node.

    Example:
        enable-driver _LINK_INET4 127.0.0.1:2222
    """
    global node
    if node is None:
        typer.echo("Node not initialized")
        raise typer.Exit(1)
    link_enum = getattr(pydaasiot.link_t, link)
    node.enableDriver(link_enum, uri)
    typer.echo(f"Driver enabled: {link} at {uri}")

@app.command()
def map(din: int, link: str, uri: str):
    """
    Map a remote node in the DaaS network.
    """
    global node
    if node is None:
        typer.echo("Node not initialized")
        raise typer.Exit(1)
    link_enum = getattr(pydaasiot.link_t, link)
    node.map(din, link_enum, uri)
    typer.echo(f"Mapped remote node DIN={din} at {uri}")

@app.command()
def perform(mode: str = typer.Option("PERFORM_CORE_THREAD", help="Execution mode")):
    """
    Start the internal processing loop.
    """
    global node
    if node is None:
        typer.echo("Node not initialized")
        raise typer.Exit(1)
    mode_enum = getattr(pydaasiot.performs_mode_t, mode)
    node.doPerform(mode_enum)
    typer.echo(f"doPerform started with mode {mode}")

@app.command()
def push(din: int, message: str):
    """
    Push a text message to a remote node.
    """
    global node
    if node is None:
        typer.echo("Node not initialized")
        raise typer.Exit(1)
    ddo = pydaasiot.DDO()
    ddo.setOrigin(din)
    ddo.setTypeset(1)
    ddo.allocatePayload(len(message))
    ddo.appendPayloadData(message.encode())
    err = node.push(din, ddo)
    typer.echo(f"Push result: {err}")

@app.command()
def pull(din: int):
    """
    Pull messages manually from a remote node.
    """
    global node
    if node is None:
        typer.echo("Node not initialized")
        raise typer.Exit(1)
    err, ddo = node.pull(din)
    if err == pydaasiot.daas_error_t.ERROR_NONE and ddo:
        typer.echo(f"Pulled data: {ddo.getPayloadAsBinary()}")
    else:
        typer.echo(f"Pull failed: {err}")

if __name__ == "__main__":
    app()
