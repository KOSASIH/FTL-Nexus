export function randomize(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

export function normalize(arr) {
  return arr.map(x => x / Math.max(...arr));
}
