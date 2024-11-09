import maya.cmds as cmds
import re

def create_quick_light_camera(*args):
    # Create the camera with the unique name
    latest_ver = get_latest_version(base_name='Light_Camera_v001__CAMERA')
    camera = cmds.camera()
    new_cam = cmds.rename(camera[0], 'light_camera_v{}__CAMERA'.format(latest_ver))

    # Create light with matching name
    light = cmds.directionalLight().replace('Shape','')
    new_light = cmds.rename(light, 'light_camera_v{}__LIGHT'.format(latest_ver))

    #Create ctrl and grp came and light
    curve = create_arrow_curve()
    new_crv = cmds.rename(curve, 'light_camera_v{}__CTRL'.format(latest_ver))
    sub_grp = cmds.group(new_cam, new_light,
            name='Light_Camera_v{}__SUBGRP'.format(latest_ver))

    #Parent everything together and group it 
    cmds.parentConstraint(new_crv,sub_grp)
    grp = cmds.group(new_crv, sub_grp,
                    name='Light_Camera_v{}__GRP'.format(latest_ver))

    return grp

def get_latest_version(base_name='Camera_v001__CAMERA'):
    latest_ver = 0
    pattern = r'_v(\d{3})__'  # Pattern to capture version number
    all_cam = cmds.listCameras() or []

    for each_cam in all_cam:
        match = re.search(pattern,each_cam)
        if match:
            ver_num = int(match.group(1))
            latest_ver = max(latest_ver,ver_num)
    if not latest_ver:
        return '001'
    latest_ver+=1
    return str(latest_ver).zfill(3)

def create_arrow_curve():
    # Define the points for the arrow shape
    points = [
        (0.5, -0, 1),  # Start at the bottom center
        (-0.5, -0, 1),  # Mid right
        (-0.5, -0, -1),  # Top right side
        (-2, -0, -1),  # Arrow tip right
        (-0, -0, -3),  # Arrow tip
        (2, -0, -1),  # Arrow tip left
        (0.5, -0, -1),  # Top left side
        (0.5, -0, 1),  # Mid left
    ]

    # Create the curve with the specified points
    arrow_curve = cmds.curve(p=points, degree=1, name="arrow_curve")
    return arrow_curve


create_quick_light_camera()