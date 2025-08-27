#!/usr/bin/env python3
"""
Simple Quantum Cryptography Example using liboqs
Basic demonstration of post-quantum cryptography operations
"""

import oqs
import time

def simple_kem_example():
    """Simple Key Encapsulation Mechanism example"""
    print("=== Simple KEM Example ===")
    
    # Use ML-KEM-512 (Kyber variant)
    kem_alg = "ML-KEM-512"
    
    try:
        # Create client and server instances
        with oqs.KeyEncapsulation(kem_alg) as client:
            with oqs.KeyEncapsulation(kem_alg) as server:
                print(f"Using algorithm: {kem_alg}")
                
                # Client generates keypair
                print("1. Client generating keypair...")
                public_key = client.generate_keypair()
                print(f"   Public key size: {len(public_key)} bytes")
                
                # Server encapsulates secret using client's public key
                print("2. Server encapsulating secret...")
                ciphertext, shared_secret_server = server.encap_secret(public_key)
                print(f"   Ciphertext size: {len(ciphertext)} bytes")
                print(f"   Shared secret size: {len(shared_secret_server)} bytes")
                
                # Client decapsulates to get shared secret
                print("3. Client decapsulating secret...")
                shared_secret_client = client.decap_secret(ciphertext)
                
                # Verify both secrets match
                if shared_secret_client == shared_secret_server:
                    print("✓ SUCCESS: Shared secrets match!")
                    print(f"   Secret: {shared_secret_client[:16].hex()}...")
                else:
                    print("✗ FAILED: Shared secrets don't match!")
                    
    except Exception as e:
        print(f"Error: {e}")

def simple_signature_example():
    """Simple Digital Signature example"""
    print("\n=== Simple Signature Example ===")
    
    # Use ML-DSA-44 (Dilithium variant)
    sig_alg = "ML-DSA-44"
    message = b"Hello, Quantum World!"
    
    try:
        with oqs.Signature(sig_alg) as signer:
            with oqs.Signature(sig_alg) as verifier:
                print(f"Using algorithm: {sig_alg}")
                print(f"Message: {message.decode()}")
                
                # Generate keypair
                print("1. Generating keypair...")
                public_key = signer.generate_keypair()
                print(f"   Public key size: {len(public_key)} bytes")
                
                # Sign message
                print("2. Signing message...")
                signature = signer.sign(message)
                print(f"   Signature size: {len(signature)} bytes")
                
                # Verify signature
                print("3. Verifying signature...")
                is_valid = verifier.verify(message, signature, public_key)
                
                if is_valid:
                    print("✓ SUCCESS: Signature is valid!")
                else:
                    print("✗ FAILED: Signature verification failed!")
                    
    except Exception as e:
        print(f"Error: {e}")

def benchmark_algorithms():
    """Benchmark different algorithms"""
    print("\n=== Algorithm Benchmark ===")
    
    # Test different KEM algorithms
    kem_algorithms = ["ML-KEM-512", "ML-KEM-768", "ML-KEM-1024"]
    
    for alg in kem_algorithms:
        try:
            start_time = time.time()
            
            with oqs.KeyEncapsulation(alg) as client:
                with oqs.KeyEncapsulation(alg) as server:
                    public_key = client.generate_keypair()
                    ciphertext, shared_secret_server = server.encap_secret(public_key)
                    shared_secret_client = client.decap_secret(ciphertext)
                    
                    execution_time = time.time() - start_time
                    
                    if shared_secret_client == shared_secret_server:
                        print(f"{alg}: ✓ {execution_time:.4f}s (key: {len(public_key)}B)")
                    else:
                        print(f"{alg}: ✗ FAILED")
                        
        except Exception as e:
            print(f"{alg}: ✗ ERROR - {e}")

def show_available_algorithms():
    """Show available algorithms"""
    print("=== Available Algorithms ===")
    
    try:
        kem_mechanisms = oqs.get_enabled_kem_mechanisms()
        sig_mechanisms = oqs.get_enabled_sig_mechanisms()
        
        print(f"KEM Mechanisms ({len(kem_mechanisms)}):")
        for i, alg in enumerate(list(kem_mechanisms.keys())[:10]):
            print(f"  {i+1:2d}. {alg}")
        if len(kem_mechanisms) > 10:
            print(f"      ... and {len(kem_mechanisms) - 10} more")
            
        print(f"\nSignature Mechanisms ({len(sig_mechanisms)}):")
        for i, alg in enumerate(list(sig_mechanisms.keys())[:10]):
            print(f"  {i+1:2d}. {alg}")
        if len(sig_mechanisms) > 10:
            print(f"      ... and {len(sig_mechanisms) - 10} more")
            
    except Exception as e:
        print(f"Error getting algorithms: {e}")

def main():
    """Main function"""
    print("Quantum Cryptography with liboqs - Simple Examples")
    print("=" * 50)
    
    # Show liboqs version
    try:
        print(f"liboqs version: {oqs.oqs_version()}")
        print(f"liboqs-python version: {oqs.oqs_python_version()}")
    except Exception as e:
        print(f"Error getting version: {e}")
    
    # Run examples
    show_available_algorithms()
    simple_kem_example()
    simple_signature_example()
    benchmark_algorithms()
    
    print("\n" + "=" * 50)
    print("Examples completed!")

if __name__ == "__main__":
    main()
