import numpy as np
from scipy.ndimage import fourier_shift
from skimage.registration import phase_cross_correlation

from mbo_utilities import log

TWO_DIM_PHASECORR_METHODS = {"frame", None}
THREE_DIM_PHASECORR_METHODS = ["mean", "max", "std", "mean-sub"]

MBO_WINDOW_METHODS = {
    "mean": lambda X: np.mean(X, axis=0),
    "max": lambda X: np.max(X, axis=0),
    "std": lambda X: np.std(X, axis=0),
    "mean-sub": lambda X: X[0]
    - np.mean(X, axis=0),  # mostly for compatibility with gui window functions
}

ALL_PHASECORR_METHODS = set(TWO_DIM_PHASECORR_METHODS) | set(
    THREE_DIM_PHASECORR_METHODS
)

logger = log.get("phasecorr")


def _phase_corr_2d(frame, upsample=4, border=0, max_offset=4):
    if frame.ndim != 2:
        raise ValueError("Expected a 2D frame, got a 3D array.")

    h, w = frame.shape

    if isinstance(border, int):
        t = b = l = r = border
    else:
        t, b, l, r = border

    pre, post = frame[::2], frame[1::2]
    m = min(pre.shape[0], post.shape[0])

    row_start = t
    row_end = m - b if b else m
    col_start = l
    col_end = w - r if r else w

    a = pre[row_start:row_end, col_start:col_end]
    b_ = post[row_start:row_end, col_start:col_end]

    _shift, *_ = phase_cross_correlation(a, b_, upsample_factor=upsample)
    dx = float(_shift[1])
    if max_offset:
        return np.sign(dx) * min(abs(dx), max_offset)
    return dx


def _apply_offset(img, offset, subpixel=False):
    """
    Apply one scalar `shift` (in X) to every *odd* row of an
    (..., Y, X) array.  Works for 2-D or 3-D stacks.
    """
    if img.ndim < 2:
        return img

    rows = img[..., 1::2, :]

    if subpixel:
        f = np.fft.fftn(rows, axes=(-2, -1))
        shift_vec = (0,) * (f.ndim - 1) + (offset,)  # e.g. (0,0,dx) for 3-D
        rows[:] = np.fft.ifftn(fourier_shift(f, shift_vec), axes=(-2, -1)).real
    else:
        rows[:] = np.roll(rows, shift=int(round(offset)), axis=-1)
    return img


def nd_windowed(arr, *, method="mean", upsample=4, max_offset=4, border=0):
    """Return (corrected array, offsets)."""

    # 1. Get offsets
    if arr.ndim == 2:
        offs = _phase_corr_2d(arr, upsample, border, max_offset)
    else:
        flat = arr.reshape(arr.shape[0], *arr.shape[-2:])
        if method == "frame":
            offs = np.array(
                [_phase_corr_2d(f, upsample, border, max_offset) for f in flat]
            )
        else:
            if method not in MBO_WINDOW_METHODS:
                raise ValueError(f"unknown method {method}")
            img = MBO_WINDOW_METHODS[method](flat)
            offs = _phase_corr_2d(img, upsample, border, max_offset)

    # 2. Apply offsets
    if np.ndim(offs) == 0:  # scalar
        out = _apply_offset(arr.copy(), float(offs))
    else:
        out = np.stack(
            [
                _apply_offset(f.copy(), float(s))  # or _apply_offset
                for f, s in zip(arr, offs)
            ]
        )
    return out, offs


def apply_scan_phase_offsets(arr, offs):
    out = np.asarray(arr).copy()
    if np.isscalar(offs):
        return _apply_offset(out, offs)
    for k, off in enumerate(offs):
        out[k] = _apply_offset(out[k], off)
    return out


if __name__ == "__main__":
    from mbo_utilities import get_files, imread

    files = get_files(r"D:\tests\data", "tif")
    fpath = r"D:\W2_DATA\kbarber\2025_03_01\mk301\green"
    if not files:
        raise ValueError("No files found matching '*.tif'")

    import matplotlib.pyplot as plt
    # fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    array_object = imread(fpath)
    lazy_array = array_object
    lazy_array.fix_phase = False
    array = lazy_array[:2000, 8, :, :]
    fig, ax = plt.subplots()
    for num in [1, 3, 9]:
        _, ofs = nd_windowed(array, method="frame", upsample=num)
        ax.plot(ofs, label=f"upsample={num}")
    ax.axhline(0, color="k", ls="--")
    ax.set_xlabel("Frame")
    ax.set_ylabel("Offset (pixels)")
    ax.legend()
    plt.show()

    # fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    # for ax, m in zip(axs.flat, MBO_WINDOW_METHODS):
    #     corr, offs = nd_windowed(array, method=m, upsample=2)
    #     ax.imshow(corr.mean(0)[150:170, 330:350], cmap="gray")
    #     ax.set_title(f"{m}\nμ={np.mean(offs):.2f}")
    #     ax.axis("off")
    # plt.tight_layout()
    # plt.show()
