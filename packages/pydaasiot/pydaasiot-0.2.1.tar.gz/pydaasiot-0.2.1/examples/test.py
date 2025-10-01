import pydaasiot

# Istanzia il wrapper (senza eventi, per ora)
wrapper = pydaasiot.DaasWrapper()

print("Libreria caricata correttamente.")
v = wrapper.getVersion()
print("Versione: ",v)


