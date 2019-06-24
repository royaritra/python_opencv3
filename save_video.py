import cv2
  
capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_original = cv2.VideoWriter('output_original.avi',fourcc, 20.0, (640,480))
out_gray = cv2.VideoWriter('output_gray.avi',fourcc, 20.0, (640,480),0)
out_gray_flipped = cv2.VideoWriter('output_gray_flipped.avi',fourcc, 20.0, (640,480),0)
 
while(True):
      
    ret, frame = capture.read()
    #out_original.write(frame)
 
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out_gray.write(grayFrame)
    grayFrame_flipped=cv2.flip(grayFrame,0);
 
    cv2.imshow('video gray', grayFrame)
    cv2.imshow('video original', frame)
    cv2.imshow('video gray flipped',grayFrame_flipped)
    out_original.write(frame)
    
    out_gray_flipped.write(grayFrame_flipped)
      
    if cv2.waitKey(1) == 27:
        break
  
capture.release()
out_original.release()
out_gray.release()
out_gray_flipped.release()
cv2.destroyAllWindows()