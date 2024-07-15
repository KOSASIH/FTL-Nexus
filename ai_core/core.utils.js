export function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

export function normalize(value, min, max) {
  return (value - min) / (max - min);
}
