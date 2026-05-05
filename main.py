import os
from asciify_img import ASCIIFY_IMG
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def process_image(img_filename):
    """Worker function to process a single image."""
    print(f"Working on {img_filename}")
    input_path = os.path.join('./assets/downloads', img_filename)
    output_path = os.path.join('./assets/output', img_filename)

    try:
        img_obj = ASCIIFY_IMG(input_path)
        img_obj.asciify()
        img_obj.save(output_path)
        return f"Successfully processed: {img_filename}"
    except Exception as e:
        raise Exception(f'Failed to process {img_filename}')


if __name__ == '__main__':

    # img_obj=ASCIIFY_IMG('./assets/downloads/0.jpg')
    # img_obj.asciify()
    # img_obj.save(os.path.join('./assets/output', '0.jpg'))
    
    input_dir = './assets/downloads'
    output_dir = './assets/output'

    os.makedirs(output_dir, exist_ok=True)

    # Gather all image files
    images = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    print(f"Starting batch processing of {len(images)} images...")

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(process_image, images))

    print("\n".join(results))

