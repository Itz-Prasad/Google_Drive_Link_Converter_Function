# THIS PROGRAM MAKES THE GOOGLE DRIVE SHARE LINK EMBEDDEBLE IN HTML FOR E.G.,IMAGES WITH THE HELP OF FUNCTION.


print("Give space after giving URL as input so as to not open the URL AND Do not give space if you are embedding it in a code ")      # WARNING

old_drive_link = str((input("Enter link : \n")))  #Takes Url as input

# old_drive_link =  "https://drive.google.com/file/d/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/view?usp=sharing"  : FORMAT OF GOOGLE DRIVE SHARE LINK

def Link_Conerter(old_drive_link):
    splited_link = old_drive_link.split("/")        # SPLITS IT INTO A LIST [.....]
    id_part = splited_link[5]      # ACESSES TJE ID PART OF URL

    # print(id_part)    : PRINT IT TO CHECK TH ID PART

    joining_part = "https://drive.google.com/uc?export=view&id="       # THIS PART MAKES LINK EMBEDDEBLE IN HTML

    link_to_embed = joining_part + id_part       # JOINS THE ID AND EMBEDDEBLE PART & GIVES FINAL LINK

    return link_to_embed        # RETURN THE FINAL EMBEDDEBLE LINK

a = Link_Conerter(old_drive_link) # ASSIGN THE FINAL EMBEDDEBLE LINK
print(a) # GET THE FINAL EMBEDDEBLE LINK
