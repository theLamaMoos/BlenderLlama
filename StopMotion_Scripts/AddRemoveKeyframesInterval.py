# Author: BlenderLlama
# Date: 20250129
# Purpose: To create keyframes for an already animated sequence
# in preset infervals, and remove all other keyframes
# to prep for stop-motion effects in Blender

import bpy

# Define the frame range and step interval
start_frame = 0
end_frame = 600
step = 3

# Select the active object
obj = bpy.context.object

if obj:
    # Loop through frames by interval amounts
    for frame in range(start_frame, end_frame + 1, step):
        bpy.context.scene.frame_set(frame)
        
        #set the keyframe
        bpy.ops.anim.keyframe_insert()

    #block to remove keyframes out of step with the interval
    for frame in range(start_frame, end_frame + 1):  # Include end_frame
        # Check if the frame is not a multiple of the interval
        if frame % step != 0:
            for fcurve in obj.animation_data.action.fcurves:
                # Find the keyframe at the current frame
                keyframe = next((kp for kp in fcurve.keyframe_points if kp.co.x == frame), None)
                    
                # Delete the keyframe if it exists
                if keyframe:
                    fcurve.keyframe_points.remove(keyframe, fast=True)
        
