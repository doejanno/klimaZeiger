import matplotlib.pyplot as plt
import readData as data

MAX_DATA_POINT = 6
counter = []

# Live plot erstellen
def livePlot():
    try:
        x = []
        y = []

        fig, ax = plt.subplots()

        plt.show(block=False)

        while True:
            liveTemp = data.getTestData()
            x.append(len(counter) + 1)
            y.append(liveTemp)
            counter.append(len(counter)+1)

            if len(x) > MAX_DATA_POINT:
                x.pop(0)
                y.pop(0)

            ax.clear()
            ax.plot(x, y, color='b')
            plt.title("Data logger Readings")
            plt.xlabel("Time")
            plt.ylabel("Zahl")
            plt.draw()
            plt.pause(1)
    except:
        print('Graph could not be shown')
