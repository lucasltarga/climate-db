def export_to_csv(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

def export_to_json(dataframe, file_path):
    dataframe.to_json(file_path, orient='records', lines=True)