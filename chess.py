import pygame

pygame.init()

PATH=r"C:\Users\HP\Contacts\3D Objects"
x_points=[80*i for i in range(9)]
y_points=[80*i for i in range(9)]
RUN=True



#loading all the sprites into the code
d_brown=pygame.image.load(PATH+"\dbrown.png")
l_brown=pygame.image.load(PATH+"\lbrown.png")
grey=pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\thefk.png")
black=[[pygame.image.load(PATH+"\pawn.png"),0,80,0],[pygame.image.load(PATH+"\pawn.png"),80,80,0],[pygame.image.load(PATH+"\pawn.png"),160,80,0],[pygame.image.load(PATH+"\pawn.png"),240,80,0],[pygame.image.load(PATH+"\pawn.png"),320,80,0],[pygame.image.load(PATH+"\pawn.png"),400,80,0],[pygame.image.load(PATH+"\pawn.png"),480,80,0],[pygame.image.load(PATH+"\pawn.png"),560,80,0],[pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\rook.png"),0,0],[pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\horse.png"),80,0],[pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\bishop.png"),160,0],[pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\queen.png"),240,0],[pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\keng.png"),320,0],[pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\bishop.png"),400,0],[pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\horse.png"),480,0],[pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\rook.png"),560,0]]
white=[[pygame.image.load(PATH+"\w_pawn.png"),0,480,0],[pygame.image.load(PATH+"\w_pawn.png"),80,480,0],[pygame.image.load(PATH+"\w_pawn.png"),160,480,0],[pygame.image.load(PATH+"\w_pawn.png"),240,480,0],[pygame.image.load(PATH+"\w_pawn.png"),320,480,0],[pygame.image.load(PATH+"\w_pawn.png"),400,480,0],[pygame.image.load(PATH+"\w_pawn.png"),480,480,0],[pygame.image.load(PATH+"\w_pawn.png"),560,480,0],[pygame.image.load(PATH+"\w_rook.png"),0,560],[pygame.image.load(PATH+"\w_horse.png"),80,560],[pygame.image.load(PATH+"\w_bishop.png"),160,560],[pygame.image.load(PATH+"\w_queen.png"),240,560],[pygame.image.load(PATH+"\w_keng.png"),320,560],[pygame.image.load(PATH+"\w_bishop.png"),400,560],[pygame.image.load(PATH+"\w_horse.png"),480,560],[pygame.image.load(PATH+"\w_rook.png"),560,560]]
red=pygame.image.load(r"C:\Users\HP\Contacts\3D Objects\red.jpg")

#screen setting
W,H=640,640
screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("CHESS(MERENEMAZZ)")

#function to draw the chess board
def draw_board(win):
    #below code builds and blits the board in a horizondal manner where cnt(1,cnt1(1-->8)--->8)
    cnt=1
    global x_points,y_points,temp,grey_list_points,xclicked,yclicked,fk

    while cnt<=8:
        if not(cnt%2==0):
            cnt1=1
            while cnt1<=8:
                if not(cnt1%2==0):
                    win.blit(d_brown,(x_points[cnt1-1],y_points[cnt-1]))
                else:
                    win.blit(l_brown,(x_points[cnt1-1],y_points[cnt-1]))
                cnt1+=1
            
        else :
           cnt1=1
           while cnt1<=8:
                if not(cnt1%2==0):
                    win.blit(l_brown,(x_points[cnt1-1],y_points[cnt-1]))
                else:
                    win.blit(d_brown,(x_points[cnt1-1],y_points[cnt-1]))

                cnt1+=1
        cnt+=1
    if element or element==0:
        for points in grey_list_points:
            win.blit(grey,(points[0],points[1]))
            
            
    if len(temp.keys())>1:
        grey_list_points=[]
        temp={}
    
    if checkmate()[0]:
        win.blit(red,checkmate()[1])

def draw_piece(win):
    for piece in black:
        if piece:
            win.blit(piece[0],(piece[1],piece[2]))

    for piece in white:
        if piece:
            win.blit(piece[0],(piece[1],piece[2]))

    pygame.display.update()


def is_clicked(x_pos,y_pos):
    
    global x_points,y_points,xclicked,yclicked,element,player_list,opposition_list,sprite,temp,grey_list_points,Turn,dont_change,RUN
    
    
    for i in range(len(x_points)-1):
        if x_pos>=x_points[i] and x_pos<x_points[i+1] :
            xclicked=x_points[i]
        
    for i in range(len(y_points)-1):
        if y_pos>=y_points[i] and y_pos<y_points[i+1] :
            yclicked=y_points[i]

    temp_list=[(i[1],i[2]) if bool(i) else 0 for i in player_list]


    
    if (xclicked,yclicked) in grey_list_points:
        player_list[element][1],player_list[element][2]=xclicked,yclicked

        if element<=7:
            player_list[element][3]+=1

        """if check(xclicked,yclicked):
            
            fk=True
            pygame.display.update()"""
        Turn+=1
        grey_list_points=[]
        cond=checkhit(xclicked,yclicked)[::2]
        if cond[0]:
            opposition_list[cond[1]]=0
            if opposition_list[12]==0:
                RUN=False
            
            element=None
    if not(dont_change):
        if (xclicked,yclicked) in temp_list:
            element=temp_list.index((xclicked,yclicked))
            temp[element]=None
        else:
            element=None
    sprite=[xclicked,yclicked,element]
    

