cmake_minimum_required(VERSION 3.15)
project(SIDLL LANGUAGES CXX)

# --- C++ Standard ---
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# --- Library Definition ---

#add_library(sidll MODULE
#	SIDLL.cpp
#)

find_package(pybind11 REQUIRED)
pybind11_add_module(sidll pySIDLL.cpp SIDLL.cpp)
#add_subdirectory(external/pybind11)

# --- Python Integration ---
# Find the interpreter first to get its exact version.
# scikit-build-core ensures this finds the Python that's running the build.

find_package(Python3 COMPONENTS Interpreter Development)

# Now, perform an EXACT search for the development components of that specific version.
# This is more robust in complex environments like manylinux containers.
#find_package(Python3 ${Python3_VERSION} EXACT REQUIRED COMPONENTS Development)

# Use the modern "Python::Module" target for linking. This automatically handles
# include directories, library paths, and other flags correctly.
# This single line replaces the old target_include_directories and target_link_libraries calls.
#target_link_libraries(sidll PRIVATE pybind11::Module)

# --- Platform-Specific Compiler and Linker Options ---
if(MSVC)
    # --- Windows (MSVC) Specific Configuration ---

    # Set the generator platform to x64 for Visual Studio.
    # This setting is specific to the MSVC generator and has no effect on Linux.
    #set(CMAKE_GENERATOR_PLATFORM x64)
	if (CMAKE_GENERATOR MATCHES "Visual Studio")
        set(CMAKE_GENERATOR_PLATFORM x64)
    endif()

    # Set C++ exception handling model and MSVC runtime library.
    target_compile_options(sidll PRIVATE /EHsc)
    set_property(TARGET sidll PROPERTY MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:DebugDLL>")

    # Add specific architecture optimization flags (e.g., AVX2 support for MSVC)
    target_compile_options(sidll PRIVATE /arch:AVX2)
else()
    # --- Linux (GCC/Clang) & macOS Specific Configuration ---

    # -fPIC (Position-Independent Code) is REQUIRED for shared libraries on Linux/macOS.
    target_compile_options(sidll PRIVATE -fPIC)

    # Optional: Add common optimization and warning flags for release builds.
    target_compile_options(sidll PRIVATE $<$<CONFIG:Release>:-O3 -DNDEBUG>)
    target_compile_options(sidll PRIVATE $<$<CONFIG:Debug>:-g>) # Add debug symbols for debug builds
    target_compile_options(sidll PRIVATE -Wall -Wextra) # Recommended warning flags

    # Optional: Add the equivalent architecture optimization for GCC/Clang
    target_compile_options(sidll PRIVATE -mavx2)
endif()

# --- Output Properties for Python Module ---
# Ensure the output file has the proper extension and no "lib" prefix.
set_target_properties(sidll PROPERTIES PREFIX "")
if(WIN32)
    set_target_properties(sidll PROPERTIES SUFFIX ".pyd")
else()
    # On Linux and macOS, Python extension modules are ".so" (shared object) files.
    set_target_properties(sidll PROPERTIES SUFFIX ".so")
endif()

# --- Installation ---
# This command is used by scikit-build and cibuildwheel.
install(TARGETS sidll
    LIBRARY DESTINATION .
    RUNTIME DESTINATION .
    ARCHIVE DESTINATION .
)

# --- Debugging Information ---
# This section works on all platforms and helps diagnose configuration issues.
# (You can remove this for cleaner output once your build is stable)
message(STATUS "--- CMake Configuration for SIDLL ---")
message(STATUS "CMAKE_SYSTEM_NAME: ${CMAKE_SYSTEM_NAME}")
message(STATUS "CMAKE_CXX_COMPILER_ID: ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
message(STATUS "Python3_LIBRARIES: ${Python3_LIBRARIES}")
message(STATUS "--- End CMake Configuration for SIDLL ---")