def run_installation(settings, function_code):
    # write here a installation script 
    settings_dict = {
        'basic_features': settings.get('var1', 0),
        'advanced_features': settings.get('var2', 0),
        'desktop_shortcut': settings.get('var3', 0)
    }
    
    try:
        exec(function_code)
        return True, "Installation completed successfully"
    except Exception as e:
        return False, f"Installation failed: {str(e)}"