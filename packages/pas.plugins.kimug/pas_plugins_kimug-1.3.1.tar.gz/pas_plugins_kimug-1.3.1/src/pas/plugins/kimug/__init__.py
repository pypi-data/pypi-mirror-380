"""Init and utils."""

from AccessControl.Permissions import manage_users
from Products.PluggableAuthService import registerMultiPlugin
from zope.i18nmessageid import MessageFactory

import logging
import os


PACKAGE_NAME = "pas.plugins.kimug"
PLUGIN_ID = "oidc"
_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
tpl_dir = os.path.join(os.path.dirname(__file__), "static")


def initialize(context):
    """Initializer called when used as a Zope 2 product.

    This is referenced from configure.zcml. Registrations as a "Zope 2 product"
    is necessary for GenericSetup profiles to work, for example.

    Here, we call the Archetypes machinery to register our content types
    with Zope and the CMF.
    """
    from pas.plugins.kimug import plugin

    registerMultiPlugin("Kimug Plugin")
    context.registerClass(
        plugin.KimugPlugin,
        permission=manage_users,
        icon=os.path.join(tpl_dir, "logo.svg"),
        constructors=(plugin.manage_addKimugPluginForm, plugin.manage_addKimugPlugin),
        visibility=None,
    )
