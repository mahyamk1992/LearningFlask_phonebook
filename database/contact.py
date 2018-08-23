class Contact:
    first_name = None
    last_name = None
    phone = None
    mobile = None




if __name__ == '__main__':
    c=Contact()
    c.first_name="hasan"
    Contact.first_name="ali"


    print(c.first_name)