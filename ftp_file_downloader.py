# FTP File Downloader

import os

console_width = os.get_terminal_size().columns

# main variables
main_objects = {
    'folders': [],
    'files': [],
    # {
    #     'file_name': '',
    #     'file_url': ''
    # }
    'folder_length': 0,
    'file_length': 0, 
    'current_folder': '_root'
    }
root_ftp_url = ''
temp_ftp_url = ''
ftp_url_arr = []
user_option = 0

# fetch ftp data
def fetch_ftp_data(url):
    # gets all the informations of the url (folders and files)
    # adds data to main_objects each time this function is called
    # return main_objects
    print(url)


def download_files():
    # if main_objects.file_length > 0
    #  for file in main_objects.files: => 
    # download to the location with the name
    # create the folder
    # fetch_files(file, folder)
    print("download_files")
    fetch_files({'file_name': 'demo', 'file_url': 'ftp://demo_url'}, 'Demo Folder')
    # pass


def fetch_files(file, folder):
    # download the file to the location
    print(f"File: {file} Folder Name: {folder}")
    # pass

def print_folders():
    # Prints all folders in the location..
    # main_objects['folders']
    print('Prints all folders in the location..')

def move_to_folder():
    _folder_name = input("Enter the folder name....")

    if _folder_name in main_objects['folders']:
        # change the values of temp_ftp_url = '' ftp_url_arr = [] based on the call
        # and call fetch_ftp_data() to refresh main_objects's data
        pass
    else:
        print("Please enter the correct folder name.")
        print_folders()

def return_to_previous_folder():
    # change the values of temp_ftp_url = '' ftp_url_arr = [] based on the call
    # move one step back in the folder tree and fetch fetch_ftp_data
    print(f"Moved one step back:\n The present folder is {main_objects['current_folder']}")


print("Welcome to FTP File Downloader".center(console_width))
print("*******************".center(console_width))

print("NOTE: Open ES File Explore and make your android device as FTP server (can you any other app)".center(console_width))
print("1) Enter the FTP url and select the folder and download the files".center(console_width))
print("*******************".center(console_width))

# FTP link
root_ftp_url = input("Please enter the FTP url: ")
print(root_ftp_url)

# ################################################################

fetch_ftp_data(root_ftp_url)

# start of while
while True:
    print(f"There are {main_objects['folder_length']} folders and {main_objects['file_length']} files in {main_objects['current_folder']}")

    # if both folder and files length is zero then exit
    if main_objects['folder_length'] == 0 and main_objects['file_length'] == 0 and main_objects['current_folder'] == '_root':
        print("+++++++++++++++++++++".center(console_width))
        print("FTP url might be wrong or the folder is empty".center(console_width))
        print("+++++++++++++++++++++".center(console_width))
        break

    # if current_folder not _root and if both folder and files length is zero
    if main_objects['folder_length'] == 0 and main_objects['file_length'] == 0 and main_objects['current_folder'] == '_root':
        print("+++++++++++++++++++++".center(console_width))
        print("The folder is empty".center(console_width))
        return_to_previous_folder()
        print("+++++++++++++++++++++".center(console_width))

    # print when folders and files length is greater than 0
    if main_objects['folder_length'] > 0 and main_objects['file_length'] > 0:
        print(f"""
            Select the following options
            0) You can even do Ctrl + c to quit the program.
            1) Download all {main_objects['file_length']} files.
            2) List all {main_objects['folder_length']} avalable folders.
            3) Total Folders and files in {main_objects['current_folder']}.
            
        """)

        user_option = int(input())

        if user_option == 0:
            break

        if user_option == 1:
            # downloads all the available files int the location
            download_files()

        if user_option == 2:
            # list all folders
            print_folders()

        if user_option == 3:
            print(f"There are {main_objects['folder_length']} folders and {main_objects['file_length']} files in {main_objects['current_folder']}")

    
    # when folder length > 0 and file length == 0
    if main_objects['folder_length'] > 0 and main_objects['file_length'] == 0:
        print(f"""
            Select the following options
            0) You can even do Ctrl + c to quit the program.
            1) List all {main_objects['folder_length']} avalable folders.
            2) Enter folder name to go into the folder.
            3) Total Folders and files in {main_objects['current_folder']}.
        """)

        user_option = int(input())

        if user_option == 0:
            break

        if user_option == 1:
            # list all folders
            print_folders()

        if user_option == 2:
            # Enter folder name to move into this
            move_to_folder()

        if user_option == 3:
            print(f"There are {main_objects['folder_length']} folders and {main_objects['file_length']} files in {main_objects['current_folder']}")
