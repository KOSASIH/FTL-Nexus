import { Navigation } from './pilot.modules/navigation';
import { Control } from './pilot.modules/control';
import { Sensors } from './pilot.modules/sensors';
import { Actuators } from './pilot.modules/actuators';
import { Core } from './pilot.modules/core';

class Pilot {
  constructor() {
    this.navigation = new Navigation();
    this.control = new Control();
    this.sensors = new Sensors();
    this.actuators = new Actuators();
    this.core = new Core();
  }

  async init() {
    // Initialize the pilot system
    await this.navigation.init();
    await this.control.init();
    await this.sensors.init();
    await this.actuators.init();
    await this.core.init();
  }

  async run() {
    // Run the pilot system
    while (true) {
      const sensorData = await this.sensors.read();
      const controlSignal = await this.control.calculate(sensorData);
      await this.actuators.write(controlSignal);
      await this.core.update();
    }
  }
}

export default Pilot;
