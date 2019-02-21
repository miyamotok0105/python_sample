import io
import argparse
from PIL import Image, ImageDraw
from gcp_ocr_package.ocr import render_doc_text

parser = argparse.ArgumentParser()
parser.add_argument('detect_file', help='The image for text detection.')
parser.add_argument('-out_file', help='Optional output file', default=0)
args = parser.parse_args()
parser = argparse.ArgumentParser()

image = Image.open(args.detect_file)
with io.open(args.detect_file, 'rb') as image_file:
    image_content = image_file.read()

render_doc_text(image, image_content, args.out_file)
