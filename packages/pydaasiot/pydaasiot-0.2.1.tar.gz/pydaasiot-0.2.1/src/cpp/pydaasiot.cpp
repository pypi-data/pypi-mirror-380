/**
 * @file pydaasiot_bindings.cpp
 * @brief Python bindings for the DaaS-IoT SDK (libdaas.a) using pybind11.
 *
 * This module exposes the main components of the DaaS system to Python, including:
 * - The DDO class (data packets for communication)
 * - The IDaasApiEvent interface for asynchronous event handling
 * - The DaasWrapper class as the main API access point
 *
 * These bindings allow integration of DaaS node logic into Python-based applications.
 *
 * @author Sebyone
 * @date 2025
 */

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>      // buffer protocol / numpy
#include "daaswrapper.h"         // includes daas.hpp -> daas_types.hpp

namespace py = pybind11;
using namespace daas::api;

/**
 * @class PyIDaasApiEvent
 * @brief Trampoline class to forward asynchronous events from libdaas to Python.
 */
class PyIDaasApiEvent : public IDaasApiEvent {
public:
    using IDaasApiEvent::IDaasApiEvent;

    void dinAcceptedEvent(din_t din) override {
        PYBIND11_OVERRIDE_PURE(void, IDaasApiEvent, dinAcceptedEvent, din);
    }
    void ddoReceivedEvent(int payload_size, typeset_t t, din_t din) override {
        PYBIND11_OVERRIDE_PURE(void, IDaasApiEvent, ddoReceivedEvent, payload_size, t, din);
    }
    void frisbeeReceivedEvent(din_t din) override {
        PYBIND11_OVERRIDE_PURE(void, IDaasApiEvent, frisbeeReceivedEvent, din);
    }
    void nodeStateReceivedEvent(din_t din) override {
        PYBIND11_OVERRIDE_PURE(void, IDaasApiEvent, nodeStateReceivedEvent, din);
    }
    void atsSyncCompleted(din_t din) override {
        PYBIND11_OVERRIDE_PURE(void, IDaasApiEvent, atsSyncCompleted, din);
    }
    void frisbeeDperfCompleted(din_t din, uint32_t packets_sent, uint32_t block_size) override {
        PYBIND11_OVERRIDE_PURE(void, IDaasApiEvent, frisbeeDperfCompleted, din, packets_sent, block_size);
    }
};

/**
 * @brief Python module exposing libdaas (DaaS-IoT SDK) to Python.
 */