def movement(x,y):
    global element,x_points,y_points,grey_list_points,P,player_list
    #x,y=sprite[:2]
    
    if element or element==0:
        #PAWN MOVEMENTS
        if element<=7:
            if player_list[element][3]==0:
                for i in range(2):
                    if checkhit(x,y_points[y_points.index(y)+P+P*i])[0] or checkhit(x,y_points[y_points.index(y)+P+P*i])[1]:
                        break
                    else:
                        grey_list_points.append((x,y_points[y_points.index(y)+P+P*i]))
            else:
                if not(checkhit(x,y_points[y_points.index(y)+P])[0]):
                    grey_list_points.append((x,y_points[y_points.index(y)+P]))
            if checkhit(x_points[x_points.index(x)+1],y_points[y_points.index(y)+P])[0]:
                grey_list_points.append((x_points[x_points.index(x)+1],y_points[y_points.index(y)+P]))
            if checkhit((x_points[x_points.index(x)-1]),y_points[y_points.index(y)+P])[0]:
                grey_list_points.append((x_points[x_points.index(x)-1],y_points[y_points.index(y)+P]))

        #ROOK MOVEMENTS
        if element==8 or element==15:
            lxb=x_points[:x_points.index(x)]#lxb--->list of X below
            lxa=x_points[x_points.index(x)+1:]#lxa--->list of X above
            lyb=y_points[:y_points.index(y)]#same for Y
            lya=y_points[y_points.index(y)+1:]# ""
            for point in lxb[::-1]:
                cond=checkhit(point,y)
                
                if cond[0] or cond[1]:
                    if cond[0]:
                        grey_list_points.append((point,y))
                        break
                    break
                else:
                    grey_list_points.append((point,y))
            for point in lxa:
                cond=checkhit(point,y)
                if cond[0] or cond[1]:
                    if cond[0]:
                        grey_list_points.append((point,y))
                        break
                    break
                else:
                    grey_list_points.append((point,y))
            for point in lyb[::-1]:
                cond=checkhit(x,point)
                if cond[0] or cond[1]:
                    if cond[0]:
                        grey_list_points.append((x,point))
                        break
                    break
                else:
                    grey_list_points.append((x,point))
            for point in lya:
                cond=checkhit(x,point)
                if cond[0] or cond[1]:
                    if cond[0]:
                        grey_list_points.append((x,point))
                        break
                    break
                else:
                    grey_list_points.append((x,point))

        #HORSE MOVEMENTS
        if element==9 or element==14:
                     if len(y_points[y_points.index(y)+1:])>=2:
                         if len(x_points[x_points.index(x)+1:])>1:
                             if not(checkhit(x_points[x_points.index(x)+1],y_points[y_points.index(y)+2])[1]):
                                 grey_list_points.append((x_points[x_points.index(x)+1],y_points[y_points.index(y)+2]))
                             
                     #top right condition
                     if len(y_points[:y_points.index(y)])>=2:
                         if len(x_points[x_points.index(x)+1:])>1:
                             if not(checkhit(x_points[x_points.index(x)+1],y_points[y_points.index(y)-2])[1]):
                                 grey_list_points.append((x_points[x_points.index(x)+1],y_points[y_points.index(y)-2]))
                     # down left
                     if len(y_points[y_points.index(y)+1:])>=2:
                         if len(x_points[:x_points.index(x)])>=1:
                             if not(checkhit(x_points[x_points.index(x)-1],y_points[y_points.index(y)+2])[1]):
                                 
                                 grey_list_points.append((x_points[x_points.index(x)-1],y_points[y_points.index(y)+2]))
                                 
                     #top left
                     if len(y_points[:y_points.index(y)])>=2:
                         if len(x_points[:x_points.index(x)])>=1:
                             if not(checkhit(x_points[x_points.index(x)-1],y_points[y_points.index(y)-2])[1]):
                                 grey_list_points.append((x_points[x_points.index(x)-1],y_points[y_points.index(y)-2]))
                    
                     #HORIZONDAL L's
                     #bottom left
                     if len(x_points[:x_points.index(x)])>=2:
                         if len(y_points[y_points.index(y)+1:])>1:
                             if not(checkhit(x_points[x_points.index(x)-2],y_points[y_points.index(y)+1])[1]):
                                 grey_list_points.append((x_points[x_points.index(x)-2],y_points[y_points.index(y)+1]))
                     #top left
                     if len(x_points[:x_points.index(x)])>=2:
                         if len(y_points[:y_points.index(y)+1])>1:
                             if not(checkhit(x_points[x_points.index(x)-2],y_points[y_points.index(y)-1])[1]):
                                 grey_list_points.append((x_points[x_points.index(x)-2],y_points[y_points.index(y)-1]))
                     #bottom right
                     if len(x_points[x_points.index(x):])>2:
                         if len(y_points[y_points.index(y)+1:])>1:
                             if not (checkhit(x_points[x_points.index(x)+2],y_points[y_points.index(y)+1])[1]):
                                 grey_list_points.append((x_points[x_points.index(x)+2],y_points[y_points.index(y)+1]))
                     #top right
                     if len(x_points[x_points.index(x):])>2:
                         if len(y_points[:y_points.index(y)+1])>1:
                             if not(checkhit(x_points[x_points.index(x)+2],y_points[y_points.index(y)-1])[1]):
                                 grey_list_points.append((x_points[x_points.index(x)+2],y_points[y_points.index(y)-1]))

        #BISHOP MOVEMENTS
        if element==10 or element==13:
            lxb=x_points[:x_points.index(x)]#lxb--->list of X below
            lxa=x_points[x_points.index(x)+1:]#lxa--->list of X above
            lyb=y_points[:y_points.index(y)]#same for Y
            lya=y_points[y_points.index(y)+1:]# ""
            for points in zip(lxb[::-1],lyb[::-1]):
                if not(checkhit(points[0],points[1])[1] or checkhit(points[0],points[1])[0]):
                    grey_list_points.append(points)
                else:
                    if checkhit(points[0],points[1])[0]:
                        grey_list_points.append(points)
                        break
                    else:
                        break
            for points in zip(lxb[::-1],lya):
                
                if not(checkhit(points[0],points[1])[1] or checkhit(points[0],points[1])[0]):
                    
                    grey_list_points.append(points)
                else:
                    if checkhit(points[0],points[1])[0]:
                        grey_list_points.append(points)
                        break
                    else:
                        break
            for points in zip(lxa,lyb[::-1]):
                if not(checkhit(points[0],points[1])[1] or checkhit(points[0],points[1])[0]):
                    
                    grey_list_points.append(points)
                else:
                    if checkhit(points[0],points[1])[0]:
                        grey_list_points.append(points)
                        break
                    else:
                        break
            for points in zip(lxa,lya):
                if not(checkhit(points[0],points[1])[1] or checkhit(points[0],points[1])[0]):
                    
                    grey_list_points.append(points)
                else:
                    if checkhit(points[0],points[1])[0]:
                        grey_list_points.append(points)
                        break
                    else:
                        break
            
        #QUEEN MOVEMENTS
        if element==11:
            lxb=x_points[:x_points.index(x)]#lxb--->list of X below
            lxa=x_points[x_points.index(x)+1:]#lxa--->list of X above
            lyb=y_points[:y_points.index(y)]#same for Y
            lya=y_points[y_points.index(y)+1:]# ""
            
            for points in zip(lxb[::-1],lyb[::-1]):
                if not(checkhit(points[0],points[1])[1] or checkhit(points[0],points[1])[0]):
                    grey_list_points.append(points)
                else:
                    if checkhit(points[0],points[1])[0]:
                        grey_list_points.append(points)
                        break
                    else:
                        break
            for points in zip(lxb[::-1],lya):
                
                if not(checkhit(points[0],points[1])[1] or checkhit(points[0],points[1])[0]):
                    
                    grey_list_points.append(points)
                else:
                    if checkhit(points[0],points[1])[0]:
                        grey_list_points.append(points)
                        break
                    else:
                        break
            for points in zip(lxa,lyb[::-1]):
                if not(checkhit(points[0],points[1])[1] or checkhit(points[0],points[1])[0]):
                    
                    grey_list_points.append(points)
                else:
                    if checkhit(points[0],points[1])[0]:
                        grey_list_points.append(points)
                        break
                    else:
                        break
            for points in zip(lxa,lya):
                if not(checkhit(points[0],points[1])[1] or checkhit(points[0],points[1])[0]):
                    
                    grey_list_points.append(points)
                else:
                    if checkhit(points[0],points[1])[0]:
                        grey_list_points.append(points)
                        break
                    else:
                        break
            
            for point in lxb[::-1]:
                cond=checkhit(point,y)
                if cond[0] or cond[1]:
                    if cond[0]:
                        grey_list_points.append((point,y))
                        break
                    break
                else:
                    grey_list_points.append((point,y))
            for point in lxa:
                cond=checkhit(point,y)
                
                if cond[0] or cond[1]:
                    if cond[0]:
                        grey_list_points.append((point,y))
                        break
                    break
                else:
                    grey_list_points.append((point,y))
            for point in lyb[::-1]:
                cond=checkhit(x,point)
                if cond[0] or cond[1]:
                    if cond[0]:
                        grey_list_points.append((x,point))
                        break
                    break
                else:
                    grey_list_points.append((x,point))
            for point in lya:
                cond=checkhit(x,point)
                if cond[0] or cond[1]:
                    if cond[0]:
                        grey_list_points.append((x,point))
                        break
                    break
                else:
                    grey_list_points.append((x,point))


        #KENG MOVEMENTS
        if element==12:
            if not(y==0):
                if not(checkhit(x,y_points[y_points.index(y)-1])[1]):
                       grey_list_points.append((x,y_points[y_points.index(y)-1]))
                if not(x==0):
                       if not(checkhit(x_points[x_points.index(x)-1],y_points[y_points.index(y)-1])[1]):
                            grey_list_points.append((x_points[x_points.index(x)-1],y_points[y_points.index(y)-1]))  
            if not(y==560):
                if not(checkhit(x,y_points[y_points.index(y)+1]))[1]:
                       grey_list_points.append((x,y_points[y_points.index(y)+1]))
                if not(x==560):
                    if not(checkhit(x_points[x_points.index(x)+1],y_points[y_points.index(y)+1]))[1]:
                              grey_list_points.append((x_points[x_points.index(x)+1],y_points[y_points.index(y)+1]))
            if not(x==0):
                if not(checkhit(x_points[x_points.index(x)+1],y)[1]):
                       grey_list_points.append((x_points[x_points.index(x)+1],y))
                if not(y==0):
                       if not(checkhit(x_points[x_points.index(x)+1],y_points[y_points.index(y)-1])[1]):
                              grey_list_points.append((x_points[x_points.index(x)+1],y_points[y_points.index(y)-1]))
            if not(x==560):
                if not(checkhit(x_points[x_points.index(x)-1],y)[1]):
                       grey_list_points.append((x_points[x_points.index(x)-1],y))
                if not(y==560):
                    if not(checkhit(x_points[x_points.index(x)-1],y_points[y_points.index(y)+1])[1]):
                        grey_list_points.append((x_points[x_points.index(x)-1],y_points[y_points.index(y)+1]))
                
                 

