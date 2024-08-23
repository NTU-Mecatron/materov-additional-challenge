import yaml
import supervision as sv
from ultralytics import YOLO
import cv2
import numpy as np
from signal import signal, SIGINT
import sys, os, time

# Function to load configuration from YAML file
def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Function for slicer callback
def slicer_callback(slice: np.ndarray) -> sv.Detections:
    result = model(slice, verbose=False, imgsz=imgsz, conf=config['confidence'], iou=1)[0]
    detections = sv.Detections.from_ultralytics(result)
    return detections

if __name__ == "__main__":
    
    # Load configuration from YAML file
    config = load_config("config/predict_with_slicer.yaml")
    
    # Load the YOLOv8 model
    model = YOLO(config['model_path'])
    imgsz = 640 # Image size for training, keep it same as training resolution
    overlapping = 0.2 # Overlap between tiles during inference on a video
    
    # List all image files in the directory
    image_dir = config['input_path']
    image_files = [f for f in os.listdir(image_dir) 
                   if (os.path.isfile(os.path.join(image_dir, f)))]

    # Create an InferenceSlicer object
    slicer = sv.InferenceSlicer(
        callback=slicer_callback,
        slice_wh=(imgsz, imgsz),
        overlap_ratio_wh=(overlapping, overlapping),
        overlap_filter_strategy=sv.OverlapFilter.NON_MAX_MERGE,
        iou_threshold=config['iou_threshold']
    )
    
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()   
    
    image_count = 0
    prev_time = time.time()
    # Loop through the image files
    for image_file in image_files:
        # Read a frame from the video
        image_path = os.path.join(image_dir, image_file)
        frame = cv2.imread(image_path)
        
        # Increment the frame count and calculate the inference FPS
        image_count += 1
        current_time = time.time()
        inference_fps = round(1 / (current_time - prev_time), 2)

        # Print frame count and FPS on the same line
        sys.stdout.write(f"\rImage count: {image_count}, FPS: {inference_fps}")
        sys.stdout.flush()
        prev_time = current_time
    
        # Run YOLOv8 inference on the frame
        detections = slicer(frame)

        annotated_frame = box_annotator.annotate(
            scene=frame, detections=detections)
        
        ## Uncomment the following lines to display class labels
        # annotated_frame = label_annotator.annotate(
        #     scene=annotated_frame, detections=detections)      
    
        # Display the annotated frame
        display_x_axis = config.get('display_x_axis', 0)
        display_y_axis = config.get('display_y_axis', 0)
        if display_x_axis != 0 and display_y_axis != 0:
            display_frame = cv2.resize(annotated_frame, (display_x_axis, display_y_axis))  # Adjust the size as needed
            cv2.imshow("Inference", display_frame)

        # Optionally, save or display the annotated frame
        # For example, save the annotated frame
        annotated_image_path = os.path.join(image_dir, f"annotated_{image_file}")
        cv2.imwrite(annotated_image_path, annotated_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(100) & 0xFF == ord("q"):
           break
    
    # Release the video capture object and close the display window
    cv2.destroyAllWindows()