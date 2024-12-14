from loguru import logger

logger.remove()
logger.add(
    lambda msg: print(msg),
    format="<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> | <green>{level: <8}</green> | <level>{message}</level>",
    colorize=True
)
