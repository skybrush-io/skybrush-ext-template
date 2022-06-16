from trio import sleep

from flockwave.server.ext.base import Extension

__all__ = ("ExtensionTemplate", )


class ExtensionTemplate(Extension):
    """Template for Skybrush Server extensions."""

    async def run(self, app, configuration, logger):
        """This function is called when the extension was loaded.

        The signature of this function is flexible; you may use zero, one, two
        or three positional arguments after ``self``. The extension manager
        will detect the number of positional arguments and pass only the ones
        that you expect.

        Parameters:
            app: the Skybrush server application that the extension belongs to.
                Also available as ``self.app``.
            configuration: the configuration object. Also available in the
                ``configure()`` method.
            logger: Python logger object that the extension may use. Also
                available as ``self.log``.
        """
        self.log.info("Extension is now running.")
        await sleep(2)
        self.log.warn(configuration.get("bacon"))
        await sleep(3)
        self.log.info("Five seconds have passed, exiting.")

