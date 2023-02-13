#%%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import calplot
import cv2
import calendar
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

#%%
df = pd.read_csv("data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)
df.insert(0, "timestamp", df.index)
df["count"] = 1
#%%
df_weekdays = df.groupby(["author", "weekday"]).sum().reset_index()
cats = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
df_weekdays["weekday"] = pd.Categorical(df_weekdays["weekday"], cats)
df_weekdays = df_weekdays.sort_values("weekday")


# Counts
df_counts = df.drop(columns="timestamp").reset_index()
df_counts["month_date"] = pd.to_datetime(df_counts["timestamp"].dt.strftime("%Y-%m"))

at_df = df_counts[df_counts.author == "Antonio"]
ph_df = df_counts[df_counts.author == "Perlei"]

# Monthly stats by month name
df_months = (
    df_counts.groupby(["author", df_counts.timestamp.dt.month])["words"]
    .sum()
    .reset_index()
)
df_months["timestamp"] = df_months["timestamp"].apply(lambda x: calendar.month_name[x])

# Monthly dates stats
love_words_per_month_date = (
    df_counts.groupby(["author", df_counts.month_date.dt.date])["words"]
    .sum()
    .reset_index()
)

# Monthly stats
love_words_per_month = df_counts.groupby(df_counts.timestamp.dt.month)["words"].sum()
at_words_per_month = at_df.groupby(at_df.timestamp.dt.month)["words"].sum()
ph_words_per_month = ph_df.groupby(ph_df.timestamp.dt.month)["words"].sum()


# Daily dates stats
love_words_per_day_date = (
    df_counts.groupby(["author", df_counts.timestamp.dt.date])["words"]
    .sum()
    .reset_index()
)

# Daily stats
love_words_per_day = df_counts.groupby(df_counts.timestamp.dt.date)["words"].sum()
at_words_per_day = at_df.groupby(at_df.timestamp.dt.date)["words"].sum()
ph_words_per_day = ph_df.groupby(ph_df.timestamp.dt.date)["words"].sum()

love_max_words_per_day = love_words_per_day.max()
love_date_max = love_words_per_day.idxmax().strftime("%d/%m/%Y")
at_max_words_per_day = at_words_per_day.max()
at_date_max = at_words_per_day.idxmax().strftime("%d/%m/%Y")
ph_max_words_per_day = ph_words_per_day.max()
ph_date_max = ph_words_per_day.idxmax().strftime("%d/%m/%Y")

love_min_words_per_day = love_words_per_day.min()
love_date_min = love_words_per_day.idxmin().strftime("%d/%m/%Y")
at_min_words_per_day = at_words_per_day.min()
at_date_min = at_words_per_day.idxmin().strftime("%d/%m/%Y")
ph_min_words_per_day = ph_words_per_day.min()
ph_date_min = ph_words_per_day.idxmin().strftime("%d/%m/%Y")

love_mean_words_per_day = round(love_words_per_day.mean(), 2)
at_mean_words_per_day = round(at_words_per_day.mean(), 2)
ph_mean_words_per_day = round(ph_words_per_day.mean(), 2)


print(f"Max Love: {love_max_words_per_day} words.\n   Date: {love_date_max}")
print(f"Max AT: {at_max_words_per_day} words.\n   Date: {at_date_max}")
print(f"Max PH: {ph_max_words_per_day} words.\n   Date: {ph_date_max}")
print("\n")

print(f"Min Love: {love_min_words_per_day} words.\n   Date: {love_date_min}")
print(f"Min AT: {at_min_words_per_day} words.\n   Date: {at_date_min}")
print(f"Min PH: {ph_min_words_per_day} words.\n   Date: {ph_date_min}")
print("\n")

print(f"Mean Love: {round(love_mean_words_per_day,2)} words.")
print(f"Mean AT: {round(at_mean_words_per_day,2)} words.")
print(f"Mean PH: {round(ph_mean_words_per_day,2)} words.")

metrics_dict = {
    "max": {
        "value": {
            "love": love_max_words_per_day,
            "AT": at_max_words_per_day,
            "PH": ph_max_words_per_day,
        },
        "date": {"love": love_date_max, "AT": at_date_max, "PH": ph_date_max},
    },
    "min": {
        "value": {
            "love": love_min_words_per_day,
            "AT": at_min_words_per_day,
            "PH": ph_min_words_per_day,
        },
        "date": {"love": love_date_min, "AT": at_date_min, "PH": ph_date_min},
    },
    "mean": {
        "value": {
            "love": love_mean_words_per_day,
            "AT": at_mean_words_per_day,
            "PH": ph_mean_words_per_day,
        },
        "date": {"love": "", "AT": "", "PH": ""},
    },
}

# %%
def text_format(color, name, header):
    title = f"<{header} style='text-align: center; color: {color};'>{name}</{header}>"
    return title


def filter_df(
    name=["Antonio", "Perlei"],
    date_min=df.timestamp.min().strftime("%Y/%m/%d"),
    date_max=df.timestamp.max().strftime("%Y/%m/%d"),
):
    df_filtered = df[
        (df.author.isin(name)) & (df.index.to_series().between(date_min, date_max))
    ].sort_index()

    df_filtered.columns = [i.title() for i in df_filtered.columns]

    return df_filtered


def ad_grid(data):
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True)  # Add pagination
    gb.configure_side_bar()  # Add a sidebar
    # gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode="AS_INPUT",
        update_mode="MODEL_CHANGED",
        fit_columns_on_grid_load=False,
        theme="streamlit",  # Add theme color to the table
        enable_enterprise_modules=True,
        height=600,
        width="100%",
        reload_data=True,
    )
    return grid_response


