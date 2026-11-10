
import numpy as np
import cv2
# Connect webcam
cap = cv2.VideoCapture(0)

while True:

    # Capture webcam frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define blue colour range
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create blue colour mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Extract blue colour
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Add titles to windows
    cv2.putText(frame, "ORIGINAL FRAME",
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2)

    cv2.putText(mask, "BLUE COLOUR MASK",
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, 255, 2)

    cv2.putText(result, "BLUE DETECTION",
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2)

    # Display three windows
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Blue Mask", mask)
    cv2.imshow("Blue Detection", result)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()