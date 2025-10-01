import tkinter as tk
from tkinter import scrolledtext, messagebox
import multiprocessing as mp
import queue as std_queue

# usa pydaasiot in un processo separato
def core_process(cmd_q: mp.Queue, evt_q: mp.Queue):
    """
    Processo separato che incapsula pydaasiot:
    - Crea DaasWrapper
    - Gestisce init/enable/map/start/stop/push
    - Gestisce gli eventi e fa pull nel core (non in GUI)
    - Invia tutto alla GUI via evt_q
    """
    try:
        import pydaasiot
        from pydaasiot import DDO, IDaasApiEvent, DaasWrapper
    except Exception as e:
        evt_q.put({"type": "fatal", "text": f"Impossibile importare pydaasiot: {e}"})
        return

    wrapper = None
    running = True

    # Handler eventi: esegue il pull QUI nel core e spedisce alla GUI
    class Handler(IDaasApiEvent):
        def __init__(self, wrapper_ref):
            super().__init__()
            self.wrapper = wrapper_ref

        def ddoReceivedEvent(self, payload_size, typeset, din_src):
            try:
                # Faccio il pull nel core, poi mando i dati alla GUI
                # [RX] = ricezione, [TX] = trasmissione
                result, ddo = self.wrapper.pull(din_src)
                if result == pydaasiot.daas_error_t.ERROR_NONE and ddo:
                    data = ddo.getPayloadAsBinary()
                    evt_q.put({"type": "rx", "din": din_src, "data": data, "typeset": typeset})
                else:
                    evt_q.put({"type": "log", "text": f"[RX] pull fallito (res={result})"})
            except Exception as e:
                evt_q.put({"type": "error", "text": f"[RX] eccezione pull: {e}"})

        def dinAcceptedEvent(self, din):
            evt_q.put({"type": "log", "text": f"[EVENT] DIN accettato: {din}"})

        def frisbeeReceivedEvent(self, din):
            pass
        def nodeStateReceivedEvent(self, din):
            pass
        def atsSyncCompleted(self, din):
            pass
        def frisbeeDperfCompleted(self, din, packets_sent, block_size):
            pass

    handler = None

    # helper sicuro per rimandare log alla GUI
    def log(txt):
        evt_q.put({"type": "log", "text": txt})

    def do_init(sid, din):
        nonlocal wrapper, handler
        try:
            handler = Handler(None)  # wrapper lo assegno dopo
            wrapper = DaasWrapper("", handler)
            handler.wrapper = wrapper
            err = wrapper.doInit(sid, din)
            if err == pydaasiot.daas_error_t.ERROR_NONE:
                log(f"doInit ok (SID={sid}, DIN={din})")
                evt_q.put({"type": "ok", "op": "init"})
            else:
                evt_q.put({"type": "error", "text": f"doInit err={err}"})
        except Exception as e:
            evt_q.put({"type": "error", "text": f"doInit exception: {e}"})

    def do_enable(link, uri):
        try:
            err = wrapper.enableDriver(link, uri)
            if err == pydaasiot.daas_error_t.ERROR_NONE:
                log(f"enableDriver {uri}")
                evt_q.put({"type": "ok", "op": "enable"})
            else:
                evt_q.put({"type": "error", "text": f"enableDriver err={err}"})
        except Exception as e:
            evt_q.put({"type": "error", "text": f"enableDriver exception: {e}"})

    def do_map(din_remote, link, uri):
        try:
            err = wrapper.map(din_remote, link, uri)
            if err == pydaasiot.daas_error_t.ERROR_NONE:
                log(f"map DIN {din_remote} -> {uri}")
                evt_q.put({"type": "ok", "op": "map"})
            else:
                evt_q.put({"type": "error", "text": f"map err={err}"})
        except Exception as e:
            evt_q.put({"type": "error", "text": f"map exception: {e}"})

    def do_start():
        try:
            err = wrapper.doPerform(pydaasiot.performs_mode_t.PERFORM_CORE_THREAD)
            if err == pydaasiot.daas_error_t.ERROR_NONE:
                log("core avviato")
                evt_q.put({"type": "ok", "op": "start"})
            else:
                evt_q.put({"type": "error", "text": f"doPerform err={err}"})
        except Exception as e:
            evt_q.put({"type": "error", "text": f"doPerform exception: {e}"})

    def do_stop():
        try:
            if wrapper:
                wrapper.doEnd()
            evt_q.put({"type": "ok", "op": "stop"})
        except Exception as e:
            evt_q.put({"type": "error", "text": f"doEnd exception: {e}"})

    def do_send(my_din, dest_din, text):
        try:
            ddo = DDO()
            ddo.setOrigin(my_din)
            ddo.setTypeset(1)
            ddo.allocatePayload(len(text))
            ddo.appendPayloadData(text.encode("utf-8"))
            err = wrapper.push(dest_din, ddo)
            if err == pydaasiot.daas_error_t.ERROR_NONE:
                evt_q.put({"type": "txok", "to": dest_din, "text": text})
            else:
                evt_q.put({"type": "error", "text": f"push err={err}"})
        except Exception as e:
            evt_q.put({"type": "error", "text": f"push exception: {e}"})

    # loop comandi
    try:
        while running:
            try:
                cmd = cmd_q.get(timeout=0.1)
            except std_queue.Empty:
                continue

            if not isinstance(cmd, dict):
                continue

            ctype = cmd.get("type")
            if ctype == "init":
                do_init(cmd["sid"], cmd["din"])
            elif ctype == "enable":
                do_enable(cmd["link"], cmd["uri"])
            elif ctype == "map":
                do_map(cmd["din_remote"], cmd["link"], cmd["uri"])
            elif ctype == "start":
                do_start()
            elif ctype == "stop":
                do_stop()
            elif ctype == "send":
                do_send(cmd["my_din"], cmd["dest_din"], cmd["text"])
            elif ctype == "shutdown":
                do_stop()
                running = False
            else:
                evt_q.put({"type": "error", "text": f"Comando sconosciuto: {ctype}"})
    except Exception as e:
        evt_q.put({"type": "fatal", "text": f"Core exception: {e}"})
    finally:
        try:
            if wrapper:
                wrapper.doEnd()
        except Exception:
            pass
        evt_q.put({"type": "exit", "code": 0})