#CHECKMATE                    
def checkmate():
    global grey_list_points,opposition_list,RUN
    try:
        if (opposition_list[12][1],opposition_list[12][2]) in grey_list_points:
            return True,(opposition_list[12][1],opposition_list[12][2])
        else:
            return (False,0)
    except:
        return (False,0)
        RUN=False


"""def check(x,y):
    global element,grey_list_points,opposition_list
    print(x,y,"dsssssssssssssssssssssssssssssssssssssss")
    temp_poss=[]
    movement(x,y)
    for i in grey_list_points:
        temp_poss.append(i)
    grey_list_points=[]
    if element>7:
        print(temp_poss)
        print((opposition_list[12][1],opposition_list[12][2]))
    if (opposition_list[12][1],opposition_list[12][2]) in temp_poss:
        return True
    else:
        return False"""


    
#CHECKING FOR FRIENDLY OR OPPOSITE SPRITE IN X,Y                
def checkhit(x,y):
    global opposition_list
    hit_opp,hit_player=False,False
    opp_element=None
    temp_list2=[(i[1],i[2]) if bool(i) else 0 for i in opposition_list]
    if (x,y) in temp_list2:
        hit_opp=True
        opp_element=temp_list2.index((x,y))
        
    temp_list=[(i[1],i[2]) if bool(i) else 0 for i in player_list]
    if (x,y) in temp_list:
        #print((x,y))
        hit_player=True
        
    return (hit_opp,hit_player,opp_element)


#GAME VARIABLES AND LISTS    
Turn=1
xclick,yclick=0,0
xclicked,yclicked=0,0
element=None
player_list=white
opposition_list=black
sprite=[]
grey_list_points=[]
P=0
dont_change=False
temp={}
                                        
#GAMELOOP
while RUN:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            
    
    click=pygame.mouse.get_pressed()[0]
    
    if click==1:
        xclick,yclick=pygame.mouse.get_pos()
    
    if not(Turn%2==0):
        player_list=white
        opposition_list=black
        P=-1
    else :
        player_list=black
        opposition_list=white
        P=1
        
    is_clicked(xclick,yclick)
    movement(xclicked,yclicked)
    draw_board(screen)
    draw_piece(screen)
    
    
   
    

