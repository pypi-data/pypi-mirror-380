from __future__ import annotations

import typing
from . import colors as colors_module

if typing.TYPE_CHECKING:
    import polars as pl
    import plotly.graph_objects as go  # type: ignore


def plot_metric_by_category(
    data: pl.DataFrame, metric_column: str, metric_name: str
) -> None:
    import polars as pl
    import plotly.graph_objects as go
    import toolstr

    fig = go.Figure()
    colors = colors_module.get_category_colors()

    project = False

    categories = (
        data.group_by('category')
        .agg(metric=pl.sum(metric_column))
        .sort('metric', descending=True)['category']
    )

    total = data.group_by('timestamp', maintain_order=True).agg(
        pl.sum(metric_column)
    )
    fig.add_trace(
        go.Scatter(
            x=total['timestamp'],
            y=total[metric_column],
            mode='lines',
            name='TOTAL',
            line=dict(color='black', width=5),
            legendgroup='TOTAL',
            customdata=[
                toolstr.format(
                    value, order_of_magnitude=True, decimals=1, prefix='$'
                )
                for value in total[metric_column]
            ],
            line_simplify=False,
            hovertemplate='TOTAL' + ': %{customdata}<extra></extra>',
        )
    )

    for category in categories:
        category_data = data.filter(category=category)
        x = category_data['timestamp']
        y = category_data[metric_column]
        color = colors.get(category, '#e377c2')

        if not project:
            fig.add_trace(
                go.Scatter(
                    x=x,
                    y=y,
                    mode='lines',
                    name=category,
                    line=dict(color=color, width=3),
                    legendgroup=category,
                    customdata=[
                        toolstr.format(
                            value,
                            order_of_magnitude=True,
                            decimals=1,
                            prefix='$',
                        )
                        for value in y
                    ],
                    line_simplify=False,
                    hovertemplate=category + ': %{customdata}<extra></extra>',
                )
            )
        else:
            fig.add_trace(
                go.Scatter(
                    x=x[:-1],
                    y=y[:-1],
                    mode='lines',
                    name=category,
                    line=dict(color=color, width=3),
                    legendgroup=category,
                    customdata=[
                        toolstr.format(
                            value,
                            order_of_magnitude=True,
                            decimals=1,
                            prefix='$',
                        )
                        for value in y[:-1]
                    ],
                    line_simplify=False,
                    hovertemplate=category + ': %{customdata}<extra></extra>',
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=x[-2:],
                    y=y[-2:],
                    mode='lines',
                    line=dict(color=color, width=3, dash='5 3'),
                    marker=dict(size=6),
                    hoverinfo='skip',
                    showlegend=False,
                    legendgroup=category,
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=x[-1:],
                    y=y[-1:],
                    mode='markers',
                    line=dict(color=color, width=3, dash='dot'),
                    marker=dict(size=6),
                    name=category,
                    showlegend=False,
                    legendgroup=category,
                )
            )

    grid_style = dict(
        showgrid=True,  # Show/hide gridlines
        gridwidth=1,  # Width of gridlines
        gridcolor='rgba(128, 128, 128, 0.2)',  # Color with transparency
        griddash='5 3',
    )
    label_style = {'size': 18, 'color': '#000000'}

    fig.update_layout(
        margin=dict(t=55, b=0, l=0, r=0, pad=0),
        title={
            'text': 'Kalshi ' + metric_name + ' By Category',
            'x': 0.5,  # Centers the title
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#000000'},
        },
        yaxis=dict(
            title={'text': metric_name, 'font': label_style, 'standoff': 24},
            range=[
                -total[metric_column][-7:].max() * 0.07,  # type: ignore
                total[metric_column][-7:].max() * 1.1,  # type: ignore
            ],
            fixedrange=False,
            tickfont=label_style,
            tickprefix='$',
            **grid_style,
        ),
        height=600,
        hovermode='x unified',
        xaxis=dict(
            range=['2025-03-01', data['timestamp'].max()],
            title={'font': label_style},
            tickfont=label_style,
            tickformatstops=[
                dict(dtickrange=['M12', None], value='%Y'),
                dict(dtickrange=['M1', 'M12'], value='%Y-%m'),
                dict(dtickrange=[None, 'M1'], value='%Y-%m-%d'),
            ],
            rangeslider=dict(visible=True, thickness=0.1),
            type='date',
            **grid_style,
        ),
        legend=dict(
            orientation='v',
            yanchor='top',
            y=1,
            xanchor='left',
            x=1.02,
            font=label_style,
        ),
        template='plotly_white',
    )
    fig.update_xaxes(hoverformat='%Y-%m-%d')
    hires_config = {
        'toImageButtonOptions': {
            'format': 'png',
            'filename': 'kalshi-volume',
            'height': 600,
            'width': 1000,
            'scale': 2,
        },
        'displayModeBar': False,
    }

    fig.show(config=hires_config)
