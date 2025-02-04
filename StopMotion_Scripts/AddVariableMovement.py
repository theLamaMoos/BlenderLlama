# Author: BlenderLlama
# Date: 20250129
# Purpose: This script will add random movements
# to a bone or existing sequence for a jittering effect
# such as those present in stop-motion animations

import bpy
import random
import math

#return a random multiplier to make the value positive or negative
def multiplier():
    return random.choice([-1, 1])

# Define the frame range and step interval
start_frame = 0
end_frame = 600
step = 3

# Define the rotation range
low_range = .5
high_range = 1  # Adjust to control the randomness

# Define specific bones to rotate
allowed_bones = ["spine.011", "spine.010", "spine.009"]  # Change these to match your rig

obj = bpy.context.object

if obj and obj.type == "ARMATURE":
    if bpy.context.mode != "POSE":
        print("Switching to Pose Mode...")
        bpy.ops.object.mode_set(mode='POSE')  # Ensure you're in Pose Mode

    # Apply rotation at interval frames
    for frame in range(start_frame, end_frame + 1, step):
        bpy.context.scene.frame_set(frame)
        
        bones = [b for b in obj.pose.bones if b.name in allowed_bones]
        
        if bones:
            if frame % (3*step) == 0:
                bpy.ops.pose.select_all(action='DESELECT')
                random_bone = random.choice(bones)
                random_bone.bone.select = True
            
                # Generate random rotation values for X, Y, Z
                rot_x = math.radians(random.uniform(low_range, high_range)) * multiplier()
                rot_y = math.radians(random.uniform(low_range, high_range)) * multiplier()
                rot_z = math.radians(random.uniform(low_range, high_range)) * multiplier()
            
            # Apply the random rotation
            bpy.ops.transform.rotate(value=rot_x, orient_axis='X')
            bpy.ops.transform.rotate(value=rot_y, orient_axis='Y')
            bpy.ops.transform.rotate(value=rot_z, orient_axis='Z')

            # Insert keyframe for the bone's rotation
            bpy.ops.anim.keyframe_insert()
                
