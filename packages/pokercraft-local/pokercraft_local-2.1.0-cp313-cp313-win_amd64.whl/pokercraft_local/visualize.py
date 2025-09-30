import logging
import math
import typing
import warnings

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as plgo
import statsmodels.api as smapi
from markdown import markdown
from plotly.subplots import make_subplots

from .bankroll import analyze_bankroll
from .constants import (
    BASE_HTML_FRAME,
    DEFAULT_WINDOW_SIZES,
    HAND_STAGE_TYPE,
    HORIZONTAL_PLOT_DIVIDER,
)
from .data_structures import (
    GeneralSimpleSegTree,
    HandHistory,
    SequentialHandHistories,
    TournamentSummary,
)
from .rust import equity as rust_equity
from .translate import (
    HAND_HISTORY_PLOT_DOCUMENTATIONS,
    TOURNEY_SUMMARY_PLOT_DOCUMENTATIONS,
    Language,
    format_dollar,
    format_percent,
    generate_summary_table_md,
    get_software_credits,
)

logger = logging.getLogger("pokercraft_local.visualize")


def log2_or_nan(x: float | typing.Any) -> float:
    return math.log2(x) if x > 0 else math.nan


def get_historical_charts(
    tournaments: list[TournamentSummary],
    lang: Language,
    *,
    window_sizes: tuple[int, ...] = DEFAULT_WINDOW_SIZES,
) -> plgo.Figure:
    """
    Get historical charts.
    """
    TRKEY_PREFIX: typing.Final[str] = "plot.tourney_summary.historical_performance"

    df_base = pd.DataFrame(
        {
            "Tournament Name": [t.name for t in tournaments],
            "Time": [t.start_time for t in tournaments],
            "Profit": [t.profit for t in tournaments],
            "Rake": [t.rake * t.my_entries for t in tournaments],
            "Profitable": [1 if t.profit > 0 else 0 for t in tournaments],
            "Buy In": [t.buy_in for t in tournaments],
        }
    )
    df_base["Net Profit"] = df_base["Profit"].cumsum()
    df_base["Net Rake"] = df_base["Rake"].cumsum()
    df_base["Ideal Profit"] = df_base["Net Profit"] + df_base["Net Rake"]
    df_base["Max Profit"] = df_base["Net Profit"].cummax()
    df_base["Drawdown"] = df_base["Net Profit"] - df_base["Max Profit"]
    df_base["Max Drawdown"] = df_base["Drawdown"].cummin()
    df_base.index += 1

    # Profitable ratio
    profitable_expanding = df_base["Profitable"].expanding()
    max_rolling_profitable: float = 0
    min_rolling_profitable: float = 1
    df_base["Profitable Ratio"] = (
        profitable_expanding.sum() / profitable_expanding.count()
    )
    for window_size in window_sizes:
        this_title = f"Profitable Ratio W{window_size}"
        df_base[this_title] = (
            df_base["Profitable"].rolling(window_size).sum() / window_size
        )
        max_rolling_profitable = max(max_rolling_profitable, df_base[this_title].max())
        min_rolling_profitable = min(min_rolling_profitable, df_base[this_title].min())

    # Avg buy-in
    buyin_expanding = df_base["Buy In"].expanding()
    df_base["Avg Buy In"] = buyin_expanding.sum() / buyin_expanding.count()
    max_rolling_buyin: float = 0
    min_rolling_buyin: float = 1e9
    for window_size in window_sizes:
        this_title = f"Avg Buy In W{window_size}"
        df_base[this_title] = df_base["Buy In"].rolling(window_size).mean()
        max_rolling_buyin = max(max_rolling_buyin, df_base[this_title].max())
        min_rolling_buyin = min(min_rolling_buyin, df_base[this_title].min())

    figure = make_subplots(
        rows=3,
        cols=1,
        shared_xaxes=True,
        row_titles=[
            lang << f"{TRKEY_PREFIX}.y_axes.net_profit_and_rake",
            lang << f"{TRKEY_PREFIX}.y_axes.profitable_ratio",
            lang << f"{TRKEY_PREFIX}.y_axes.average_buy_in",
        ],
        vertical_spacing=0.01,
    )
    common_options = {"x": df_base.index, "mode": "lines"}

    for col, trkey_suffix in (
        ("Net Profit", "legends.net_profit"),
        ("Net Rake", "legends.net_rake"),
        ("Ideal Profit", "legends.ideal_profit"),
        ("Max Drawdown", "legends.max_drawdown"),
    ):
        figure.add_trace(
            plgo.Scatter(
                y=df_base[col],
                legendgroup="Profit",
                legendgrouptitle_text=lang
                << f"{TRKEY_PREFIX}.legends.profits_and_rakes",
                name=lang << f"{TRKEY_PREFIX}.{trkey_suffix}",
                hovertemplate="%{y:$,.2f}",
                **common_options,
            ),
            row=1,
            col=1,
        )

    def get_translated_column_moving_average(lang: Language, window_size: int) -> str:
        """
        Get translated column name for moving average.
        """
        if window_size == 0:
            return lang << "plot.tourney_summary.historical_performance.legends.since_0"
        else:
            return (
                lang << "plot.tourney_summary.historical_performance.legends.recent"
            ) % (window_size,)

    for window_size in (0,) + window_sizes:
        pr_col = (
            "Profitable Ratio"
            if window_size == 0
            else f"Profitable Ratio W{window_size}"
        )
        figure.add_trace(
            plgo.Scatter(
                y=df_base[pr_col],
                meta=[y * 100 for y in df_base[pr_col]],
                legendgroup="Profitable Ratio",
                legendgrouptitle_text=lang
                << f"{TRKEY_PREFIX}.legends.profitable_ratio",
                name=get_translated_column_moving_average(lang, window_size),
                hovertemplate="%{meta:.2f}%",
                **common_options,
            ),
            row=2,
            col=1,
        )

        avb_col = "Avg Buy In" if window_size == 0 else f"Avg Buy In W{window_size}"
        figure.add_trace(
            plgo.Scatter(
                y=df_base[avb_col],
                legendgroup="Avg Buy In",
                legendgrouptitle_text=lang << f"{TRKEY_PREFIX}.legends.average_buy_in",
                name=get_translated_column_moving_average(lang, window_size),
                hovertemplate="%{y:$,.2f}",
                **common_options,
            ),
            row=3,
            col=1,
        )

    # Update layouts and axes
    figure.update_layout(
        title=lang << f"{TRKEY_PREFIX}.title",
        hovermode="x unified",
        yaxis1={"tickformat": "$"},
        yaxis2={"tickformat": ".2%"},
        yaxis3={"tickformat": "$"},
        xaxis={
            "rangeslider": {"visible": True, "autorange": True},
            "labelalias": {
                i: (lang << f"{TRKEY_PREFIX}.etc.tourney_number") % (i,)
                for i in range(1, len(df_base) + 1)
            },
        },
        legend_groupclick="toggleitem",
    )
    figure.update_traces(
        visible="legendonly",
        selector=(
            lambda barline: (
                barline.name
                in (
                    any_lang << f"{TRKEY_PREFIX}.legends.net_rake"
                    for any_lang in Language
                )
            )
            or any(str(num) in barline.name for num in (100, 400, 800))
        ),
    )
    figure.update_traces(xaxis="x")
    figure.update_yaxes(
        row=2,
        col=1,
        minallowed=0,
        maxallowed=1,
        range=[min_rolling_profitable - 0.015, max_rolling_profitable + 0.015],
    )
    figure.update_yaxes(
        row=3,
        col=1,
        patch={
            "type": "log",
            "range": [
                math.log10(max(min_rolling_buyin, 0.1)) - 0.05,
                math.log10(max(max_rolling_buyin, 0.1)) + 0.05,
            ],
            "nticks": 8,
        },
    )
    figure.update_xaxes(
        autorange=True,
        minallowed=1,
        maxallowed=len(df_base),
        rangeslider_thickness=0.075,
    )
    figure.update_yaxes(fixedrange=False)

    # Hlines
    OPACITY_RED = "rgba(255,0,0,0.3)"
    OPACITY_BLUE = "rgba(0,0,255,0.3)"
    OPACITY_BLACK = "rgba(0,0,0,0.3)"
    OPACITY_PURPLE = "rgba(171,99,250,0.5)"
    figure.add_hline(
        y=0.0,
        line_color=OPACITY_RED,
        line_dash="dash",
        row=1,
        col=1,
        label={
            "text": lang << f"{TRKEY_PREFIX}.horizontal_lines.break_even",
            "textposition": "end",
            "font": {"color": OPACITY_RED, "weight": 1000, "size": 18},
            "yanchor": "top",
        },
        exclude_empty_subplots=False,
    )
    figure.add_hline(
        y=df_base["Net Profit"].iat[-1],
        line_color=OPACITY_BLUE,
        line_dash="dash",
        row=1,
        col=1,
        label={
            "text": lang << f"{TRKEY_PREFIX}.horizontal_lines.current_net_profit",
            "textposition": "start",
            "font": {"color": OPACITY_BLUE, "weight": 1000, "size": 18},
            "yanchor": "bottom",
        },
    )
    figure.add_hline(
        y=df_base["Max Drawdown"].min(),
        line_color=OPACITY_PURPLE,
        line_dash="dash",
        row=1,
        col=1,
        label={
            "text": lang << f"{TRKEY_PREFIX}.horizontal_lines.max_drawdown",
            "textposition": "start",
            "font": {"color": OPACITY_PURPLE, "weight": 1000, "size": 18},
            "yanchor": "bottom",
        },
    )
    for threshold, trkey_suffix in [
        (5.0, "micro_low"),
        (20.0, "low_mid"),
        (100.0, "mid_high"),
    ]:
        figure.add_hline(
            y=threshold,
            line_color=OPACITY_BLACK,
            line_dash="dash",
            row=3,
            col=1,
            label={
                "text": lang << f"{TRKEY_PREFIX}.horizontal_lines.{trkey_suffix}",
                "textposition": "start",
                "font": {"color": OPACITY_BLACK, "weight": 1000, "size": 18},
                "yanchor": "top",
            },
            exclude_empty_subplots=False,
        )
    figure.update_shapes(xref="x domain", xsizemode="scaled", x0=0, x1=1)

    return figure


