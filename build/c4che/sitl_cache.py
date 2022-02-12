AP_LIBRARIES = ['AP_HAL_SITL', 'SITL']
AP_LIBRARIES_OBJECTS_KW = {}
AR = ['/usr/bin/ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/bin'
BOARD = 'sitl'
BOOTLOADER = False
BUILD_SUMMARY_HEADER = ['target', 'size_text', 'size_data', 'size_bss', 'size_total']
CC = ['/usr/bin/gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('9', '3', '0')
CFLAGS = ['-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wshadow', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-MMD']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = []
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXFLAGS = ['-std=gnu++11', '-fdata-sections', '-ffunction-sections', '-fno-exceptions', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wshadow', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-Wno-reorder', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Werror=format-security', '-Werror=array-bounds', '-Werror=uninitialized', '-Werror=init-self', '-Werror=switch', '-Werror=sign-compare', '-Wfatal-errors', '-Wno-trigraphs', '-Werror=unused-but-set-variable', '-O3', '-DCYGWIN_BUILD', '-MMD']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = []
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEBUG = False
DEFINES = ['SKETCHBOOK="/cygdrive/d/ardupilot"', 'CONFIG_HAL_BOARD=HAL_BOARD_SITL', 'CONFIG_HAL_BOARD_SUBTYPE=HAL_BOARD_SUBTYPE_NONE']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'HAVE_CMATH_ISINF': '', 'NEED_CMATH_ISFINITE_STD_NAMESPACE': '', 'NEED_CMATH_ISNAN_STD_NAMESPACE': '', 'WAF_BUILD': '', 'NEED_CMATH_ISINF_STD_NAMESPACE': '', '__STDC_FORMAT_MACROS': '', 'HAVE_ENDIAN_H': '', 'HAVE_BYTESWAP_H': '', 'PYTHONDIR': '', 'HAVE_CMATH_ISFINITE': '', 'HAVE_CMATH_ISNAN': '', '_GNU_SOURCE': '', 'PYTHONARCHDIR': ''}
DEST_BINFMT = 'pe'
DEST_CPU = 'x86_64'
DEST_OS = 'cygwin'
DSDL_COMPILER = '/cygdrive/d/ardupilot/modules/uavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc'
DSDL_COMPILER_DIR = '/cygdrive/d/ardupilot/modules/uavcan/libuavcan/dsdl_compiler'
ENABLE_GCCDEPS = ['c', 'cxx']
ENABLE_HEADER_CHECKS = False
GIT = ['/usr/bin/git']
GIT_SUBMODULES = ['gtest', 'mavlink']
HAS_GTEST = True
HAVE_BYTESWAP_H = 1
HAVE_CMATH_ISFINITE = 1
HAVE_CMATH_ISINF = 1
HAVE_CMATH_ISNAN = 1
HAVE_ENDIAN_H = 1
IMPLIB_ST = '-Wl,--out-implib,%s'
INCLUDES = ['/cygdrive/d/ardupilot/libraries/', '/cygdrive/d/ardupilot/libraries/AP_Common/missing']
LIB = ['m', 'winmm']
LIBDIR = '/usr/bin'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS = ['-Wl,--gc-sections', '-pthread']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared', '-Wl,--enable-auto-image-base']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared', '-Wl,--enable-auto-image-base']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
MAVGEN = '/cygdrive/d/ardupilot/modules/mavlink/pymavlink/tools/mavgen.py'
MAVLINK_DIR = '/cygdrive/d/ardupilot/modules/mavlink'
NEED_CMATH_ISFINITE_STD_NAMESPACE = 1
NEED_CMATH_ISINF_STD_NAMESPACE = 1
NEED_CMATH_ISNAN_STD_NAMESPACE = 1
PREFIX = '/usr'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/lib/python2.7/site-packages'
PYTHONDIR = '/usr/lib/python2.7/site-packages'
PYTHON_VERSION = '2.7'
ROMFS_FILES = []
RPATH_ST = '-Wl,-rpath,%s'
RSYNC = ['/usr/bin/rsync']
SHLIB_MARKER = '-Wl,-Bdynamic'
SIZE = ['/usr/bin/size']
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUBMODULE_UPDATE = True
TOOLCHAIN = 'native'
cfg_files = ['/cygdrive/d/ardupilot/build/sitl/ap_config.h']
cprogram_PATTERN = '%s.exe'
cshlib_PATTERN = 'cyg%s.dll'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s.exe'
cxxshlib_PATTERN = 'cyg%s.dll'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
implib_PATTERN = 'lib%s.dll.a'
macbundle_PATTERN = '%s.bundle'
