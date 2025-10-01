#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2021
# @Author :  GitOPEN
# @Email  :  gitopen@gmail.com
# @Date   :  2021-05-22 17:08:35
# @Description :  一些画图的相关工具函数


__version__ = "0.7.9.11"


import itertools

import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from gitopenlib.utils import files as gf
from matplotlib import ticker
from matplotlib.axes import Axes
from matplotlib.offsetbox import AnchoredText
from matplotlib.ticker import MaxNLocator
from typing import Union


def set_4k_dpi():
    matplotlib.rcParams["figure.dpi"] = 200


def sns_bar_hatch(
    ax: Axes,
    hatch: bool = True,
    hatches: list = None,
):
    """
    Set the hatches of a bar plot in Seaborn.
    """

    # set hatches to each bar
    if hatch:
        # set hatch symbol list
        if hatches is None:
            hatches = ["///", "*", "\\/", "+", "---", "o", "|||", "x", "O", "."]
        # get the number of bar in the barplot
        bar_kind_num = len(ax.containers[0])
        # get the corresponding number of hatches
        hatches = itertools.cycle(hatches)
        hatches = list(itertools.islice(hatches, bar_kind_num))
        # set hatch for each kind bar.
        for bars, hatch in zip(ax.containers, hatches):
            # Set a different hatch for each group of bars
            for bar in bars:
                bar.set_hatch(hatch)


def sns_barplot_text(
    ax: Axes,
    bar_orient: str = "vertical",
    decimal: int = 3,
    fontsize: int = 9,
    color: str = "black",
    rotation: int = 0,
):
    """
    使用seaborn画条形图，给每个bar上添加数值标签。
    如默认字体样式不能满足需求，请copy下面代码自定义。
    """
    for bars in ax.containers:
        for bar in bars:
            if bar_orient == "vertical":
                x = bar.get_x() + bar.get_width() / 2.0
                y = bar.get_height()
                text = str(f"%.{decimal}f" % y) if decimal > 0 else str(int(y))
                ha = "center"
                va = "bottom"
            if bar_orient == "horizontal":
                x = bar.get_width()
                y = bar.get_y() + bar.get_height() / 2.0
                text = str(f"%.{decimal}f" % x) if decimal > 0 else str(int(x))
                ha = "left"  # 'center', 'right', 'left'
                va = "center_baseline"  # 'top', 'bottom', 'center', 'baseline', 'center_baseline'
            ax.text(
                x,
                y,
                text,
                fontsize=fontsize,
                color=color,
                ha=ha,
                va=va,
                rotation=rotation,
            )
    pass


def sns_barplot_text1(
    ax: Axes,
    bar_orient: str = "vertical",
    decimal: int = 2,
    fontsize: int = 8,
    color: str = "black",
    rotation: int = 90,
):
    """
    使用seaborn画条形图，给每个bar上添加数值标签。
    如默认字体样式不能满足需求，请copy下面代码自定义。
    """
    if bar_orient == "vertical":
        for p in ax.patches:
            height = p.get_height()
            text = str(f"%.{decimal}f" % height) if decimal > 0 else str(int(height))
            # text = str(round(height, decimal)) if decimal > 0 else str(int(height))
            ax.text(
                p.get_x() + p.get_width() / 2.0,
                height,
                text,
                fontsize=fontsize,
                color=color,
                ha="center",
                va="bottom",
                rotation=rotation,
            )
    if bar_orient == "horizontal":
        for p in ax.patches:
            width = p.get_width()
            text = str(f"%.{decimal}f" % width) if decimal > 0 else str(int(width))
            # text = str(round(width, decimal)) if decimal > 0 else str(int(width))
            ax.text(
                width,
                p.get_y() + p.get_height() / 2.0,
                text,
                fontsize=fontsize,
                color=color,
                # 'center', 'right', 'left'
                ha="left",
                # 'top', 'bottom', 'center', 'baseline', 'center_baseline'
                va="center_baseline",
                rotation=rotation,
            )