def get_profit_heatmap_charts(
    tournaments: list[TournamentSummary],
    lang: Language,
) -> plgo.Figure:
    """
    Get profit scatter charts.
    """
    TRKEY_PREFIX: typing.Final[str] = "plot.tourney_summary.rre"

    df_base = pd.DataFrame(
        {
            "Tournament Name": [t.name for t in tournaments],
            "Buy In": [t.buy_in for t in tournaments],
            "RRE": [t.rre for t in tournaments],
            "Prize Ratio": [
                t.my_prize / t.total_prize_pool if t.total_prize_pool > 0 else math.nan
                for t in tournaments
            ],
            "Total Entries": [t.total_players for t in tournaments],
            "Profitable": [t.profit > 0 for t in tournaments],
            "Weekday": [t.time_of_week[0] for t in tournaments],
            "TimeOfDay": [t.time_of_week[1] for t in tournaments],
        }
    )

    BLACK_WHITE_COLORSCALE: typing.Final[list[list]] = [
        [0, "rgba(255, 255, 255, 0.6)"],
        [1, "rgba(0, 0, 0, 0.6)"],
    ]
    GOT_X_PROFIT: typing.Final[str] = (
        lang << f"{TRKEY_PREFIX}.cell_overlay.got_x_profit"
    )

    figure = make_subplots(
        1,
        4,
        shared_yaxes=True,
        column_titles=[
            lang << f"{TRKEY_PREFIX}.x_axes.by_buy_in",
            lang << f"{TRKEY_PREFIX}.x_axes.by_total_entries",
            lang << f"{TRKEY_PREFIX}.x_axes.by_time_of_day",
            lang << f"{TRKEY_PREFIX}.x_axes.marginal",
        ],
        y_title=lang << f"{TRKEY_PREFIX}.y_axis",
        horizontal_spacing=0.01,
        column_widths=[0.2, 0.2, 0.2, 0.1],
    )
    fig1_common_options = {
        "y": df_base["RRE"].apply(log2_or_nan),
        "ybins": {"size": 0.5, "start": -3},
        "z": df_base["RRE"],
        "coloraxis": "coloraxis",
        "histfunc": "sum",
    }
    figure.add_trace(
        plgo.Histogram2d(
            x=df_base["Buy In"].apply(log2_or_nan),
            name=lang << f"{TRKEY_PREFIX}.cell_overlay.rre_by_buy_in",
            hovertemplate="Log2(RRE) = [%{y}]<br>Log2("
            + (lang << f"{TRKEY_PREFIX}.cell_overlay.formula.buy_in")
            + ") = [%{x}]<br>"
            + (GOT_X_PROFIT % ("%{z:.3f}",)),
            **fig1_common_options,
        ),
        row=1,
        col=1,
    )
    figure.add_trace(
        plgo.Histogram2d(
            x=df_base["Total Entries"].apply(log2_or_nan),
            name=lang << f"{TRKEY_PREFIX}.cell_overlay.rre_by_entries",
            hovertemplate="Log2(RRE) = [%{y}]<br>Log2("
            + (lang << f"{TRKEY_PREFIX}.cell_overlay.formula.total_entries")
            + ") = [%{x}]<br>"
            + (GOT_X_PROFIT % ("%{z:.3f}",)),
            xbins={"start": 1.0, "size": 1.0},
            **fig1_common_options,
        ),
        row=1,
        col=2,
    )
    figure.add_trace(
        plgo.Histogram2d(
            x=df_base["TimeOfDay"],
            name=lang << f"{TRKEY_PREFIX}.cell_overlay.rre_by_time_of_day",
            hovertemplate="Log2(RRE) = [%{y}]<br>"
            + (lang << f"{TRKEY_PREFIX}.cell_overlay.formula.time_of_day")
            + " = [%{x}] mins<br>"
            + (GOT_X_PROFIT % ("%{z:.3f}",)),
            xbins={"start": 0.0, "size": 60.0 * 2, "end": 60.0 * 24},
            **fig1_common_options,
        ),
        row=1,
        col=3,
    )

    # Marginal distribution
    figure.add_trace(
        plgo.Histogram(
            x=df_base["RRE"],
            y=fig1_common_options["y"],
            name=lang << f"{TRKEY_PREFIX}.cell_overlay.marginal_rre",
            histfunc=fig1_common_options["histfunc"],
            orientation="h",
            ybins=fig1_common_options["ybins"],
            hovertemplate="Log2(RRE) = [%{y}]<br>" + (GOT_X_PROFIT % ("%{x:.3f}",)),
            marker={"color": "rgba(70,70,70,0.35)"},
        ),
        row=1,
        col=4,
    )

    figure.update_layout(
        title=lang << f"{TRKEY_PREFIX}.title",
        title_subtitle_text=lang << f"{TRKEY_PREFIX}.subtitle",
        title_subtitle_font_style="italic",
    )
    figure.update_coloraxes(colorscale=BLACK_WHITE_COLORSCALE)

    for y, color, trkey_suffix in [
        (0.0, "rgb(140, 140, 140)", "horizontal_lines.break_even"),
        (2.0, "rgb(90, 90, 90)", "horizontal_lines.good_run"),
        (5.0, "rgb(40, 40, 40)", "horizontal_lines.deep_run"),
    ]:
        for col in range(1, 4):
            figure.add_hline(
                y=y,
                line_color=color,
                line_dash="dash",
                row=1,
                col=col,
                label={
                    "text": lang << f"{TRKEY_PREFIX}.{trkey_suffix}",
                    "textposition": "start",
                    "font": {"color": color, "weight": 1000, "size": 16},
                    "yanchor": "bottom",
                },
            )

    figure.update_xaxes(fixedrange=True)
    figure.update_yaxes(fixedrange=True)
    return figure


