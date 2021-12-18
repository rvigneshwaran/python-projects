
def convertTime(seconds):
    """Function created in order to convert seconds to
    hours,minutes and seconds.

    Args:
        seconds ([type]): [Takes Inputs as seconds]

    Returns:
        Hours:Minutes:Seconds in String Format
    """
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)