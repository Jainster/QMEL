import qiskit as qs

circuit = qs.QuantumCircuit(2,2)  # 2 qubits, 2 classical bits 

# currently: 0,0
circuit.x(0)
# 1, 0
circuit.cx() #cnot, controlled not. Flips 2nd qubit value IF first qubit is a 1
# 1, 1
circuit.measure([0,1], [0,1]) # ([qbitregister], [classicalbitregister]) Measure qubit 0 and 1 to classical bits 0 and 1
circuit.draw()