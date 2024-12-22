def validate_input(theme, style, valid_themes, valid_styles):
    """Validates the user's theme and style input."""
    print(f"Validating theme: '{theme}', style: '{style}'")
    if theme not in valid_themes:
        raise ValueError(f"Invalid theme: {theme}. Valid options: {valid_themes}")
    if style not in valid_styles:
        raise ValueError(f"Invalid style: {style}. Valid options: {valid_styles}")
    return True

def validate_traits(traits, valid_traits):
    """Validates user-selected traits."""
    print(f"Validating traits: {traits}")
    for trait in traits:
        if trait not in valid_traits:
            raise ValueError(f"Invalid trait: {trait}. Valid options: {valid_traits}")
    return True
