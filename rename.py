import os 
  
# Function to rename multiple files 
def main(): 
    for filename in os.listdir("pre_test"): 
        dst ="20_" + filename  #00, 04, 11, 14, 17, 19, 20, 33, 34, 40
        src ='pre_test/'+ filename 
        dst ='test/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 

