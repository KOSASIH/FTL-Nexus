import * as tf from 'tensorflow';

class Vision {
  constructor() {
    this.tf = tf;
  }

  async perceive(sensors) {
    // Use computer vision to perceive the environment
    const image = sensors.camera.getImage();
    const objects = this.tf.tidy(() => {
      const img = tf.tensor3d(image, [1, 224, 224, 3]);
      const model = this.tf.loadLayersModel('mobilenet_v2');
      const output = model.predict(img);
      return output;
    });
    return objects;
  }
}

export default Vision;
