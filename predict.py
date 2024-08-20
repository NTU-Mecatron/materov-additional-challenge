import supervision as sv
from ultralytics import YOLO
import cv2
import numpy as np

# Load the YOLOv8 model
model = YOLO("best.pt")
slice_size = 640
slize_overlap = 0.2

# Open the video file
video_path = "seafloor_footage.mp4"
cap = cv2.VideoCapture(video_path)  

def slicer_callback(slice: np.ndarray) -> sv.Detections:
    result = model(slice, imgsz=slice_size, conf=0.1, iou=1)[0]
    detections = sv.Detections.from_ultralytics(result)
    return detections

slicer = sv.InferenceSlicer(
    callback=slicer_callback,
    slice_wh=(slice_size, slice_size),
    overlap_ratio_wh=(slize_overlap, slize_overlap),
    overlap_filter_strategy=sv.OverlapFilter.NON_MAX_MERGE,
    iou_threshold=0.3
)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        detections = slicer(frame)

        annotated_frame = sv.BoundingBoxAnnotator().annotate(
                            scene=frame.copy(),
                            detections=detections)

        # Display the annotated frame
        cv2.imshow("Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()