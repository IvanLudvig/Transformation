import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, 5, 0],
              [-11, 10, 0],
              [0, 0, 1]])


# Tested on:
# A = np.array([[-4, 7, 0],
#               [8, 1, 0],
#               [0, 0, 1]])
# A = np.array([[3, 0, 0],
#               [0, 4, 0],
#               [0, 0, 1]])
# A = np.array([[1, 0, 0],
#               [-1, 1, 0],
#               [0, 0, 1]])
# A = np.array([[0, 3, -2],
#               [-4, 0, 0],
#               [0, 0, 1]])
# A = np.array([[1, np.sqrt(3), 2],
#               [-3*np.sqrt(3), 3, np.sqrt(3)],
#               [0, 0, 1]])


def formatFloat(float):
    return '{:.5f}'.format(float).rstrip("0").rstrip(".")


def formatFloatWithSign(float):
    return '{:+.5f}'.format(float).rstrip("0").rstrip(".")


def angle(v1, v2):
    angle = np.arccos(np.dot(v2[0:2], v1[0:2]) / (np.linalg.norm(v2[0:2]) * np.linalg.norm(v1[0:2])))
    if np.linalg.det([v2[0:2], v1[0:2]]) > 0:
        return angle
    else:
        return -angle


V = np.array([(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)])

c = [(A[0][0] * A[0][1]) + (A[1][0] * A[1][1]),
     -(A[1][1] ** 2) - (A[0][1] ** 2) + (A[1][0] ** 2) + (A[0][0] ** 2),
     -(A[0][0] * A[0][1]) - (A[1][0] * A[1][1])]

roots = np.roots(c)

if (roots.size > 0):
    e1, e2 = np.array([1, roots[0], 1]), np.array([roots[0], -1, 1])
    ne1, ne2 = A[0:2, 0:2] @ e1[0:2], A[0:2, 0:2] @ e2[0:2]

    angle = angle(ne1, e1)
    if round(((1 - A[0][0]) * (1 - A[1][1])) - (A[0][1] * A[1][0]), 8) != 0:
        o = [
            ((A[0][1] * A[1][2]) + (A[0][2] * (1 - A[1][1]))) / (((1 - A[0][0]) * (1 - A[1][1])) - (A[0][1] * A[1][0])),
            ((A[0][2] * A[1][0]) + (A[1][2] * (1 - A[0][0]))) / (((1 - A[0][0]) * (1 - A[1][1])) - (A[0][1] * A[1][0]))]
    else:
        o = [0, 0]

    scalex = np.linalg.norm(ne1[0:2]) / np.linalg.norm(e1[0:2])
    scaley = np.linalg.norm(ne2[0:2]) / np.linalg.norm(e2[0:2])

    print("rotate around (" + formatFloat(o[0]), formatFloat(o[1]) + ") by", formatFloat(angle))
    print("scale by " + formatFloat(scalex), "to",
          formatFloat(ne1[0]) + "x" if ne1[0] != 0 else "",
          formatFloatWithSign(ne1[1]) + "y" if ne1[1] != 0 else "",
          formatFloatWithSign(o[0]) if o[0] != 0 else "",
          "= 0")
    print("scale by", formatFloat(scaley), "to",
          formatFloat(ne2[0]) + "x" if ne2[0] != 0 else "",
          formatFloatWithSign(ne2[1]) + "y" if ne2[1] != 0 else "",
          formatFloatWithSign(o[1]) if o[1] != 0 else "",
          "= 0")

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
    x, y, z = v
    X1.append(x)
    Y1.append(y)
    plt.scatter(X1, Y1)

X.append(X[0])
Y.append(Y[0])
X1.append(X1[0])
Y1.append(Y1[0])

plt.plot(X, Y, color="red")
plt.plot(X1, Y1, color="black")
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
plt.grid()
plt.show()
