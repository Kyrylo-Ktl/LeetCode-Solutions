import logging
import sys

sys.path.append('.')
from infrastructure.src.formatter import MarkdownFormatter

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    MarkdownFormatter.format()
