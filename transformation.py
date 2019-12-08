import matplotlib.pyplot as plt
import numpy as np
import string

a, b, c, d = (0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)
E = np.array([a, b, d, c])

A = np.array([[2, 5, 0],
              [-11, 10, 0],
              [0, 0, 1]])
c = [(A.item(0, 0) * A.item(0, 1)) + (A.item(1, 0) * A.item(1, 1)),
     -(A.item(1, 1) ** 2) - (A.item(0, 1) ** 2) + (A.item(1, 0) ** 2) + (A.item(0, 0) ** 2),
     -(A.item(0, 0) * A.item(0, 1)) - (A.item(1, 0) * A.item(1, 1))]
b1, b2 = np.roots(c)
e1, e2 = [1, b1], [b2, 1]
ne1, ne2 = np.matmul((A[0:2, 0:2]), e1), np.matmul((A[0:2, 0:2]), e2)
angle = np.arccos(np.dot(ne1, e1) / (np.linalg.norm(ne1) * np.linalg.norm(e1)))
scalex = np.linalg.norm(ne1) / np.linalg.norm(e1)
scaley = np.linalg.norm(ne2) / np.linalg.norm(e2)
print("rotate by: ", angle)
print("scale by ", scalex, " to ", ne1.item(0), "x", '{:+f}'.format(ne1.item(1)).rstrip("0"), "y", "=0")
print("scale by ", scaley, " to ", ne2.item(0), "x", '{:+f}'.format(ne2.item(1)).rstrip("0"), "y", "=0")
X = []
Y = []
X1 = []
Y1 = []
fig = plt.figure()
ax = plt.gca()

for v in E:
    transform = np.eye(3) @ v
    x, y, z = transform
    X.append(x)
    Y.append(y)
    plt.scatter(X, Y)

for v in E:
    transform = A @ v
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
