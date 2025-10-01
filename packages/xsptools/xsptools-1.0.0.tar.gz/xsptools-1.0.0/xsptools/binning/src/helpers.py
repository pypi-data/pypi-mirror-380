import numpy as np



def decode_bits(value: int) -> list:

    """
    Value is bit decoded. Return is a list containing activated bits.
    Refer to libxsp-usermanual-lambda-v2.7.
    """
    active_bits = []
    for i in range(32):
        if value & (1 << i):
            active_bits.append(i)
            
    
    return active_bits



def decode_mask(pixel_mask: np.ndarray) -> np.ndarray:

    """
    Transform pixel mask such that its entries are lists of activated bits.
    """

    decoded_pixel_mask = np.array([[decode_bits(j) for j in row] for row in pixel_mask], dtype=object)

    
    return decoded_pixel_mask



def pixel_mask_nn_interpolation_indices(decoded_pixel_mask: np.ndarray) -> tuple:

    """ 
    Return the indices of the pixels that are to be interpolated. 
    Return the indices and not the mask itself because they are needed for the interpolation.
    See function 'nn_interpolation(frame, indices)'.
    """

    interpolation_pixel_mask = np.array([
        [
            any(bit in {1,2,3,4} for bit in lst)
            for lst in row
        ]
        for row in decoded_pixel_mask
    ])
        
    
    return np.where(interpolation_pixel_mask)



def pixel_mask_widened_strip(decoded_pixel_mask: np.ndarray) -> np.ndarray:

    """ Widen the pixel mask with the vertical dead strip widened by 1 pixel.
        Return is a pixel mask with bool entries, i.e. True for dead pixel, False otherwise.
    """

    vertical_strip_pixel_mask = np.array([
        [
            any(bit in {0} for bit in lst)
            for lst in row
        ]
        for row in decoded_pixel_mask
    ])

    row_indices,column_indices = np.where(vertical_strip_pixel_mask)

    unique_cols = np.unique(column_indices)
    adjusted_left_colum = np.min(unique_cols) - 1
    adjusted_right_column = np.max(unique_cols) + 1  

    expanded_mask = np.zeros_like(vertical_strip_pixel_mask, dtype=bool)
    for row in np.unique(row_indices):
        expanded_mask[row, adjusted_left_colum:adjusted_right_column+1] = True

     
    return expanded_mask



def nn_interpolation(frame: np.ndarray, indices: tuple) -> np.ndarray:

    rows, columns = indices[0], indices[1]
    neighbor_offsets = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

    for r, c in zip(rows, columns):
        neighbors = []
        for dr, dc in neighbor_offsets:
            neighbor_row, neighbor_column = r + dr, c + dc
            if 0 <= neighbor_row < frame.shape[0] and 0 <= neighbor_column < frame.shape[1]:
                if frame[neighbor_row, neighbor_column]:
                    neighbors.append(frame[neighbor_row, neighbor_column])
        if neighbors:
            frame[r, c] = np.mean(neighbors)


    return frame
