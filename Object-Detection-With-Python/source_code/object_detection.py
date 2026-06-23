from ultralytics import YOLO
import cv2

# Load highest accuracy model
model = YOLO("yolov8m.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Predict with higher confidence threshold
    results = model(frame, conf=0.5)

    # Draw predictions
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("High Accuracy Object Detection", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()