__version__ = "3.2.1b2"


from vendy_bc import core, cli


__all__ = ["core", "cli"]


def run():
    from vendy_bc import __main__

    __main__.main()
