import pandas as pd

def process_csv(reader, writer):
    writer.write(f"Station Name,Date,Min Temp,Max Temp,First Temp,Last Temp\n")
    df = pd.read_csv(reader)
    df['date'] = pd.to_datetime(df['Measurement Timestamp']).dt.strftime('%m/%d/%Y')
    df['Measurement Timestamp'] = pd.to_datetime(df['Measurement Timestamp'])
    df = df.sort_values(['Station Name', 'Measurement Timestamp'])
    df = df.groupby(['Station Name', 'date']).agg({'Air Temperature': ['min', 'max', 'first', 'last']})
    for i_row in df.iterrows():
        writer.write(f"{i_row[0][0]},{i_row[0][1]},{i_row[1][('Air Temperature', 'min')]},{i_row[1][('Air Temperature', 'max')]},{i_row[1][('Air Temperature', 'first')]},{i_row[1][('Air Temperature', 'last')]}\n")
