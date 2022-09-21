# Import the library we needed
import tkinter as tk
from tkinter.font import BOLD
import requests
import json
import PIL.ImageTk, PIL.Image
import urllib.request

# Make the class for our app
class app(tk.Tk):
    def __init__(self):
        # Init the app window
        super().__init__()
        # Set the window to not resizable
        self.resizable(False,False)
        # Set the window resoultion
        self.geometry("600x600")
        # Calling our UI init method
        self.initUI()
    
    def searchData(self,playerName):
        global p_nospace
        global a
        # The plain API Link, we'd combine them with player name which will be pass
        # via the parameter
        link = "https://www.thesportsdb.com/api/v1/json/2/searchplayers.php?p="
        # Change the value of " " in playerName variable to "%20" to fit the API criteria
        p_nospace=playerName.replace(" ", "%20")
        # Combine the link and the playerName variable
        a = link + p_nospace
        print("The Link : {}".format(a))
        # Requests the data from the API link which we combined before
        data_r = requests.get(a)
        # Load the data using json.loads
        data = json.loads(data_r.text)
        # Assigning the player name from the API
        # The ['player'] is the key
        # The [0] is the index
        # The ['strPlayer'] is the key
        # Analogi :
        # So it means we go to a room called 'player', and then search through a cabinet called "0"
        # and then looking for the player name file called "strPlayer". After we found it we assign it
        # to a variable called "plaName". So if we called "plaName", it'd return the value of 'strPlayer'
        plaName=data['player'][0]['strPlayer']
        plaImage=data['player'][0]['strFanart2']
        plaNationality=data['player'][0]['strNationality']
        plaTeam=data['player'][0]['strTeam']
        # replace p_nospace in link variable to empty
        a=link.replace(p_nospace,"")
        print("The Link After The Data Loaded : {}".format(a))
        # call the generate_player_pro method
        self.generate_player_pro(plaName,plaImage,plaNationality,plaTeam)

    def generate_player_pro(self,plaName,plaImage, plaNationality, plaTeam):
        global profilePanel
        # Generate Frame
        profilePanel=tk.Frame(profileFrame,width=600,height=500, bg="#161616")
        profilePanel.pack(fill=tk.BOTH,expand=1)
        # Make a button to make the frame dissapear
        clr=tk.Button(profilePanel,text="Search again",command=self.destroy_frame)
        clr.place(relx=0.5,rely=0.65,anchor=tk.CENTER)
        # Generate Canvas that'd contains our image
        photoCanvas=tk.Canvas(profilePanel,width=150,height=150,highlightthickness=0)
        photoCanvas.place(relx=0.5,rely=0.2,anchor=tk.CENTER)
        # Generate Label
        namaPlayer=tk.Label(profilePanel,text="Name : " + plaName,foreground="White",background="#161616", font=("Arial",14))
        namaPlayer.place(relx=0.5,rely=0.45,anchor=tk.CENTER)
        # Generate Label
        nationalityPlayer=tk.Label(profilePanel,text="Nationality : " + plaNationality,foreground="White",background="#161616", font=("Arial",14))
        nationalityPlayer.place(relx=0.5,rely=0.50,anchor=tk.CENTER)
        # Generate Label
        teamPlayer=tk.Label(profilePanel,text="Team : " + plaTeam,foreground="White",background="#161616", font=("Arial",14))
        teamPlayer.place(relx=0.5,rely=0.55,anchor=tk.CENTER)
        # Retrieve the image from the API, and then save it as 'gambar.jpg'
        foto = urllib.request.urlretrieve(plaImage, "gambar.jpg")
        # Load the image we saved from the API, and then resize it
        img =PIL.ImageTk.PhotoImage(PIL.Image.open("./gambar.jpg").resize((150,150), PIL.Image.ANTIALIAS))
        # Make an image
        photoCanvas.create_image(0,0,image=img,anchor=tk.NW)
        # Anchor the image
        photoCanvas.img=img
        self.update_idletasks()
        self.update()

    # Method to make the frame dissapear
    def destroy_frame(self):
        global result
        result = playerSearch.delete('1.0', tk.END)
        profilePanel.destroy()

    
    # Method to init UI
    def initUI(self):
        global headerFrame
        global profileFrame
        # Make the mainframe that'd contains header and proile frame
        mainFrame=tk.Frame(self,bg="Red")
        mainFrame.pack(fill=tk.BOTH,expand=1)
        headerFrame=tk.Frame(mainFrame,bg="#1B2430",width=600,height=100)
        headerFrame.grid(row=0,column=0,sticky=tk.NW)
        profileFrame=tk.Frame(mainFrame,bg="#161616",width=600,height=500)
        profileFrame.grid(row=1,column=0,sticky=tk.NW)
        self.headerUI()
        self.profileFrameUI()
    
    # Method to get the value of text box
    def getPlayerSearch(self,event):
        global result
        # Get the value of text box
        result = playerSearch.get(1.0, "end-1c")
        # Call the search data method and pass result as param
        self.searchData(result)
    
    # Method to inisiate the profile Frame UI
    def profileFrameUI(self):
        global playerSearch
        global photoCanvas
        # Make a label
        playerSearchLbl=tk.Label(profileFrame,text="Enter Player Name : ", foreground="White", background="#161616",font=("Arial,12"))
        playerSearchLbl.place(relx=0.5,rely=0.025,anchor=tk.CENTER)
        # Make a text box called "profileSearch"
        playerSearch=tk.Text(profileFrame,width=20,height=1,foreground="Black", background="#FFFFFF",font=("Arial",12),bd=0)
        playerSearch.place(relx=0.5,rely=0.080,anchor=tk.CENTER)
        playerSearch.bind('<Return>',self.getPlayerSearch)
    
    # Method to inisiate the header UI
    def headerUI(self):
        # Make a title for header
        header_tit=tk.Label(headerFrame,text="SOCCER PLAYER BIO SEARCH",background="#1B2430",foreground="white",font=("Helvetica",18,BOLD))
        header_tit.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        
# Driver to run the app
if __name__=='__main__':
    a = app()
    a.mainloop()