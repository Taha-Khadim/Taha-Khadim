class Signs:
    def __init__(self,hand):
        self.tipIds = [4, 8, 12, 16, 20]
        self.hand=hand
# ______________________________________________________________________________________________________________________________________________________________       
    def sign1(self):
        lmlist = self.hand["lmList"]
        if (
            lmlist[13][1]>lmlist[14][1] and # Ring       Down
            lmlist[14][1]<lmlist[16][1] and
            lmlist[17][1]>lmlist[18][1] and # Pinky      Down
            lmlist[18][1]<lmlist[20][1] and
            lmlist[5][1]>lmlist[8][1] and # Index        Up
            lmlist[9][1]>lmlist[12][1] # Middle          Up
           ):
                return 1
        else:
            return 0
# ______________________________________________________________________________________________________________________________________________________________
    def sign2(self):
        fingers=0
        lmlist = self.hand["lmList"]
        for i in range(1,5):                #All fingers up check
            if lmlist[self.tipIds[i]][1]<lmlist[self.tipIds[i]-1][1] and lmlist[self.tipIds[i]-1][1]<lmlist[self.tipIds[i]-2][1] and lmlist[20][0]<lmlist[8][0]:
                fingers+=1
        if fingers==4:
            return 1
        else:
            return 0
# ______________________________________________________________________________________________________________________________________________________________
    def sign3(self):
        fingers=0
        lmlist = self.hand["lmList"]
        for i in range(2,5):    #All 3 fingers except Index
            if lmlist[self.tipIds[i]][1]<lmlist[self.tipIds[i]-1][1] and lmlist[self.tipIds[i]-1][1]<lmlist[self.tipIds[i]-2][1] and lmlist[20][0]<lmlist[8][0]:
                fingers+=1
        if lmlist[5][1]>lmlist[6][1] and lmlist[6][1]<=lmlist[8][1]:     #Index Down
            fingers+=1
        if fingers==4:
            return 1
        else:
            return 0
# ______________________________________________________________________________________________________________________________________________________________
    def sign4(self):
        lmlist = self.hand["lmList"]
        if (
            lmlist[5][1]>lmlist[6][1] and
            lmlist[6][1]<lmlist[17][1] and
            lmlist[6][1]<lmlist[8][1] and
            lmlist[10][1]<lmlist[12][1] and
            lmlist[14][1]<lmlist[16][1] and
            lmlist[18][1]<lmlist[20][1] and
            lmlist[4][1]<lmlist[2][1]  #Thumb
           ):
                return 1
        else:
            return 0
# ______________________________________________________________________________________________________________________________________________________________            
    def sign5(self):
        lmlist = self.hand["lmList"]
        if (lmlist[self.tipIds[4]][0]<lmlist[self.tipIds[4]-1][0] and      #Pinky check
            lmlist[self.tipIds[1]-1][0]<lmlist[self.tipIds[1]-2][0] and     #Index check
            lmlist[4][1]<lmlist[2][1] ):   #Thumb
                return 1
        else:
            return 0
# ______________________________________________________________________________________________________________________________________________________________      
    def sign6(self):
        lmlist = self.hand["lmList"]
        if (
            lmlist[1][1]<lmlist[5][1] and      # Wrist and Index's Base
            lmlist[1][1]<lmlist[9][1] and      # Wrist and Middle's Base
            lmlist[1][1]<lmlist[13][1] and     # Wrist and Ring's Base
            lmlist[0][0]>lmlist[4][0] and
            lmlist[0][0]>lmlist[8][0] and
            lmlist[0][0]>lmlist[12][0]
           ):
                return 1
        else:
            return 0
# ______________________________________________________________________________________________________________________________________________________________       
    def sign7(self):
        lmlist = self.hand["lmList"]
        if (
            lmlist[5][1]>lmlist[6][1] and # Index
            lmlist[6][1]<lmlist[8][1] and
            lmlist[9][1]>lmlist[10][1] and # Middle
            lmlist[10][1]<lmlist[12][1] and
            lmlist[13][1]>lmlist[16][1] and # Ring
            lmlist[17][1]>lmlist[20][1] # Pinky
           ):
                return 1
        else:
            return 0
# ______________________________________________________________________________________________________________________________________________________________
    def sign8(self):
        lmlist = self.hand["lmList"]
        if (lmlist[5][1]>lmlist[6][1] and # Index
            lmlist[6][1]>lmlist[8][1] and
            lmlist[9][1]>lmlist[10][1] and # Middle
            lmlist[10][1]>lmlist[12][1] and
            lmlist[13][1]<lmlist[16][1] and # Ring
            lmlist[17][1]<lmlist[20][1] ):
                return 1
        else:
            return 0
# ______________________________________________________________________________________________________________________________________________________________
