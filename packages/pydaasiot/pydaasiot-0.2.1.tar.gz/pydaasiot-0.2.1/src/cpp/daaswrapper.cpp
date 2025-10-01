#include "daaswrapper.h"
#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
// #include <ifaddrs.h>
// #include <net/if.h>
// #include <sys/types.h>
// #include <dirent.h>
// #include <sys/stat.h>
// #include <unistd.h>
#include <regex>
#include <vector>
#include <string>
#include "net_utils.h"
#include <set>
#include <sstream>
#include <algorithm>
using json = nlohmann::json;

#define NODE_LHVER "GNUSDK"

namespace daas {
namespace api {

DaasWrapper::DaasWrapper(const char* configPath, IDaasApiEvent* handler)
    : eventHandler(handler)
{
    daasInstance = new DaasAPI(handler, NODE_LHVER);
}

DaasWrapper::~DaasWrapper() {
    // cleanup
}

// ------------------------------------
// LIST SYSTEM INTERFACES (Linux-only)
// ------------------------------------
std::vector<InterfaceInfo> DaasWrapper::listSystemInterfaces() {
    std::vector<InterfaceInfo> interfaces;
    // TODO: implementare versione Windows
    // Codice Linux originale rimosso/commentato per evitare errori di compilazione.
    return interfaces;
}

// ------------------------------------

std::vector<std::string> DaasWrapper::getActiveInterfaces() {
    // net_utils.cpp è stato commentato, quindi ritorniamo vuoto
    return {};
}

const char* DaasWrapper::listAvailableDrivers() {
    return daasInstance->listAvailableDrivers();
}

nodestate_t DaasWrapper::getStatus() {
    return daasInstance->getStatus();
}

const nodestate_t& DaasWrapper::status(din_t din) {
    return daasInstance->status(din);
}

const nodestate_t& DaasWrapper::fetch(din_t din, uint16_t opts) {
    return daasInstance->fetch(din, opts);
}

dinlist_t DaasWrapper::listNodes() {
    return daasInstance->listNodes();
}

bool DaasWrapper::storeConfiguration(IDepot* storage_interface) {
    return daasInstance->storeConfiguration(storage_interface);
}

bool DaasWrapper::loadConfiguration(IDepot* storage_interface) {
    return daasInstance->loadConfiguration(storage_interface);
}

daas_error_t DaasWrapper::doInit(din_t sid, din_t din) {
    return daasInstance->doInit(sid, din);
}

daas_error_t DaasWrapper::doPerform(performs_mode_t mode) {
    return daasInstance->doPerform(mode);
}

daas_error_t DaasWrapper::doEnd() {
    return daasInstance->doEnd();
}

daas_error_t DaasWrapper::doReset() {
    return daasInstance->doReset();
}

const char* DaasWrapper::getVersion() {
    return daasInstance->getVersion();
}

const char* DaasWrapper::getInfos() {
    const char *version = daasInstance->getVersion();
    const char *build = daasInstance->getBuildInfo();

    if (!version) version = "UNKNOWN";
    if (!build) build = "UNKNOWN";

    snprintf(infoBuffer, sizeof(infoBuffer),
             "Version: %s | Build: %s", version, build);
    return infoBuffer;
}

daas_error_t DaasWrapper::enableDriver(link_t link, const char* driver) {
    return daasInstance->enableDriver(link, driver);
}

daas_error_t DaasWrapper::setupNode(din_t sid, din_t din, link_t link, const char *uri) {
    daas_error_t err;
    err = doInit(sid, din);
    if (err != ERROR_NONE) return err;
    err = enableDriver(link, uri);
    if (err != ERROR_NONE) return err;

    return ERROR_NONE;
}

daas_error_t DaasWrapper::setupNode(const char* configFilePath) {
    std::ifstream file(configFilePath);
    if (!file.is_open()) return ERROR_UNKNOWN;

    json config;
    file >> config;

    // Cache SID e DIN
    din_t sid = static_cast<din_t>(config["sid"].get<int>());
    din_t din = static_cast<din_t>(config["din"].get<int>());
    configCache["sid"] = std::to_string(sid);
    configCache["din"] = std::to_string(din);

    // Pulisce eventuali vecchi driver
    driversCache.clear();

    // Legge array di driver
    for (const auto& drv : config["drivers"]) {
        link_t link = static_cast<link_t>(drv["link"].get<int>());
        std::string uri = drv["uri"].get<std::string>();
        driversCache.push_back(DriverConfig{link, uri});
    }

    // Inizializza il nodo
    daas_error_t err = doInit(sid, din);
    if (err != ERROR_NONE) return err;

    // Attiva tutti i driver letti da file
    for (const auto& drv : driversCache) {
        err = enableDriver(drv.link, drv.uri.c_str());
        if (err != ERROR_NONE) return err;
    }

    return ERROR_NONE;
}

daas_error_t DaasWrapper::map(din_t din) {
    return daasInstance->map(din);
}

daas_error_t DaasWrapper::map(din_t din, link_t link, const char* uri) {
    return daasInstance->map(din, link, uri);
}

daas_error_t DaasWrapper::map(din_t din, link_t link, const char* uri, const char* securityKey) {
    return daasInstance->map(din, link, uri, securityKey);
}

daas_error_t DaasWrapper::remove(din_t din) {
    return daasInstance->remove(din);
}

daas_error_t DaasWrapper::locate(din_t din) {
    return daasInstance->locate(din);
}

daas_error_t DaasWrapper::availablesPull(din_t din, uint32_t &count) {
    return daasInstance->availablesPull(din, count);
}

daas_error_t DaasWrapper::pull(din_t din, DDO** inboundDDO) {
    return daasInstance->pull(din, inboundDDO);
}

daas_error_t DaasWrapper::push(din_t din, DDO *outboundDDO) {
    return daasInstance->push(din, outboundDDO);
}

daas_error_t DaasWrapper::frisbee(din_t din) {
    return daasInstance->frisbee(din);
}

void DaasWrapper::setEventHandler(IDaasApiEvent* handler) {
    this->eventHandler = handler;
}

} // namespace api
} // namespace daas
