import cv2
import numpy as np
import math

def theoretical_k1_k2_calculation(fov_degrees, image_width=500):
    #image_width does't matter

    fov_rad = np.radians(fov_degrees)
    
    # calculate_focal_length
    focal_length = image_width / (2 * np.tan(fov_rad / 2))
    
    # Theorical distortion factor
    distortion_factor = (image_width / 2) / focal_length
    
    k1 = -0.1 * distortion_factor**2
    k2 = 0.01 * distortion_factor**3
    
    return k1, k2

def undistortion_fov(image_path, fov):
    """
    배럴 왜곡(barrel distortion) 보정
    k1, k2, k3: 왜곡 계수 (음수면 배럴, 양수면 핀쿠션)
    """
    img = cv2.imread(image_path)
    h, w = img.shape[:2]

    k1, k2 = theoretical_k1_k2_calculation(fov)
    
    # 카메라 매트릭스 생성 (가정값)
    camera_matrix = np.array([[w, 0, w/2],
                             [0, h, h/2],
                             [0, 0, 1]], dtype=np.float32)
    
    # 왜곡 계수
    dist_coeffs = np.array([k1, k2, 0, 0, 0], dtype=np.float32)
    
    # 왜곡 보정
    undistorted = cv2.undistort(img, camera_matrix, dist_coeffs)

    return undistorted