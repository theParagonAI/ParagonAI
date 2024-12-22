class Analytics:
    def __init__(self):
        self.data = []

    def record_creation(self, theme, style):
        print(f"Recording avatar creation: Theme='{theme}', Style='{style}'")
        self.data.append({"theme": theme, "style": style})

    def get_trend_analysis(self):
        print("Analyzing trends...")
        trends = {}
        for record in self.data:
            key = (record["theme"], record["style"])
            trends[key] = trends.get(key, 0) + 1
        return sorted(trends.items(), key=lambda x: x[1], reverse=True)

    def get_usage_statistics(self):
        print("Generating usage statistics...")
        total = len(self.data)
        by_theme = {}
        by_style = {}
        for record in self.data:
            by_theme[record["theme"]] = by_theme.get(record["theme"], 0) + 1
            by_style[record["style"]] = by_style.get(record["style"], 0) + 1
        return {
            "total_creations": total,
            "by_theme": by_theme,
            "by_style": by_style
        }
