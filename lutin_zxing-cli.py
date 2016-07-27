#!/usr/bin/python
import lutin.module as module
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

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
		"zxing-cpp/cli/src/jpgd.cpp",
		"zxing-cpp/cli/src/lodepng.cpp",
		"zxing-cpp/cli/src/ImageReaderSource.cpp",
		"zxing-cpp/cli/src/main.cpp",
		])
	# build in C mode
	my_module.compile_version("c++", 2003)
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "zxing-cpp", "cli", "src"))
	my_module.add_module_depend('zxing')
	return my_module


