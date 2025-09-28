"""Utilities for getting WCS"""

import bz2
import functools
import json
import os
import warnings

import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import Angle, SkyCoord

from . import PACKAGEDIR, log


def deprecated(replacement=None):
    """
    A decorator to mark functions as deprecated.

    Args:
        replacement (str): The name of the replacement function to include in the warning.
    """

    def decorator(func):
        replacement_msg = f" Use '{replacement}' instead." if replacement else ""
        message = f"The function '{func.__name__}' is deprecated.{replacement_msg}"

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                message,
                DeprecationWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def _fix_keys(dict):
    return {
        int(key): np.asarray(item) if isinstance(item, list) else item
        for key, item in dict.items()
    }


def _load_wcs_database():
    log.debug("Loading WCS data from file")
    filename = f"{PACKAGEDIR}/data/TESS_wcs_data.json.bz2"
    if not os.path.isfile(filename):
        raise ValueError(
            "`tesswcs` database doesn't exist, run `tesswcs.database.update_database()`."
        )
    with bz2.open(filename, "rt", encoding="utf-8") as f:
        wcs_dict = json.load(f)
    log.debug("Adding correct units to WCS data")
    _wcs_dicts = {}
    for sector in wcs_dict.keys():
        _wcs_dicts[int(sector)] = {
            "ra": wcs_dict[sector]["ra"],
            "dec": wcs_dict[sector]["dec"],
            "roll": wcs_dict[sector]["roll"],
        }
        for camera in "1234"[::-1]:
            _wcs_dicts[int(sector)][int(camera)] = {}
            for ccd in "1234"[::-1]:
                _wcs_dicts[int(sector)][int(camera)][int(ccd)] = {
                    "pa": Angle(wcs_dict[sector][camera][ccd]["pa"] * u.rad),
                    "sep": Angle(wcs_dict[sector][camera][ccd]["sep"] * u.deg),
                    "pa_sip": Angle(wcs_dict[sector][camera][ccd]["pa_sip"] * u.rad),
                    "sep_sip": Angle(wcs_dict[sector][camera][ccd]["sep_sip"] * u.deg),
                    "ccd_center_crval": wcs_dict[sector][camera][ccd][
                        "ccd_center_crval"
                    ],
                    "ccd_center_crval_sip": wcs_dict[sector][camera][ccd][
                        "ccd_center_crval_sip"
                    ],
                    "ccd_center_crpix": wcs_dict[sector][camera][ccd][
                        "ccd_center_crpix"
                    ],
                    "crval0": wcs_dict[sector][camera][ccd]["crval0"],
                    "crpix0": wcs_dict[sector][camera][ccd]["crpix0"],
                    "cd": np.asarray(wcs_dict[sector][camera][ccd]["cd"]),
                    "sip_a_order": wcs_dict[sector][camera][ccd]["sip_a_order"],
                    "sip_a": np.asarray(wcs_dict[sector][camera][ccd]["sip_a"]),
                    "sip_b": np.asarray(wcs_dict[sector][camera][ccd]["sip_b"]),
                    "sip_ap": np.asarray(wcs_dict[sector][camera][ccd]["sip_ap"]),
                    "sip_bp": np.asarray(wcs_dict[sector][camera][ccd]["sip_bp"]),
                    "corner_pa": Angle(
                        wcs_dict[sector][camera][ccd]["corner_pa"] * u.rad
                    ),
                    "corner_sep": Angle(
                        wcs_dict[sector][camera][ccd]["corner_sep"] * u.deg
                    ),
                    "corner": SkyCoord(
                        wcs_dict[sector][camera][ccd]["corner_ra"],
                        wcs_dict[sector][camera][ccd]["corner_dec"],
                        unit="deg",
                    ),
                    "corner_sip_pa": Angle(
                        wcs_dict[sector][camera][ccd]["corner_pa"] * u.rad
                    ),
                    "corner_sip_sep": Angle(
                        wcs_dict[sector][camera][ccd]["corner_sep"] * u.deg
                    ),
                    "corner_sip": SkyCoord(
                        wcs_dict[sector][camera][ccd]["corner_sip_ra"],
                        wcs_dict[sector][camera][ccd]["corner_sip_dec"],
                        unit="deg",
                    ),
                }
    return _wcs_dicts


