include( CMakeFindDependencyMacro )

find_dependency( eckit  HINTS ${CMAKE_CURRENT_LIST_DIR}/../eckit /tmp/fdb/prereqs/eckitlib/lib/cmake/eckit )
find_dependency( metkit HINTS ${CMAKE_CURRENT_LIST_DIR}/../metkit /tmp/fdb/prereqs/metkitlib/lib/cmake/metkit )

if( 0 )
    find_dependency( eccodes HINTS ${CMAKE_CURRENT_LIST_DIR}/../eccodes /tmp/fdb/prereqs/eccodeslib/lib/cmake/eccodes )
endif()
