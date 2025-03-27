import os

class ImageProcessor:
    @staticmethod
    def get_image_paths(image_path):
        if os.path.isdir(image_path) and "images" in image_path and "general_cam_" not in image_path:
            return [os.path.join(image_path, file) for file in os.listdir(image_path) if file.endswith((".jpg", ".png"))]
        return []

    @staticmethod
    def get_metadata_path(image_path):
        metadata_path = os.path.join(os.path.dirname(os.path.dirname(image_path)), "metadata")
        image_file = os.path.basename(image_path)
        metadata_file = image_file.replace(".jpg", ".json").replace(".png", ".json")
        return os.path.join(metadata_path, metadata_file)