# GUI (processo principale) 
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Nodo Bidirezionale")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # Input parametri
        tk.Label(frame, text="MIO DIN").grid(row=0, column=0, sticky="e", pady=2)
        self.din_entry = tk.Entry(frame); self.din_entry.grid(row=0, column=1, pady=2)

        tk.Label(frame, text="MIO IP").grid(row=1, column=0, sticky="e", pady=2)
        self.ip_entry = tk.Entry(frame); self.ip_entry.grid(row=1, column=1, pady=2)

        tk.Label(frame, text="MIA PORTA").grid(row=2, column=0, sticky="e", pady=2)
        self.porta_entry = tk.Entry(frame); self.porta_entry.grid(row=2, column=1, pady=2)

        tk.Label(frame, text="DIN REMOTO").grid(row=3, column=0, sticky="e", pady=2)
        self.din_remoto_entry = tk.Entry(frame); self.din_remoto_entry.grid(row=3, column=1, pady=2)

        tk.Label(frame, text="IP REMOTO").grid(row=4, column=0, sticky="e", pady=2)
        self.ip_remoto_entry = tk.Entry(frame); self.ip_remoto_entry.grid(row=4, column=1, pady=2)

        tk.Label(frame, text="PORTA REMOTA").grid(row=5, column=0, sticky="e", pady=2)
        self.porta_remoto_entry = tk.Entry(frame); self.porta_remoto_entry.grid(row=5, column=1, pady=2)

        # Pulsanti
        btn_frame = tk.Frame(frame, pady=5); btn_frame.grid(row=6, column=0, columnspan=2)
        self.start_btn = tk.Button(btn_frame, text="Avvia Nodo", command=self.start_nodo, width=15)
        self.start_btn.pack(side="left", padx=5)
        self.stop_btn = tk.Button(btn_frame, text="Ferma Nodo", command=self.stop_nodo, width=15)
        self.stop_btn.pack(side="left", padx=5)

        # Log
        self.log_area = scrolledtext.ScrolledText(frame, width=80, height=18, bg="black", fg="lime", font=("Consolas", 10))
        self.log_area.grid(row=7, column=0, columnspan=2, pady=10)

        # Invio messaggi
        msg_frame = tk.Frame(frame); msg_frame.grid(row=8, column=0, columnspan=2, pady=5)
        self.msg_entry = tk.Entry(msg_frame, width=60); self.msg_entry.pack(side="left", padx=5)
        self.msg_entry.bind("<Return>", lambda e: self.invia_msg())
        self.send_btn = tk.Button(msg_frame, text="Invia", command=self.invia_msg, width=10)
        self.send_btn.pack(side="left")

        # IPC
        self.core_proc = None
        self.cmd_q = None
        self.evt_q = None

        # Polling eventi
        self.root.after(100, self.poll_events)

    def log(self, text):
        self.log_area.insert(tk.END, text + "\n")
        self.log_area.see(tk.END)

    def ensure_core(self):
        if self.core_proc and self.core_proc.is_alive():
            return True
        # (ri)crea core
        self.cmd_q = mp.Queue()
        self.evt_q = mp.Queue()
        self.core_proc = mp.Process(target=core_process, args=(self.cmd_q, self.evt_q), daemon=True)
        self.core_proc.start()
        self.log("Core avviato in processo separato")
        return True

    def start_nodo(self):
        try:
            self.ensure_core()
            sid = 100
            my_din = int(self.din_entry.get())
            my_uri = f"{self.ip_entry.get()}:{int(self.porta_entry.get())}"
            remote_din = int(self.din_remoto_entry.get())
            remote_uri = f"{self.ip_remoto_entry.get()}:{int(self.porta_remoto_entry.get())}"

            # Init
            self.cmd_q.put({"type": "init", "sid": sid, "din": my_din})
            # Enable
            import pydaasiot
            self.cmd_q.put({"type": "enable", "link": pydaasiot.link_t._LINK_INET4, "uri": my_uri})
            # Map
            self.cmd_q.put({"type": "map", "din_remote": remote_din, "link": pydaasiot.link_t._LINK_INET4, "uri": remote_uri})
            # Start
            self.cmd_q.put({"type": "start"})

            self.log("Avvio nodo in corso...")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def stop_nodo(self):
        try:
            if self.cmd_q:
                self.cmd_q.put({"type": "stop"})
                self.cmd_q.put({"type": "shutdown"})
            self.log("Richiesta stop inviata")
        except Exception as e:
            self.log(f"Errore stop: {e}")

    def invia_msg(self):
        if not (self.core_proc and self.core_proc.is_alive()):
            messagebox.showwarning("Attenzione", "Core non attivo")
            return
        try:
            text = self.msg_entry.get().strip()
            if not text:
                return
            my_din = int(self.din_entry.get())
            dest_din = int(self.din_remoto_entry.get())
            self.cmd_q.put({"type": "send", "my_din": my_din, "dest_din": dest_din, "text": text})
            self.msg_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def poll_events(self):
        # controlla core vivo
        if self.core_proc and not self.core_proc.is_alive():
            self.log(" Il core si è arrestato (processo terminato)")
            self.core_proc = None

        if self.evt_q:
            try:
                while True:
                    evt = self.evt_q.get_nowait()
                    et = evt.get("type")
                    if et == "log":
                        self.log(evt.get("text", ""))
                    elif et == "ok":
                        self.log(f"[OK] {evt.get('op')}")
                    elif et == "error":
                        self.log(f" {evt.get('text')}")
                    elif et == "fatal":
                        self.log(f"FATALE: {evt.get('text')}")
                    elif et == "rx":
                        data = evt.get("data", b"")
                        try:
                            msg = data.decode("utf-8")
                        except Exception:
                            msg = str(data)
                        self.log(f"[RX] da {evt.get('din')} : {msg}")
                    elif et == "txok":
                        self.log(f"[TX] a {evt.get('to')} : {evt.get('text')}")
                    elif et == "exit":
                        self.log("Core ha segnalato uscita")
            except std_queue.Empty:
                pass

        self.root.after(150, self.poll_events)


if __name__ == "__main__":
    # Su alcune piattaforme è più sicuro usare 'spawn'
    try:
        mp.set_start_method("spawn")
    except RuntimeError:
        pass

    root = tk.Tk()
    app = App(root)
    root.mainloop()
