<div align="center">
  <img src="https://raw.githubusercontent.com/LarsMonstad/amt-augmentor/refs/heads/main/images/BotsForMusic_Logo_Black_2.png" alt="Bots for Music Logo" width="300">

  # AMT-Augmentor

  ## Python Data Augmentation Toolkit for Automatic Music Transcription (AMT)

  **Developed by [Bots for Music](https://botsformusic.com), maintained by Lars Monstad**

  [![PyPI version](https://badge.fury.io/py/amt-augmentor.svg)](https://badge.fury.io/py/amt-augmentor)
  [![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![CI](https://github.com/LarsMonstad/amt-augmentor/actions/workflows/ci.yml/badge.svg)](https://github.com/LarsMonstad/amt-augmentor/actions/workflows/ci.yml)
  [![Downloads](https://pepy.tech/badge/amt-augmentor)](https://pepy.tech/project/amt-augmentor)
</div>

> **📦 [View on PyPI](https://pypi.org/project/amt-augmentor/)** 
>
> **Note:** Formerly known as `amt-augpy`. Starting with v1.0.9, the package is **`amt-augmentor`**.

A Python toolkit for augmenting Automatic Music Transcription (AMT) datasets through various audio transformations while maintaining synchronization between audio and MIDI files. The dataset follows the same format as [MAESTRO v3.0.0](https://magenta.tensorflow.org/datasets/maestro), which is commonly used for Automatic Music Transcription (AMT) tasks. 

The toolkit expects a folder containing paired audio and MIDI files with matching names. The audio file and MIDI file must be ground truth data, as this toolkit is only for augmenting existing datasets - a common technique in Machine Learning.

```
dataset/
├── song1.wav        # Audio file
├── song1.mid        # Ground truth annotated midi file
```

## Features

### Audio Transformations
- **Time Stretching**: Tempo modification while maintaining pitch
- **Pitch Shifting**: Transposition while preserving timing
- **Reverb & Filtering**: Room acoustics and frequency filtering effects
- **Gain & Chorus**: Depth and richness enhancement
- **Noise Augmentation**: Controlled noise addition for robustness training
- **Pause Manipulation**: Detection and modification of musical pauses
- **Audio Merging**: Combine multiple audio files into one for complex training scenarios

### Processing & Dataset Handling
- **Audio Standardization**: Conversion to 44.1kHz WAV format
- **Parallel Processing**: Multi-core processing for faster augmentation
- **Configuration System**: YAML-based parameter customization
- **Dataset Validation**: Automatic validation of train/test/validation splits
- **Dataset Modification**: Built-in tools to modify existing dataset splits
- **MAESTRO Compatibility**: Dataset format compatible with MAESTRO v3.0.0

## Why AMT-Augmentor?

Built for AMT, not just audio. Unlike general audio augmenters, AMT-Augmentor keeps paired audio+MIDI aligned by applying transform-consistent updates to MIDI (transpose for pitch shift, time-scale for stretch) and ships MAESTRO-style dataset tools (CSV builder + split validation) to avoid leakage. It also supports semitone/time-aware transforms and reproducible runs via --seed.

## Requirements

- Python 3.9, 3.10, 3.11, 3.12, or 3.13
- System dependencies: `libsndfile` and `ffmpeg` (for audio processing)

## Installation

You can install AMT-Augmentor either via pip or by cloning the repository:

### Using pip

```bash
pip install amt-augmentor
```

### From source

```bash
git clone https://github.com/LarsMonstad/amt-augmentor.git
cd amt-augmentor
pip install -e .
```


## Usage

### Basic Usage

```bash
amt-augmentor /path/to/dataset/directory
# Or running directly
python -m amt_augmentor.main /path/to/dataset/directory
```



This will process all compatible audio files in the directory and their corresponding MIDI files. The script automatically selects random parameters within predefined ranges for each augmentation type.

### Advanced Usage

```bash
# Use a custom configuration file
amt-augmentor /path/to/dataset/directory --config my_config.yaml

# Set random seed for reproducible augmentation
amt-augmentor /path/to/dataset/directory --seed 42

# Specify an output directory
amt-augmentor /path/to/dataset/directory --output-directory /path/to/output

# Generate a default configuration file
amt-augmentor --generate-config my_config.yaml

# Disable specific effects
amt-augmentor /path/to/dataset/directory --disable-effect timestretch --disable-effect chorus

# Control merge behavior (default merges 1 random file with each file)
amt-augmentor /path/to/dataset/directory --merge-num 2  # Merge 2 files with each file

# Modify existing dataset CSV files
amt-augmentor --modify-csv dataset.csv --list-split all  # List all songs
amt-augmentor --modify-csv dataset.csv --move-to-split test --song-patterns "Mozart"  # Move songs
amt-augmentor --modify-csv dataset.csv --remove-songs --song-patterns "BadRecording"  # Remove songs

# Parallel processing with 8 workers
amt-augmentor /path/to/dataset/directory --num-workers 8

# Custom train/test/validation split
amt-augmentor /path/to/dataset/directory --train-ratio 0.8 --test-ratio 0.1 --validation-ratio 0.1

# Force specific songs to test set (prevents augmentation)
amt-augmentor /path/to/dataset/directory --custom-test-songs "song1,song3,song5"

# Dry run to preview what will be processed
amt-augmentor /path/to/dataset/directory --dry-run

# Verbose output for debugging
amt-augmentor /path/to/dataset/directory --verbose

# Check for valid MIDI-WAV pairs before processing
amt-augmentor /path/to/dataset/directory --check-pairs

# List available effects
amt-augmentor --list-effects

# Check version
amt-augmentor --version
```

### Help and options

```bash
amt-augmentor --help
```

## Configuration

All augmentation parameters can be customized using a YAML configuration file. See `config.sample.yaml` for a complete example with documentation.


## File Format Support

### Audio
- Input: WAV, FLAC, MP3, M4A, AIFF 
- Output: WAV (44.1kHz)

### Annotations
- MIDI (.mid)

## Output Structure

For each input file pair (audio + MIDI), the toolkit generates multiple augmented versions with the following naming convention:

    original_name_augmented_effect_parameter_randomsuffix.extension

The `_augmented_` identifier ensures all augmented files are properly recognized and handled during dataset creation.

Example:

    piano_augmented_timestretch_1.2_abc123.wav
    piano_augmented_timestretch_1.2_abc123.mid
    piano_augmented_noise_1.5_def456.wav
    piano_augmented_noise_1.5_def456.mid
    piano_augmented_merge_piano2_ghi789.wav
    piano_augmented_merge_piano2_ghi789.mid

## Dataset Creation & Validation

The dataset follows the same format as [MAESTRO v3.0.0](https://magenta.tensorflow.org/datasets/maestro). Songs assigned to test or validation splits will have their augmented versions excluded to prevent data leakage.

### Creating the Dataset CSV

```bash
# Create dataset with default split ratios (70% train, 15% test, 15% validation)
amt-augmentor /path/to/directory

# Create dataset with custom split ratios
amt-augmentor /path/to/directory --train-ratio 0.8 --test-ratio 0.1 --validation-ratio 0.1

# Force specific songs to test set (they won't be augmented)
amt-augmentor /path/to/directory --custom-test-songs "song1,song3,song5"
```

### Validating the Dataset Split

Dataset split validation is automatically performed after CSV creation to ensure:
- Augmented songs are not included in test/validation splits
- No cross-split contamination occurs
- Original and augmented songs are properly distributed

### CSV Format

The generated CSV follows the MAESTRO format with the following columns:
- canonical_composer
- canonical_title
- split
- year
- midi_filename
- audio_filename
- duration

### Modifying Existing Datasets

After creating a dataset CSV, you can easily modify it to adjust train/test/validation splits:

```bash
# List all songs and their distribution
amt-augmentor --modify-csv dataset.csv --list-split all

# List only test songs
amt-augmentor --modify-csv dataset.csv --list-split test

# List all songs with detailed view
amt-augmentor --modify-csv dataset.csv --list-split all --verbose

# Move songs to a different split (substring matching)
amt-augmentor --modify-csv dataset.csv --move-to-split test --song-patterns "Mozart,Chopin"

# Remove songs from dataset
amt-augmentor --modify-csv dataset.csv --remove-songs --song-patterns "BadRecording1,BadRecording2"

# Create backup before modifications (off by default)
amt-augmentor --modify-csv dataset.csv --move-to-split validation --song-patterns "Bach" --backup
```

**Features:**
- **Substring matching**: Patterns like "Mozart" match any song containing that substring
- **Smart augmented handling**: Augmented versions automatically stay in train split only
- **Backup option**: Use `--backup` to create a backup before modifications

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

For development:
1. Install development dependencies: `pip install -e ".[dev]"`
2. Run tests: `pytest tests/`
3. Check typing: `mypy amt_augmentor`
4. Format code: `black amt_augmentor`

## Contributors

- **Lars Monstad (@LarsMonstad)** – Original author and maintainer
- **@monoamine11231** – Noise augmentation, custom test songs feature, and various improvements

## Contact

For questions or collaboration:
- Email: lars@botsformusic.com
- Organization: https://botsformusic.com
- GitHub: https://github.com/LarsMonstad/amt-augmentor

## License

MIT License - see LICENSE file for details.

## Citation

If you use this toolkit in your research, please cite:

```bibtex
@software{amt_augmentor,
  author       = {Lars Monstad and contributors},
  title        = {AMT-Augmentor: Audio + MIDI augmentation toolkit for AMT datasets},
  version      = {1.1.2},
  year         = {2025},
  publisher    = {Bots for Music},
  url          = {https://github.com/LarsMonstad/amt-augmentor}
}
```
