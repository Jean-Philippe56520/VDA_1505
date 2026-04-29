from .gothic_base import DARK_AGE_CSS as _BASE

DARK_AGE_CSS = _BASE.replace(
    "</style>",
    """
/* texture overlay (discret) */
[data-testid="stAppViewContainer"]::before{
  content:"";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(circle at 50% 12%, rgba(0,0,0,0.0) 0%, rgba(0,0,0,0.22) 55%, rgba(0,0,0,0.42) 100%),
    repeating-linear-gradient(45deg, rgba(255,255,255,0.015) 0, rgba(255,255,255,0.015) 1px, transparent 1px, transparent 14px),
    repeating-linear-gradient(-45deg, rgba(255,255,255,0.012) 0, rgba(255,255,255,0.012) 1px, transparent 1px, transparent 16px);
  mix-blend-mode: overlay;
}
</style>
"""
)