def metrics(max=True, min=True, mean=True):

    fig = go.Figure()

    fig.update_layout(
        height=600, grid={"rows": int(max) + int(min) + int(mean), "columns": 3}
    )

    # Perlei stats
    # max
    c = 0
    if max:
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=ph_max_words_per_day,
                domain={"row": c, "column": 0},
                title=f"Max<br>{ph_date_max}",
            )
        )
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=love_max_words_per_day,
                domain={"row": c, "column": 1},
                title=f"Max<br>{love_date_max}",
            )
        )
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=at_max_words_per_day,
                domain={"row": c, "column": 2},
                title=f"Max<br>{at_date_max}",
            )
        )
        c += 1

    if min:
        # min
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=ph_min_words_per_day,
                domain={"row": c, "column": 0},
                title=f"Min<br>{ph_date_min}",
            )
        )
        # min
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=love_min_words_per_day,
                domain={"row": c, "column": 1},
                title=f"Min<br>{love_date_min}",
            )
        )
        # min
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=at_min_words_per_day,
                domain={"row": c, "column": 2},
                title=f"Min<br>{at_date_min}",
            )
        )
        c += 1
    if mean:
        # mean
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=ph_mean_words_per_day,
                domain={"row": c, "column": 0},
                title="Mean",
            )
        )
        # mean
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=love_mean_words_per_day,
                domain={"row": c, "column": 1},
                title="Mean",
            )
        )
        # mean
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=at_mean_words_per_day,
                domain={"row": c, "column": 2},
                title="Mean",
            )
        )

    return fig


def daily_scatter():
    fig = px.scatter(
        love_words_per_day_date,
        x="timestamp",
        y="words",
        color="author",
        title="Word count per entity",
    )
    return fig


def monthly_bar():
    fig = px.bar(
        love_words_per_month_date,
        x="month_date",
        y="words",
        color="author",
        title="Monthly Word count per entity",
    )
    return fig


def month_bar():
    fig = px.bar(
        df_months,
        x="timestamp",
        y="words",
        color="author",
        title="Week days Chat per entity",
    )
    return fig


def weekday_bar():
    fig = px.bar(
        df_weekdays,
        x="weekday",
        y="words",
        color="author",
        title="Week days Chat per entity",
    )
    return fig


def daily_calender():
    cal = calplot.calplot(
        data=df["words"],
        how="sum",
        cmap="magma_r",
        figsize=(16, 8),
        suptitle="Word count Calender",
    )
    return cal


def image_show(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    fig = px.imshow(img)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    return fig


# %%
