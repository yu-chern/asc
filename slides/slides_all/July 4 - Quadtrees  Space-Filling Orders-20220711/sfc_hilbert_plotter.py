import matplotlib.pyplot as plt

# functions to plot vertical and horizontal lines,
# returns the end-point of the line
def plotLineUp(x, y, length):
	x.append(x[len(x) - 1])
	y.append(y[len(y) - 1] + length)

def plotLineDown(x, y, length):
	x.append(x[len(x) - 1])
	y.append(y[len(y) - 1] - length)

def plotLineLeft(x, y, length):
	x.append(x[len(x) - 1] - length)
	y.append(y[len(y) - 1])

def plotLineRight(x, y, length):
	x.append(x[len(x) - 1] + length)
	y.append(y[len(y) - 1])

#-------------------------------------------------------------------------------------------------

# recursive rules for Hilbert curve

def H(depth, x, y):
	if depth >= 0:
		A(depth-1, x, y)
		plotLineUp(x, y, 1.0)
		H(depth-1, x, y)
		plotLineRight(x, y, 1.0)
		H(depth-1, x, y)
		plotLineDown(x, y, 1.0)
		B(depth-1, x, y)

def A(depth, x, y):
	if depth >= 0:
		H(depth-1, x, y)
		plotLineRight(x, y, 1.0)
		A(depth-1, x, y)
		plotLineUp(x, y, 1.0)
		A(depth-1, x, y)
		plotLineLeft(x, y, 1.0)
		C(depth-1, x, y)

def B(depth, x, y):
	if depth >= 0:
		C(depth-1, x, y)
		plotLineLeft(x, y, 1.0)
		B(depth-1, x, y)
		plotLineDown(x, y, 1.0)
		B(depth-1, x, y)
		plotLineRight(x, y, 1.0)
		H(depth-1, x, y)

def C(depth, x, y):
	if depth >= 0:
		B(depth-1, x, y)
		plotLineDown(x, y, 1.0)
		C(depth-1, x, y)
		plotLineLeft(x, y, 1.0)
		C(depth-1, x, y)
		plotLineUp(x, y, 1.0)
		A(depth-1, x, y)

def plotLineStrip(x, y, title = None):
    fig, ax = plt.subplots()
    plt.plot(x, y)
    if title is not None:
        plt.title(title)
    ax.set_xlim(min(x)-1, max(x)+1)
    ax.set_ylim(min(y)-1, max(y)+1)
    ax.axis('equal')
    plt.show()
    


###############################################################
# This is the main function of this python script.
# Switch the exercise number to test the single exercises.
###############################################################
if __name__ == '__main__':
    # set delay for animation
    delay = 0.0
    
    depth = 4
    x = [0.5]
    y = [0.5]
    H(depth, x, y)
    
    if delay > 0.0:
        plotCurveDelayed(x, y, delay)
    else:
        plotLineStrip(x, y, None)
    
    