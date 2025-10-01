cmake_minimum_required(VERSION 3.20)
project(pydaasiot_native LANGUAGES CXX)

# Python & pybind11
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Allinea la CRT alla runtime di Python su MSVC
if (MSVC)
  set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>DLL")
endif()

# Percorsi include (globali o per-target; manteniamo semplici i globali)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/third-parties)

# Percorsi librerie (override da riga di comando se vuoi)
set(DAAS_WIN_ROOT   "${CMAKE_CURRENT_SOURCE_DIR}/lib/windows-msvc-x64" CACHE PATH "Path to Windows .lib")
set(DAAS_LINUX_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/lib/linux-gcc-x86_64" CACHE PATH "Path to Linux .a/.so")

# Normalizza eventuali backslash in input (Windows) -> sempre forward-slash
file(TO_CMAKE_PATH "${DAAS_WIN_ROOT}"   DAAS_WIN_ROOT)
file(TO_CMAKE_PATH "${DAAS_LINUX_ROOT}" DAAS_LINUX_ROOT)

# Sorgenti C++ del binding
set(SRC_CPP
  ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/pydaasiot.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/daaswrapper.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/net_utils.cpp
)

# Modulo Python nativo: verrà installato come pydaasiot/_core.* (pyd/so)
pybind11_add_module(_core MODULE ${SRC_CPP})

# Su libreria statica, abilita PIC (utile su Linux)
set_target_properties(_core PROPERTIES POSITION_INDEPENDENT_CODE ON)

# Link a lib daas
if (WIN32)
  target_link_libraries(_core PRIVATE
    $<$<CONFIG:Release>:${DAAS_WIN_ROOT}/daas.lib>
    $<$<CONFIG:Debug>:${DAAS_WIN_ROOT}/daas_Debug.lib>
    ws2_32
  )
elseif(UNIX)
  # Preferisci statica se presente
  if (EXISTS "${DAAS_LINUX_ROOT}/libdaas.a")
    target_link_libraries(_core PRIVATE ${DAAS_LINUX_ROOT}/libdaas.a)
  elseif (EXISTS "${DAAS_LINUX_ROOT}/libdaas.so")
    target_link_libraries(_core PRIVATE ${DAAS_LINUX_ROOT}/libdaas.so)
  else()
    message(FATAL_ERROR "libdaas non trovata in ${DAAS_LINUX_ROOT}")
  endif()

  # BlueZ opzionale (se disponibile)
  find_library(BLUEZ_LIB bluetooth)
  if (BLUEZ_LIB)
    target_link_libraries(_core PRIVATE ${BLUEZ_LIB})
  endif()

  # RPATH per caricare .so accanto al modulo
  set_target_properties(_core PROPERTIES
    INSTALL_RPATH "\$ORIGIN"
    BUILD_WITH_INSTALL_RPATH ON
  )
endif()

# Installa il modulo dentro il package Python
install(TARGETS _core DESTINATION pydaasiot)
