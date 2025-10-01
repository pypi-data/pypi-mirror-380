#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "odccore" for configuration "RelWithDebInfo"
set_property(TARGET odccore APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(odccore PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib64/libodccore.so"
  IMPORTED_SONAME_RELWITHDEBINFO "libodccore.so"
  )

list(APPEND _cmake_import_check_targets odccore )
list(APPEND _cmake_import_check_files_for_odccore "${_IMPORT_PREFIX}/lib64/libodccore.so" )

# Import target "odctools" for configuration "RelWithDebInfo"
set_property(TARGET odctools APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(odctools PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib64/libodctools.so"
  IMPORTED_SONAME_RELWITHDEBINFO "libodctools.so"
  )

list(APPEND _cmake_import_check_targets odctools )
list(APPEND _cmake_import_check_files_for_odctools "${_IMPORT_PREFIX}/lib64/libodctools.so" )

# Import target "odctest" for configuration "RelWithDebInfo"
set_property(TARGET odctest APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(odctest PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib64/libodctest.so"
  IMPORTED_SONAME_RELWITHDEBINFO "libodctest.so"
  )

list(APPEND _cmake_import_check_targets odctest )
list(APPEND _cmake_import_check_files_for_odctest "${_IMPORT_PREFIX}/lib64/libodctest.so" )

# Import target "odc" for configuration "RelWithDebInfo"
set_property(TARGET odc APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(odc PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/bin/odc"
  )

list(APPEND _cmake_import_check_targets odc )
list(APPEND _cmake_import_check_files_for_odc "${_IMPORT_PREFIX}/bin/odc" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
