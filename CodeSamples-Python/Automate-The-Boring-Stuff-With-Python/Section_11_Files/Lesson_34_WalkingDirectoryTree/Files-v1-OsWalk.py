# Import relevant Modules
import os, shutil

# Create a variable for a Backup Folder File Path
backupFolderPath = 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_34_WalkingDirectoryTree\\BackupFiles'

# Check if the Folder exists continue, otherwise create it
if os.path.isdir(backupFolderPath):
    # shutil.copy(os.path.join(folderName, file), os.path.join('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_34_WalkingDirectoryTree\\BackupFiles', file + '.backup'))
    shutil.rmtree(backupFolderPath)
else:
    os.makedirs(backupFolderPath)

# Utilize os.walk() for a specified directory to Print all the Files and Subfolders contained therein
for folderName, subfolders, filenames in os.walk('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python'):
    print('The folder is: \n' + folderName)
    print('\nThe subfolders in: \n' + folderName + ' are: ' + str(subfolders))
    print('\nThe filenames in: \n' + folderName + ' are: ' + str(filenames))
    print()

    # Iterate through Subfolders and delete any Folder called 'fish'
    for subfolder in subfolders:
        if 'fish' in subfolder:
            # os.rmdir(subfolder)       # Debug Dry Run
            print('rmdir on ' + subfolder)

    # Iterate through Subfolders and Backup Python Files
    for file in filenames:
        if file.endswith('.py'):
            # v1 Comment In to create a local backup in the Current Working Directory
            # shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup'))
            
            # v2 Comment In to create a local backup in the BackupFiles Folder
            # shutil.copy(os.path.join(folderName, file), 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_34_WalkingDirectoryTree\\BackupFiles')

            # v3 Comment In to create a local backup in the Current Working Directory
            shutil.copy(os.path.join(folderName, file), os.path.join('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_34_WalkingDirectoryTree\\BackupFiles', file + '.backup'))
            
    # NOT Used, for v1 Loop: Iterate through Subfolders and Delete the Backup Python Files
    for file in filenames:
        if file.endswith('.backup'):
            # Delete a file utilizing os.unlink() from the current working directory
            # os.unlink(file)                   # Debug Print the file to be deleted
            print('os.unlink(file)' + file)     # Debug Print the file to be deleted

# Clean up Backup files created
shutil.rmtree(backupFolderPath)         # Comment In to ensure the Copied files can be verified
