file = input("File name: ").lower().strip()

if "." in file:
    filename , type = file.rsplit(".", 1)

    if type == 'gif':
        print('image/gif')
    elif type == 'jpg' or type == 'jpeg':
        print('image/jpeg')
    elif type == 'png':
        print('image/png')
    elif type == 'pdf':
        print('application/pdf')
    elif type == 'txt':
        print('text/plain')
    elif type == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')

else:
    print('application/octet-stream')
