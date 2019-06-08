from pyecharts import options as opts
from pyecharts.charts import Bar3D


def dataFrame2list(pd_complete):
    data = []
    npdata = pd_complete.to_numpy()
    for i in range(len(npdata)):
        for j in range(len(npdata[i])):
            data.append([pd_complete.index[i], pd_complete.columns[j], npdata[i][j]])
    return data


def bar3d_base(pd_complete) -> Bar3D:
    data = dataFrame2list(pd_complete)
    max_ = max(data)
    return Bar3D().set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=max_[2]),
        title_opts=opts.TitleOpts(title="Bar3D"),
    ).add(
        "",
        data,
        xaxis3d_opts=opts.Axis3DOpts(type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )

"""
bar3d_base(dm.load("new_found_relation")(p.getObjectPair("objectB")[0],
                                         p.getObjectPair("objectA")[0],
                                         p.getDIFF_NewFoundRelationPair()[0])).render_notebook()
"""
