import bpy

###RIG CONTROLS

class RigUI(bpy.types.Panel):
    bl_label = "Rig Controls"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "posemode"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        pose_bones = context.active_object.pose.bones
        try:
            selected_bones = [bone.name for bone in context.selected_pose_bones]
            selected_bones += [context.active_pose_bone.name]
        except (AttributeError, TypeError):
            return
        
        def is_selected(names):
        #Returns whether any of the named bones are selected
            if type(names) == list:
                for name in names:
                    if name in selected_bones:
                        return True
            elif names in selected_bones:
                return True
            return False
    
        #Define the names we'll use for bones
        
        head = "head"
        neck = "neck"
        
        ribs = "ribs"
        hips = "hips"
        
        shoulderl = "shoulder.L"
        uparmfkl = "upper_arm_FK.L"
        forearmfkl = "forearm_FK.L"
        handfkl = "hand_FK.L"
        
        shoulderr = "shoulder.R"
        uparmfkr = "upper_arm_FK.R"
        forearmfkr = "forearm_FK.R"
        handfkr = "hand_FK.R"
        
        thighfkl = "thigh_FK.L"
        shinfkl = "shin_FK.L"
        footfkl = "foot_FK.L"
        toefkl = "toe_FK.L"
        
        thighfkr = "thigh_FK.R"
        shinfkr = "shin_FK.R"
        footfkr = "foot_FK.R"
        toefkr = "toe_FK.R"
        
        handikl = "hand_IK.L"
        elbowpolel = "elbow_pole.L"
        
        handikr = "hand_IK.R"
        elbowpoler = "elbow_pole.R"
        
        footikl = "foot_IK.L"
        kneepolel = "knee_pole.L"
        
        footikr = "foot_IK.R"
        kneepoler = "knee_pole.R"
        
        swordattachl = "sword_attach.L"
        swordattachr = "sword_attach.R"
        
        saiattachl = "sai_attach.L"
        saiattachr = "sai_attach.R"
        
        knife1attach = "knife_attach.1"
        knife2attach = "knife_attach.2"
        knife3attach = "knife_attach.3"
        
        swordl = "sword.L"
        swordr = "sword.R"
        
        sail = "sai.L"
        sair = "sai.R"
        
        knife1 = "knife.1"
        knife2 = "knife.2"
        knife3 = "knife.3"
        
        
        #Define what controls to show depending on the bones selected
        
        if is_selected([head, neck]):
            layout.prop(pose_bones["head"], '["isolate head"]', slider=True)
           
        if is_selected([ribs, hips]):
            layout.prop(pose_bones["ribs"], '["isolate torso"]', slider=True)
            
        if is_selected([shoulderl, uparmfkl, forearmfkl, handfkl]):
            layout.prop(pose_bones["upper_arm_FK.L"], '["isolate left arm"]', slider=True)
            
        if is_selected([shoulderr, uparmfkr, forearmfkr, handfkr]):
            layout.prop(pose_bones["upper_arm_FK.R"], '["isolate right arm"]', slider=True)
        
        if is_selected([thighfkl, shinfkl, footfkl, toefkl]):
            layout.prop(pose_bones["thigh_FK.L"], '["isolate left leg"]', slider=True)
            
        if is_selected([thighfkr, shinfkr, footfkr, toefkr]):
            layout.prop(pose_bones["thigh_FK.R"], '["isolate right leg"]', slider=True)
            
        if is_selected([handikl, elbowpolel, shoulderl, uparmfkl, forearmfkl, handfkl]):
            layout.prop(pose_bones["hand_IK.L"], '["ik/fk left arm"]', slider=True)
            
        if is_selected([handikr, elbowpoler, shoulderr, uparmfkr, forearmfkr, handfkr]):
            layout.prop(pose_bones["hand_IK.R"], '["IK/FK right arm"]', slider=True)
            
        if is_selected([footikl, kneepolel, thighfkl, shinfkl, footfkl, toefkl]):
            layout.prop(pose_bones["foot_IK.L"], '["IK/FK left leg"]', slider=True)
            
        if is_selected([footikr, kneepoler, thighfkr, shinfkr, footfkr, toefkr]):
            layout.prop(pose_bones["foot_IK.R"], '["IK/FK right leg"]', slider=True)
        
        if is_selected([handikl, swordattachl]):
            layout.prop(pose_bones["hand_IK.L"], '["sword attach left"]', slider=True)
            
        if is_selected([handikr, swordattachr]):
            layout.prop(pose_bones["hand_IK.R"], '["sword attach right"]', slider=True)
           
        if is_selected([handikl, saiattachl]):
            layout.prop(pose_bones["hand_IK.L"], '["sai attach left"]', slider=True)
        
        if is_selected([handikr, saiattachr]):
            layout.prop(pose_bones["hand_IK.R"], '["sai attach right"]', slider=True)
            
        if is_selected([handikl, knife1attach]):
            layout.prop(pose_bones["hand_IK.L"], '["knife 1 attach"]', slider=True)
            
        if is_selected([handikl, knife2attach]):
            layout.prop(pose_bones["hand_IK.L"], '["knife 2 attach"]', slider=True)
            
        if is_selected([handikl, knife3attach]):
            layout.prop(pose_bones["hand_IK.L"], '["knife 3 attach"]', slider=True)
        
        if is_selected([swordl, swordattachl]):
            layout.prop(pose_bones["sword.L"], '["sheath sword left"]', slider=True)
            
        if is_selected([swordr, swordattachr]):
            layout.prop(pose_bones["sword.R"], '["sheath sword right"]', slider=True)
            
        if is_selected([sail, saiattachl]):
            layout.prop(pose_bones["sai.L"], '["sheath sai left"]', slider=True)
            
        if is_selected([sair, saiattachr]):
            layout.prop(pose_bones["sai.R"], '["sheath sai right"]', slider=True)
            
        if is_selected([knife1, knife1attach]):
            layout.prop(pose_bones["knife.1"], '["sheath knife 1"]', slider=True)
            
        if is_selected([knife2, knife2attach]):
            layout.prop(pose_bones["knife.2"], '["sheath knife 2"]', slider=True)
            
        if is_selected([knife3, knife3attach]):
            layout.prop(pose_bones["knife.3"], '["sheath knife 3"]', slider=True)
            
#Custom Rig layers

class RigLayers(bpy.types.Panel):
    bl_label = "Rig Controls"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Rig Layers"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 0, toggle=True, text='head')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 7, toggle=True, text='torso')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 1, toggle=True, text='left arm FK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 3, toggle=True, text='right arm FK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 2, toggle=True, text='left arm IK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 4, toggle=True, text='right arm IK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 8, toggle=True, text='left leg FK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 10, toggle=True, text='right leg FK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 9, toggle=True, text='left leg IK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 11, toggle=True, text='right leg IK')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 5, toggle=True, text='fingers main')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 6, toggle=True, text='fingers extra')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 16, toggle=True, text='face')
        1
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 12, toggle=True, text='swords')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 14, toggle=True, text='sai')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 15, toggle=True, text='knives/flaps')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index = 24, toggle=True, text='ROOT')





bpy.utils.register_class(RigUI)
bpy.utils.register_class(RigLayers)