# Quantum Cryptography with liboqs

This directory contains examples and simulations of post-quantum cryptography (PQC) using the liboqs library.

## What is Post-Quantum Cryptography?

Post-quantum cryptography refers to cryptographic algorithms that are believed to be secure against attacks by both classical and quantum computers. Traditional cryptographic algorithms like RSA and ECC may become vulnerable when large-scale quantum computers become available.

## Files Overview

### 1. `quantum-cryptography.py` - Comprehensive Simulation
A full-featured quantum cryptography simulator that includes:
- **Key Encapsulation Mechanisms (KEM)**: ML-KEM (Kyber variants)
- **Digital Signatures**: ML-DSA (Dilithium variants)
- **Performance benchmarking** across different algorithms
- **Quantum attack simulation** demonstrating why PQC is needed
- **Comprehensive analysis** of security levels and key sizes

### 2. `simple_quantum_example.py` - Basic Examples
A simpler version showing basic operations:
- Basic KEM key exchange
- Digital signature creation and verification
- Algorithm benchmarking
- Available algorithm listing

### 3. `requirements.txt` - Dependencies
Required Python packages for running the examples.

## Installation

1. **Install liboqs-python**:
   ```bash
   pip install liboqs-python
   ```

2. **Install additional dependencies** (optional):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Simple Example
```bash
python simple_quantum_example.py
```

### Run the Comprehensive Simulation
```bash
python quantum-cryptography.py
```

## Key Algorithms Demonstrated

### Key Encapsulation Mechanisms (KEM)
- **ML-KEM-512**: 128-bit security level
- **ML-KEM-768**: 192-bit security level  
- **ML-KEM-1024**: 256-bit security level

### Digital Signatures
- **ML-DSA-44**: 128-bit security level
- **ML-DSA-65**: 192-bit security level
- **ML-DSA-87**: 256-bit security level

## What You'll Learn

1. **How KEM works**: Key exchange without direct key transmission
2. **Digital signatures**: Creating and verifying quantum-resistant signatures
3. **Performance characteristics**: Speed and key size comparisons
4. **Security levels**: Understanding different security classifications
5. **Quantum threats**: Why traditional cryptography may become vulnerable

## Key Concepts

### Key Encapsulation Mechanism (KEM)
```
Client                    Server
  |                        |
  |-- public_key --------> |
  |                        |
  |<-- ciphertext -------- |
  |                        |
  |-- decapsulate -------> |
  |                        |
Both now have the same shared secret!
```

### Digital Signatures
```
Signer                    Verifier
  |                        |
  |-- public_key --------> |
  |                        |
  |-- message + sig -----> |
  |                        |
  |<-- verification -----> |
```

## Security Considerations

- **Hybrid schemes**: Consider combining classical and post-quantum algorithms
- **Key sizes**: Post-quantum algorithms typically have larger key sizes
- **Performance**: Some PQC algorithms may be slower than classical alternatives
- **Standardization**: NIST is currently finalizing PQC standards

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure liboqs-python is installed
   ```bash
   pip install liboqs-python
   ```

2. **Algorithm Not Available**: Some algorithms may not be available in your liboqs build
   - Check available algorithms with the examples
   - Use alternative algorithms if needed

3. **Performance Issues**: 
   - Some algorithms are computationally intensive
   - Consider using smaller security levels for testing

## Further Reading

- [liboqs Documentation](https://github.com/open-quantum-safe/liboqs)
- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [ML-KEM (Kyber) Specification](https://pq-crystals.org/kyber/)
- [ML-DSA (Dilithium) Specification](https://pq-crystals.org/dilithium/)

## License

This code is provided for educational purposes. Please refer to the liboqs license for the underlying cryptographic library.
