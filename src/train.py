import yaml
from ultralytics import YOLO

# Function to load configuration from YAML file
def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    
    # Load configuration from YAML file
    config = load_config("train_config.yaml")

    # Initialize the YOLO model using the model path from the config
    model = YOLO(config['model_path'])

    # Remove the model path from the config dictionary
    config.pop('model_path')
    
    # Train the model using the loaded configuration
    results = model.train(**config)