def _load_support_dicts():
    log.debug("Loading support dictionaries from file")

    support_dicts = []

    for var in ["xs", "ys", "xcent", "ycent", "M"]:
        filename = f"{PACKAGEDIR}/data/TESS_wcs_{var}.json.bz2"
        with bz2.open(filename, "rt", encoding="utf-8") as f:
            support_dict = json.load(f)
        support_dict = {int(key): _fix_keys(dict) for key, dict in support_dict.items()}
        support_dicts.append(support_dict)

    filename = f"{PACKAGEDIR}/data/TESS_wcs_sip.json.bz2"
    with bz2.open(filename, "rt", encoding="utf-8") as f:
        sip = json.load(f)
    sip_dict = {
        key: _fix_keys({int(key): _fix_keys(dict) for key, dict in sip_dict.items()})
        for key, sip_dict in sip.items()
    }
    support_dicts.append(sip_dict)
    return support_dicts


def _load_warp_matrices():
    log.debug("Loading warp matrices dictionary from file")
    filename = f"{PACKAGEDIR}/data/TESS_wcs_Ms.json.bz2"
    if not os.path.isfile(filename):
        log.warn(
            "No warp matrices found. Either download them or fit them using `tesswcs.tesswcs._build_warp_matrices`"
        )
        return None, None
    with bz2.open(filename, "rt", encoding="utf-8") as f:
        Ms = json.load(f)
    Ms = {int(key): _fix_keys(dict) for key, dict in Ms.items()}
    filename = f"{PACKAGEDIR}/data/TESS_wcs_offset_weights.json.bz2"
    if not os.path.isfile(filename):
        log.warn(
            "No warp matrices found. Either download them or fit them using `tesswcs.tesswcs._build_warp_matrices`"
        )
        return None, None
    with bz2.open(filename, "rt", encoding="utf-8") as f:
        offset_weights = json.load(f)
    offset_weights = {int(key): _fix_keys(dict) for key, dict in offset_weights.items()}
    return Ms, offset_weights


def angle_to_matrix(theta):
    """Convert an angle theta in degrees to a rotation matrix"""
    cos_angle = np.cos(np.deg2rad(theta))
    sin_angle = np.sin(np.deg2rad(theta))
    return np.array([[cos_angle, -sin_angle], [sin_angle, cos_angle]])


def angle_from_matrix(matrix):
    """Convert a rotation matrix to an angle in degrees"""
    theta = np.rad2deg(np.arctan2(matrix[1, 0], matrix[0, 0]))
    return theta


def footprint(npoints=50, rows=2078, columns=2136):
    """Gets the column and row points for CCD edges"""
    column = np.hstack(
        [
            np.zeros(npoints),
            np.linspace(0, rows, npoints),
            np.linspace(0, rows, npoints),
            np.ones(npoints) * rows,
        ]
    )
    row = np.hstack(
        [
            np.linspace(0, columns, npoints),
            np.zeros(npoints),
            np.ones(npoints) * columns,
            np.linspace(0, columns, npoints),
        ]
    )
    return np.vstack([row, column]).T


def get_M(truth, approx):
    """Finds the transformation matrix that makes `approx` best fit `truth`"""
    truth = np.hstack([truth, np.ones((truth.shape[0], 1))])
    approx = np.hstack([approx, np.ones((approx.shape[0], 1))])
    a, b, e = np.linalg.solve(truth.T.dot(truth), truth.T.dot(approx[:, 0]))
    c, d, f = np.linalg.solve(truth.T.dot(truth), truth.T.dot(approx[:, 1]))

    M = np.linalg.inv(np.asarray([[a, b, e], [c, d, f], [0, 0, 1]]))
    return M


def plot_geometry(ax=None):
    # This lets us reorganize four coordinate corners to plot a square
    s = [0, 1, 3, 2, 0]

    xs, ys, xcent, ycent, M, _ = _load_support_dicts()
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(5, 5))
    for camera in np.arange(1, 5):
        for ccd in np.arange(1, 5):
            ax.plot(
                ys[camera][ccd][s],
                xs[camera][ccd][s],
                c=f"C{camera - 1}",
            )
            ax.scatter(
                ys[camera][ccd].mean(),
                xs[camera][ccd].mean(),
                c=f"C{camera - 1}",
            )
    lim = 60
    ax.set(
        xlim=(-lim, lim),
        ylim=(-lim, lim),
        xlabel="Column [degrees]",
        ylabel="Row [degrees]",
        title="TESS Observatory Geometry",
    )
    return ax
