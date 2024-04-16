import plotly.express as px
import pandas as pd
from pathlib import Path

data_dir = Path('city=Jakarta')
full_df = pd.DataFrame()

# for parquet_file in data_dir.glob("*.parquet"):
#     print(f"Adding file: {parquet_file}")
#     full_df = pd.concat([full_df, pd.read_parquet(parquet_file)], ignore_index=True)

full_df = pd.concat([full_df, pd.read_parquet("city=Jakarta\part-00000-8bbff892-97d2-4011-9961-703e38972569.c000.snappy.parquet")], ignore_index=True)

full_df['minute_timestamp'] = pd.to_datetime(full_df['pingtimestamp'], unit='s').dt.floor('min')

print(full_df)

sampled_df = full_df[(full_df['pingtimestamp'] > 1555801200) & (full_df['pingtimestamp'] < 1555844400)]

sampled_df = sampled_df.sort_values(by='minute_timestamp')

print(sampled_df)

color_scale = [(0, 'green'), (1,'red')]
fig = px.scatter_mapbox(sampled_df, 
                        lat="rawlat", 
                        lon="rawlng",
                        color="trj_id",
                        zoom=8, 
                        height=800,
                        animation_frame="minute_timestamp")

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()