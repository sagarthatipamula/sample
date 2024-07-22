# myapp/views.py
import json
import os
import pandas as pd
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required
from pkg_resources import require

from .models import UploadedFile
from datetime import datetime, timezone
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import os
import base64
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import logging
from django.utils import timezone
logger = logging.getLogger(__name__)


def read_excel(search_value, name, staffid_col, user_active_col):
    folderpath = "Application Files/" + name
    dirfiles = [f for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]

    df = pd.DataFrame()

    for file in dirfiles:
        fname = folderpath + "/" + file
        df = df._append(pd.read_excel(fname))

    return transform_data(df, search_value, name, staffid_col, user_active_col)


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


x = {
    "Samplefile1": read_excel,
    "Samplefile2": read_excel,
    "Samplefile3": read_excel
}


@csrf_protect
def search_api(request, file_name, search_value):
    # Split the search_values string into a list of individual search values
    search_values_list = search_value.split(',')

    print(f"Received request - File Name: {file_name}, Search Values: {search_values_list}")

    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_file_path = os.path.join(base_dir, 'new_config.json')

        with open(config_file_path) as file:
            data = json.load(file)

        result_dataframe = pd.DataFrame(columns=['app_name', 'status'])

        if file_name.lower() == 'all':
            # Search across all files
            for i in data:
                for search_value in search_values_list:
                    df = x[i["name"]](search_value.strip(), i["name"], i["staffid_col"], i["user_active_col"])
                    result_dataframe = result_dataframe._append(df)
        else:
            # Search within a specific file
            for i in data:
                if i["name"].lower() == file_name.lower():
                    for search_value in search_values_list:
                        df = x[i["name"]](search_value.strip(), i["name"], i["staffid_col"], i["user_active_col"])
                        result_dataframe = result_dataframe._append(df)
                    break

        # Drop duplicates based on 'app_name' column
        result_dataframe = result_dataframe.drop_duplicates(subset='app_name')

        # Convert result_dataframe to dictionary format
        response_data = result_dataframe.to_dict(orient='records')

        print(response_data)
        return JsonResponse(response_data, safe=False)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return JsonResponse({"error": error_message}, status=500)


# Additional function to render the search page with file names
def show_search_page(request):
    # Fetch the file names from your data source
    file_names = ['All', 'Samplefile1', 'Samplefile2', 'Samplefile3']
    return render(request, 'myapp/search_page.html', {'file_names': file_names})


# myapp/views.py
@csrf_exempt
@login_required()
def upload_file(request):
    if request.method == "POST":
        try:
            user = request.user
            print(user)
            folder_name = request.POST.get('fileName', '')
            file_name = request.POST.get('AttachmentName', '')
            file_data = request.POST.get('AttachmentBytes', '')
            uploaded_file = UploadedFile(user=user, file_name=file_name, uploaded_at=timezone.now())
            print(uploaded_file)
            uploaded_file.save()
            file_decode_data = base64.b64decode(file_data.encode())

            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            print(base_dir)
            destination_folder = os.path.join(base_dir, 'Application Files', folder_name)
            print(destination_folder)
            file_path = os.path.join(destination_folder, file_name)
            print(file_name)
            archive_folder = os.path.join(destination_folder, 'Archive')
            os.makedirs(archive_folder, exist_ok=True)

            existing_files = [item for item in os.listdir(destination_folder) if
                              os.path.isfile(os.path.join(destination_folder, item))]

            for existing_file in existing_files:
                if existing_file != 'Archive':
                    existing_file_path = os.path.join(destination_folder, existing_file)
                    archive_file_path = os.path.join(archive_folder, existing_file)

                    if os.path.exists(archive_file_path):
                        file_name, file_extension = os.path.splitext(existing_file)
                        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                        new_file_name = f"{file_name}_{timestamp}{file_extension}"
                        os.rename(existing_file_path, os.path.join(archive_folder, new_file_name))
                    else:
                        os.rename(existing_file_path, archive_file_path)

            with open(file_path, 'wb') as destination:
                destination.write(file_decode_data)

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        file_names = ["Samplefile1", "Samplefile2", "Samplefile3"]
        return render(request, 'myapp/upload.html', {"filename": file_names})


# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)
#
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
def show_login_page(request):
    return render(request, 'myapp/login.html')


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user already exists
        user, created = User.objects.get_or_create(username=username)

        # If the user is newly created, set the password
        if created:
            user.set_password(password)
            user.save()

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Login successful'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def get_upload_history(request):
    # Retrieve all upload history records
    upload_history = UploadedFile.objects.all()

    # Print details of each record
    for history in upload_history:
        print(f"Application Name: {history.application_name}")
        print(f"Uploaded By: {history.uploaded_by.username}")
        print(f"Uploaded At: {history.uploaded_at}")
        print("\n")

    return JsonResponse({'status': 'success'})


@require_GET
def get_folder_names(request):
    try:
        folder_names = ["Samplefile1", "Samplefile2", "Samplefile3"]  # Replace with your logic
        return JsonResponse({"folder_names": folder_names})
    except Exception as e:
        logger.error(f"Error getting folder names: {e}")
        return JsonResponse({"error": "Unable to retrieve folder names"})
