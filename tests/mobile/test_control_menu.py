from qa_guru_python_diploma.pages.mobile import control_menu


def test_control_buttons_should_be_shown():
    # THEN
    control_menu.button_my_ivi_should_be_shown()
    control_menu.button_catalog_should_be_shown()
    control_menu.button_downloads_should_be_shown()
    control_menu.button_profile_should_be_shown()