def heatmap(
    data,
    row_labels,
    col_labels,
    ax=None,
    cbar_kw=None,
    cbarlabel="",
    **kwargs,
):
    """
    Create a heatmap from a numpy array and two lists of labels.

    The link of this helper function:
    `https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html`

    Here is the usage example:
        vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
                  "potato", "wheat", "barley"]
        farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
                   "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]
        harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                            [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                            [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                            [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                            [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                            [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                            [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
        fig, ax = plt.subplots()
        im, cbar = heatmap(harvest, vegetables, farmers, ax=ax,
                           cmap="YlGn", cbarlabel="harvest [t/year]")
        texts = annotate_heatmap(im, valfmt="{x:.1f} t")
        fig.tight_layout()
        plt.show()

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

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1] + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - 0.5, minor=True)
    ax.grid(which="minor", color="w", linestyle="-", linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(
    im,
    data=None,
    valfmt="{x:.2f}",
    textcolors=("black", "white"),
    threshold=None,
    **textkw,
):
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
        threshold = im.norm(data.max()) / 2.0

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center", verticalalignment="center")
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


def set_spines_line_width(ax: Axes, left=0.5, top=0, right=0, bottom=0.5):
    """设置坐标轴的粗细"""
    ax.spines["left"].set_linewidth(left)
    ax.spines["top"].set_linewidth(top)
    ax.spines["right"].set_linewidth(right)
    ax.spines["bottom"].set_linewidth(bottom)


def set_figsize(plt, width: float or int = 4, height: float or int = 3):
    """设置图片的大小，单位为英寸"""
    plt.rcParams["figure.figsize"] = (width, height)


def save_pdf(plt, path: str, dpi: int = 300, backup: bool = True):
    """保存为PDF格式的文件。

    Parameters
    ----------
    plt : pyplot
        pyplot别名。
    path : str
        图片路径。
    dpi : int
        dpi大小，默认350。
    backup : bool
        默认为True，表示如果path存在，则备份之前的文件。
    """
    if backup:
        gf.if_path_exist_then_backup(path)
    plt.savefig(path, dpi=dpi, format="pdf")


def save_svg(plt, path: str, dpi: int = 300, backup: bool = True):
    """保存为svg格式的矢量图。

    Parameters
    ----------
    plt : pyplot
        pyplot别名。
    path : str
        图片路径。
    dpi : int
        dpi大小，默认350。
    backup : bool
        默认为True，表示如果path存在，则备份之前的文件。
    """
    if backup:
        gf.if_path_exist_then_backup(path)
    plt.savefig(path, dpi=dpi, format="svg")


def set_ax_space(plt, w: float = 0.2, h: float = 0.2):
    """设置子图间距

    Parameters
    ----------
    plt : pyplot
        pyplot别名。
    w : float
        横向的间距，值为小数，表示横向间距是子图平均宽度的百分比。
    h : float
        纵向的间距，值为小数，表示纵向间距是子图平均高度的百分比。
    """
    plt.tight_layout()
    plt.subplots_adjust(wspace=w, hspace=h)


def set_tick_integer(ax: Axes, axis: str = "both"):
    """设置横纵轴刻度值为整数

    Parameters
    ----------
    ax : Axes
        轴，可以理解为某个子图存放的位置。

    axis : str
        默认值为'both'，表示横纵轴的刻度都设置为整数；可选值维'x'或'y'。

    """
    if axis == "both":
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    elif axis == "x":
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    elif axis == "y":
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    else:
        pass


def set_legend_style(
    ax: Axes,
    title: str = None,
    labels: list = None,
    loc: int or str = 0,
    bbox_to_anchor: tuple = None,
    ncol: int = 1,
    alpha: float = 1.0,
    fontsize: int = None,
    edgecolor: str = "black",
    facecolor: str = "white",
    linewidth: float = 0.5,
    **kws,
):
    """自定义图例的样式。

    Parameters
    ----------
    ax : Axes
        轴，可以理解为某个子图存放的地方。
    title : str
        图例的标题。默认为None，表示不自定义标题，用默认标题。
    labels : list
        图例的标签。默认为None，表示不自定义标签，用默认标签。
    loc : int
        图例的位置。默认为0。\n
        当和bbox_to_anchor一起使用时，loc表示图例身上的哪个点，\n
        例如“左下”，意味着图例的左下角与bbox_to_anchor指定的位置(x,y)重合。
        ```
        0自动，1右上，2左上，3左下，4右下，
        5右边，6左中，7右中，8中下，9中上，10正中
        ```
        也可以使用字符串，
        ```
        'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right',
        'center left', 'center right', 'lower center', 'upper center', 'center'
        ```
    bbox_to_anchor : tuple
        指定图例的锚点位置。
    ncol : int
        图例的列数。
    alpha : float
        图例的透明度。
    fontsize : int
        图例的字体大小。
    edgecolor : str
        图例的边框颜色。
    facecolor : str
        图例的背景颜色。
    linewidth : float
        图例的边框宽度。
    **kws
        其他参数。
    """
    kwargs = locals()

    old_legend = ax.legend_
    old_handles = old_legend.legend_handles
    old_labels = [t.get_text() for t in old_legend.get_texts()]
    old_title = old_legend.get_title().get_text()

    if labels is None:
        kwargs["labels"] = old_labels

    if title is None:
        kwargs["title"] = old_title

    kwargs["handles"] = old_handles
    kws = kwargs.pop("kws", {})
    for k, v in kws.items():
        kwargs[k] = v

    ax = kwargs.pop("ax", ax)
    edgecolor = kwargs.pop("edgecolor", "black")
    facecolor = kwargs.pop("facecolor", "white")
    linewidth = kwargs.pop("linewidth", 0.5)
    alpha = kwargs.pop("alpha", 1.0)

    legend = ax.legend(**kwargs)
    frame = legend.get_frame()
    frame.set_edgecolor(edgecolor)
    frame.set_facecolor(facecolor)
    frame.set_linewidth(linewidth)
    frame.set_alpha(alpha)


def set_legend_outside(ax: Union[Axes, np.ndarray], title: str = "", **kws):
    """设置图例在图片的外侧右下角，默认没有title，没有边框。

    如果ax为Axes，直接设置；
    如果ax为包含Axes的`numpy.ndarray`，则需要打平后再设置。
    """
    if isinstance(ax, Axes):
        axes = [ax]
    else:
        axes = list(ax)

    for i in range(len(axes)):
        if i == len(axes) - 1:
            set_legend_style(
                ax=axes[i],
                title=title,
                loc=3,
                bbox_to_anchor=(1.0, 0.0),
                alpha=0.0,
                **kws,
            )
        else:
            axes[i].legend_.remove()


def set_axis_tick(ax: Axes, axis: str = "y", format="%.2f"):
    """
    横轴或者纵轴的刻度标签的格式，例如，%.2f 表示两位小数；
    %.2e 科学计数法
    """
    if axis == "x":
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(format))
    if axis == "y":
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(format))


def legend_text(
    ax: Axes, text: str, loc=2, fontsize: int = 10, fontcolor: str = "black"
):
    """
    在ax上添加一个仅包含文本的legend

    Args:
        ax (Axes): 子图的轴
        text (str): 要显示的文字内容
        loc (int): legend的位置，1表示右上角，2表示左上角，3表示左下角，4表示右下角
        fontsize (int): 字体大小
        fontcolor (str): 字体颜色

    Returns:
        AnchoredText: 返回AnchoredText实例
    """
    at = AnchoredText(
        text, prop=dict(size=fontsize, color=fontcolor), frameon=True, loc=loc
    )
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(at)
    return at


def set_font(fname: str = "SimSun", fsize: int = 12):
    """
    设置字体；
    若是在windows系统，可以使用SimSun，SimHei，SimKai，SimFang等字体；
    若在linux、macOS系统下，可搜索SimSun.ttf字体安装后使用（必要时候需要重启系统）。

    Args:
        fname (str): 字体的名称。
        fsize (int): 字体的大小。

    Returns:
        None
    """
    # 用来正常显示中文标签
    plt.rcParams["font.sans-serif"].insert(0, fname)
    # 用来设置字体大小
    plt.rcParams["font.size"] = fsize
    # 用来正常显示负号
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["mathtext.fontset"] = "cm"
