import numpy as np
from numpy.lib import recfunctions as rfn
from pathlib import Path
from .detector import Detector


class DynamicOrientation:
    """
    Handler for dynamic orientation files.
    """

    def __init__(self, filename, detector=None):
        self.filename = Path(filename)
        self._fits = None
        if self.filename.suffix == ".root":
            self.read_file_root()
        else:
            raise NotImplemented(
                "Error, only dynamic  file in root format are supported"
            )

        if detector:
            self._detector = Detector(detector)

    def read_file_root(self):
        """
        Implement the reading of the root tree so populate self._head and self._fits.
        """
        import uproot

        with uproot.open(self.filename) as fin:
            tree = fin["ORIENTATION/ORIENTATION"]
            keys = ["id", "t", "a", "b", "c", "d", "roll", "pitch", "yaw"]
            aliases = {
                "roll": "atan2(2 * (a*b + c*d), 1 - 2 * (b**2 + c**2))",
                "pitch": "arcsin(2 * (a*c - d*b))",
                "yaw": "atan2(2 * (a*d + b*c), 1 - 2 * (b**2 + d**2))",
            }
            self._fits = tree.arrays(keys, aliases=aliases).to_numpy()

    @property
    def du_floor(self):
        """
        Enrich the fits informations with the du:floor position from detector file
        """
        mapping = self._detector.module_id_mapping
        du_floor = np.stack([mapping[module] for module in self._fits["id"]])
        return du_floor[:, 0], du_floor[:, 1]

    @property
    def fits(self):
        """Return the content of 'ORIENTATION/"""
        return self._fits
