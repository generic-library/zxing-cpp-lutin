#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "zxing cpp library (QR-code reader)"

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
	    "zxing-cpp/core/src/bigint/BigIntegerUtils.cc",
	    "zxing-cpp/core/src/bigint/BigInteger.cc",
	    "zxing-cpp/core/src/bigint/BigIntegerAlgorithms.cc",
	    "zxing-cpp/core/src/bigint/BigUnsigned.cc",
	    "zxing-cpp/core/src/bigint/BigUnsignedInABase.cc",
	    "zxing-cpp/core/src/zxing/aztec/detector/Detector.cpp",
	    "zxing-cpp/core/src/zxing/aztec/AztecDetectorResult.cpp",
	    "zxing-cpp/core/src/zxing/aztec/decoder/Decoder.cpp",
	    "zxing-cpp/core/src/zxing/aztec/AztecReader.cpp",
	    "zxing-cpp/core/src/zxing/Reader.cpp",
	    "zxing-cpp/core/src/zxing/Binarizer.cpp",
	    "zxing-cpp/core/src/zxing/MultiFormatReader.cpp",
	    "zxing-cpp/core/src/zxing/LuminanceSource.cpp",
	    "zxing-cpp/core/src/zxing/ResultPoint.cpp",
	    "zxing-cpp/core/src/zxing/BarcodeFormat.cpp",
	    "zxing-cpp/core/src/zxing/DecodeHints.cpp",
	    "zxing-cpp/core/src/zxing/multi/GenericMultipleBarcodeReader.cpp",
	    "zxing-cpp/core/src/zxing/multi/MultipleBarcodeReader.cpp",
	    "zxing-cpp/core/src/zxing/multi/ByQuadrantReader.cpp",
	    "zxing-cpp/core/src/zxing/multi/qrcode/detector/MultiDetector.cpp",
	    "zxing-cpp/core/src/zxing/multi/qrcode/detector/MultiFinderPatternFinder.cpp",
	    "zxing-cpp/core/src/zxing/multi/qrcode/QRCodeMultiReader.cpp",
	    "zxing-cpp/core/src/zxing/FormatException.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/detector/LinesSampler.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/detector/Detector.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/PDF417Reader.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/Decoder.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/BitMatrixParser.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/DecodedBitStreamParser.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/ec/ModulusPoly.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/ec/ModulusGF.cpp",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/ec/ErrorCorrection.cpp",
	    "zxing-cpp/core/src/zxing/Result.cpp",
	    "zxing-cpp/core/src/zxing/ResultPointCallback.cpp",
	    "zxing-cpp/core/src/zxing/InvertedLuminanceSource.cpp",
	    "zxing-cpp/core/src/zxing/ResultIO.cpp",
	    "zxing-cpp/core/src/zxing/BinaryBitmap.cpp",
	    "zxing-cpp/core/src/zxing/common/detector/WhiteRectangleDetector.cpp",
	    "zxing-cpp/core/src/zxing/common/detector/MonochromeRectangleDetector.cpp",
	    "zxing-cpp/core/src/zxing/common/DecoderResult.cpp",
	    "zxing-cpp/core/src/zxing/common/GlobalHistogramBinarizer.cpp",
	    "zxing-cpp/core/src/zxing/common/reedsolomon/GenericGF.cpp",
	    "zxing-cpp/core/src/zxing/common/reedsolomon/ReedSolomonDecoder.cpp",
	    "zxing-cpp/core/src/zxing/common/reedsolomon/ReedSolomonException.cpp",
	    "zxing-cpp/core/src/zxing/common/reedsolomon/GenericGFPoly.cpp",
	    "zxing-cpp/core/src/zxing/common/GridSampler.cpp",
	    "zxing-cpp/core/src/zxing/common/IllegalArgumentException.cpp",
	    "zxing-cpp/core/src/zxing/common/BitArray.cpp",
	    "zxing-cpp/core/src/zxing/common/BitMatrix.cpp",
	    "zxing-cpp/core/src/zxing/common/Str.cpp",
	    "zxing-cpp/core/src/zxing/common/StringUtils.cpp",
	    "zxing-cpp/core/src/zxing/common/PerspectiveTransform.cpp",
	    "zxing-cpp/core/src/zxing/common/BitSource.cpp",
	    "zxing-cpp/core/src/zxing/common/DetectorResult.cpp",
	    "zxing-cpp/core/src/zxing/common/BitArrayIO.cpp",
	    "zxing-cpp/core/src/zxing/common/GreyscaleLuminanceSource.cpp",
	    "zxing-cpp/core/src/zxing/common/HybridBinarizer.cpp",
	    "zxing-cpp/core/src/zxing/common/GreyscaleRotatedLuminanceSource.cpp",
	    "zxing-cpp/core/src/zxing/common/CharacterSetECI.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/detector/Detector.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/detector/CornerPoint.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/detector/DetectorException.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/Version.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/DataMatrixReader.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/decoder/DataBlock.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/decoder/Decoder.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/decoder/BitMatrixParser.cpp",
	    "zxing-cpp/core/src/zxing/datamatrix/decoder/DecodedBitStreamParser.cpp",
	    "zxing-cpp/core/src/zxing/Exception.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/detector/Detector.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/detector/AlignmentPatternFinder.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/detector/AlignmentPattern.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/detector/FinderPatternFinder.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/detector/FinderPattern.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/detector/FinderPatternInfo.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/FormatInformation.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/Version.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/ErrorCorrectionLevel.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/Mode.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/DataBlock.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/Decoder.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/BitMatrixParser.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/DecodedBitStreamParser.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/DataMask.cpp",
	    "zxing-cpp/core/src/zxing/qrcode/QRCodeReader.cpp",
	    "zxing-cpp/core/src/zxing/ChecksumException.cpp",
	    "zxing-cpp/core/src/zxing/oned/CodaBarReader.cpp",
	    "zxing-cpp/core/src/zxing/oned/UPCEANReader.cpp",
	    "zxing-cpp/core/src/zxing/oned/Code39Reader.cpp",
	    "zxing-cpp/core/src/zxing/oned/UPCEReader.cpp",
	    "zxing-cpp/core/src/zxing/oned/ITFReader.cpp",
	    "zxing-cpp/core/src/zxing/oned/OneDResultPoint.cpp",
	    "zxing-cpp/core/src/zxing/oned/Code93Reader.cpp",
	    "zxing-cpp/core/src/zxing/oned/EAN8Reader.cpp",
	    "zxing-cpp/core/src/zxing/oned/UPCAReader.cpp",
	    "zxing-cpp/core/src/zxing/oned/Code128Reader.cpp",
	    "zxing-cpp/core/src/zxing/oned/EAN13Reader.cpp",
	    "zxing-cpp/core/src/zxing/oned/MultiFormatUPCEANReader.cpp",
	    "zxing-cpp/core/src/zxing/oned/MultiFormatOneDReader.cpp",
	    "zxing-cpp/core/src/zxing/oned/OneDReader.cpp"
	    ])
	# build in C mode
	my_module.compile_version("c++", 2003)
	my_module.add_depend([
	    'cxx',
	    'm',
	    'pthread'
	    ])
	#my_module.add_path(os.path.join(tools.get_current_path(__file__), "zxing-cpp", "core", "src"))
	my_module.add_flag('c++', [
	    "-D_CRT_SECURE_NO_WARNINGS"
	    ])
	#my_module.add_optionnal_depend('iconv', [], ["c", "-DNO_ICONV=1"])
	my_module.add_flag('c++', [
	    "-DNO_ICONV=1"
	    ],
	    export=True)

	my_module.add_header_file([
	    "zxing-cpp/core/src/bigint/BigUnsignedInABase.hh",
	    "zxing-cpp/core/src/bigint/NumberlikeArray.hh",
	    "zxing-cpp/core/src/bigint/BigInteger.hh",
	    "zxing-cpp/core/src/bigint/BigUnsigned.hh",
	    "zxing-cpp/core/src/bigint/BigIntegerLibrary.hh",
	    "zxing-cpp/core/src/bigint/BigIntegerUtils.hh",
	    "zxing-cpp/core/src/bigint/BigIntegerAlgorithms.hh",
	    ], destination_path="bigint")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/aztec/detector/Detector.h",
	    ], destination_path="zxing/aztec/detector")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/aztec/decoder/Decoder.h",
	    ], destination_path="zxing/aztec/decoder")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/aztec/AztecDetectorResult.h",
	    "zxing-cpp/core/src/zxing/aztec/AztecReader.h",
	    ], destination_path="zxing/aztec")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/multi/GenericMultipleBarcodeReader.h",
	    "zxing-cpp/core/src/zxing/multi/ByQuadrantReader.h",
	    "zxing-cpp/core/src/zxing/multi/MultipleBarcodeReader.h",
	    ], destination_path="zxing/multi")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/multi/qrcode/detector/MultiDetector.h",
	    "zxing-cpp/core/src/zxing/multi/qrcode/detector/MultiFinderPatternFinder.h",
	    ], destination_path="zxing/multi/qrcode/detector")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/multi/qrcode/QRCodeMultiReader.h",
	    ], destination_path="zxing/multi/qrcode")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/pdf417/detector/Detector.h",
	    "zxing-cpp/core/src/zxing/pdf417/detector/LinesSampler.h",
	    ], destination_path="zxing/pdf417/detector")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/pdf417/decoder/Decoder.h",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/DecodedBitStreamParser.h",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/BitMatrixParser.h",
	    ], destination_path="zxing/pdf417/decoder")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/pdf417/decoder/ec/ModulusPoly.h",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/ec/ModulusGF.h",
	    "zxing-cpp/core/src/zxing/pdf417/decoder/ec/ErrorCorrection.h",
	    ], destination_path="zxing/pdf417/decoder/ec")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/pdf417/PDF417Reader.h",
	    ], destination_path="zxing/pdf417")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/common/detector/MathUtils.h",
	    "zxing-cpp/core/src/zxing/common/detector/WhiteRectangleDetector.h",
	    "zxing-cpp/core/src/zxing/common/detector/JavaMath.h",
	    "zxing-cpp/core/src/zxing/common/detector/MonochromeRectangleDetector.h",
	    ], destination_path="zxing/common/detector")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/common/reedsolomon/GenericGF.h",
	    "zxing-cpp/core/src/zxing/common/reedsolomon/GenericGFPoly.h",
	    "zxing-cpp/core/src/zxing/common/reedsolomon/ReedSolomonException.h",
	    "zxing-cpp/core/src/zxing/common/reedsolomon/ReedSolomonDecoder.h",
	    ], destination_path="zxing/common/reedsolomon")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/common/StringUtils.h",
	    "zxing-cpp/core/src/zxing/common/BitSource.h",
	    "zxing-cpp/core/src/zxing/common/Counted.h",
	    "zxing-cpp/core/src/zxing/common/IllegalArgumentException.h",
	    "zxing-cpp/core/src/zxing/common/BitArray.h",
	    "zxing-cpp/core/src/zxing/common/GlobalHistogramBinarizer.h",
	    "zxing-cpp/core/src/zxing/common/DetectorResult.h",
	    "zxing-cpp/core/src/zxing/common/Str.h",
	    "zxing-cpp/core/src/zxing/common/GridSampler.h",
	    "zxing-cpp/core/src/zxing/common/DecoderResult.h",
	    "zxing-cpp/core/src/zxing/common/Point.h",
	    "zxing-cpp/core/src/zxing/common/HybridBinarizer.h",
	    "zxing-cpp/core/src/zxing/common/BitMatrix.h",
	    "zxing-cpp/core/src/zxing/common/GreyscaleRotatedLuminanceSource.h",
	    "zxing-cpp/core/src/zxing/common/GreyscaleLuminanceSource.h",
	    "zxing-cpp/core/src/zxing/common/PerspectiveTransform.h",
	    "zxing-cpp/core/src/zxing/common/Array.h",
	    "zxing-cpp/core/src/zxing/common/CharacterSetECI.h",
	    ], destination_path="zxing/common")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/datamatrix/detector/DetectorException.h",
	    "zxing-cpp/core/src/zxing/datamatrix/detector/Detector.h",
	    "zxing-cpp/core/src/zxing/datamatrix/detector/CornerPoint.h",
	    ], destination_path="zxing/datamatrix/detector")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/datamatrix/decoder/Decoder.h",
	    "zxing-cpp/core/src/zxing/datamatrix/decoder/DecodedBitStreamParser.h",
	    "zxing-cpp/core/src/zxing/datamatrix/decoder/BitMatrixParser.h",
	    "zxing-cpp/core/src/zxing/datamatrix/decoder/DataBlock.h",
	    ], destination_path="zxing/datamatrix/decoder")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/datamatrix/DataMatrixReader.h",
	    "zxing-cpp/core/src/zxing/datamatrix/Version.h",
	    ], destination_path="zxing/datamatrix")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/qrcode/detector/Detector.h",
	    "zxing-cpp/core/src/zxing/qrcode/detector/FinderPatternFinder.h",
	    "zxing-cpp/core/src/zxing/qrcode/detector/FinderPattern.h",
	    "zxing-cpp/core/src/zxing/qrcode/detector/AlignmentPatternFinder.h",
	    "zxing-cpp/core/src/zxing/qrcode/detector/AlignmentPattern.h",
	    "zxing-cpp/core/src/zxing/qrcode/detector/FinderPatternInfo.h",
	    ], destination_path="zxing/qrcode/detector")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/qrcode/FormatInformation.h",
	    "zxing-cpp/core/src/zxing/qrcode/QRCodeReader.h",
	    "zxing-cpp/core/src/zxing/qrcode/ErrorCorrectionLevel.h",
	    "zxing-cpp/core/src/zxing/qrcode/Version.h",
	    ], destination_path="zxing/qrcode")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/qrcode/decoder/Decoder.h",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/DecodedBitStreamParser.h",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/Mode.h",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/BitMatrixParser.h",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/DataBlock.h",
	    "zxing-cpp/core/src/zxing/qrcode/decoder/DataMask.h",
	    ], destination_path="zxing/qrcode/decoder")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/oned/OneDResultPoint.h",
	    "zxing-cpp/core/src/zxing/oned/CodaBarReader.h",
	    "zxing-cpp/core/src/zxing/oned/EAN13Reader.h",
	    "zxing-cpp/core/src/zxing/oned/OneDReader.h",
	    "zxing-cpp/core/src/zxing/oned/Code39Reader.h",
	    "zxing-cpp/core/src/zxing/oned/EAN8Reader.h",
	    "zxing-cpp/core/src/zxing/oned/MultiFormatUPCEANReader.h",
	    "zxing-cpp/core/src/zxing/oned/UPCEReader.h",
	    "zxing-cpp/core/src/zxing/oned/ITFReader.h",
	    "zxing-cpp/core/src/zxing/oned/Code128Reader.h",
	    "zxing-cpp/core/src/zxing/oned/MultiFormatOneDReader.h",
	    "zxing-cpp/core/src/zxing/oned/UPCAReader.h",
	    "zxing-cpp/core/src/zxing/oned/UPCEANReader.h",
	    "zxing-cpp/core/src/zxing/oned/Code93Reader.h",
	    ], destination_path="zxing/oned")
	my_module.add_header_file([
	    "zxing-cpp/core/src/zxing/BinaryBitmap.h",
	    "zxing-cpp/core/src/zxing/Result.h",
	    "zxing-cpp/core/src/zxing/BarcodeFormat.h",
	    "zxing-cpp/core/src/zxing/ChecksumException.h",
	    "zxing-cpp/core/src/zxing/ReaderException.h",
	    "zxing-cpp/core/src/zxing/DecodeHints.h",
	    "zxing-cpp/core/src/zxing/ResultPointCallback.h",
	    "zxing-cpp/core/src/zxing/ZXing.h",
	    "zxing-cpp/core/src/zxing/NotFoundException.h",
	    "zxing-cpp/core/src/zxing/Reader.h",
	    "zxing-cpp/core/src/zxing/ResultPoint.h",
	    "zxing-cpp/core/src/zxing/InvertedLuminanceSource.h",
	    "zxing-cpp/core/src/zxing/IllegalStateException.h",
	    "zxing-cpp/core/src/zxing/MultiFormatReader.h",
	    "zxing-cpp/core/src/zxing/Exception.h",
	    "zxing-cpp/core/src/zxing/Binarizer.h",
	    "zxing-cpp/core/src/zxing/LuminanceSource.h",
	    "zxing-cpp/core/src/zxing/FormatException.h"
	    ], destination_path="zxing")
	
	if "Windows" in target.get_type():
		my_module.add_src_file([
		    "zxing-cpp/core/src/win32/zxing/win_iconv.c"
		    ])
		my_module.add_header_file([
		    "zxing-cpp/core/src/win32/zxing/iconv.h",
		    "zxing-cpp/core/src/win32/zxing/stdint.h",
		    ])
	my_module.add_path("zxing-cpp/core/src/win32")
	
	return True