def get_bankroll_charts(
    tournaments: list[TournamentSummary],
    lang: Language,
    *,
    initial_capitals: typing.Iterable[int] = (10, 20, 50, 100, 200, 500),
    min_simulation_iterations: int,
    simulation_count: int,
) -> plgo.Figure | None:
    """
    Get bankroll charts.
    """
    TRKEY_PREFIX: typing.Final[str] = "plot.tourney_summary.bankroll"
    INITIAL_CAPITAL: typing.Final[str] = lang << f"{TRKEY_PREFIX}.x_axis"
    BANKRUPTCY_RATE: typing.Final[str] = (
        lang << f"{TRKEY_PREFIX}.legends.bankruptcy_rate"
    )
    SURVIVAL_RATE: typing.Final[str] = lang << f"{TRKEY_PREFIX}.legends.survival_rate"

    try:
        analyzed = analyze_bankroll(
            tournaments,
            initial_capital_and_exits=tuple((ic, 0.0) for ic in initial_capitals),
            max_iteration=max(min_simulation_iterations, len(tournaments) * 10),
            simulation_count=simulation_count,
        )
    except ValueError as err:
        warnings.warn(
            (
                "Bankroll analysis failed with reason(%s)."
                " Perhaps your relative returns are losing."
            )
            % (err,)
        )
        return None
    else:
        df_base = pd.DataFrame(
            {
                INITIAL_CAPITAL: [
                    (lang << f"{TRKEY_PREFIX}.x_labels") % (k,) for k in analyzed.keys()
                ],
                BANKRUPTCY_RATE: [v.get_bankruptcy_rate() for v in analyzed.values()],
                SURVIVAL_RATE: [v.get_survival_rate() for v in analyzed.values()],
            }
        )

    figure = px.bar(
        df_base,
        x=INITIAL_CAPITAL,
        y=[BANKRUPTCY_RATE, SURVIVAL_RATE],
        title=lang << f"{TRKEY_PREFIX}.title",
        color_discrete_sequence=["rgb(242, 111, 111)", "rgb(113, 222, 139)"],
        text_auto=True,
    )
    figure.update_traces(hovertemplate="%{x}: %{y:.2%}")
    figure.update_xaxes(fixedrange=True)
    figure.update_yaxes(
        tickformat=".2%",
        minallowed=0.0,
        maxallowed=1.0,
        fixedrange=True,
    )
    figure.update_layout(
        modebar_remove=["select2d", "lasso2d"],
        legend_title_text=lang << f"{TRKEY_PREFIX}.legends.title",
        yaxis_title=None,
        title_subtitle_text=lang << f"{TRKEY_PREFIX}.subtitle",
        title_subtitle_font_style="italic",
    )
    return figure


