import argparse
from gcp_ocr_package.ocr import render_doc_text

parser = argparse.ArgumentParser()
parser.add_argument('detect_file', help='The image for text detection.')
parser.add_argument('-out_file', help='Optional output file', default=0)
args = parser.parse_args()

parser = argparse.ArgumentParser()
render_doc_text(args.detect_file, args.out_file)
