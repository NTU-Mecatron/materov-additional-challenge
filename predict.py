import yaml
import supervision as sv
from ultralytics import YOLO
import cv2, sys, os
import numpy as np
from signal import signal, SIGINT

# Function to load configuration from YAML file
def load_config(config_path):
    with open(config _path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Function for slicer callback
def slicer_callback(slice: np.ndarray) -> sv.Detections:
    result = model(slice, imgsz=imgsz, conf=0.1, iou=1)[0]
    detections = sv.Detections.from_ultralytics(result)
    return detections

# Function for handler to deal with CTRL+C
def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    out.release()
    cap.release() 
    csv_writer.close()
    cv2.destroyAllWindows()
    sys.exit(0)

if __name__ == "__main__":
    
    # Load configuration from YAML file
    config = load_config("predict_config.yaml")
    
    # Load the YOLOv8 model
    model = YOLO(config['model_path'])
    imgsz = config['imgsz']
    overlapping = config['overlapping']
    
    # Open the video file
    video_path = config['video_path']
    output_path = config['output_path']
    if os.path.exists(output_path):
        print(f"Error: The output_path already exists.")
        sys.exit(1)
    else:
        cap = cv2.VideoCapture(video_path)  
    
    # Get the video frame width, height, and frames per second (fps)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 file
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

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
    
    # Create a CSV sink to write the detections
    csv_path = config['csv_path']
    # Check if the CSV file already exists
    if os.path.exists(csv_path):
        print(f"Error: The csv_path already exists.")
        sys.exit(1)
    else:
        csv_writer = sv.CSVSink(csv_path)
        csv_writer.open()
    
    signal(SIGINT, handler)
    
    # Loop through the video frames
    frame_count = 0
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()
    
        if not success:
            break
        
        frame_count += 1
    
        # Run YOLOv8 inference on the frame
        detections = slicer(frame)
    
        csv_writer.append(detections, {"frame_number": frame_count})
    
        annotated_frame = box_annotator.annotate(
            scene=frame, detections=detections)
        
        ## Uncomment the following lines to display class labels
        # annotated_frame = label_annotator.annotate(
        #     scene=annotated_frame, detections=detections)
    
        # Write the frame to the output video
        out.write(annotated_frame)
    
        # Display the annotated frame
        display_frame = cv2.resize(annotated_frame, (config['display_x-axis'], config['display_y-axis']))  # Adjust the size as needed
        cv2.imshow("Inference", display_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(2) & 0xFF == ord("q"):
            break
    
    # Release the video capture object and close the display window
    cap.release()
    out.release()
    csv_writer.close()
    cv2.destroyAllWindows()
