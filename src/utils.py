import os, gdown

base_url = "http://download.tensorflow.org/models/object_detection/tf2/20200711/"

def download_model(model_name):
    """ Download model from TensorFlow.org if not exists extract and return path to model """
    url = f"{base_url}{model_name}" # Model URL
    model_path = f"models/{model_name}" # Model zip path

    model_dir = model_path.replace(".tar.gz", "") # Model directory path

    if not os.path.exists(model_dir):
        # If not exists download model and extract
        gdown.cached_download(url, model_path, postprocess=gdown.extractall)

        # remove the zip file
        os.remove(model_path)

    return os.path.join(model_dir, "saved_model")