def get_profit_pies(
    tournaments: list[TournamentSummary],
    lang: Language,
) -> plgo.Figure:
    """
    Get pie charts of absolute profits
    from past tournament summaries.
    """
    TRKEY_PREFIX: typing.Final[str] = "plot.tourney_summary.prize_pie"

    weekday_strs = [
        lang << f"{TRKEY_PREFIX}.cell_overlay.{s.lower()}"
        for s in ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    ]
    df_base = pd.DataFrame(
        {
            "ID": [t.id for t in tournaments],
            "Tournament Name": [t.name_with_date() for t in tournaments],
            "Prize": [t.my_prize for t in tournaments],
            "Date": [t.start_time for t in tournaments],
            "Weekday": [weekday_strs[t.time_of_week[0]] for t in tournaments],
        }
    )
    total_prizes: float = df_base["Prize"].sum()

    figure = make_subplots(
        2,
        1,
        specs=[[{"type": "pie"}], [{"type": "sunburst"}]],
        horizontal_spacing=0.01,
        vertical_spacing=0.01,
    )

    df_main = df_base.copy(deep=True)
    other_condition = df_main["Prize"] < total_prizes * 0.01
    df_main.loc[other_condition, "ID"] = 0
    df_main.loc[other_condition, "Tournament Name"] = "Others"
    df_main.loc[other_condition, "Date"] = math.nan
    df_main = df_main.groupby("ID").aggregate(
        {"Prize": "sum", "Tournament Name": "first", "Date": "first"}
    )
    figure.add_trace(
        plgo.Pie(
            labels=df_main["Tournament Name"],
            values=df_main["Prize"],
            name=lang << f"{TRKEY_PREFIX}.cell_overlay.individual_prizes",
        ),
        row=1,
        col=1,
    )

    df_weekday = df_base.copy(deep=True)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)
        for weekday_idx, weekday_str in enumerate(weekday_strs):
            df_weekday.loc[-1] = {
                "ID": weekday_str,
                "Tournament Name": f"{weekday_str}",
                "Prize": df_weekday[df_weekday["Weekday"] == weekday_str][
                    "Prize"
                ].sum(),
                "Weekday": weekday_str,
            }
            df_weekday.index = df_weekday.index + 1
    df_weekday = df_weekday.sort_index()
    df_weekday["Parent"] = df_weekday.apply(
        (lambda r: r["Weekday"] if r["ID"] != r["Weekday"] else ""),
        axis=1,
    )
    df_weekday = df_weekday[df_weekday["Prize"] > 0.005 * total_prizes]
    figure.add_trace(
        plgo.Sunburst(
            labels=df_weekday["Tournament Name"],
            parents=df_weekday["Parent"],
            values=df_weekday["Prize"],
            maxdepth=2,
            name=lang << f"{TRKEY_PREFIX}.cell_overlay.prizes_by_weekday",
        ),
        row=2,
        col=1,
    )

    figure.update_traces(
        row=1,
        col=1,
        showlegend=False,
        pull=[0.075 if id_ == 0 else 0 for id_ in df_main.index],
    )
    figure.update_traces(hovertemplate="%{label}: %{value:$,.2f}")
    figure.update_layout(
        title=lang << f"{TRKEY_PREFIX}.title",
        title_subtitle_text=lang << f"{TRKEY_PREFIX}.subtitle",
        title_subtitle_font_style="italic",
    )
    return figure


