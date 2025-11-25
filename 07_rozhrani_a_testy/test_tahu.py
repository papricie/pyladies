def test_spatneho_tahu():
    """🤘 vs. 🖖 není správný vstup"""
    with pytest.raises(ValueError):
        vyhodnot('metal', 'spock')