# Standard library
import warnings
from functools import lru_cache

# Third-party
import astropy.units as u
import numpy as np
from astropy.constants import c, h
from astropy.coordinates import Distance, SkyCoord
from astropy.time import Time
from astroquery.gaia import Gaia


@lru_cache
def get_sky_catalog(
    ra: float,
    dec: float,
    radius: float = 0.155,
    epoch: float = 2000,
    gbpmagnitude_range: tuple = (-3, 20),
    limit=None,
    gaia_keys: list = [],
    time: Time = Time.now(),
) -> dict:
    """
    Gets a catalog of coordinates on the sky based on an input RA, Dec, and radius as well as
    a magnitude range for Gaia. The user can also specify additional keywords to be grabbed
    from Gaia catalog.

    Parameters
    ----------
    ra : float
        Right Ascension of the center of the query radius in degrees.
    dec : float
        Declination of the center of the query radius in degrees.
    radius : float
        Radius centered on ra and dec that will be queried in degrees.
    epoch: float
        The epoch for your input RA and Dec. If not set, assumed to be 2000.
    gbpmagnitude_range : tuple
        Magnitude limits for the query. Targets outside of this range will not be included in
        the final output dictionary.
    limit : int
        Maximum number of targets from query that will be included in output dictionary. If a
        limit is specified, targets will be included based on proximity to specified ra and dec.
    gaia_keys : list
        List of additional Gaia archive columns to include in the final output dictionary.
    time : astropy.Time object
        Time at which to evaluate the positions of the targets in the output dictionary.

    Returns
    -------
    cat : dict
        Dictionary of values from the Gaia archive for each keyword.
    """

    base_keys = [
        "source_id",
        "ra",
        "dec",
        "parallax",
        "pmra",
        "pmdec",
        "radial_velocity",
        "ruwe",
        "phot_bp_mean_mag",
        "teff_gspphot",
        "logg_gspphot",
        "phot_g_mean_flux",
        "phot_g_mean_mag",
    ]

    all_keys = base_keys + gaia_keys

    query_str = f"""
    SELECT {f"TOP {limit} " if limit is not None else ""}* FROM (
        SELECT gaia.{", gaia.".join(all_keys)}, dr2.teff_val AS dr2_teff_val,
        dr2.rv_template_logg AS dr2_logg, tmass.j_m, tmass.j_msigcom, tmass.ph_qual, DISTANCE(
        POINT({u.Quantity(ra, u.deg).value}, {u.Quantity(dec, u.deg).value}),
        POINT(gaia.ra, gaia.dec)) AS ang_sep,
        EPOCH_PROP_POS(gaia.ra, gaia.dec, gaia.parallax, gaia.pmra, gaia.pmdec,
        gaia.radial_velocity, gaia.ref_epoch, {epoch}) AS propagated_position_vector
        FROM gaiadr3.gaia_source AS gaia
        JOIN gaiadr3.tmass_psc_xsc_best_neighbour AS xmatch USING (source_id)
        JOIN gaiadr3.dr2_neighbourhood AS xmatch2 ON gaia.source_id = xmatch2.dr3_source_id
        JOIN gaiadr2.gaia_source AS dr2 ON xmatch2.dr2_source_id = dr2.source_id
        JOIN gaiadr3.tmass_psc_xsc_join AS xjoin USING (clean_tmass_psc_xsc_oid)
        JOIN gaiadr1.tmass_original_valid AS tmass ON
        xjoin.original_psc_source_id = tmass.designation
        WHERE 1 = CONTAINS(
        POINT({u.Quantity(ra, u.deg).value}, {u.Quantity(dec, u.deg).value}),
        CIRCLE(gaia.ra, gaia.dec, {(u.Quantity(radius, u.deg) + 50 * u.arcsecond).value}))
        AND gaia.parallax IS NOT NULL
        AND gaia.phot_bp_mean_mag > {gbpmagnitude_range[0]}
        AND gaia.phot_bp_mean_mag < {gbpmagnitude_range[1]}) AS subquery
    WHERE 1 = CONTAINS(
    POINT({u.Quantity(ra, u.deg).value}, {u.Quantity(dec, u.deg).value}),
    CIRCLE(COORD1(subquery.propagated_position_vector), COORD2(subquery.propagated_position_vector), {u.Quantity(radius, u.deg).value}))
    ORDER BY ang_sep ASC
    """
    job = Gaia.launch_job_async(query_str, verbose=False)
    tbl = job.get_results()
    if len(tbl) == 0:
        raise ValueError("Could not find matches.")
    plx = tbl["parallax"].value.filled(fill_value=0)
    plx[plx < 0] = 0
    cat = {
        "jmag": tbl["j_m"].data.filled(np.nan),
        "bmag": tbl["phot_bp_mean_mag"].data.filled(np.nan),
        "gmag": tbl["phot_g_mean_mag"].data.filled(np.nan),
        "gflux": tbl["phot_g_mean_flux"].data.filled(np.nan),
        "ang_sep": tbl["ang_sep"].data.filled(np.nan) * u.deg,
    }
    cat["teff"] = (
        tbl["teff_gspphot"].data.filled(
            tbl["dr2_teff_val"].data.filled(np.nan)
        )
        * u.K
    )
    cat["logg"] = tbl["logg_gspphot"].data.filled(
        tbl["dr2_logg"].data.filled(np.nan)
    )
    cat["RUWE"] = tbl["ruwe"].data.filled(99)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        cat["coords"] = SkyCoord(
            ra=tbl["ra"].value.data * u.deg,
            dec=tbl["dec"].value.data * u.deg,
            pm_ra_cosdec=tbl["pmra"].value.filled(fill_value=0)
            * u.mas
            / u.year,
            pm_dec=tbl["pmdec"].value.filled(fill_value=0) * u.mas / u.year,
            obstime=Time.strptime("2016", "%Y"),
            distance=Distance(parallax=plx * u.mas, allow_negative=True),
            radial_velocity=tbl["radial_velocity"].value.filled(fill_value=0)
            * u.km
            / u.s,
        ).apply_space_motion(time)
    cat["source_id"] = np.asarray(
        [f"Gaia DR3 {i}" for i in tbl["source_id"].value.data]
    )
    for key in gaia_keys:
        cat[key] = tbl[key].data.filled(np.nan)
    return cat


def photon_energy(wavelength):
    """Converts photon wavelength to energy."""
    return ((h * c) / wavelength) * 1 / u.photon


def wavelength_to_rgb(wavelength, gamma=0.8):
    """This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    """

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return np.asarray((int(R), int(G), int(B))) / 256
