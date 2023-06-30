import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        
    if csv_file.tell() == 0:
        writer.writerow("Name","Age","Contact","E-Mail Id")

    writer.writerow(info_list)

if __name__=='__main__':
    condition= True
    student_num= 1
    while(condition):
        student_info=input("Enter some student infomation for student #{} in the following format[name,age,contact,email id]:".format(student_num))
        print("enterd information" +student_info)
        
        student_info_list=student_info.split(' ')
        print ("entered information:"+str(student_info_list))
        print("\nThe entered information is -\nName :{}\nAge :{}\nContact:{} \nE-Mail Id:{}".format(student_info_list[0] ,student_info_list[1], student_info_list[2] ,student_info_list[3]))

        choice=input ("IS THE ENTERED INFO CORRECT?(YES/NO)- ")
        if choice=="yes":
            write_into_csv(student_info_list)
            check=input("enter(yes/no)if you want to enter infofor another student")
            if (check=="yes"):
                    condition=True
                    student_num=student_num+1
            elif(check=="no"):
                    condition=False
        elif choice =="no":
            print("\nPlease re-enter the values!")

            
        