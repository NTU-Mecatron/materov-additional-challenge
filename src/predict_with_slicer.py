import yaml
import supervision as sv
from ultralytics import YOLO
import cv2
import numpy as np
from signal import signal, SIGINT
import sys, os, time
from convert_spreadsheet import convert_spreadsheet

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

def cleanup():
    cap.release()
    if do_save_video:
        out.release()
    if do_save_csv:
        csv_writer.close()
        print("\n\nConverting CSV to XLSX...")
        convert_spreadsheet(csv_path)
        print("Conversion complete.")

    cv2.destroyAllWindows()
    sys.exit(0)

# Function for handler to deal with CTRL+C
def handler(signal_received, frame):
    print("\n\nSIGINT or CTRL-C detected. Exiting gracefully:D")
    cleanup()

if __name__ == "__main__":
    
    # Load configuration from YAML file
    config = load_config("config/predict_with_slicer.yaml")
    
    # Load the YOLOv8 model
    model = YOLO(config['model_path'])
    imgsz = 640 # Image size for training, keep it same as training resolution
    overlapping = 0.2 # Overlap between tiles during inference on a video
    
    # Open the video file
    video_path = config['input_path']
    try:
        cap = cv2.VideoCapture(video_path)  
        # Get the video frame width, height, and frames per second (fps)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        input_fps = cap.get(cv2.CAP_PROP_FPS)
    except:
        print(f"Error: Could not open the video file at {video_path}")
        sys.exit(1)

    # Save the annotated video to the output path
    output_path = config.get('output_path', '')
    if not output_path: # If output_path is not provided, do not save the video
        do_save_video = False
        print("Not saving video.")
    elif os.path.exists(output_path): # If the output_path already exists, exit the program
        do_save_video = False
        print(f"Error: The output_path already exists.")
        sys.exit(1)
    else:   
        do_save_video = True
        print(f"Saving annotated video to {output_path}")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 file
        out = cv2.VideoWriter(output_path, fourcc, input_fps, (frame_width, frame_height))
    
    # Create a CSV sink to write the detections
    csv_path = config.get('csv_path', '')
    if not csv_path: # If csv_path is not provided, do not save the csv
        do_save_csv = False
        print("Not saving csv.")
    elif os.path.exists(csv_path):  # If the csv_path already exists, exit the program
        do_save_csv = False
        print(f"Error: The csv_path already exists.")
        sys.exit(1)
    else:
        do_save_csv = True
        print(f"Saving detections to {csv_path}")
        csv_writer = sv.CSVSink(csv_path)
        csv_writer.open()

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
    
    signal(SIGINT, handler)
    
    # Loop through the video frames
    frame_count = 0
    prev_time = time.time()
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()
    
        if not success:
            break
        
        # Increment the frame count and calculate the inference FPS
        frame_count += 1
        current_time = time.time()
        time_elapsed = round(frame_count / input_fps, 2)
        inference_fps = round(1 / (current_time - prev_time), 2)

        # Print frame count and FPS on the same line
        sys.stdout.write(f"\rFrame: {frame_count}, FPS: {inference_fps}, Video Time Elapsed: {time_elapsed} seconds")
        sys.stdout.flush()
        prev_time = current_time
    
        # Run YOLOv8 inference on the frame
        detections = slicer(frame)

        annotated_frame = box_annotator.annotate(
            scene=frame, detections=detections)
        
        ## Uncomment the following lines to display class labels
        # annotated_frame = label_annotator.annotate(
        # scene=annotated_frame, detections=detections)
    
        # Write the detections to the CSV file
        if do_save_csv:
            csv_writer.append(detections, {"frame_number": frame_count, "time_elapsed": time_elapsed})

        # Write the frame to the output video
        if do_save_video:
            out.write(annotated_frame)         
    
        # Display the annotated frame
        display_x_axis = config.get('display_x_axis', 0)
        display_y_axis = config.get('display_y_axis', 0)
        if display_x_axis != 0 and display_y_axis != 0:
            display_frame = cv2.resize(annotated_frame, (display_x_axis, display_y_axis))  # Adjust the size as needed
            cv2.imshow("Inference", display_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(2) & 0xFF == ord("q"):
           break
    
    # Release the video capture object and close the display window
    cleanup()