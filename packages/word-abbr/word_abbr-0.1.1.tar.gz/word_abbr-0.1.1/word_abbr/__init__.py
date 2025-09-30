from .abbreviator import Abbreviator

__version__ = "0.1.1"
__all__ = ["Abbreviator"]

# 便捷函数（可选）
def get_abbr(word: str) -> str:
    return Abbreviator().get(word)