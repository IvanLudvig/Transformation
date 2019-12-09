import matplotlib.pyplot as plt
import numpy as np
import string

V = np.array([(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)])

A = np.array([[2, 5, 0],
              [-11, 10, 0],
              [0, 0, 1]])
A = np.array([[-4, 7, 0],
              [8, 1, 0],
              [0, 0, 1]])
c = [(A.item(0, 0) * A.item(0, 1)) + (A.item(1, 0) * A.item(1, 1)),
     -(A.item(1, 1) ** 2) - (A.item(0, 1) ** 2) + (A.item(1, 0) ** 2) + (A.item(0, 0) ** 2),
     -(A.item(0, 0) * A.item(0, 1)) - (A.item(1, 0) * A.item(1, 1))]
b1, b2 = np.roots(c)
e1, e2 = np.array([1, b1, 1]), np.array([b1, -1, 1])
print(e1, e2)
ne1, ne2 = np.matmul(A, e1), np.matmul(A, e2)
angle = np.arccos(np.dot(ne1[0:2], e1[0:2]) / (np.linalg.norm(ne1[0:2]) * np.linalg.norm(e1[0:2])))
scalex = np.linalg.norm(ne1[0:2]) / np.linalg.norm(e1[0:2])
scaley = np.linalg.norm(ne2[0:2]) / np.linalg.norm(e2[0:2])

print("rotate by: ", angle)
print("scale by ", scalex, " to ", '{:+f}'.format(ne1.item(0)).rstrip("0").rstrip("."), "x",
      '{:+f}'.format(ne1.item(1)).rstrip("0").rstrip("."), "y", "= 0")
print("scale by ", scaley, " to ", '{:+f}'.format(ne2.item(0)).rstrip("0").rstrip("."), "x",
      '{:+f}'.format(ne2.item(1)).rstrip("0").rstrip("."), "y", "= 0")

sc = np.diag([scalex, scaley, 1])
rot = np.array([[np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle), np.cos(angle), 0],
                [0, 0, 1]])
p = np.array([[ne1.item(0), ne2.item(0), 0], [ne1.item(1), ne2.item(1), 0], [0, 0, 1]])
print(p)
sc = np.matmul(p, sc)
sc = np.matmul(sc, np.linalg.inv(p))
# sc = np.transpose(sc)
# print(sc)
u = (np.matmul(sc, rot))
print(u)
X = []
Y = []
X1 = []
Y1 = []
fig = plt.figure()
ax = plt.gca()

for v in V:
    transform = A @ v
    x, y, z = transform
    X.append(x)
    Y.append(y)
    plt.scatter(X, Y)

for v in V:
    transform = u @ v
    x, y, z = transform
    X1.append(x)
    Y1.append(y)
    plt.scatter(X1, Y1)

X.append(X[0])
Y.append(Y[0])
X1.append(X1[0])
Y1.append(Y1[0])

plt.plot(X, Y, color="blue")
plt.plot(X1, Y1, color="red")
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
plt.grid()
plt.show()
