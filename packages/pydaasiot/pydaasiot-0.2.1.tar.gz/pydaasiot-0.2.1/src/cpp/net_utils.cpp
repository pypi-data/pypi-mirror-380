/*#include "net_utils.h"
#include <ifaddrs.h>
#include <net/if.h>
#include <string.h>
#include <algorithm>
#include "daaswrapper.h"


std::vector<std::string> listSystemNetworkInterfaces() {
    std::vector<std::string> interfaces;
    struct ifaddrs *ifaddr, *ifa;

    if (getifaddrs(&ifaddr) == -1) {
        return interfaces;  // Vuoto se errore
    }

    for (ifa = ifaddr; ifa != nullptr; ifa = ifa->ifa_next) {
        if (ifa->ifa_name && (ifa->ifa_flags & IFF_UP)) {
            std::string name(ifa->ifa_name);
            if (std::find(interfaces.begin(), interfaces.end(), name) == interfaces.end()) {
                interfaces.push_back(name);
            }
        }
    }

    freeifaddrs(ifaddr);
    return interfaces;
}*/
