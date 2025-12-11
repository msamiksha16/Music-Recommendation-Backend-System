def generate_recommendations(sp, genre="pop", mood=None):
    # search by genre
    results = sp.search(
        q=f"genre:{genre}",
        type="track",
        limit=20,
        market="US"
    )

    tracks = results["tracks"]["items"]

    # simple mood-based filtering using popularity
    if mood == "happy":
        tracks = [t for t in tracks if t["popularity"] >= 60]
    elif mood == "sad":
        tracks = [t for t in tracks if t["popularity"] <= 40]
    elif mood == "energetic":
        tracks = [t for t in tracks if t["popularity"] >= 70]

    # format result
    recommendations = []
    for t in tracks[:10]:
        recommendations.append({
            "name": t["name"],
            "artist": t["artists"][0]["name"],
            "url": t["external_urls"]["spotify"],
            "popularity": t["popularity"],
        })

    return recommendations
