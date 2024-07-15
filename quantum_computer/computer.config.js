export default {
  quantum_processor: {
    architecture: 'superconducting_qubit',
    num_qubits: 100
  },
  quantum_memory: {
    type: 'quantum_RAM',
    capacity: 10000
  },
  quantum_algorithm: {
    type: 'shor_algorithm',
    complexity: 'exponential'
  },
  quantum_interface: {
    type: 'quantum_gate_array',
    num_gates: 1000
  }
};
