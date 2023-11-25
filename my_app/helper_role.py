from flask import current_app
from flask_login import current_user
from flask_principal import identity_loaded, identity_changed, ActionNeed, RoleNeed, Permission, Identity, AnonymousIdentity
from enum import Enum

# Custom roles and actions
class Role(str, Enum):
    editor = "editor"
    viewer = "viewer"

class Action(str, Enum):
    edit = "create, update and delete"
    view = "list and read"

# Needs
__editor_role_need = RoleNeed(Role.editor)
__viewer_role_need = RoleNeed(Role.viewer)

__edit_action_need = ActionNeed(Action.edit)
__view_action_need = ActionNeed(Action.view)

# Permissions
require_editor_role = Permission(__editor_role_need)
require_viewer_role = Permission(__viewer_role_need)

require_edit_permission = Permission(__edit_action_need)
require_view_permission = Permission(__view_action_need)

@identity_loaded.connect
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'role'):
        if current_user.role == Role.editor:
            # Role needs
            identity.provides.add(__editor_role_need)
            # Action needs
            identity.provides.add(__edit_action_need)
            identity.provides.add(__view_action_need)
        elif current_user.role == Role.viewer:
            # Role needs
            identity.provides.add(__viewer_role_need)
            # Action needs
            identity.provides.add(__view_action_need)
        else:
            current_app.logger.debug("Unkown role")

def notify_identity_changed():
    if hasattr(current_user, 'email'):
        identity = Identity(current_user.email)
    else:
        identity = AnonymousIdentity()
    
    identity_changed.send(current_app._get_current_object(), identity = identity)