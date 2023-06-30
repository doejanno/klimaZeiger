import matplotlib.pyplot as plt
import readData as data

__MAX_DATA_POINT = 6

# Live plot erstellen
def livePlot(HOST, PORT):
    try:
        # initialise arrays
        x = []
        y = []
        counter = []
        
        fig, ax = plt.subplots()

        plt.show(block=False)

        # loop the plot
        while True:
            # get a TEST dataset
            liveTemp = data.getTestData()
            x.append(len(counter) + 1)
            y.append(liveTemp)
            counter.append(len(counter)+1)

            # Shorten the array to the max length
            if len(x) > __MAX_DATA_POINT:
                x.pop(0)
                y.pop(0)

            # Plot the graph
            ax.clear()
            ax.plot(x, y, color='b')
            plt.title("Data logger Readings")
            plt.xlabel("Time")
            plt.ylabel("Zahl")
            plt.pause(1)
            plt.draw()
    except:
        print('Graph was closed')
