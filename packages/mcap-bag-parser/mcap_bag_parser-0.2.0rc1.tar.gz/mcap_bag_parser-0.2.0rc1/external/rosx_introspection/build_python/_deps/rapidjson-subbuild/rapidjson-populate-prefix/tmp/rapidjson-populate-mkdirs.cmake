# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

# If CMAKE_DISABLE_SOURCE_CHANGES is set to true and the source directory is an
# existing directory in our source tree, calling file(MAKE_DIRECTORY) on it
# would cause a fatal error, even though it would be a no-op.
if(NOT EXISTS "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-src")
  file(MAKE_DIRECTORY "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-src")
endif()
file(MAKE_DIRECTORY
  "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-build"
  "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-subbuild/rapidjson-populate-prefix"
  "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-subbuild/rapidjson-populate-prefix/tmp"
  "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-subbuild/rapidjson-populate-prefix/src/rapidjson-populate-stamp"
  "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-subbuild/rapidjson-populate-prefix/src"
  "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-subbuild/rapidjson-populate-prefix/src/rapidjson-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-subbuild/rapidjson-populate-prefix/src/rapidjson-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/Users/neal/dev/personal/mcap-bag-parser/external/rosx_introspection/build_python/_deps/rapidjson-subbuild/rapidjson-populate-prefix/src/rapidjson-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