def get_rr_by_rank_chart(
    tournaments: list[TournamentSummary], lang: Language
) -> plgo.Figure:
    """
    Get `RR by Rank Percentile` chart.
    """
    TRKEY_PREFIX: typing.Final[str] = "plot.tourney_summary.rr_by_rank"

    df_base = pd.DataFrame(
        {
            "Rank": [t.my_rank for t in tournaments],
            "Rank Percentile": [t.my_rank / t.total_players for t in tournaments],
            "RR": [t.rrs[-1] + 1.0 if t.rrs else math.nan for t in tournaments],
            "Name": [
                "%s (%s)" % (t.name, t.start_time.strftime("%Y%m%d"))
                for t in tournaments
            ],
            "Total Players": [t.total_players for t in tournaments],
        }
    )
    df_base["Percentile mul RR"] = df_base["Rank Percentile"] * df_base["RR"]
    df_base = df_base[df_base["RR"] > 0.0]
    max_rr = df_base["RR"].max()
    best_percentile_log = math.log10(df_base["Rank Percentile"].min())

    # Linear regression
    df_hhh_only = df_base[df_base["Rank Percentile"] <= 1 / 8.0].copy()
    df_hhh_only["RR"] = df_hhh_only["RR"].apply(log2_or_nan)
    df_hhh_only["Rank Percentile"] = df_hhh_only["Rank Percentile"].apply(log2_or_nan)
    fit_results = (
        smapi.OLS(
            df_hhh_only["RR"],
            smapi.add_constant(df_hhh_only["Rank Percentile"]),
            missing="drop",
        )
        .fit()
        .predict()
    )
    df_hhh_only["Fitted"] = fit_results
    df_hhh_only["Fitted"] = df_hhh_only["Fitted"].apply(lambda x: 2**x)
    df_hhh_only["RR"] = df_hhh_only["RR"].apply(lambda x: 2**x)
    df_hhh_only["Rank Percentile"] = df_hhh_only["Rank Percentile"].apply(
        lambda x: 2**x
    )

    COMMON_CUSTOM_DATA = np.stack(
        (
            df_base["Name"],
            df_base["Total Players"],
            df_base["Rank"],
            df_base["RR"],
            df_base["Percentile mul RR"],
        ),
        axis=-1,
    )
    COMMON_OPTIONS = {
        "x": df_base["Rank Percentile"],
        "mode": "markers",
        "customdata": COMMON_CUSTOM_DATA,
        "hovertemplate": lang << f"{TRKEY_PREFIX}.hovertemplate",
    }

    figure = make_subplots(specs=[[{"secondary_y": True}]])
    figure.add_trace(
        plgo.Scatter(
            y=df_base["RR"],
            name=lang << f"{TRKEY_PREFIX}.legends.rr_by_percentile",
            **COMMON_OPTIONS,
        )
    )
    figure.add_trace(
        plgo.Scatter(
            y=df_base["Percentile mul RR"],
            name=lang << f"{TRKEY_PREFIX}.legends.perr",
            visible="legendonly",
            marker_color="#BB75FF",
            **COMMON_OPTIONS,
        ),
        secondary_y=True,
    )
    figure.add_trace(
        plgo.Scatter(
            x=df_hhh_only["Rank Percentile"],
            y=df_hhh_only["Fitted"],
            name=lang << f"{TRKEY_PREFIX}.legends.rr_trendline",
            showlegend=True,
            mode="lines",
            hoverinfo="skip",
            marker_color="RGBA(54,234,201,0.4)",
        )
    )
    figure.update_layout(
        title=lang << f"{TRKEY_PREFIX}.title",
        title_subtitle_text=lang << f"{TRKEY_PREFIX}.subtitle",
        title_subtitle_font_style="italic",
        xaxis_title=lang << f"{TRKEY_PREFIX}.x_axis",
    )
    OPACITY_RED = "rgba(255,0,0,0.3)"
    OPACITY_GRAY = "rgb(180,180,180)"
    OPACITY_GREEN = "rgba(74,131,78,0.7)"
    figure.add_vline(x=1.0, line_dash="dash", line_color=OPACITY_GRAY)
    figure.add_vline(
        x=1 / 8.0,
        line_dash="dash",
        line_color=OPACITY_GREEN,
        label={
            "text": lang << f"{TRKEY_PREFIX}.lines.rough_itm_cut",
            "font": {"size": 16, "color": OPACITY_GREEN, "weight": 1000},
            "textposition": "end",
            "xanchor": "right",
        },
    )
    figure.add_hline(
        y=1.0,
        line_dash="dash",
        line_color=OPACITY_RED,
        label={
            "text": lang << f"{TRKEY_PREFIX}.lines.break_even",
            "font": {"size": 28, "color": OPACITY_RED, "weight": 1000},
            "textposition": "end",
            "yanchor": "top",
        },
    )
    figure.update_xaxes(
        type="log",
        range=[0, best_percentile_log - 0.2],
        minallowed=-7.0,
        maxallowed=1.0,
        tickformat=",.2%",
        dtick=0.5,
    )
    figure.update_yaxes(
        type="log",
        minallowed=-2.0,
        maxallowed=7.0,
        range=[-1.0, math.log10(max(max_rr, 1)) + 0.1],
        autorange=False,
        title_text="RR",
        secondary_y=False,
    )
    figure.update_yaxes(
        type="log",
        range=[math.log10(0.01), math.log10(0.75)],
        title_text="PERR",
        secondary_y=True,
        autorange=False,
    )
    return figure


def get_summaries(tournaments: list[TournamentSummary]) -> list[tuple[str, typing.Any]]:
    """
    Get summaries from tournament results.
    """
    TRKEY_PREFIX: typing.Final[str] = "plot.tourney_summary.head_summaries"

    df_base = pd.DataFrame(
        {
            "Time": [t.start_time for t in tournaments],
            "Profit": [t.profit for t in tournaments],
            "Rake": [t.rake * t.my_entries for t in tournaments],
            "Profitable": [1 if t.profit > 0 else 0 for t in tournaments],
            "Buy In": [t.buy_in for t in tournaments],
            "Entries": [t.my_entries for t in tournaments],
        }
    )
    df_base["Net Profit"] = df_base["Profit"].cumsum()
    df_base["Max Profit"] = df_base["Net Profit"].cummax()
    df_base["Drawdown"] = df_base["Net Profit"] - df_base["Max Profit"]
    net_profit = df_base["Profit"].sum()
    total_buy_in = df_base["Buy In"].sum()

    return [
        (f"{TRKEY_PREFIX}.net_profit", format_dollar(net_profit)),
        (f"{TRKEY_PREFIX}.roi", format_percent(net_profit / total_buy_in)),
        (
            f"{TRKEY_PREFIX}.profitable_ratio",
            format_percent(df_base["Profitable"].sum() / len(df_base)),
        ),
        (f"{TRKEY_PREFIX}.paid_rake", format_dollar(df_base["Rake"].sum())),
        (f"{TRKEY_PREFIX}.total_entries", "#%d" % (df_base["Entries"].sum(),)),
        (f"{TRKEY_PREFIX}.highest_buy_in", format_dollar(df_base["Buy In"].max())),
        (f"{TRKEY_PREFIX}.max_drawdown", format_dollar(df_base["Drawdown"].min())),
    ]


def plot_tournament_summaries(
    nickname: str,
    tournaments: typing.Iterable[TournamentSummary],
    lang: Language = Language.ENGLISH,
    *,
    sort_key: typing.Callable[[TournamentSummary], typing.Any] = (
        lambda t: t.sorting_key()
    ),
    window_sizes: tuple[int, ...] = DEFAULT_WINDOW_SIZES,
    bankroll_simulation_count: int = 25_000,
    bankroll_min_simulation_iterations: int = 40_000,
) -> str:
    """
    Generate all chart reports from tournament summaries
    and return a complete HTML string.
    """
    tournaments = sorted(tournaments, key=sort_key)
    figures: list[plgo.Figure | None] = [
        get_historical_charts(
            tournaments,
            lang,
            window_sizes=window_sizes,
        ),
        get_profit_heatmap_charts(tournaments, lang),
        get_bankroll_charts(
            tournaments,
            lang,
            simulation_count=bankroll_simulation_count,
            min_simulation_iterations=bankroll_min_simulation_iterations,
        ),
        get_profit_pies(tournaments, lang),
        get_rr_by_rank_chart(tournaments, lang),
    ]
    return BASE_HTML_FRAME.format(
        title=(lang << "plot.tourney_summary.title") % (nickname,),
        summary=markdown(
            generate_summary_table_md(lang, *get_summaries(tournaments)),
            extensions=["tables"],
        ),
        plots=HORIZONTAL_PLOT_DIVIDER.join(  # type: ignore[var-annotated]
            fig.to_html(include_plotlyjs=("cdn" if i == 0 else False), full_html=False)
            + markdown(doc_dict[lang])
            for i, (doc_dict, fig) in enumerate(
                zip(TOURNEY_SUMMARY_PLOT_DOCUMENTATIONS, figures, strict=True)
            )
            if fig is not None
        ),
        software_credits=get_software_credits(lang),
    )


