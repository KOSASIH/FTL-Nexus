export default {
  navigation: {
    algorithm: 'astar',
    resolution: 0.1
  },
  control: {
    frequency: 100,
    amplitude: 10
  },
  sensors: {
    type: 'lidar',
    range: 100
  },
  actuators: {
    type: 'electric',
    power: 500
  }
};
