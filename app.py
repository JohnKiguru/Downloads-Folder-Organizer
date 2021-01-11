import os,shutil

def move_file(file,path):
    shutil.move(file,path)

def perform_copy(join_path,file,copy_path):
    shutil.copy(os.path.join(join_path,file),copy_path)    

def organizeDownloads():
    '''
    Go inside my Downloads folder :
    If a file is a pdf, create a folder named PDF_Files and move all pdf there.
    Create a backup folder with files in the documents folder C:\\Users\\JS Pundit\\Documents\\Backup_Captures
    If a file is a video with .mp4 ,create videos file and move them there : Backup in C:\\Users\\JS Pundit\\Videos\\Captures
    If a file is a .exe create a programs folder
    '''
    if os.path.exists("C:\\Users\\JS Pundit\\Downloads"):
        print("About to sort Your Downloads ....")
        os.chdir("C:\\Users\\JS Pundit\\Downloads")
        downloaded_files=os.listdir()
        
        for file in downloaded_files:

            if file.endswith(".mp4"):
                if os.path.exists("C:\\Users\\JS Pundit\\Downloads\\videos"):
                    move_file(file,"C:\\Users\\JS Pundit\\Downloads\\videos")
                    perform_copy("C:\\Users\\JS Pundit\\Downloads\\videos",file,"C:\\Users\\JS Pundit\\Videos")
                    
                else:

                    os.makedirs("C:\\Users\\JS Pundit\\Downloads\\videos")
                    move_file(file,"C:\\Users\\JS Pundit\\Downloads\\videos")
                    perform_copy("C:\\Users\\JS Pundit\\Downloads\\videos",file,"C:\\Users\\JS Pundit\\Videos")
                    
                    
            elif file.endswith(".pdf"):

                if os.path.exists("C:\\Users\\JS Pundit\\Downloads\\PDF_Files"):

                    move_file(file,"C:\\Users\\JS Pundit\\Downloads\\PDF_Files")

                    perform_copy("C:\\Users\\JS Pundit\\Downloads\\PDF_Files",file,"C:\\Users\\JS Pundit\\Documents\\PDF_Backup")
                    
                else:

                    os.makedirs("C:\\Users\\JS Pundit\\Downloads\\PDF_Files")
                    move_file(file,"C:\\Users\\JS Pundit\\Downloads\\PDF_Files")
                    perform_copy("C:\\Users\\JS Pundit\\Downloads\\PDF_Files",file,"C:\\Users\\JS Pundit\\Documents\\PDF_Backup")
                    

            elif file.endswith(".exe") or file.endswith(".msi") or file.endswith(".webm"):
                
                if os.path.exists("C:\\Users\\JS Pundit\\Downloads\\Programs"):
                    move_file(file,"C:\\Users\\JS Pundit\\Downloads\\Programs")
                else:

                     os.makedirs("C:\\Users\\JS Pundit\\Downloads\\Programs")
                     move_file(file,"C:\\Users\\JS Pundit\\Downloads\\Programs")

            elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                if os.path.exists("C:\\Users\\JS Pundit\\Downloads\\Pics"):
                    move_file(file,"C:\\Users\\JS Pundit\\Downloads\\Pics")
                else:
                    os.makedirs("C:\\Users\\JS Pundit\\Downloads\\Pics")
                    move_file(file,"C:\\Users\\JS Pundit\\Downloads\\Pics")            
            else:
                print("This file sorts is of unsupported format:)")                                    
    print("100% ..Done")

organizeDownloads()