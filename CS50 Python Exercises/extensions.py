# Solution 1
'''def main():
    # Take file name from user
    file = input("File Name: ").lower()
    separated = file.split(".")
    extension = separated[-1].strip()
    media_type = check_media_type_case(extension)
    print(media_type)
    #media_type = check_media_type_if(file)
    #print(media_type)


def check_media_type_case(extension):
    match extension:
        case "jpeg" | "jpg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "gif":
            return "image/gif"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


if __name__ == '__main__':
    main()
'''

# check if .extension is "in" name for all cases
'''def check_media_type_if(file_name):
    if ".jpeg" in file_name:
        return "image/jpeg"
    elif ".gif" in file_name:
        return "image/gif"
    elif ".jpg" in file_name:
        return "image/jpeg"
    elif ".png" in file_name:
        return "image/png"
    elif ".pdf" in file_name:
        return "application/pdf"
    elif ".txt" in file_name:
        return "text/plain"
    elif ".zip" in file_name:
        return "application/zip"
    else:
        return "application/octet-stream"'''




# Solution 2
ext_vs_media = { "jpeg" : "image/jpeg",
                "jpg" : "image/jpeg",
                "png" : "image/png",
                "gif" : "image/gif",
                "txt" : "text/plain",
                "pdf" : "application/pdf",
                "zip" : "application/zip",
                "No_Extension_Found" : "application/octet-stream"
}

file_name = input("File Name: ").lower()
separated = file_name.split(".")
ext = separated[-1].strip()
try:
    media_type = ext_vs_media[ext]
except KeyError:
    print(ext_vs_media["No_Extension_Found"])
else:
    print(media_type)
