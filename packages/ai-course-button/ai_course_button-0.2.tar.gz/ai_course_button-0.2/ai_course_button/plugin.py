from openedx.core.djangoapps.plugins.constants import PluginSettings, ProjectType
from openedx.core.djangoapps.plugins import PluginConfig

class AICourseButtonPluginConfig(PluginConfig):
    plugin_app = {
        PluginSettings.CONFIG: {
            ProjectType.CMS: {
                PluginSettings.INSTALLED_APPS: ["ai_course_button"],
            }
        }
    }

