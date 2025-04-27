def get_bandeira(nacionalidade):
    """Retorna o emoji da bandeira correspondente à nacionalidade."""
    bandeiras = {
        "Brasil": "🇧🇷",
        "Cazaquistão": "🇰🇿",
        "Letônia": "🇱🇻",
        "Espanha": "🇪🇸",
        "Estados Unidos": "🇺🇸",
        "Canadá": "🇨🇦",
        "Portugal": "🇵🇹",
        "Suécia": "🇸🇪",
        "Dinamarca": "🇩🇰",
        "França": "🇫🇷",
        # Adicione mais países conforme precisar
    }

    return bandeiras.get(nacionalidade, "🏳️") 