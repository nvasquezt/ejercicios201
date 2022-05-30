def sector(x,y):
    cord_x=float(x)
    cord_y=float(y)

    if cord_x < 3 or cord_x > 8 or cord_y <3 or cord_y>10:
        print("Deniska ha escapado")
    elif (cord_x==2 and cord_y== 3)or(cord_x==2 and cord_y== 9)or(cord_x==5 and cord_y== 6)or(cord_x==8 and cord_y== 3)or(cord_x==8 and cord_y== 9):
        print("")
    elif (cord_x>=2 and cord_x<5) and (cord_y>6 and cord_y<=10):
        print("S1")
    elif (cord_x>5 and cord_x<=8) and (cord_y>6 and cord_y<=10):
        print("S2")
    elif (cord_x>=2 and cord_x<5) and (cord_y>=3 and cord_y<6):
        print("S3")
    elif (cord_x>5 and cord_x<=8) and (cord_y>=3 and cord_y<6):
        print("S4")
    elif cord_x==5 and (cord_y>6 and cord_y<=10):
        print("Deniska está entre el Sector 1 y 2")
    elif cord_x==5 and (cord_y>=3 and cord_y<6):
        print("Deniska está entre el Sector 3 y 4")
    elif (cord_x>=2 and cord_x<5) and  cord_y==6:
        print("Deniska está entre el Sector 1 y 3")
    elif (cord_x>5 and cord_x<=8) and cord_y==6:
        print("Deniska está entre el Sector 2 y 4")

sector(5,4)
sector(8,2.1)
sector(-1.1,2.4)
sector(6,7.1)
sector(4,6)
sector(6,5)
sector(2,3)
sector(6,7)
sector(100,200)

