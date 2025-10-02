import numpy as np
import pandas as pd

from atomic_term_symbol_calculator.terms import calc_microstates, calc_term_symbols

class TestCalcMicrostates:
    """Test cases for calc_microstates function"""
    
    def test_basic_microstates(self):
        """Test basic microstate calculations"""
        assert calc_microstates(2, 1) == 2   # 1 electron in s shell
        assert calc_microstates(6, 2) == 15  # 2 electrons in p shell
        assert calc_microstates(10, 3) == 120 # 3 electrons in d shell
        
    def test_edge_cases(self):
        """Test edge cases for microstate calculations"""
        assert calc_microstates(2, 0) == 1   # 0 electrons
        assert calc_microstates(2, 2) == 1   # filled s shell
        assert calc_microstates(6, 6) == 1   # filled p shell
        assert calc_microstates(10, 10) == 1 # filled d shell
        
    def test_common_configurations(self):
        """Test microstates for common electron configurations"""
        # s orbital configurations
        assert calc_microstates(2, 1) == 2   # s1
        
        # p orbital configurations 
        assert calc_microstates(6, 1) == 6   # p1
        assert calc_microstates(6, 3) == 20  # p3
        assert calc_microstates(6, 5) == 6   # p5
        
        # d orbital configurations
        assert calc_microstates(10, 1) == 10  # d1
        assert calc_microstates(10, 2) == 45  # d2
        assert calc_microstates(10, 4) == 210 # d4
        assert calc_microstates(10, 5) == 252 # d5
        assert calc_microstates(10, 6) == 210 # d6
        assert calc_microstates(10, 8) == 45  # d8
        assert calc_microstates(10, 9) == 10  # d9

class TestCalcTermSymbols:
    """Test cases for calc_term_symbols function"""
    
    def test_simple_configurations(self):
        """Test term symbols for simple electron configurations"""
        # Hydrogen-like (1 electron)
        result = calc_term_symbols("1s1")
        assert "2S1/2" in result
        assert len(result) == 1
        
        # Helium (filled s shell)
        result = calc_term_symbols("1s2")
        assert result == ["1S0"]
        
    def test_p_orbital_configurations(self):
        """Test term symbols for p orbital configurations"""
        # p1 configuration (like B)
        result = calc_term_symbols("2p1")
        expected_terms = ["2P1/2", "2P3/2"]
        for term in expected_terms:
            assert term in result
            
        # p2 configuration (like C)
        result = calc_term_symbols("2p2")
        # Should include 3P, 1D, 1S terms
        assert any("3P" in term for term in result)
        assert any("1D" in term for term in result)
        assert any("1S" in term for term in result)
        
    def test_d_orbital_configurations(self):
        """Test term symbols for d orbital configurations"""
        # d1 configuration
        result = calc_term_symbols("3d1")
        expected_terms = ["2D3/2", "2D5/2"]
        for term in expected_terms:
            assert term in result
            
        # d2 configuration
        result = calc_term_symbols("3d2")
        # Should include multiple terms including 3F, 3P, 1G, 1D, 1S
        assert any("3F" in term for term in result)
        assert any("3P" in term for term in result)
        assert any("1G" in term for term in result)
        
    def test_mixed_orbital_configurations(self):
        """Test term symbols for mixed orbital configurations"""
        # s1p1 configuration
        result = calc_term_symbols("2s1.2p1")
        # Should have both singlet and triplet states
        assert any("1P" in term for term in result)
        assert any("3P" in term for term in result)
        
    def test_filled_shell_configurations(self):
        """Test that filled shells return 1S0"""
        # Various filled shell configurations
        result = calc_term_symbols("1s2.2s2.2p6")
        assert result == ["1S0"]
        
        result = calc_term_symbols("3d10")
        assert result == ["1S0"]
        
    def test_input_format_variations(self):
        """Test different input format variations"""
        # Space separated
        result1 = calc_term_symbols("2s1 2p1")
        # Dot separated
        result2 = calc_term_symbols("2s1.2p1")
        # Should give same results
        assert set(result1) == set(result2)
        
    def test_configuration_with_implicit_occupancy(self):
        """Test configurations where occupancy is implicit (defaults to 1)"""
        result1 = calc_term_symbols("2p1")
        result2 = calc_term_symbols("2p")
        assert set(result1) == set(result2)
        
    def test_ground_state_configurations(self):
        """Test known ground state configurations"""
        # Carbon ground state (2p2)
        result = calc_term_symbols("2p2")
        assert "3P0" in result  # Ground state term
        
        # Nitrogen ground state (2p3)
        result = calc_term_symbols("2p3")
        assert "4S3/2" in result  # Ground state term
        
        # Oxygen ground state (2p4)
        result = calc_term_symbols("2p4")
        assert "3P2" in result  # Ground state term
        
    def test_return_type_and_format(self):
        """Test that function returns proper format"""
        result = calc_term_symbols("2p1")
        assert isinstance(result, list)
        assert all(isinstance(term, str) for term in result)
        # Check that terms follow proper format (multiplicity + letter + J)
        import re
        pattern = r'^\d+[SPDFGHIKLMNOQRTUVWXYZ]\d+(/\d+)?$'
        for term in result:
            assert re.match(pattern, term), f"Term {term} doesn't match expected format"

class TestEdgeCasesAndValidation:
    """Test edge cases and input validation"""
    
    def test_large_configurations(self):
        """Test with larger, more complex configurations"""
        # Test f orbital configuration
        result = calc_term_symbols("4f1")
        assert len(result) == 2  # Should have 2F5/2 and 2F7/2
        assert "2F5/2" in result
        assert "2F7/2" in result
        
    def test_multiple_shells(self):
        """Test configurations with multiple partially filled shells"""
        # Configuration with multiple partially filled shells
        result = calc_term_symbols("2s1.2p1.3s1")
        assert isinstance(result, list)
        assert len(result) > 0
        
    def test_consistency_check(self):
        """Test that results are consistent and reasonable"""
        # Test that number of terms makes sense
        result = calc_term_symbols("2p3")
        # p3 should have multiple terms but not too many
        assert 1 < len(result) < 20
        
        # Check that all terms are unique
        assert len(result) == len(set(result))
        
    def test_term_symbol_properties(self):
        """Test properties of returned term symbols"""
        result = calc_term_symbols("3d2")
        
        # Check that we have multiple spin states
        multiplicities = []
        for term in result:
            multiplicity = int(term[0])
            multiplicities.append(multiplicity)
            
        # d2 should include both triplet and singlet states
        assert 3 in multiplicities  # Triplet states
        assert 1 in multiplicities  # Singlet states
        
    def test_known_term_counts(self):
        """Test against known term symbol counts for specific configurations"""
        # d2 configuration has a known number of terms
        result = calc_term_symbols("3d2")
        # d2 should have multiple terms but manageable number
        assert len(result) > 5
        assert len(result) < 20
        
        # p3 configuration
        result = calc_term_symbols("2p3")
        # p3 should have 4S, 2D, 2P terms with J splittings
        term_letters = [term[1] for term in result]
        assert 'S' in term_letters
        assert 'D' in term_letters
        assert 'P' in term_letters