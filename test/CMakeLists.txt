project(VorbisTest)
cmake_minimum_required(VERSION 3.0.0)
SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/..)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(testVorbis main.cpp)
target_link_libraries(testVorbis ${CONAN_LIBS})

IF(WIN32 AND NOT MINGW)
  SET_TARGET_PROPERTIES(testVorbis PROPERTIES LINK_FLAGS "/NODEFAULTLIB:\"LIBCMTD\" /NODEFAULTLIB:\"LIBCMT\"")
ENDIF()