PYBIND11_MODULE(_core, m) {
    m.doc() = "Python bindings for libdaas.a (DaaS-IoT SDK)";

    // ---------------- Enums ----------------
    py::enum_<daas_error_t>(m, "daas_error_t")
        .value("ERROR_NONE", ERROR_NONE)
        .value("ERROR_CORE_ALREADY_INITIALIZED", ERROR_CORE_ALREADY_INITIALIZED)
        .value("ERROR_CORE_STOPPED", ERROR_CORE_STOPPED)
        .value("ERROR_CANNOT_INITIALIZE", ERROR_CANNOT_INITIALIZE)
        .value("ERROR_CANNOT_CREATE_NODE", ERROR_CANNOT_CREATE_NODE)
        .value("ERROR_DIN_ALREADY_EXIST", ERROR_DIN_ALREADY_EXIST)
        .value("ERROR_CANNOT_MAP_NODE", ERROR_CANNOT_MAP_NODE)
        .value("ERROR_INVALID_USER_TYPESET", ERROR_INVALID_USER_TYPESET)
        .value("ERROR_SEND_DDO", ERROR_SEND_DDO)
        .value("ERROR_NO_DDO_PRESENT", ERROR_NO_DDO_PRESENT)
        .value("ERROR_DIN_UNKNOWN", ERROR_DIN_UNKNOWN)
        .value("ERROR_CHANNEL_FAILURE", ERROR_CHANNEL_FAILURE)
        .value("ERROR_ATS_NOT_SYNCED", ERROR_ATS_NOT_SYNCED)
        .value("ERROR_INVALID_DME", ERROR_INVALID_DME)
        .value("ERROR_THREADS_ALREADY_STARTED", ERROR_THREADS_ALREADY_STARTED)
        .value("ERROR_NOT_IMPLEMENTED", ERROR_NOT_IMPLEMENTED)
        .value("ERROR_UNKNOWN", ERROR_UNKNOWN)
        .export_values();

    py::enum_<link_t>(m, "link_t")
        .value("_LINK_NONE", _LINK_NONE)
        .value("_LINK_DAAS", _LINK_DAAS)
        .value("_LINK_INET4", _LINK_INET4)
        .value("_LINK_BT", _LINK_BT)
        .value("_LINK_MQTT5", _LINK_MQTT5)
        .value("_LINK_UART", _LINK_UART)
        .export_values();

    py::enum_<performs_mode_t>(m, "performs_mode_t")
        .value("PERFORM_CORE_THREAD", PERFORM_CORE_THREAD)
        .value("PERFORM_CORE_NO_THREAD", PERFORM_CORE_NO_THREAD)
        .export_values();

    // ---------------- DDO ----------------
    py::class_<DDO>(m, "DDO")
        .def(py::init<>(), "Default constructor")
        .def(py::init<typeset_t>(), "Constructor with a typeset")
        .def(py::init<typeset_t, stime_t>(), "Constructor with typeset and timestamp")

        .def("clearPayload", &DDO::clearPayload, "Clear the payload buffer")
        .def("setOrigin", &DDO::setOrigin, "Set the origin device ID")
        .def("setTypeset", &DDO::setTypeset, "Set the typeset field")
        .def("setTimestamp", &DDO::setTimestamp, "Set the timestamp value")

        .def("getOrigin", &DDO::getOrigin, "Get the origin device ID")
        .def("getTypeset", &DDO::getTypeset, "Get the typeset")
        .def("getTimestamp", &DDO::getTimestamp, "Get the timestamp")

        .def("allocatePayload", &DDO::allocatePayload, "Allocate a payload buffer")

        // appendPayloadData: bytes/bytearray
        .def("appendPayloadData",
             [](DDO &self, py::bytes data) {
                 std::string buffer = data; // copy from Python bytes
                 return self.appendPayloadData(buffer.data(), static_cast<uint32_t>(buffer.size()));
             },
             "Append binary data (bytes/bytearray) to the payload")

        // appendPayloadData: buffer protocol (memoryview / numpy 1-D)
        .def("appendPayloadData",
             [](DDO &self, py::buffer b) {
                 py::buffer_info info = b.request();
                 if (info.ndim != 1) {
                     throw py::value_error("appendPayloadData expects a 1-D contiguous buffer");
                 }
                 const uint32_t nbytes = static_cast<uint32_t>(info.size * info.itemsize);
                 return self.appendPayloadData(info.ptr, nbytes);
             },
             "Append data from a 1-D buffer (memoryview/numpy) to the payload")

        // setPayload: bytes/bytearray
        .def("setPayload",
             [](DDO &self, py::bytes data) {
                 std::string buffer = data; // copy from Python bytes
                 return self.setPayload(buffer.data(), static_cast<uint32_t>(buffer.size()));
             },
             py::arg("data"),
             "Set the payload from Python bytes/bytearray (overwrites existing payload)")

        // setPayload: buffer protocol (memoryview / numpy 1-D)
        .def("setPayload",
             [](DDO &self, py::buffer b) {
                 py::buffer_info info = b.request();
                 if (info.ndim != 1) {
                     throw py::value_error("setPayload expects a 1-D contiguous buffer");
                 }
                 const uint32_t nbytes = static_cast<uint32_t>(info.size * info.itemsize);
                 return self.setPayload(info.ptr, nbytes);
             },
             py::arg("data"),
             "Set the payload from a 1-D buffer (memoryview/numpy), overwriting any existing payload")

        .def("getPayloadSize", &DDO::getPayloadSize, "Return the payload size in bytes")

        .def("getPayloadAsBinary",
             [](DDO &self) {
                 uint32_t size = self.getPayloadSize();
                 std::vector<uint8_t> buf(size);
                 if (size) {
                     self.getPayloadAsBinary(buf.data(), 0, size);
                 }
                 return py::bytes(reinterpret_cast<char*>(buf.data()), size);
             },
             "Return the payload as a Python bytes object");

    // ---------------- IDaasApiEvent ----------------
    py::class_<IDaasApiEvent, PyIDaasApiEvent>(m, "IDaasApiEvent")
        .def(py::init<>(), "Base class for DaaS event handlers");

    // ---------------- DaasWrapper ----------------
    py::class_<DaasWrapper>(m, "DaasWrapper")
        .def(py::init([]() {
            return new DaasWrapper(nullptr, nullptr);
        }), "Default constructor with no configuration and no event handler")

        .def(py::init<const char*, IDaasApiEvent*>(),
             py::arg("config") = nullptr,
             py::arg("eventHandler") = nullptr,
             "Construct a DaaS wrapper with configuration and optional event handler")

        .def("doInit", &DaasWrapper::doInit, py::arg("sid"), py::arg("din"),
             "Initialize the DaaS node with SID and DIN")

        .def("doPerform", &DaasWrapper::doPerform, py::arg("mode"),
             "Start internal execution loop")

        .def("doEnd", &DaasWrapper::doEnd, "Terminate node activities")
        .def("doReset", &DaasWrapper::doReset, "Reset the node")

        .def("getVersion", &DaasWrapper::getVersion, "Return the library version")
        .def("getInfos", &DaasWrapper::getInfos, "Return version and build information")

        .def("listAvailableDrivers", &DaasWrapper::listAvailableDrivers, "List available drivers")

        .def("enableDriver", &DaasWrapper::enableDriver,
             py::arg("link"), py::arg("driver"),
             "Enable a driver on this node")

        .def("setupNode",
             py::overload_cast<din_t, din_t, link_t, const char*>(&DaasWrapper::setupNode),
             py::arg("sid"), py::arg("din"), py::arg("link"), py::arg("uri"),
             "Configure and start a node (direct parameters)")

        .def("setupNode",
             py::overload_cast<const char*>(&DaasWrapper::setupNode),
             py::arg("configFilePath"),
             "Configure and start a node using a JSON config file")

        .def("getStatus", &DaasWrapper::getStatus, "Return local node status")
        .def("status", &DaasWrapper::status, py::arg("din"), "Return status of a remote node")
        .def("fetch", &DaasWrapper::fetch, py::arg("din"), py::arg("opts"),
             "Fetch state from a remote node")
        .def("listNodes", &DaasWrapper::listNodes, "List known nodes")

        .def("storeConfiguration", &DaasWrapper::storeConfiguration, py::arg("storage_interface"),
             "Store configuration (requires C++ IDepot)")
        .def("loadConfiguration", &DaasWrapper::loadConfiguration, py::arg("storage_interface"),
             "Load configuration (requires C++ IDepot)")

        .def("map", py::overload_cast<din_t>(&DaasWrapper::map), py::arg("din"),
             "Map a known node")
        .def("map", py::overload_cast<din_t, link_t, const char*>(&DaasWrapper::map),
             py::arg("din"), py::arg("link"), py::arg("uri"),
             "Map a node with link and URI")
        .def("map", py::overload_cast<din_t, link_t, const char*, const char*>(&DaasWrapper::map),
             py::arg("din"), py::arg("link"), py::arg("uri"), py::arg("securityKey"),
             "Map a node with link, URI and security key")

        .def("remove", &DaasWrapper::remove, py::arg("din"), "Remove a mapped node")
        .def("locate", &DaasWrapper::locate, py::arg("din"), "Locate a node in the network")

        .def("availablesPull", &DaasWrapper::availablesPull,
             py::arg("din"), py::arg("count"),
             "Return the number of available packets from a remote node")

        .def("pull",
             [](DaasWrapper &self, din_t din) {
                 DDO* ddo_ptr = nullptr;
                 daas_error_t err = self.pull(din, &ddo_ptr);
                 if (err != ERROR_NONE || ddo_ptr == nullptr) {
                     return py::make_tuple(err, py::none());
                 }
                 return py::make_tuple(err, ddo_ptr);
             },
             py::arg("din"),
             "Pull a DDO from a remote node; returns (err, ddo)")

        .def("push",
             [](DaasWrapper &self, din_t din, DDO* outboundDDO) {
                 return self.push(din, outboundDDO);
             },
             py::arg("din"), py::arg("outboundDDO"),
             "Push a DDO to a remote node")

        .def("frisbee", &DaasWrapper::frisbee, py::arg("din"),
             "Send a frisbee ping to a node")

        .def("getActiveInterfaces", &DaasWrapper::getActiveInterfaces,
             "Get active network interfaces")

        .def("listSystemInterfaces", &DaasWrapper::listSystemInterfaces,
             "List all network interfaces on the system");
}
