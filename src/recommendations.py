# Intelligent Recommendation Engine

class RecommendationEngine:
    def __init__(self, system_specs):
        self.system_specs = system_specs

    def recommend_tools(self):
        recommendations = []
        if self.system_specs['cpu'] >= 8:
            recommendations.append("High-performance Graphics Software")
        if self.system_specs['ram'] >= 16:
            recommendations.append("Video Editing Tools")
        if self.system_specs['storage'] >= 512:
            recommendations.append("Large Database Management Systems")
        return recommendations

# Example usage:
# specs = {'cpu': 8, 'ram': 16, 'storage': 512}
# engine = RecommendationEngine(specs)
# print(engine.recommend_tools())