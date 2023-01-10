"""
Takes a file of mails deletes whitespaces

"""



def concatenate(mail):


    """
    splits the string by whitespace
    and puts everything together

    e xample@gmail .com
    returns example@gmail.com

    """

    splitted_mail = mail.split()
    new_mail = ""
    for segment in splitted_mail:
        new_mail+=segment.strip()
    return new_mail

def read_file():

    """
    reads the file and takes only the lines that contains something

    email@example.com
    

    email2@example.com
    will return 

    email@example.com
    email2@example.com

    avoiding whitespace jump.
    
    
    """

    file_content = []
    file = open("mails.txt",'r',encoding="utf8")
    
    for line in file:
        if  not len(line.split()) == 0:
            file_content.append(concatenate(line.strip()))


    
    file.close()

    return file_content
    

def create_output(mails):

    """
    generates a new file with the content obtain from the 
    main file.
    """
    file = open("output.txt",'w',encoding="utf8")
    
    for mail in mails:
        file.write(mail+"\n")
    file.close()
def main():

    file_content  = read_file()
    create_output(file_content)


if __name__ == "__main__":

    main()
