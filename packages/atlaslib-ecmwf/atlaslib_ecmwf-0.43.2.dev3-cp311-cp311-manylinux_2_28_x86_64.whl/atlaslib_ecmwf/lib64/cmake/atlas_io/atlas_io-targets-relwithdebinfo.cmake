#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "atlas_io" for configuration "RelWithDebInfo"
set_property(TARGET atlas_io APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(atlas_io PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib64/libatlas_io.so"
  IMPORTED_SONAME_RELWITHDEBINFO "libatlas_io.so"
  )

list(APPEND _cmake_import_check_targets atlas_io )
list(APPEND _cmake_import_check_files_for_atlas_io "${_IMPORT_PREFIX}/lib64/libatlas_io.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
