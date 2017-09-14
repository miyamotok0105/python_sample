data = [
('betty', 1),
('bought', 1),
('a', 1),
('bit', 1),
('of', 1),
('butter', 2),
('but', 1),
('the', 1),
('was', 1),
('bitter', 1)]

print(data)
print(sorted(data, key=lambda tup:(-tup[1], tup[0])))

# data = [[1,2,3], [4,5,6], [7,8,9]]

data = [(1,3,6), (2,2,3), (3,1,9)]
print("tup[0]:",sorted(data, key=lambda tup: tup[0]))
print("tup[1]:",sorted(data, key=lambda tup: tup[1]))
print("tup[2]:",sorted(data, key=lambda tup: tup[2]))


data = [
('__label1__', 3),
('__label2__', 2),
('__label3__', 1)]
print(sorted(data, key=lambda tup:(tup[0])))