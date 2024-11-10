import maya.cmds as cmds
import re


def create_quick_light_camera(*args):
    # Create the camera with the unique name
    latest_ver = get_latest_version(base_name='Light_Camera_v001__CAMERA')
    camera = cmds.camera()
    new_cam = cmds.rename(camera[0], 'Camera_v{}__CAMERA'.format(latest_ver))

    # Create light with matching name
    light = cmds.directionalLight().replace('Shape','')
    new_light = cmds.rename(light, 'Light_v{}__LIGHT'.format(latest_ver))

    #Parent and, group light and camera
    cmds.parentConstraint(new_cam,new_light)
    cmds.group(new_cam, new_light, name='Camera_v{}__GRP'.format(latest_ver))


def get_latest_version(base_name='Light_Camera_v001__CAMERA'):
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


create_quick_light_camera()