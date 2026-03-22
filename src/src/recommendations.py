"""
Recommendations Engine - Recomenda ferramentas baseado no sistema
"""

import json
from pathlib import Path

class RecommendationEngine:
    """Motor de recomendações inteligente"""
    
    # Base de dados de ferramentas
    TOOLS_DATABASE = {
        "ANTIGA": {
            "system": [
                {"name": "CCleaner", "category": "Limpeza", "link": "https://www.ccleaner.com"},
                {"name": "Autoruns", "category": "Startup", "link": "https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns"},
                {"name": "Recuva", "category": "Recuperação", "link": "https://www.ccleaner.com/recuva"}
            ],
            "development": [
                {"name": "VS Code", "category": "Editor", "link": "https://code.visualstudio.com"},
                {"name": "Git", "category": "Versionamento", "link": "https://git-scm.com"},
                {"name": "Python", "category": "Runtime", "link": "https://www.python.org"}
            ],
            "media": [
                {"name": "VLC", "category": "Vídeo", "link": "https://www.videolan.org"},
                {"name": "Audacity", "category": "Áudio", "link": "https://www.audacityteam.org"}
            ]
        },
        "BÁSICA": {
            "system": [
                {"name": "CCleaner", "category": "Limpeza", "link": "https://www.ccleaner.com"},
                {"name": "HWiNFO", "category": "Monitoramento", "link": "https://www.hwinfo.com"},
                {"name": "7-Zip", "category": "Compressão", "link": "https://www.7-zip.org"}
            ],
            "development": [
                {"name": "VS Code", "category": "Editor", "link": "https://code.visualstudio.com"},
                {"name": "Git", "category": "Versionamento", "link": "https://git-scm.com"},
                {"name": "Node.js", "category": "Runtime", "link": "https://nodejs.org"}
            ],
            "media": [
                {"name": "VLC", "category": "Vídeo", "link": "https://www.videolan.org"},
                {"name": "ImageMagick", "category": "Imagem", "link": "https://imagemagick.org"}
            ]
        },
        "MÉDIA": {
            "system": [
                {"name": "HWiNFO", "category": "Monitoramento", "link": "https://www.hwinfo.com"},
                {"name": "Razer Cortex", "category": "Gaming", "link": "https://www.razer.com/cortex"},
                {"name": "WizTree", "category": "Análise Disco", "link": "https://wiztreefree.com"}
            ],
            "development": [
                {"name": "Visual Studio Code", "category": "IDE", "link": "https://code.visualstudio.com"},
                {"name": "Git", "category": "Versionamento", "link": "https://git-scm.com"},
                {"name": "Docker", "category": "Containerização", "link": "https://www.docker.com"}
            ],
            "media": [
                {"name": "OBS Studio", "category": "Streaming", "link": "https://obsproject.com"},
                {"name": "DaVinci Resolve", "category": "Edição", "link": "https://www.blackmagicdesign.com"}
            ]
        },
        "AVANÇADA": {
            "system": [
                {"name": "HWiNFO", "category": "Monitoramento", "link": "https://www.hwinfo.com"},
                {"name": "MSI Afterburner", "category": "Overclock", "link": "https://www.msi.com/Landing/afterburner"},
                {"name": "Prime95", "category": "Stress Test", "link": "https://www.mersenne.org/prime95"}
            ],
            "development": [
                {"name": "Visual Studio", "category": "IDE", "link": "https://visualstudio.microsoft.com"},
                {"name": "JetBrains Suite", "category": "IDE", "link": "https://www.jetbrains.com"},
                {"name": "Docker", "category": "Containerização", "link": "https://www.docker.com"}
            ],
            "media": [
                {"name": "Adobe Creative Suite", "category": "Professional", "link": "https://www.adobe.com"},
                {"name": "DaVinci Resolve Studio", "category": "Pós-produção", "link": "https://www.blackmagicdesign.com"}
            ]
        }
    }
    
    def __init__(self):
        pass
    
    def get_recommendations(self, system_analysis):
        """Retorna recomendações baseadas na análise do sistema"""
        category = system_analysis["category"]
        score = system_analysis["performance_score"]
        
        recommendations = {
            "category": category,
            "score": score,
            "tools": self.TOOLS_DATABASE.get(category, {})
        }
        
        return recommendations
    
    def get_improvement_suggestions(self, system_analysis):
        """Sugestões de melhoria específicas"""
        suggestions = []
        
        # CPU
        if system_analysis["cpu"]["usage_percent"] > 80:
            suggestions.append({
                "type": "CPU",
                "issue": "Uso elevado de CPU",
                "solution": "Feche programas desnecessários ou atualize processador"
            })
        
        # RAM
        if system_analysis["ram"]["usage_percent"] > 80:
            suggestions.append({
                "type": "RAM",
                "issue": "Memória quase cheia",
                "solution": "Adicione mais RAM ou feche abas do navegador"
            })
        
        # Storage
        if system_analysis["storage"]["usage_percent"] > 85:
            suggestions.append({
                "type": "STORAGE",
                "issue": "Espaço em disco crítico",
                "solution": "Limpe arquivos temporários ou remova programas"
            })
        
        return suggestions

if __name__ == "__main__":
    engine = RecommendationEngine()
    print(json.dumps(engine.TOOLS_DATABASE, indent=2))
