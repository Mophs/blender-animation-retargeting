bl_info = {
	"name" : "Animation Retargeting",
	"author" : "Mwni, Mophs",
	"description" : "Retarget animations from one rig to another",
	"version": (1, 1, 0),
	"blender" : (2, 90, 1),
	"location" : "3D View > Tools (Right Side) > Retarget",
	"warning" : "",
	"category" : "Animation",
	'wiki_url': 'https://github.com/Mophs/blender-animation-retargeting',
    'tracker_url': 'https://github.com/Mophs/blender-animation-retargeting',
}

from . import addon

def register():
	addon.register()

def unregister():
	addon.unregister()