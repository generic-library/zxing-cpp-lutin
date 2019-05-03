#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "BINARY"

def get_sub_type():
	return "TEST"

def get_desc():
	return "zxing test binary (QR-code reader)"

def get_licence():
	return "APACHE-2"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "unknow"

def get_maintainer():
	return []

def get_version():
	return [0,0]

def configure(target, my_module):
	my_module.add_src_file([
	    "zxing-cpp/core/tests/src/common/reedsolomon/ReedSolomonTest.cpp",
	    "zxing-cpp/core/tests/src/common/BitMatrixTest.cpp",
	    "zxing-cpp/core/tests/src/common/BitArrayTest.cpp",
	    "zxing-cpp/core/tests/src/common/PerspectiveTransformTest.cpp",
	    "zxing-cpp/core/tests/src/common/BitSourceTest.cpp",
	    "zxing-cpp/core/tests/src/common/CountedTest.cpp",
	    "zxing-cpp/core/tests/src/qrcode/VersionTest.cpp",
	    "zxing-cpp/core/tests/src/qrcode/ErrorCorrectionLevelTest.cpp",
	    "zxing-cpp/core/tests/src/qrcode/decoder/DataMaskTest.cpp",
	    "zxing-cpp/core/tests/src/qrcode/decoder/ModeTest.cpp",
	    "zxing-cpp/core/tests/src/qrcode/FormatInformationTest.cpp",
	    "zxing-cpp/core/tests/src/TestRunner.cpp",
	    ])
	# build in C mode
	my_module.compile_version("c++", 2003)
	my_module.add_path("zxing-cpp/core/test/src")
	my_module.add_depend([
	    'zxing',
	    'cppunit'
	    ])
	return True


