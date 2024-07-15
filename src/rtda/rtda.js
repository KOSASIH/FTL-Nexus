import { DataFrame } from 'data-forge';
import * as Plotly from 'plotly.js-dist';

class RTDA {
    constructor(data) {
        this.data = data;
    }

    visualize_data() {
        // Visualize the data using Plotly
        const df = new DataFrame(this.data);
        const plot = df.plot({
            x: 'time',
            y: 'peed',
            type: 'line'
        });
        //...
    }

    analyze_data() {
        // Analyze the data using machine learning algorithms
        //...
    }
}

const data = [...]; // Load data from the spacecraft
const rtda = new RTDA(data);
rtda.visualize_data();
rtda.analyze_data();
