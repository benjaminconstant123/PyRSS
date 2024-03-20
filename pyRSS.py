import feedparser

# URL du flux RSS à récupérer
url_flux_rss = 'https://www.gamekult.com/feed.xml'

# Analyser le flux RSS
flux = feedparser.parse(url_flux_rss)

# Vérifier s'il y a des erreurs lors de l'analyse du flux
if 'bozo_exception' in flux and isinstance(flux.bozo_exception, Exception):
    print("Erreur lors de l'analyse du flux RSS:", flux.bozo_exception)
else:
    # Afficher les informations du flux RSS
    print("Titre du flux RSS:", flux.feed.title)
    print("Description du flux RSS:", flux.feed.description)
    print("Lien du flux RSS:", flux.feed.link)
    print()

    # Afficher les titres et les liens des éléments du flux RSS
    print("Articles:")
    for entry in flux.entries:
        print("Titre:", entry.title)
        print("Lien:", entry.link)
        print()
