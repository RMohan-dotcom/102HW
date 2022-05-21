import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BHR7v49QnHBZHZSJ4OVai7yWRxeaAEgrQl2gRlE750Y9RvqVTCSkju3pnXtVPiiAykM5xhTm0Z-9fISjHU0wcqlKxxM8d45F6sn2QopDJLXdJp50MzhNrXWw-Mvai4T_aIsfA9Q9tUs'
    transferData = TransferData(access_token)

    folder_from = input("Enter the file path to transfer : -")
    folder_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_folder(folder_from, folder_to)
    print("file has been moved !!!")


main()