def get_all_in_equity_histogram(
    hand_histories: list[HandHistory],
    lang: Language,
    *,
    max_length: int = -1,
) -> plgo.Figure:
    """
    Get all-in win/lose histogram.
    """
    TRKEY_PREFIX: typing.Final[str] = "plot.hand_history.all_in_equity"

    all_in_hand_histories = list(
        filter(
            lambda h: (
                (h.all_ined_street("Hero") in ("preflop", "flop", "turn"))
                and len(h.showdown_players()) >= 2
            ),
            hand_histories,
        )
    )
    if max_length > 0:
        all_in_hand_histories = all_in_hand_histories[
            : min(max_length, len(all_in_hand_histories))
        ]

    all_in_streets: list[typing.Literal["preflop", "flop", "turn"]] = typing.cast(
        list[typing.Literal["preflop", "flop", "turn"]],
        [h.all_ined_street("Hero") for h in all_in_hand_histories],
    )
    logger.info(
        "Total %d all-in hands found. "
        "Preflop all-in = %d hands, preflop heads-up all-in = %d hands",
        len(all_in_hand_histories),
        all_in_streets.count("preflop"),
        sum(
            1
            for hh, street in zip(all_in_hand_histories, all_in_streets)
            if street == "preflop" and len(hh.showdown_players()) == 2
        ),
    )

    equities_by_streets: list[dict[HAND_STAGE_TYPE, dict[str, tuple[float, bool]]]] = []
    for i, h in enumerate(all_in_hand_histories):
        eqd = h.calculate_equity_arbitrary(
            "Hero",
            *(player_id for player_id in h.showdown_players() if player_id != "Hero"),
            stages=(all_in_streets[i],),
        )
        equities_by_streets.append(eqd)
        if (i + 1) % 50 == 0:
            logger.info("Calculated equity for %d all-in hands", i + 1)

    was_best_hands = [h.was_best_hand("Hero") for h in all_in_hand_histories]
    MAIN_COLUMN_NAME: typing.Final[str] = "Hero Equity"
    df_base = pd.DataFrame(
        {
            "Hand ID": [h.id for h in all_in_hand_histories],
            "Tournament ID": [h.tournament_id or 0 for h in all_in_hand_histories],
            MAIN_COLUMN_NAME: [
                eqd[street]["Hero"][0]
                for street, eqd in zip(all_in_streets, equities_by_streets)
            ],
            "Actual Got": [0 if wbh < 0 else 1.0 / (wbh + 1) for wbh in was_best_hands],
        }
    )

    UPPER_LIMIT = 0.99
    LOWER_LIMIT = 1 - UPPER_LIMIT
    df_winning = df_base[df_base["Actual Got"] > UPPER_LIMIT]
    df_chopped = df_base[
        (UPPER_LIMIT >= df_base["Actual Got"]) & (df_base["Actual Got"] > LOWER_LIMIT)
    ]
    df_losing = df_base[df_base["Actual Got"] <= LOWER_LIMIT]

    luckscore_calculator = rust_equity.LuckCalculator()
    for row in df_base.itertuples(index=False):
        equity = row[2]
        actual = row[3]
        luckscore_calculator.add_result_py(equity, actual)
    luck_score = luckscore_calculator.luck_score_py()
    upper_tail, lower_tail, twosided = luckscore_calculator.tails_py()
    logger.info(
        "All-in luck score Z = %.6g, upper tail = %.6f, "
        "lower tail = %.6f, two-sided = %.6f",
        luck_score,
        upper_tail,
        lower_tail,
        twosided,
    )

    OPACITY_GREEN = "rgba(52,203,59,0.8)"
    OPACITY_YELLOW = "rgba(204,198,53,0.8)"
    OPACITY_RED = "rgba(206,37,37,0.8)"

    with np.errstate(divide="ignore", invalid="ignore"):
        bins = np.linspace(0.0, 1.0, 21)
        win_hist, _win_edges = np.histogram(df_winning[MAIN_COLUMN_NAME], bins)
        chop_hist, _chop_edges = np.histogram(df_chopped[MAIN_COLUMN_NAME], bins)
        lose_hist, _lose_edges = np.histogram(df_losing[MAIN_COLUMN_NAME], bins)
        sum_hist = win_hist + chop_hist + lose_hist
        bin_centers = (bins[1:] + bins[:-1]) / 2.0
        bin_widths = np.diff(bins)

        figure = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.01,
        )
        common_customdata = np.stack(
            (
                win_hist,
                chop_hist,
                lose_hist,
                bin_centers - bin_widths / 2.0,
                bin_centers + bin_widths / 2.0,
            ),
            axis=-1,
        )
        common_options: dict = {
            "x": bin_centers,
            "width": bin_widths,
            "customdata": common_customdata,
        }
        for bar in [
            plgo.Bar(
                y=win_hist,
                base=chop_hist / 2.0,
                name=lang << f"{TRKEY_PREFIX}.legends.hero_won",
                hovertemplate=lang << f"{TRKEY_PREFIX}.hovertemplates.hero_won",
                marker_color=OPACITY_GREEN,
                legendgroup=lang << f"{TRKEY_PREFIX}.legends.hero_won",
                **common_options,
            ),  # Winning histogram
            plgo.Bar(
                y=chop_hist,
                base=-chop_hist / 2.0,
                name=lang << f"{TRKEY_PREFIX}.legends.chopped",
                hovertemplate=lang << f"{TRKEY_PREFIX}.hovertemplates.chopped",
                marker_color=OPACITY_YELLOW,
                legendgroup=lang << f"{TRKEY_PREFIX}.legends.chopped",
                **common_options,
            ),  # Chopped histogram
            plgo.Bar(
                y=lose_hist,
                base=-chop_hist / 2.0 - lose_hist,
                name=lang << f"{TRKEY_PREFIX}.legends.hero_lost",
                hovertemplate=lang << f"{TRKEY_PREFIX}.hovertemplates.hero_lost",
                marker_color=OPACITY_RED,
                legendgroup=lang << f"{TRKEY_PREFIX}.legends.hero_lost",
                **common_options,
            ),  # Losing histogram
        ]:
            figure.add_trace(bar, row=1, col=1)

        common_options["showlegend"] = False
        for bar in [
            plgo.Bar(
                y=win_hist / sum_hist,
                base=1 - win_hist / sum_hist,
                name=lang << f"{TRKEY_PREFIX}.legends.hero_won",
                hovertemplate=lang << f"{TRKEY_PREFIX}.hovertemplates.hero_won",
                marker_color=OPACITY_GREEN,
                legendgroup=lang << f"{TRKEY_PREFIX}.legends.hero_won",
                **common_options,
            ),  # Winning histogram
            plgo.Bar(
                y=chop_hist / sum_hist,
                base=lose_hist / sum_hist,
                name=lang << f"{TRKEY_PREFIX}.legends.chopped",
                hovertemplate=lang << f"{TRKEY_PREFIX}.hovertemplates.chopped",
                marker_color=OPACITY_YELLOW,
                legendgroup=lang << f"{TRKEY_PREFIX}.legends.chopped",
                **common_options,
            ),  # Chopped histogram
            plgo.Bar(
                y=lose_hist / sum_hist,
                # base=0.0,  # No base set
                name=lang << f"{TRKEY_PREFIX}.legends.hero_lost",
                hovertemplate=lang << f"{TRKEY_PREFIX}.hovertemplates.hero_lost",
                marker_color=OPACITY_RED,
                legendgroup=lang << f"{TRKEY_PREFIX}.legends.hero_lost",
                **common_options,
            ),  # Losing histogram
        ]:
            figure.add_trace(bar, row=2, col=1)

    figure.add_shape(
        type="line",
        x0=0.0,
        x1=1.0,
        y0=1.0,
        y1=0.0,
        line={"color": "rgba(0,0,0,0.25)", "dash": "dash"},
        row=2,
        col=1,
    )

    figure.update_layout(
        barmode="overlay",
        title={
            "text": lang << f"{TRKEY_PREFIX}.title",
            "subtitle": {
                "text": (lang << f"{TRKEY_PREFIX}.subtitle").format(
                    luck_score=luck_score,
                    tail=100 * (1 - lower_tail),
                ),
                "font": {"style": "italic"},
            },
        },
        modebar_remove=["select2d", "lasso2d"],
    )
    figure.update_xaxes(fixedrange=True)
    figure.update_yaxes(fixedrange=True)
    figure.update_xaxes(
        title={"text": lang << f"{TRKEY_PREFIX}.x_axis"},
        tickformat=".2%",
        range=[0.0, 1.0],
        row=2,
        col=1,
    )
    figure.update_yaxes(
        showticklabels=False,
        title={"text": lang << f"{TRKEY_PREFIX}.y_axis1"},
        row=1,
        col=1,
    )
    figure.update_yaxes(
        title={"text": lang << f"{TRKEY_PREFIX}.y_axis2"},
        tickformat=".0%",
        range=[0.0, 1.0],
        row=2,
        col=1,
    )
    return figure


