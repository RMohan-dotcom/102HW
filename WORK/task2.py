import cv2
import dropbox
import random
import time

start_time = time.time()


def take_screenshot():
    number= random.randint(0,100)
    result= True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = input('name your file')
        element.screenshot(img_name)
        
        start_time = time.time
        result = False
    return img_name
    print("screenshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BHTw2cGZZMfIyeCPmnvFtPEHiMJbgY9HMY2_lnKaSLDKbJFVcsMi5G24Q22rM2IEF1Y7vcSdS9hhyFAXTNfsHC7SZYg1qHVXCKkyxCoIiyou0T3s_IjMSg_UxKlrpFj3N7PJ4qLkK7k"
    file =img_name
    file_from = file
    file_to = "/Pictures/test/"+(img_name)
    dbx= dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("PICTURE IS UPLOADED")

def main():
    while(True):
        if((time.time() - start.time) >= 5):
            name = take_screenshot()
            upload_file(name)

main()
