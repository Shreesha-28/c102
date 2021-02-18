import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    #to intialize cv2

    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        #read the frames while camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite()method is used to save an image to any storage device
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False

    return img_name
    print("snapshot taken")
    #releases the camera
    videoCaptureObject.release()
    #close all the window that might hv been used during the process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.Arh4BmY3PC2fvROLCjDBktA76t0vCWEKgmNGDFG9A5EuTboOeBOmhwQMvgxF4BSJwzvaRpvi05_Juw8uD-OeIXzWAlkG1BCBpwHRNsRSzATD3Q9dLrcw3N0wRbOXCafPZUJm5PU"
    file=img_name
    file_from=file
    file_to="/testFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=2):
            name=take_snapshot()
            upload_file(name)
main()