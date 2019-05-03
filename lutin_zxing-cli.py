#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "BINARY"

def get_sub_type():
	return "TOOL"

def get_desc():
	return "zxing tools library (QR-code reader)"

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
	    "zxing-cpp/cli/src/jpgd.cpp",
	    "zxing-cpp/cli/src/lodepng.cpp",
	    "zxing-cpp/cli/src/ImageReaderSource.cpp",
	    "zxing-cpp/cli/src/main.cpp",
	    ])
	# build in C mode
	my_module.compile_version("c++", 2003)
	my_module.add_path("zxing-cpp/cli/src")
	my_module.add_depend('zxing')
	return True


