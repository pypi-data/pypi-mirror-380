"""
Tests for the configuration system.
"""

import os
import tempfile
import pytest
import yaml

from amt_augmentor.config import (
    Config,
    TimeStretchConfig,
    PitchShiftConfig,
    ReverbFilterConfig,
    GainChorusConfig,
    load_config,
    save_default_config
)


def test_default_config():
    """Test that the default config has expected values."""
    config = Config()
    
    # Check time stretch defaults
    assert config.time_stretch.enabled is True
    assert config.time_stretch.variations == 3
    assert config.time_stretch.min_factor == 0.6
    assert config.time_stretch.max_factor == 1.6
    
    # Check pitch shift defaults
    assert config.pitch_shift.enabled is True
    assert config.pitch_shift.variations == 3
    assert config.pitch_shift.min_semitones == -5
    assert config.pitch_shift.max_semitones == 5
    
    # Check reverb defaults
    assert config.reverb_filter.enabled is True
    assert config.reverb_filter.variations == 3
    assert config.reverb_filter.min_room_scale == 10
    assert config.reverb_filter.max_room_scale == 100
    assert len(config.reverb_filter.cutoff_pairs) == 6  # Should have 6 default pairs
    
    # Check processing defaults
    assert config.processing.num_workers == 4
    assert config.processing.cache_dir is None
    assert config.processing.output_dir is None


def test_save_load_config():
    """Test saving and loading configuration."""
    # Create temporary file and close it immediately to avoid Windows locking
    tmp_fd, tmp_path = tempfile.mkstemp(suffix='.yaml')
    os.close(tmp_fd)  # Close file descriptor immediately

    try:
        # Save default config
        save_default_config(tmp_path)

        # Check file exists and has content
        assert os.path.exists(tmp_path)
        with open(tmp_path, 'r') as f:
            content = f.read()
            assert len(content) > 0

        # Load the config
        config = load_config(tmp_path)

        # Verify some values
        assert config.time_stretch.variations == 3
        assert config.pitch_shift.min_semitones == -5
        assert config.reverb_filter.min_room_scale == 10
        assert config.processing.num_workers == 4

    finally:
        # Clean up - use try/except for Windows
        try:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
        except (PermissionError, OSError):
            pass  # Windows may still have file locked


def test_config_modification():
    """Test modifying configuration values."""
    # Create a config with custom values
    config = Config()
    
    # Modify time stretch config
    config.time_stretch.enabled = False
    config.time_stretch.variations = 5
    config.time_stretch.min_factor = 0.8
    config.time_stretch.max_factor = 1.2
    
    # Verify changes
    assert config.time_stretch.enabled is False
    assert config.time_stretch.variations == 5
    assert config.time_stretch.min_factor == 0.8
    assert config.time_stretch.max_factor == 1.2
    
    # Other configs should remain at defaults
    assert config.pitch_shift.enabled is True
    assert config.reverb_filter.enabled is True


def test_load_partial_config():
    """Test loading a configuration with only some values specified."""
    # Create temporary file and close it immediately to avoid Windows locking
    tmp_fd, tmp_path = tempfile.mkstemp(suffix='.yaml')
    os.close(tmp_fd)  # Close file descriptor immediately

    try:
        # Create a partial config
        partial_config = {
            'time_stretch': {
                'enabled': False,
                'variations': 2
            },
            'processing': {
                'num_workers': 8
            }
        }

        # Write to file
        with open(tmp_path, 'w') as f:
            yaml.dump(partial_config, f)

        # Load the config
        config = load_config(tmp_path)

        # Check modified values
        assert config.time_stretch.enabled is False
        assert config.time_stretch.variations == 2
        assert config.processing.num_workers == 8

        # Check unmodified values (should be defaults)
        assert config.time_stretch.min_factor == 0.6  # Default
        assert config.pitch_shift.enabled is True  # Default
        assert config.pitch_shift.variations == 3  # Default

    finally:
        # Clean up - use try/except for Windows
        try:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
        except (PermissionError, OSError):
            pass  # Windows may still have file locked


def test_load_nonexistent_config():
    """Test loading a non-existent configuration file returns defaults."""
    # Use a filename that definitely doesn't exist
    nonexistent_path = os.path.join(tempfile.gettempdir(), 'definitely_not_a_real_config_file_12345.yaml')

    # Make sure it really doesn't exist
    if os.path.exists(nonexistent_path):
        try:
            os.unlink(nonexistent_path)
        except (PermissionError, OSError):
            pass  # Windows may have issues

    # Load the config
    config = load_config(nonexistent_path)

    # Should get default values
    assert config.time_stretch.enabled is True
    assert config.time_stretch.variations == 3
    assert config.pitch_shift.min_semitones == -5
    assert config.processing.num_workers == 4