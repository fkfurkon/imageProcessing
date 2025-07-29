def convert_image_format(image, target_format):
    if target_format not in ['JPEG', 'PNG', 'BMP']:
        raise ValueError("Unsupported target format. Choose from 'JPEG', 'PNG', or 'BMP'.")
    
    if target_format == 'JPEG':
        return image.convert('RGB')
    elif target_format == 'PNG':
        return image.convert('RGBA')
    elif target_format == 'BMP':
        return image.convert('RGB')
    
def validate_parameters(params, valid_ranges):
    for param, (min_val, max_val) in valid_ranges.items():
        if param in params:
            if not (min_val <= params[param] <= max_val):
                raise ValueError(f"Parameter '{param}' out of range: {min_val} <= {param} <= {max_val}")
    
def resize_image(image, size):
    return image.resize(size)