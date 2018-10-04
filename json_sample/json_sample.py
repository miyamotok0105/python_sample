import json

s = [('text', 0.9126313328742981, (198.16653442382812, 300.3179626464844, 208.556396484375, 116.07351684570312)), ('text', 0.8983753323554993, (202.06112670898438, 435.6139221191406, 198.87286376953125, 98.11067199707031)), ('text', 0.8930167555809021, (199.66700744628906, 180.60687255859375, 221.87440490722656, 104.23812103271484)), ('text', 0.8506355881690979, (158.68772888183594, 572.7786254882812, 110.84282684326172, 47.59654235839844)), ('text', 0.8435156345367432, (128.46148681640625, 377.0564880371094, 60.112754821777344, 22.179981231689453)), ('button', 0.8414376378059387, (200.66883850097656, 72.56367492675781, 201.32986450195312, 29.22214126586914)), ('button', 0.8120750188827515, (254.65025329589844, 98.60892486572266, 104.88936614990234, 26.49516487121582)), ('button', 0.7957008481025696, (144.66294860839844, 97.83570861816406, 90.96048736572266, 25.674509048461914)), ('text', 0.7869008779525757, (152.0374298095703, 502.7037048339844, 120.82577514648438, 20.625314712524414)), ('text', 0.7632841467857361, (180.47593688964844, 533.6126098632812, 178.26898193359375, 26.850793838500977))]

# print(s[0])

# for ss in s:
#     print(ss[0])
#     print(ss[1])
#     print(ss[2][0])
#     print(ss[2][1])
#     print(ss[2][2])
#     print(ss[2][3])

# array->hash->array->hash
# [
#   {
#     "rectangles": [
#       {
#         "right": 204, 
#         "top": 12, 
#         "bot": 44, 
#         "label": "logo", 
#         "width": 198, 
#         "height": 32, 
#         "prob": 74, 
#         "left": 6
#       }, 
#       ]
#   }
# ]

#============================
# json_arry = []
# rectangles_hash = {}
# rectangles_arry = []
# rect_hash = {}
# rect_hash["right"] = 1
# rect_hash["top"] = 1
# rectangles_arry.append(rect_hash)
# rectangles_hash["rectangles"] = rectangles_arry
# json_arry.append(rectangles_hash)
# print(json_arry)
#============================

json_arry = []
rectangles_hash = {}
rectangles_arry = []


for label, prob, rect in s:
    rect_hash = {}
    rect_hash["left"] = int(rect[0])
    rect_hash["right"] = int(rect[1])
    rect_hash["top"] = int(rect[2])
    rect_hash["bot"] = int(rect[3])
    rect_hash["width"] = int(rect_hash["right"]) - int(rect_hash["left"])
    harf_h = int(rect_hash["top"]) - int(rect_hash["bot"])
    rect_hash["height"] = int(harf_h)
    rect_hash["label"] = str(label)
    rect_hash["prob"] = float(prob)
    rectangles_arry.append(rect_hash)
#     print(label)
#     print(prob)
#     print(rect[0])
#     print(rect[1])
#     print(rect[2])
#     print(rect[3])

rectangles_hash["rectangles"] = rectangles_arry
json_arry.append(rectangles_hash)
# print(json_arry)

jsonstring = json.dumps(json_arry, indent=2)
print(jsonstring)


