import cv2 
  
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 31
  
    # checks whether frames were extracted 
    success = 1
    
  
    while success: 
        if(count==41):
           return
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
       
        # Saves the frames with frame-count 
        cv2.imwrite("./dataset/%d.jpg" % count, image) 
  
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
    
    # Calling the function 
      FrameCapture("4.mp4") 

