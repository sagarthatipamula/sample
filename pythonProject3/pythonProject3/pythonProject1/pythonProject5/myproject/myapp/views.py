# myapp/views.py
import json
import os
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render

def read_excel(folderpath, staffid_col, user_active_col):
    dirfiles = [f for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]
    df = pd.DataFrame()

    for file in dirfiles:
        fname = os.path.join(folderpath, file)
        df = df._append(pd.read_excel(fname))

    return df

def transform_data(df, search_value, name, staffid_col, user_active_col):
    filtered_df = df.loc[df[staffid_col].str.strip().str.lower() == search_value.strip().lower()].copy()

    if filtered_df.shape[0] > 0:
        filtered_df.loc[:, 'app_name'] = name
        filtered_df.loc[:, 'status'] = filtered_df.apply(
            lambda x: filtered_df[user_active_col] if len(user_active_col) > 0 else "Active", axis=1
        )
        filtered_df.loc[:, 'enabled'] = ""  # You can replace this with your logic for 'enabled'

        filtered_df2 = filtered_df[['app_name', 'status', 'enabled']]
        return filtered_df2

    return pd.DataFrame(columns=['app_name', 'status', 'enabled'])

def search_api(request, file_name, search_value):
    print(f"Received request - File Name: {file_name}, Search Value: {search_value}")
    search_value = search_value.lower()

    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_file_path = os.path.join(base_dir, 'new_config.json')

        with open(config_file_path) as file:
            data = json.load(file)

        result_dataframe = pd.DataFrame(columns=['app_name', 'status'])

        if file_name.lower() == 'all':
            # Search across all files
            for i in data:
                df = read_excel(os.path.join(base_dir, 'Application Files', i["name"]),
                                i["staffid_col"], i["user_active_col"])
                result_dataframe = result_dataframe._append(transform_data(df, search_value, i["name"],
                                                                          i["staffid_col"], i["user_active_col"]))
        else:
            # Search within a specific file
            for i in data:
                if i["name"].lower() == file_name.lower():
                    df = read_excel(os.path.join(base_dir, 'Application Files', i["name"]),
                                    i["staffid_col"], i["user_active_col"])
                    result_dataframe = result_dataframe._append(transform_data(df, search_value, i["name"],
                                                                              i["staffid_col"], i["user_active_col"]))
                    break

        response_data = result_dataframe.to_dict(orient='records')
        print(response_data)
        return JsonResponse(response_data, safe=False)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return JsonResponse({"error": error_message}, status=500)

# Additional function to render the search page with file names
def show_search_page(request):
    # Fetch the file names from your data source
    file_names = ['Samplefile1', 'Samplefile2', 'Samplefile3']
    return render(request, 'myapp/search_page.html', {'file_names': file_names})