def get_chip_histories(
    hand_histories: list[HandHistory],
    lang: Language,
) -> plgo.Figure:
    """
    Extract chip histories from hand histories.
    Max sampling is not applied here.
    """
    THIS_TRKEY_PREFIX: typing.Final[str] = "plot.hand_history.chip_histories"
    figure = make_subplots(
        2,
        2,
        specs=[
            [{"colspan": 2}, None],
            [{}, {}],
        ],
        vertical_spacing=0.06,
        horizontal_spacing=0.1,
    )

    # Gather data, and also add each tourney chip history
    total_tourneys: int = 0
    died_at: list[int] = []
    max_hand_lengths: int = 1
    death_thresholds: list[float] = [
        3 / 4,
        3 / 5,
        1 / 2,
        2 / 5,
        1 / 3,
        1 / 4,
        1 / 5,
        1 / 8,
        1 / 10,
    ]
    death_threshold_count: dict[float, int] = {th: 0 for th in death_thresholds}

    # Iterate each tourney
    for sequential_hand_histories in SequentialHandHistories.generate_sequences(
        hand_histories
    ):
        first_hh = sequential_hand_histories.histories[0]
        if first_hh.tournament_id is None:
            warnings.warn(
                "Dropping non-tournament hand histories(%d histories found).."
                % (len(sequential_hand_histories.histories),)
            )
            continue

        total_tourneys += 1
        chip_history_raw = sequential_hand_histories.generate_chip_history()
        initial_chips = chip_history_raw[0]

        # Build segtree to analyze several attributes
        chip_history_segtree_max = GeneralSimpleSegTree(chip_history_raw, max)

        # Death threshold
        for threshold in death_thresholds:
            if all(
                chip_history_segtree_max.get(idx, len(chip_history_raw)) <= v
                for idx, v in enumerate(chip_history_raw)
                if v <= threshold * chip_history_segtree_max.get(0, idx + 1)
            ):
                death_threshold_count[threshold] += 1

        # Chip history raw is manipulated for plot from here
        if chip_history_raw[-1] <= 0:
            died_at.append(len(chip_history_raw))
        while chip_history_raw[-1] == 0:
            chip_history_raw.pop()
        max_hand_lengths = max(max_hand_lengths, len(chip_history_raw))

        chip_history = np.array(chip_history_raw)
        chip_history = np.multiply(chip_history, 1.0 / initial_chips)
        figure.add_trace(
            plgo.Scatter(
                x=np.arange(len(chip_history)) + 1,
                y=chip_history,
                mode="lines",
                name=sequential_hand_histories.get_name(),
                hovertemplate=lang
                << f"{THIS_TRKEY_PREFIX}.hovertemplates.chip_histories",
            ),
            row=1,
            col=1,
        )

    # Danger line
    x_danger_line = np.arange(max_hand_lengths) + 1
    danger_func = lambda x: np.maximum(
        np.exp(x / 100.0 * math.log(10)) * 1.4e-2, 1.0 / 3
    )
    COLOR_DANGER_LINE = "rgba(33,33,33,0.33)"
    figure.add_trace(
        plgo.Scatter(
            x=x_danger_line,
            y=danger_func(x_danger_line),
            mode="lines",
            line={"dash": "dash", "color": COLOR_DANGER_LINE},
            name=lang << f"{THIS_TRKEY_PREFIX}.names.danger_line",
            hoverinfo="none",
        ),
        row=1,
        col=1,
    )
    DANGER_ANNOTATION_X = 0.75 * max_hand_lengths
    figure.add_annotation(
        x=DANGER_ANNOTATION_X,
        y=math.log10(danger_func(DANGER_ANNOTATION_X)),
        text=lang << f"{THIS_TRKEY_PREFIX}.names.danger_line",
        showarrow=False,
        font={"size": 24, "color": COLOR_DANGER_LINE, "weight": 1000},
        yanchor="top",
        xanchor="left",
        row=1,
        col=1,
    )

    # Died at histogram
    COLOR_DIED_AT = "rgba(38,210,87,0.9)"
    died_at_xbins = np.arange(max_hand_lengths) + 1
    died_at_histogram_y, died_at_histogram_x = np.histogram(
        died_at, bins=died_at_xbins, density=True
    )
    died_at_histogram_y = 1.0 - died_at_histogram_y.cumsum() * (
        len(died_at) / total_tourneys
    )  # Tourneys with 1st are excluded from `died_at`
    figure.add_trace(
        plgo.Bar(
            x=died_at_histogram_x,
            y=died_at_histogram_y,
            marker_color=COLOR_DIED_AT,
            name=lang << f"{THIS_TRKEY_PREFIX}.names.died_at",
            hovertemplate=lang << f"{THIS_TRKEY_PREFIX}.hovertemplates.died_at",
        ),
        row=2,
        col=1,
    )

    # Died at average
    COLOR_DIED_AT_AVG = "rgba(12,17,166,0.7)"
    died_at_avg = np.mean(died_at)
    figure.add_vline(
        x=died_at_avg,
        line_dash="dash",
        line_color=COLOR_DIED_AT_AVG,
        label={
            "text": (lang << f"{THIS_TRKEY_PREFIX}.names.died_at_avg") % (died_at_avg,),
            "font": {"color": COLOR_DIED_AT_AVG, "weight": 1000},
            "textposition": "end",
            "xanchor": "right",
        },
        row=2,
        col=1,
    )

    # Death threshold
    COLOR_DEATH_THRESHOLD = "rgba(222,118,177,0.9)"
    sorted_death_thresholds = sorted(death_thresholds, reverse=True)
    figure.add_trace(
        plgo.Bar(
            x=["%2gx" % (threshold,) for threshold in sorted_death_thresholds],
            y=[
                death_threshold_count[th] / total_tourneys
                for th in sorted_death_thresholds
            ],
            marker_color=COLOR_DEATH_THRESHOLD,
            name=lang << f"{THIS_TRKEY_PREFIX}.names.death_threshold",
            hovertemplate=lang << f"{THIS_TRKEY_PREFIX}.hovertemplates.death_threshold",
        ),
        row=2,
        col=2,
    )

    # All other settings
    figure.update_layout(
        title=lang << f"{THIS_TRKEY_PREFIX}.title",
        showlegend=False,
    )
    figure.update_xaxes(
        minallowed=0,
        maxallowed=max_hand_lengths + 1,
        title=lang << f"{THIS_TRKEY_PREFIX}.x_axes.chip_histories",
        row=1,
        col=1,
    )
    figure.update_yaxes(
        minallowed=-2.25,
        type="log",
        title=lang << f"{THIS_TRKEY_PREFIX}.y_axes.chip_histories",
        row=1,
        col=1,
    )
    figure.update_xaxes(
        minallowed=1,
        maxallowed=max_hand_lengths + 1,
        title=lang << f"{THIS_TRKEY_PREFIX}.x_axes.died_at",
        row=2,
        col=1,
    )
    figure.update_yaxes(
        minallowed=0.0,
        maxallowed=1.0,
        title=lang << f"{THIS_TRKEY_PREFIX}.y_axes.died_at",
        tickformat=".2%",
        row=2,
        col=1,
    )
    figure.update_xaxes(
        title=lang << f"{THIS_TRKEY_PREFIX}.x_axes.death_threshold",
        row=2,
        col=2,
    )
    figure.update_yaxes(
        minallowed=0.0,
        maxallowed=1.0,
        title=lang << f"{THIS_TRKEY_PREFIX}.y_axes.death_threshold",
        tickformat=".2%",
        row=2,
        col=2,
    )
    return figure


def plot_hand_histories(
    nickname: str,
    hand_histories: typing.Iterable[HandHistory],
    lang: Language = Language.ENGLISH,
    *,
    max_sampling: int | None = None,
    sort_key: typing.Callable[[HandHistory], typing.Any] = (lambda h: h.sorting_key()),
) -> str:
    """
    Generate hand history analysis HTML report.
    """
    hand_histories = sorted(hand_histories, key=sort_key)
    figures: list[plgo.Figure | None] = [
        get_all_in_equity_histogram(
            hand_histories,
            lang,
            max_length=max_sampling if max_sampling else -1,
        ),
        get_chip_histories(hand_histories, lang),
    ]

    return BASE_HTML_FRAME.format(
        title=(lang << "plot.hand_history.title") % (nickname,),
        summary=markdown("No summary yet.."),
        plots=HORIZONTAL_PLOT_DIVIDER.join(
            fig.to_html(include_plotlyjs=("cdn" if i == 0 else False), full_html=False)
            + markdown(HAND_HISTORY_PLOT_DOCUMENTATIONS[i][lang])
            for i, fig in enumerate(figures)
            if fig is not None
        ),
        software_credits=get_software_credits(lang),
    )
