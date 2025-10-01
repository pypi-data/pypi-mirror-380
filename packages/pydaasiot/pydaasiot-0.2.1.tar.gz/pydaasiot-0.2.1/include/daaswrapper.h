// daasiot/include/daas_wrapper.h
#ifndef DAAS_WRAPPER_H
#define DAAS_WRAPPER_H
#include "daas.hpp"
#include "daas_types.hpp"
#include <string>
#include <unordered_map>
#include <vector>
/**
 * @file daas_wrapper.h
 * @brief Wrapper per l'SDK DaaS-IoT su piattaforma Linux.
 *
 * Questa classe fornisce un'interfaccia semplificata per interagire con la libreria
 * nativa `libdaas.a`, nascondendo i dettagli di basso livello e gestendo configurazioni multiple.
 * 
 * 
 *
 * © 2025 Sebyone Srl. Tutti i diritti riservati.
 */
namespace daas {
namespace api {

/**
 * @struct DriverConfig
 * @brief Rappresenta la configurazione di un driver DaaS.
 */
struct DriverConfig {

  link_t link;
  std::string uri;
};

struct InterfaceInfo {
  std::string name;
  std::string type;
  std::string status;
};

/**
 * @class DaasWrapper
 * @brief Classe wrapper che incapsula la logica di utilizzo della libreria libdaas.a
 *
 * Utilizza DaasAPI internamente per esporre metodi ad alto livello per l'inizializzazione,
 * la configurazione dei driver e l'invio/ricezione di messaggi.
 */
class DaasWrapper {
private:
    DaasAPI *daasInstance;
    IDaasApiEvent *eventHandler;
    //Wrapper private
    char infoBuffer[256];
    std::unordered_map<std::string,std::string> configCache;
    /**
 * @brief Cache dei driver abilitati letti da file di configurazione.
 */
    std::vector<DriverConfig> driversCache;

public:
/**
     * @brief Costruttore
     * @param config Percorso file di configurazione (opzionale)
     * @param eventHandler Handler personalizzato per eventi DaaS
     */
    DaasWrapper(const char *config, IDaasApiEvent *eventHandler);
    ~DaasWrapper();

    std::vector<std::string> getActiveInterfaces();
    
    std::vector<InterfaceInfo> listSystemInterfaces();
    /**
     * @brief Inizializza il nodo DaaS con SID e DIN
     * @param sid System Identifier (es. identificativo rete)
     * @param din DaaS IDentifier (identificativo del nodo)
     * @return Codice errore daas_error_t
     */
    daas_error_t doInit(din_t sid, din_t din);
    
    /**
     * @brief Attiva l'esecuzione interna del nodo
     * @param mode Modalità (es. PERFORM_CORE_THREAD)
     * @return Codice errore daas_error_t
     */
    daas_error_t doPerform(performs_mode_t mode);
    
    /**
     * @brief Termina le attività del nodo
     * @return Codice errore daas_error_t
     */
    daas_error_t doEnd();
    /**
     * @brief Resetta lo stato del nodo
     * @return Codice errore daas_error_t
     */
    daas_error_t doReset();
    /**
     * @brief Restituisce la versione della libreria libdaas.a
     * @return Stringa con versione (es. "0.20.1")
     */
    const char *getVersion();
    
    const char *listAvailableDrivers();           // Returns drivers list: 2.INET4;3.UART
    
    nodestate_t getStatus(); // returns local node's instance status
    
    const nodestate_t& status(din_t din);
    
    const nodestate_t& fetch(din_t din, uint16_t opts);
    
    dinlist_t listNodes();
    /**
     * @brief Salva la configurazione corrente usando un'interfaccia IDepot
     * @param storage_interface Puntatore a oggetto IDepot
     * @return true se il salvataggio ha avuto successo
     */
    bool storeConfiguration(IDepot* storage_interface);
    
    /**
     * @brief Carica la configurazione usando un'interfaccia IDepot
     * @param storage_interface Puntatore a oggetto IDepot
     * @return true se il caricamento ha avuto successo
     */
    bool loadConfiguration(IDepot* storage_interface);
    
    /**
     * @brief Abilita un driver su uno specifico link
     * @param link Tipo di interfaccia (es. LINK_INET4)
     * @param driver URI da usare (es. "127.0.0.1:3000")
     * @return Codice errore daas_error_t
     */
    daas_error_t enableDriver(link_t link, const char *driver);
    
    /**
     * @brief Mappa un nodo con DIN noto nella rete (formato base)
     * @param din DIN nodo remoto
     * @return Codice errore
     */
    daas_error_t map(din_t din);
    
    /**
     * @brief Mappa un nodo specificando link e URI
     * @param din DIN nodo remoto
     * @param link Tipo di interfaccia
     * @param uri Interfaccia/indirizzo remoto
     * @return Codice errore
     */
    daas_error_t map(din_t din, link_t link, const char *uri);
    
    /**
     * @brief Mappa un nodo con chiave di sicurezza
     * @param din DIN remoto
     * @param link Tipo di interfaccia
     * @param uri Indirizzo remoto
     * @param securityKey Chiave di sicurezza (es. AES)
     * @return Codice errore
     */
    daas_error_t map(din_t din, link_t link, const char *uri, const char *securityKey);


    /**
     * @brief Rimuove un nodo precedentemente mappato
     * @param din DIN nodo remoto da eliminare
     * @return Codice errore
     */    
    daas_error_t remove(din_t din);
    
     /**
     * @brief Localizza un nodo in rete
     * @param din DIN nodo remoto da cercare
     * @return Codice errore
     */
    daas_error_t locate(din_t din);
    
    /**
     * @brief Restituisce il numero di pacchetti disponibili da ricevere
     * @param din DIN nodo da interrogare
     * @param count Numero di pacchetti in attesa
     * @return Codice errore
     */
    daas_error_t availablesPull(din_t din, uint32_t &count);
    
    /**
     * @brief Riceve un pacchetto DDO dal nodo remoto
     * @param din DIN mittente
     * @param inboundDDO Puntatore al DDO ricevuto
     * @return Codice errore
     */
    daas_error_t pull(din_t din, DDO **inboundDDO);
    
    /**
     * @brief Invia un pacchetto DDO al nodo remoto
     * @param din DIN destinatario
     * @param outboundDDO Puntatore al DDO da inviare
     * @return Codice errore
     */
    daas_error_t push(din_t din, DDO *outboundDDO);
    
    /**
     * @brief Esegue un invio rapido (fire-and-forget)
     * @param din DIN destinatario
     * @return Codice errore
     */
    daas_error_t frisbee(din_t din);


    /**
     * @brief Imposta un nuovo handler eventi
     * @param event Nuovo handler da usare
     */
    void setEventHandler(IDaasApiEvent* event);
    //Wrapper method
    const char *getInfos(); 
    daas_error_t setupNode(din_t sid, din_t din, link_t link, const char* uri);
    /**
     * @brief Carica e configura un nodo da file JSON
     * @param configFilePath Percorso al file JSON
     * @return Codice errore daas_error_t
     */
    daas_error_t setupNode (const char* setupFilePath); //JSON

};

} // namespace api
} // namespace daas

#endif // DAAS_WRAPPER_H
