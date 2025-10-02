import numpy as np
import pandas as pd

from term_symbols.terms import calc_microstates, calc_term_symbols

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

class TestComplexConfigurations:
    """Test cases for complex electron configurations that previously failed"""
    
    def test_d5_configuration(self):
        """Test d5 configuration that previously caused KeyError -6"""
        result = calc_term_symbols("3d5")
        
        # d5 should have many terms including high-spin sextet
        assert len(result) > 20
        
        # Check for expected high-spin ground state
        multiplicities = [int(term[0]) for term in result]
        assert 6 in multiplicities  # Sextet state (2S+1 = 6, so S = 5/2)
        
        # Check for ground state term 6S5/2
        assert "6S5/2" in result
        
        # Check for other expected terms
        term_letters = [term[1] for term in result]
        expected_letters = ['S', 'P', 'D', 'F', 'G', 'H', 'I']
        for letter in expected_letters:
            assert letter in term_letters, f"Expected term symbol with {letter} not found"
    
    def test_d6_configuration(self):
        """Test d6 configuration"""
        result = calc_term_symbols("3d6")
        assert len(result) > 10
        assert isinstance(result, list)
        
        # d6 should have quintet states
        multiplicities = [int(term[0]) for term in result]
        assert 5 in multiplicities
    
    def test_d9_configuration(self):
        """Test d9 configuration"""
        result = calc_term_symbols("3d9")
        assert len(result) == 2  # d9 has same terms as d1 (electron-hole duality)
        assert "2D3/2" in result
        assert "2D5/2" in result

class TestFOrbitalConfigurations:
    """Test cases for f orbital electron configurations"""
    
    def test_f1_configuration(self):
        """Test f1 configuration"""
        result = calc_term_symbols("4f1")
        assert len(result) == 2
        assert "2F5/2" in result
        assert "2F7/2" in result
        
        # All should be doublets
        multiplicities = [int(term[0]) for term in result]
        assert all(mult == 2 for mult in multiplicities)
    
    def test_f2_configuration(self):
        """Test f2 configuration"""
        result = calc_term_symbols("4f2")
        
        # f2 should have multiple terms
        assert len(result) > 5
        
        # Should include both singlet and triplet states
        multiplicities = [int(term[0]) for term in result]
        assert 1 in multiplicities  # Singlet
        assert 3 in multiplicities  # Triplet
        
        # Check for expected term symbols
        term_letters = [term[1] for term in result]
        for letter in ['S', 'F', 'H']:  # At minimum these should be present
            assert letter in term_letters
    
    def test_f3_configuration(self):
        """Test f3 configuration"""
        result = calc_term_symbols("4f3")
        
        # f3 should have many terms
        assert len(result) > 10
        
        # Should have quartet ground state
        multiplicities = [int(term[0]) for term in result]
        assert 4 in multiplicities  # Quartet (2S+1 = 4, so S = 3/2)
        
        # Should have various L values
        term_letters = [term[1] for term in result]
        high_L_letters = ['I', 'H', 'G', 'F']
        assert any(letter in term_letters for letter in high_L_letters)
    
    def test_f7_configuration(self):
        """Test f7 configuration (half-filled f shell)"""
        result = calc_term_symbols("4f7")
        
        # f7 (half-filled) should have high-spin ground state
        multiplicities = [int(term[0]) for term in result]
        assert 8 in multiplicities  # Octet (2S+1 = 8, so S = 7/2)
        
        # Should have many terms due to complexity
        assert len(result) > 50
        
        # Ground state should be 8S7/2
        assert "8S7/2" in result

class TestLargeMagneticRangeConfigurations:
    """Test configurations that require large ML ranges"""
    
    def test_multiple_d_orbitals(self):
        """Test configurations with multiple d orbital occupancies"""
        # These test the ML range fix
        configs_to_test = [
            ("3d4", 10),   # Should have multiple terms
            ("3d5", 20),   # Fixed KeyError -6 issue  
            ("3d6", 10),   # Should work with large ML range
            ("3d7", 10),   # Should work
            ("3d8", 5),    # Fewer terms (getting closer to filled)
        ]
        
        for config, min_terms in configs_to_test:
            result = calc_term_symbols(config)
            assert len(result) >= min_terms, f"{config} should have at least {min_terms} terms, got {len(result)}"
            assert all(isinstance(term, str) for term in result)
    
    def test_mixed_high_l_orbitals(self):
        """Test mixed configurations with high angular momentum"""
        # Test configurations that create large ML ranges
        test_configs = [
            "3d1.4f1",     # d + f combination
            "4f2.5d1",     # f + d combination  
        ]
        
        for config in test_configs:
            result = calc_term_symbols(config)
            assert len(result) > 0
            assert isinstance(result, list)
            
            # Verify format
            import re
            pattern = r'^\d+[SPDFGHIKLMNOQRTUVWXYZ]\d+(/\d+)?$'
            for term in result:
                assert re.match(pattern, term), f"Term {term} doesn't match expected format"
    
    def test_ml_range_calculation_correctness(self):
        """Test that ML range calculation handles all orbital types correctly"""
        from term_symbols.terms import calc_term_symbols
        
        # These configurations should not cause IndexErrors
        problematic_configs = [
            "4f5",     # Large f configuration
            "5f3",     # Different shell f orbital
            "6d5",     # Different shell d orbital
        ]
        
        for config in problematic_configs:
            try:
                result = calc_term_symbols(config)
                assert len(result) > 0, f"Configuration {config} should return some terms"
            except (KeyError, IndexError) as e:
                assert False, f"Configuration {config} caused ML range error: {e}"

class TestElectronHoleDuality:
    """Test electron-hole duality relationships"""
    
    def test_d1_d9_duality(self):
        """Test that d1 and d9 have the same terms"""
        d1_terms = set(calc_term_symbols("3d1"))
        d9_terms = set(calc_term_symbols("3d9"))
        assert d1_terms == d9_terms
    
    def test_d2_d8_duality(self):
        """Test that d2 and d8 have similar term structures"""
        d2_terms = calc_term_symbols("3d2")
        d8_terms = calc_term_symbols("3d8")
        
        # Should have same number of terms
        assert len(d2_terms) == len(d8_terms)
        
        # Should have same term letters (though J values may differ)
        d2_letters = sorted([term[1] for term in d2_terms])
        d8_letters = sorted([term[1] for term in d8_terms])
        assert d2_letters == d8_letters
    
    def test_f1_f13_duality(self):
        """Test that f1 and f13 have the same terms"""
        f1_terms = set(calc_term_symbols("4f1"))
        f13_terms = set(calc_term_symbols("4f13"))
        assert f1_terms == f13_terms