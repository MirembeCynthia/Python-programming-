def finding_average():
    #This program computes the average of three exam scores

    s1, s2, s3 = eval(input("Enter three scores separated by commas: "))
    average = (s1 + s2 + s3) / 2
    print("Average score is\n", average)
finding_average() 