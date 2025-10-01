"""ECG data loading and processing utilities."""

import os
from typing import Union, List, Tuple, Optional

import numpy as np
import h5py
import scipy.io as sio

try:
    import mat73
except ImportError:
    mat73 = None

try:
    import wfdb
except ImportError:
    wfdb = None

try:
    from scipy import interpolate
except ImportError:
    interpolate = None


class ECGDataLoader:
    """Loader for various ECG file formats."""
    
    @staticmethod
    def load_ecg_file(file_path: str) -> np.ndarray:
        """
        Load ECG data from various file formats.
        
        Args:
            file_path: Path to ECG file
            
        Returns:
            ECG data as numpy array of shape (channels, samples)
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"ECG file not found: {file_path}")
            
        # Determine file format
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext in ['.mat', '.matlab']:
            return ECGDataLoader._load_matlab(file_path)
        elif ext in ['.h5', '.hdf5', '.h5py']:
            return ECGDataLoader._load_hdf5(file_path)
        elif ext in ['.npy', '.npz']:
            return ECGDataLoader._load_numpy(file_path)
        elif ext in ['.csv', '.txt']:
            return ECGDataLoader._load_text(file_path)
        else:
            # Load with wfdb
            return ECGDataLoader._load_wfdb(file_path)
                
    @staticmethod
    def _load_matlab(file_path: str) -> np.ndarray:
        """Load MATLAB .mat file."""
        try:
            # Try loading with scipy (for MATLAB v7.3+ files)
            data = sio.loadmat(file_path)
            
            # Common keys for ECG data
            ecg_keys = ['ecg', 'ECG', 'data', 'signal', 'val', 'value']
            
            for key in ecg_keys:
                if key in data:
                    ecg_data = np.array(data[key])
                    # Ensure shape is (channels, samples)
                    if ecg_data.ndim == 1:
                        ecg_data = ecg_data.reshape(1, -1)
                    elif ecg_data.shape[0] > ecg_data.shape[1]:
                        ecg_data = ecg_data.T
                    return ecg_data
                    
            # If no standard key found, try the first numeric array
            for key, value in data.items():
                if not key.startswith('__') and isinstance(value, np.ndarray):
                    ecg_data = np.array(value)
                    if ecg_data.ndim >= 1 and ecg_data.size > 100:  # Likely ECG data
                        if ecg_data.ndim == 1:
                            ecg_data = ecg_data.reshape(1, -1)
                        elif ecg_data.shape[0] > ecg_data.shape[1]:
                            ecg_data = ecg_data.T
                        return ecg_data
                        
        except Exception as e:
            # Try mat73 for MATLAB v7.3+ files
            if mat73 is None:
                raise ImportError("mat73 package not available for MATLAB v7.3+ files") from e
            data = mat73.loadmat(file_path)
            
            for key in ['ecg', 'ECG', 'data', 'signal']:
                if key in data:
                    ecg_data = np.array(data[key])
                    if ecg_data.ndim == 1:
                        ecg_data = ecg_data.reshape(1, -1)
                    elif ecg_data.shape[0] > ecg_data.shape[1]:
                        ecg_data = ecg_data.T
                    return ecg_data
            raise ValueError(f"Could not load MATLAB file with scipy: {e}")
                
        raise ValueError(f"Could not extract ECG data from MATLAB file: {file_path}")
        
    @staticmethod
    def _load_hdf5(file_path: str) -> np.ndarray:
        """Load HDF5 file."""
        with h5py.File(file_path, 'r') as f:
            # Look for ECG data
            ecg_keys = ['ecg', 'ECG', 'data', 'signal', 'tracings']
            
            for key in ecg_keys:
                if key in f:
                    ecg_data = np.array(f[key])
                    if ecg_data.ndim == 1:
                        ecg_data = ecg_data.reshape(1, -1)
                    elif ecg_data.shape[0] > ecg_data.shape[1]:
                        ecg_data = ecg_data.T
                    return ecg_data
                    
            # Try first dataset
            for key in f.keys():
                data = np.array(f[key])
                if data.ndim >= 1 and data.size > 100:
                    if data.ndim == 1:
                        data = data.reshape(1, -1)
                    elif data.shape[0] > data.shape[1]:
                        data = data.T
                    return data
                    
        raise ValueError(f"Could not extract ECG data from HDF5 file: {file_path}")
        
    @staticmethod
    def _load_numpy(file_path: str) -> np.ndarray:
        """Load numpy file."""
        if file_path.endswith('.npz'):
            data = np.load(file_path)
            # Try common keys
            for key in ['ecg', 'ECG', 'data', 'arr_0']:
                if key in data:
                    ecg_data = data[key]
                    if ecg_data.ndim == 1:
                        ecg_data = ecg_data.reshape(1, -1)
                    elif ecg_data.shape[0] > ecg_data.shape[1]:
                        ecg_data = ecg_data.T
                    return ecg_data
        else:
            ecg_data = np.load(file_path)
            if ecg_data.ndim == 1:
                ecg_data = ecg_data.reshape(1, -1)
            elif ecg_data.shape[0] > ecg_data.shape[1]:
                ecg_data = ecg_data.T
            return ecg_data
            
        raise ValueError(f"Could not load ECG data from numpy file: {file_path}")
        
    @staticmethod
    def _load_text(file_path: str) -> np.ndarray:
        """Load text/CSV file."""
        # Try loading with numpy
        ecg_data = np.loadtxt(file_path, delimiter=',')
        
        if ecg_data.ndim == 1:
            ecg_data = ecg_data.reshape(1, -1)
        elif ecg_data.shape[0] > ecg_data.shape[1]:
            ecg_data = ecg_data.T
            
        return ecg_data
        
    @staticmethod
    def _load_wfdb(file_path: str) -> np.ndarray:
        """Load WFDB format files."""
        try:
            if wfdb is None:
                raise ImportError("wfdb package not installed")
            
            # Remove extension if present
            record_name = os.path.splitext(file_path)[0]
            
            # Read the record
            record = wfdb.rdrecord(record_name)
            
            # Get signal data and transpose to (channels, samples)
            ecg_data = record.p_signal.T
            
            return ecg_data
            
        except ImportError as e:
            raise ImportError(f"wfdb package not installed: {e}")
        except Exception as e:
            raise ValueError(f"Could not load WFDB file: {e}")
            
    @staticmethod
    def validate_ecg_data(
        ecg_data: np.ndarray,
        expected_channels: Optional[int] = None,
        expected_length: Optional[int] = None
    ) -> Tuple[bool, str]:
        """
        Validate ECG data shape and values.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check shape
        if ecg_data.ndim != 2:
            return False, f"Expected 2D array, got {ecg_data.ndim}D"
            
        channels, length = ecg_data.shape
        
        # Check channels
        if expected_channels is not None and channels != expected_channels:
            return False, f"Expected {expected_channels} channels, got {channels}"
            
        # Check length
        if expected_length is not None and length != expected_length:
            return False, f"Expected length {expected_length}, got {length}"
            
        # Check for NaN or Inf
        if np.any(np.isnan(ecg_data)) or np.any(np.isinf(ecg_data)):
            return False, "ECG data contains NaN or Inf values"
            
        # Check for reasonable values (typical ECG range in mV)
        if np.abs(ecg_data).max() > 100:  # Likely in wrong units
            return False, "ECG values seem too large (>100), check units"
            
        return True, "Valid"
        
    @staticmethod
    def preprocess_ecg(
        ecg_data: np.ndarray,
        target_length: Optional[int] = None,
        normalize: bool = True
    ) -> np.ndarray:
        """
        Preprocess ECG data.
        
        Args:
            ecg_data: Raw ECG data
            target_length: Target length for resampling
            normalize: Whether to normalize the data
            
        Returns:
            Preprocessed ECG data
        """
        # Resample if needed
        if target_length is not None:
            current_length = ecg_data.shape[1]
            if current_length != target_length:
                # Simple linear interpolation
                # In production, use proper signal resampling
                if interpolate is None:
                    raise ImportError("scipy.interpolate not available for resampling")
                
                channels, length = ecg_data.shape
                resampled = np.zeros((channels, target_length))
                
                x_old = np.linspace(0, 1, length)
                x_new = np.linspace(0, 1, target_length)
                
                for i in range(channels):
                    f = interpolate.interp1d(x_old, ecg_data[i], kind='linear')
                    resampled[i] = f(x_new)
                    
                ecg_data = resampled
                
        # Normalize if requested
        if normalize:
            # Remove DC offset
            ecg_data = ecg_data - np.mean(ecg_data, axis=1, keepdims=True)
            
            # Scale to [-1, 1]
            max_val = np.max(np.abs(ecg_data))
            if max_val > 0:
                ecg_data = ecg_data / max_val
                
        return ecg_data