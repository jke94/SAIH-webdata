import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def CreatePlotTittle():

    tittle = 'Temperatura ambiente (ºC) - Sistema Automático de Información Hidrológica (SAIH) (Generation Time: ' \
        + str(now.strftime("%d/%m/%y, %H:%M:%S")) + ') ' + 'Author: @JaviKarra94'

    return tittle

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

if __name__ == "__main__":

    nombres = [
            'Temperature-Velilla de La Valduerna',
            'Temperature-Morla de la Valderia',
            'Temperature-Nogarejas',
            'Temperature-Castrocalbon',
            'Temperature-Corporales',
            'Temperature-Truchillas'
        ]

    places = [
        'Velilla de La Valduerna',
        'Morla de La Valederia',
        'Nogarejas',
        'Castrocalbon',
        'Corporales',
        'Truchillas'
    ]

    dates = ["cucumber", "tomato", "lettuce", "asparagus",
                "potato", "wheat", "barley"]

    nHours = 24
    x = []
    ys = []
    dataframes = []
    now = datetime.now()
    count = 0

    for i in range(len(nombres)):
        csv_fileName = './data/saih-data-scraper/temperature/' + nombres[i].replace(' ','-') + '.csv'

        dataframes.append(pd.read_csv(csv_fileName))

    xDateTime = dataframes[0]['Datetime'].tail(nHours).values

    for i in range(len(xDateTime)):
        date = datetime.strptime(xDateTime[i], '%d/%m/%Y %H:%M')
        x.append(date.strftime("%d/%m %HH"))

    for i in range(len(places)):
        ys.append(dataframes[count]['Temperatura ambiente (ºC)'].tail(nHours).values)
        count = count + 1

    harvest = np.array([ys[0],ys[1],ys[2],ys[3],ys[4],ys[5]])

    fig, ax = plt.subplots(figsize=(28, 12))

    fig.suptitle(CreatePlotTittle(), fontsize=25)

    im, cbar = heatmap(harvest, places, x, ax=ax,
                    cmap="seismic")

    cbar.ax.tick_params(labelsize=28)
    cbar.ax.set_ylabel('ºC',fontsize=30)

    texts = annotate_heatmap(im, fontsize=17)


    fig.tight_layout()
    fig.savefig('./images/saih-temperature-36h-heatmap-'+ now.strftime("%d-%m-%y_%Hh") +'.png')