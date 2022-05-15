from tkinter import filedialog
import pygame
from HandTrackingModule import HandDetector
from tkinter import *
from PIL import Image, ImageTk
import cv2
from Signs import Signs

tipIds = [4, 8, 12, 16, 20]
check=0
def starter():
    global root,pic_label,Video_Label
    root = Tk()
    root.geometry("1920x1080+0+0")
    root.state("zoomed")
    root.iconbitmap("122111.ico")
    root.config(bg="#000000")
    root.title("Hand Signs Converter")
    # ___________________________________________________________________
    # Borders

    pygame.mixer.init()
    pygame.mixer.music.load("theme.mp3")
    pygame.mixer.music.play(loops=100)
    line1 = Frame(root , bg= '#ffdf00',height=2,width=1680)
    line1.place(x=0,y=220)
    line2 = Frame(root , bg= '#ffdf00',height=1080,width=2)
    line2.place(x=0,y=0)
    line3 = Frame(root , bg= '#ffdf00',height=3,width=1680)
    line3.place(x=0,y=0)
    line_bot = Frame(root , bg= '#ffdf00',height=3,width=1680)
    line_bot.place(x=0,y=838)
    line_up = Frame(root , bg= '#ffdf00',height=2,width=1680)
    line_up.place(x=0,y=150)
    line4 = Frame(root , bg= '#ffdf00',height=1080,width=2)
    line4.place(x=1534,y=0)
    line5 = Frame(root , bg= '#ffdf00',height=1080,width=6)
    line5.place(x=764,y=0)
    # line6 = Frame(root , bg= '#2f2f2f',height=1080,width=1)
    # line6.place(x=767,y=0)
    # ___________________________________________________________________
    Video_frame = Frame(root, height=580, width=720, bg="#2f2f2f")
    Video_Label = Label(root)
    Video_frame.place(x=15,y=240)
    Video_Label.place(x=15,y=240)
    # ___________________________________________________________________
    pic_frame = Frame(root, height=580, width=720, bg="#2f2f2f")
    pic_label = Label(root,bg="#2f2f2f")
    pic_frame.place(x=800,y=240)
    pic_label.place(x=800,y=240)
def checker():
    sign_number=0
    if hands:
            hand = hands[0]
            Sign = Signs(hand)
            if   Sign.sign4():
                sign_number=4
            elif Sign.sign2():
                sign_number=2
            elif Sign.sign3():
                sign_number=3
            elif Sign.sign1():
                sign_number=1
            elif Sign.sign5():
                sign_number=5
            elif Sign.sign6():
                sign_number=6
            elif Sign.sign7():
                sign_number=7
            elif Sign.sign8():
                sign_number=8
            else:
                sign_number=0
    return sign_number
detector = HandDetector(detectionCon=0.8, maxHands=2)
starter()
# ___________________________________________________________________
video_path=0
# For Browsing Videos
def path_select():
    global video_path,cap
    video_path = filedialog.askopenfilename()
    cap = cv2.VideoCapture(video_path)
    text = Label(root,text="Recorded Video  ",bg="#000000",fg="#ffffff",font=("Calibri",20))
    text.place(x=250,y=165)
    # pygame.mixer.music.stop()
# For Live feed
def video_live():
    global video_path,cap
    video_path = 0
    cap = cv2.VideoCapture(video_path)
    text = Label(root,text="LIVE VIDEO FEED",bg="#000000",fg="#ffffff",font=("Calibri",20))
    text.place(x=250,y=165)
# __________________________________________Live Button ________________________________________________________________
live_btn_img = cv2.imread("PICS/live.png")
live_btn_img=cv2.resize(live_btn_img,(130,50))
live_btn_img = cv2.cvtColor(live_btn_img, cv2.COLOR_BGR2RGB)
live_btn_img = ImageTk.PhotoImage(Image.fromarray(live_btn_img), Image.ANTIALIAS)
live_btn = Button(root, height = 50, width=130, image=live_btn_img, fg="#DBDBDB", bg="#2f2f2f", command=lambda:video_live())
live_btn.place(x=1200,y=20)
# __________________________________________Browse Button_______________________________________________________________
browse_btn_img = cv2.imread("PICS/browse.png")
browse_btn_img=cv2.resize(browse_btn_img,(140,50))
browse_btn_img = cv2.cvtColor(browse_btn_img, cv2.COLOR_BGR2RGB)
browse_btn_img = ImageTk.PhotoImage(Image.fromarray(browse_btn_img), Image.ANTIALIAS)
browse_btn = Button(root, height = 50, width=130,image=browse_btn_img, fg="#2f2f2f", bg="#2f2f2f", command=lambda:path_select())
browse_btn.place(x=1200,y=80)
text = Label(root,text="To Browse Video",bg="#000000",fg="#ffffff",font=("Calibri",20))
text.place(x=1000,y=90)
# ______________________________________________________________________________________________________________________
text = Label(root,text="LIVE VIDEO FEED",bg="#000000",fg="#ffffff",font=("Calibri",20))
text.place(x=250,y=165)
text = Label(root,text="   For Live Video",bg="#000000",fg="#ffffff",font=("Calibri",20))
text.place(x=1000,y=30)
text = Label(root,text="Haku's Hand Signs",bg="#000000",fg="#ffffff",font=("Calibri",70))
text.place(x=25,y=15)
# =================================================================================================================================
cap = cv2.VideoCapture(video_path)          #  LOAD VIDEO / LIVE    (HERE)
# =================================================================================================================================
text = Label(root,text="LIVE VIDEO FEED",bg="#000000",fg="#ffffff",font=("Calibri",20))
text.place(x=250,y=165)
text = Label(root,text="Reference Image",bg="#000000",fg="#ffffff",font=("Calibri",23))
text.place(x=1050,y=165)
# Main Loop/Program
while True:
    success, img = cap.read()
    if success:
        if not video_path:
            img=cv2.flip(img, 1)
        hands = detector.findHands(img,draw=False)  # with draw
        img = cv2.resize(img, (720, 580))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(img), Image.ANTIALIAS)
        fingers=0
        check=checker() 
        ref_img = 0
        if check:    
            print(1)
            path = "PICS/"+str(check)+".png"
            ref_img = cv2.imread(path)
            ref_img = cv2.resize(ref_img, (720,580))
            ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB)
            ref_img = ImageTk.PhotoImage(Image.fromarray(ref_img))
        if ref_img:
            pic_label["image"] = ref_img
        Video_Label["image"] = img
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    root.update()