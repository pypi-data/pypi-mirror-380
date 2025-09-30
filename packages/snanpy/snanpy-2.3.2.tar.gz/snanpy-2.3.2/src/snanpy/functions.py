from matplotlib import pyplot as plt
import matplotlib as mpl

mpl.rcParams.update(mpl.rcParamsDefault)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def figax(figsize=(8,6), xlim: tuple =None, ylim: tuple =None, xlabel: str=None, ylabel:str=None, title:str=None, font_size: int = 19):
    plt.rcParams.update({'font.size': font_size})
    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
    ax.grid(linewidth=0.5) 
    if xlim is not None:
        ax.set_xlim(xlim)  
    if ylim is not None:
        ax.set_ylim(ylim) 
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel) 

    return fig, ax

def saveplot(name: str, folder: str=None, dpi: int = 200):
    import os
    base_path = os.path.join(os.getcwd(), 'Figures')
    if folder:
        path = os.path.join(base_path, folder)
    else:
        path = base_path
    os.makedirs(path, exist_ok=True)

    plt.savefig(path + '\\' + name + '.png', dpi=dpi)