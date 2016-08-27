find_path(VORBIS_INCLUDE_DIR NAMES vorbis PATHS include)
find_library(VORBIS_LIBRARY NAMES vorbis vorbis_static libvorbis libvorbis_static PATHS lib )
find_library(VORBISFILE_LIBRARY NAMES vorbisfile vorbisfile_static libvorbisfile libvorbisfile_static PATHS lib )

MESSAGE("** VORBIS FOUND BY CONAN")
SET(VORBIS_FOUND TRUE)
MESSAGE("** FOUND VORBIS:  ${VORBIS_LIBRARY}")
MESSAGE("** FOUND VORBISFILE:  ${VORBISFILE_LIBRARY}")
MESSAGE("** FOUND VORBIS INCLUDE:  ${VORBIS_INCLUDE_DIR}")

set(VORBIS_INCLUDE_DIRS ${VORBIS_INCLUDE_DIR})
set(VORBIS_LIBRARIES ${VORBIS_LIBRARY} ${VORBISFILE_LIBRARY})

mark_as_advanced(VORBIS_LIBRARY VORBISFILE_LIBRARY VORBIS_INCLUDE_DIR)

set(VORBIS_MAJOR_VERSION "1")
set(VORBIS_MINOR_VERSION "3")
set(VORBIS_PATCH_VERSION "5")
