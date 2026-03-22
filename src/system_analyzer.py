"""
System Analyzer - Coleta dados completos do PC
"""

import psutil
import platform
import json
from datetime import datetime

class SystemAnalyzer:
    """Analisa e coleta informações do sistema"""
    
    def __init__(self):
        self.system_info = {}
    
    def get_cpu_info(self):
        """Coleta informações da CPU"""
        return {
            "cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
            "frequency_ghz": psutil.cpu_freq().current / 1000,
            "usage_percent": psutil.cpu_percent(interval=1),
            "processor_name": platform.processor()
        }
    
    def get_ram_info(self):
        """Coleta informações de RAM"""
        ram = psutil.virtual_memory()
        return {
            "total_gb": round(ram.total / (1024**3), 2),
            "available_gb": round(ram.available / (1024**3), 2),
            "used_gb": round(ram.used / (1024**3), 2),
            "usage_percent": ram.percent
        }
    
    def get_gpu_info(self):
        """Coleta informações de GPU"""
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                return {
                    "name": gpu.name,
                    "memory_total_mb": gpu.memoryTotal,
                    "memory_used_mb": gpu.memoryUsed,
                    "load_percent": gpu.load * 100
                }
        except:
            pass
        
        return {"name": "Integrada", "memory_total_mb": 0}
    
    def get_storage_info(self):
        """Coleta informações de armazenamento"""
        storage = psutil.disk_usage('/')
        return {
            "total_gb": round(storage.total / (1024**3), 2),
            "used_gb": round(storage.used / (1024**3), 2),
            "free_gb": round(storage.free / (1024**3), 2),
            "usage_percent": storage.percent
        }
    
    def get_os_info(self):
        """Coleta informações do Sistema Operacional"""
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.architecture()[0]
        }
    
    def get_network_info(self):
        """Coleta informações de rede"""
        net = psutil.net_if_stats()
        return {
            "interfaces": len(net),
            "connected": any(iface.isup for iface in net.values())
        }
    
    def categorize_machine(self):
        """Categoriza a máquina em: Antiga, Média, Avançada"""
        cpu = self.get_cpu_info()
        ram = self.get_ram_info()
        cores = cpu["logical_cores"]
        ram_gb = ram["total_gb"]
        
        if cores >= 8 and ram_gb >= 16:
            return "AVANÇADA", 9
        elif cores >= 6 and ram_gb >= 8:
            return "MÉDIA", 7
        elif cores >= 4 and ram_gb >= 4:
            return "BÁSICA", 5
        else:
            return "ANTIGA", 3
    
    def analyze_full(self):
        """Análise completa do sistema"""
        category, score = self.categorize_machine()
        
        return {
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "performance_score": score,
            "cpu": self.get_cpu_info(),
            "ram": self.get_ram_info(),
            "gpu": self.get_gpu_info(),
            "storage": self.get_storage_info(),
            "os": self.get_os_info(),
            "network": self.get_network_info()
        }

if __name__ == "__main__":
    analyzer = SystemAnalyzer()
    analysis = analyzer.analyze_full()
    print(json.dumps(analysis, indent=2))
