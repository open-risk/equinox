# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Jazzmin Django settings for the Equinox platform.

"""

JAZZMIN_SETTINGS = {
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    # "show_ui_builder": True,

    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Equinox",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Equinox",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Equinox",

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    "site_logo": "start/img/equinox.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Equinox",

    # Copyright on the footer
    "copyright": "Open Risk",

    # The model admin to search from the search bar, search bar omitted if excluded
    # "search_model": "auth.User",
    # "search_model": "portfolio.project",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "/", "permissions": ["auth.view_user"]},

    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/open-risk/equinox", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to expand the side menu
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ['auth'],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["start", "portfolio", "policy", "risk", "reporting", "reference", "auth"],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############

    "custom_css": "./start/css/jazzmin.css",
    "custom_js": None,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs

    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-lightblue",
    "accent": "accent-olive",
    "navbar": "navbar-lightblue navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-lightblue",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cerulean",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True
}
