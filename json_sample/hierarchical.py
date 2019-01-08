import json

links = [("Tom","Dick"),("Dick","Harry"),("Tom","Larry"),("Bob","Leroy"),("Bob","Earl")]
parents, children = zip(*links)

print("parents:", parents)
print("children:", children)

root_nodes = {x for x in parents if x not in children}

print("root_nodes:", root_nodes)

for node in root_nodes:
    links.append(('Root', node))

print("links:", links)

def get_nodes(node):
    d = {}
    d['name'] = node
    children = get_children(node)
    if children:
        d['children'] = [get_nodes(child) for child in children]
    return d

print("result=============>")
"""
get children from links list.
"""
def get_children(node):
    return [x[1] for x in links if x[0] == node]

tree = get_nodes('Root')
print(json.dumps(tree, indent=4))

# parents: ('Tom', 'Dick', 'Tom', 'Bob', 'Bob')
# children: ('Dick', 'Harry', 'Larry', 'Leroy', 'Earl')
# root_nodes: {'Bob', 'Tom'}
# links: [('Tom', 'Dick'), ('Dick', 'Harry'), ('Tom', 'Larry'), ('Bob', 'Leroy'), ('Bob', 'Earl'), ('Root', 'Bob'), ('Root', 'Tom')]
# 
# {
#     "name": "Root",
#     "children": [
#         {
#             "name": "Tom",
#             "children": [
#                 {
#                     "name": "Dick",
#                     "children": [
#                         {
#                             "name": "Harry"
#                         }
#                     ]
#                 },
#                 {
#                     "name": "Larry"
#                 }
#             ]
#         },
#         {
#             "name": "Bob",
#             "children": [
#                 {
#                     "name": "Leroy"
#                 },
#                 {
#                     "name": "Earl"
#                 }
#             ]
#         }
#     ]
# }




