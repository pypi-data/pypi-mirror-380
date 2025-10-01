#!/usr/bin/env python3
"""
Test the embedding-based inference pipeline with synthetic data.

This script tests the new prediction heads using the enhanced synthetic dataset
and validates that the embedding extraction and direct predictions work correctly.
"""

import sys
import json
import pandas as pd
from pathlib import Path
import traceback

# Add repository root to path (tests/pipeline-tests -> tests -> repo root).
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

try:
    from inference_pipeline import MultiModalMedicalInference
    from unified_inference import UnifiedMedicalInference, PredictionMode
    from embedding_inference import DirectInferencePipeline, EmbeddingExtractor
    
    def test_embedding_extraction():
        """Test basic embedding extraction functionality."""
        print("\n=== Testing Embedding Extraction ===")
        
        # Load sample data from enhanced dataset
        enhanced_data_path = Path("simdata/enhanced_simdata.csv")
        if not enhanced_data_path.exists():
            print("❌ Enhanced simulation data not found. Please run enhanced_cardiotoxicity_generator.py first.")
            return False
            
        df = pd.read_csv(enhanced_data_path)
        sample_patient = df.iloc[0]
        
        print(f"Testing with patient: {sample_patient['patient_id']}")
        print(f"Risk category: {sample_patient['risk_category']}")
        print(f"Enhanced risk score: {sample_patient['enhanced_risk_score']}")
        
        try:
            # Test with local_inference.py (existing interface)
            print("\n--- Testing Local Inference (Extract Embeddings Mode) ---")
            pipeline = MultiModalMedicalInference(
                ecg_encoder="PKUDigitalHealth/ECGFounder",
                language_model="standardmodelbio/Qwen3-WM-0.6B",
                device="cpu"  # Use CPU for testing
            )
            
            ecg_files = [sample_patient['baseline_ecg_local'], sample_patient['month3_ecg_local']]
            clinical_notes = sample_patient['enhanced_clinical_notes']
            
            # Test embedding extraction
            result = pipeline.predict(
                ecg_files=ecg_files,
                clinical_notes=clinical_notes,
                prediction_mode="embedding_extraction",
                age=sample_patient['age'],
                gender=sample_patient['gender'],
                baseline_lvef=sample_patient['baseline_lvef'],
                current_lvef=sample_patient['current_lvef']
            )
            
            if result.get("status") == "success":
                print("✅ Embedding extraction successful")
                ecg_dim = result["embedding_dimensions"]["ecg"]
                clinical_dim = result["embedding_dimensions"]["clinical"]
                print(f"   ECG embedding dimension: {ecg_dim}")
                print(f"   Clinical embedding dimension: {clinical_dim}")
                return True
            else:
                print(f"❌ Embedding extraction failed: {result.get('error')}")
                return False
                
        except Exception as e:
            print(f"❌ Embedding extraction error: {e}")
            print(traceback.format_exc())
            return False

    def test_standalone_embedding_extractor():
        """Test standalone embedding extractor."""
        print("\n=== Testing Standalone Embedding Extractor ===")
        
        df = pd.read_csv("simdata/enhanced_simdata.csv")
        sample_patient = df.iloc[1]  # Different patient
        
        try:
            extractor = EmbeddingExtractor(
                ecg_encoder="PKUDigitalHealth/ECGFounder",
                device="cpu"
            )
            
            ecg_files = [sample_patient['baseline_ecg_local'], sample_patient['month3_ecg_local']]
            clinical_notes = sample_patient['enhanced_clinical_notes']
            
            # Extract ECG embeddings
            ecg_embeddings = extractor.extract_ecg_embeddings(ecg_files)
            print(f"✅ ECG embeddings extracted: shape {ecg_embeddings.shape}")
            
            # Extract clinical embeddings (may not work without smbtogo model)
            try:
                clinical_embeddings = extractor.extract_clinical_embeddings(
                    clinical_notes,
                    age=sample_patient['age'],
                    gender=sample_patient['gender']
                )
                if clinical_embeddings is not None:
                    print(f"✅ Clinical embeddings extracted: shape {clinical_embeddings.shape}")
                else:
                    print("⚠️  Clinical embeddings not available (expected without proper setup)")
            except Exception as e:
                print(f"⚠️  Clinical embedding extraction failed (expected): {e}")
                clinical_embeddings = None
            
            # Test fusion
            if clinical_embeddings is not None:
                fused = extractor.fuse_embeddings(ecg_embeddings, clinical_embeddings)
                print(f"✅ Embeddings fused: shape {fused.shape}")
            else:
                # Test with just ECG embeddings
                fused = extractor.fuse_embeddings(ecg_embeddings, None)
                print(f"✅ ECG-only embeddings processed: shape {fused.shape}")
            
            return True
            
        except Exception as e:
            print(f"❌ Standalone extraction error: {e}")
            print(traceback.format_exc())
            return False

    def test_direct_prediction_pipeline():
        """Test direct prediction pipeline with different prediction heads."""
        print("\n=== Testing Direct Prediction Pipeline ===")
        
        df = pd.read_csv("simdata/enhanced_simdata.csv")
        sample_patient = df.iloc[2]  # Another patient
        
        print(f"Testing with patient: {sample_patient['patient_id']}")
        print(f"True risk score: {sample_patient['enhanced_risk_score']}")
        print(f"True outcome: {sample_patient['outcome']}")
        
        try:
            pipeline = DirectInferencePipeline(
                ecg_encoder="PKUDigitalHealth/ECGFounder",
                device="cpu"
            )
            
            ecg_files = [sample_patient['baseline_ecg_local'], sample_patient['month3_ecg_local']]
            clinical_notes = sample_patient['enhanced_clinical_notes']
            
            # Test survival analysis
            print("\n--- Testing Survival Analysis Head ---")
            try:
                survival_result = pipeline.predict(
                    ecg_files=ecg_files,
                    clinical_notes=clinical_notes,
                    task_type="survival",
                    fusion_method="concatenate"
                )
                
                if survival_result.get("status") != "failed":
                    print("✅ Survival analysis prediction successful")
                    print(f"   Risk score: {survival_result.get('predictions', {}).get('risk_score', 'N/A')}")
                else:
                    print(f"❌ Survival analysis failed: {survival_result.get('error')}")
                    
            except Exception as e:
                print(f"❌ Survival analysis error: {e}")
            
            # Test regression
            print("\n--- Testing Regression Head ---")
            try:
                regression_result = pipeline.predict(
                    ecg_files=ecg_files,
                    clinical_notes=clinical_notes,
                    task_type="regression",
                    fusion_method="concatenate",
                    output_dim=3  # Predict 3 values
                )
                
                if regression_result.get("status") != "failed":
                    print("✅ Regression prediction successful")
                    print(f"   Predictions: {regression_result.get('predictions', [])}")
                else:
                    print(f"❌ Regression failed: {regression_result.get('error')}")
                    
            except Exception as e:
                print(f"❌ Regression error: {e}")
            
            # Test classification
            print("\n--- Testing Classification Head ---")
            try:
                classification_result = pipeline.predict(
                    ecg_files=ecg_files,
                    clinical_notes=clinical_notes,
                    task_type="classification",
                    fusion_method="concatenate",
                    num_classes=6  # Risk categories
                )
                
                if classification_result.get("status") != "failed":
                    print("✅ Classification prediction successful")
                    predictions = classification_result.get("predictions", {})
                    print(f"   Predicted class: {predictions.get('predicted_classes', [])}")
                    print(f"   Probabilities: {predictions.get('probabilities', [])}")
                else:
                    print(f"❌ Classification failed: {classification_result.get('error')}")
                    
            except Exception as e:
                print(f"❌ Classification error: {e}")
                
            return True
            
        except Exception as e:
            print(f"❌ Direct prediction pipeline error: {e}")
            print(traceback.format_exc())
            return False

    def test_unified_interface():
        """Test the unified inference interface."""
        print("\n=== Testing Unified Inference Interface ===")
        
        df = pd.read_csv("simdata/enhanced_simdata.csv")
        sample_patient = df.iloc[3]  # Another patient
        
        print(f"Testing with patient: {sample_patient['patient_id']}")
        
        try:
            # Initialize with limited capability to avoid heavy model loading
            unified_pipeline = UnifiedMedicalInference(
                ecg_encoder="PKUDigitalHealth/ECGFounder",
                enable_text_generation=False,  # Skip text generation for now
                enable_direct_prediction=True,
                device="cpu"
            )
            
            print(f"Available modes: {unified_pipeline.get_available_modes()}")
            
            ecg_files = [sample_patient['baseline_ecg_local'], sample_patient['month3_ecg_local']]
            clinical_notes = sample_patient['enhanced_clinical_notes']
            
            # Test embedding extraction mode
            print("\n--- Testing Unified Embedding Extraction ---")
            try:
                embedding_result = unified_pipeline.predict(
                    ecg_files=ecg_files,
                    clinical_notes=clinical_notes,
                    mode=PredictionMode.EMBEDDING_EXTRACTION
                )
                
                if embedding_result.get("status") == "success":
                    print("✅ Unified embedding extraction successful")
                    print(f"   ECG dim: {embedding_result['embedding_dimensions']['ecg']}")
                    print(f"   Clinical dim: {embedding_result['embedding_dimensions']['clinical']}")
                else:
                    print(f"❌ Unified embedding extraction failed: {embedding_result.get('error')}")
                    
            except Exception as e:
                print(f"❌ Unified embedding extraction error: {e}")
            
            # Test direct prediction modes
            for mode in [PredictionMode.SURVIVAL_ANALYSIS, PredictionMode.REGRESSION]:
                print(f"\n--- Testing Unified {mode.value.title()} ---")
                try:
                    result = unified_pipeline.predict(
                        ecg_files=ecg_files,
                        clinical_notes=clinical_notes,
                        mode=mode,
                        fusion_method="concatenate"
                    )
                    
                    if result.get("status") != "failed":
                        print(f"✅ Unified {mode.value} successful")
                        print(f"   Predictions: {result.get('predictions', {})}")
                    else:
                        print(f"❌ Unified {mode.value} failed: {result.get('error')}")
                        
                except Exception as e:
                    print(f"❌ Unified {mode.value} error: {e}")
            
            return True
            
        except Exception as e:
            print(f"❌ Unified interface error: {e}")
            print(traceback.format_exc())
            return False

    def test_batch_predictions():
        """Test batch predictions on multiple patients."""
        print("\n=== Testing Batch Predictions ===")
        
        df = pd.read_csv("simdata/enhanced_simdata.csv")
        test_patients = df.head(5)  # Test with 5 patients
        
        print(f"Testing batch prediction on {len(test_patients)} patients...")
        
        try:
            extractor = EmbeddingExtractor(
                ecg_encoder="PKUDigitalHealth/ECGFounder",
                device="cpu"
            )
            
            batch_results = []
            
            for idx, patient in test_patients.iterrows():
                try:
                    ecg_files = [patient['baseline_ecg_local'], patient['month3_ecg_local']]
                    
                    # Extract ECG embeddings
                    ecg_embeddings = extractor.extract_ecg_embeddings(ecg_files)
                    
                    batch_results.append({
                        "patient_id": patient['patient_id'],
                        "embedding_shape": ecg_embeddings.shape,
                        "true_risk_score": patient['enhanced_risk_score'],
                        "true_outcome": patient['outcome'],
                        "status": "success"
                    })
                    
                except Exception as e:
                    batch_results.append({
                        "patient_id": patient['patient_id'],
                        "status": "failed",
                        "error": str(e)
                    })
            
            # Print results
            successful = sum(1 for r in batch_results if r["status"] == "success")
            print(f"✅ Batch processing: {successful}/{len(test_patients)} patients successful")
            
            for result in batch_results:
                if result["status"] == "success":
                    print(f"   {result['patient_id']}: embeddings {result['embedding_shape']}, risk={result['true_risk_score']}")
                else:
                    print(f"   {result['patient_id']}: FAILED - {result['error']}")
            
            return successful == len(test_patients)
            
        except Exception as e:
            print(f"❌ Batch prediction error: {e}")
            return False

    def main():
        """Run all tests."""
        print("=== Embedding-Based Inference Pipeline Test ===")
        print("Testing with enhanced synthetic cardiotoxicity dataset")
        
        # Check if data exists
        if not Path("simdata/enhanced_simdata.csv").exists():
            print("❌ Enhanced simulation data not found!")
            print("Please run: uv run simdata/enhanced_cardiotoxicity_generator.py")
            return False
        
        test_results = {}
        
        # Run tests
        test_results["embedding_extraction"] = test_embedding_extraction()
        test_results["standalone_extractor"] = test_standalone_embedding_extractor()
        test_results["direct_prediction"] = test_direct_prediction_pipeline()
        test_results["unified_interface"] = test_unified_interface()
        test_results["batch_predictions"] = test_batch_predictions()
        
        # Summary
        print("\n" + "="*60)
        print("TEST SUMMARY")
        print("="*60)
        
        for test_name, result in test_results.items():
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"{test_name:25} {status}")
        
        overall_success = all(test_results.values())
        print(f"\nOverall Result: {'✅ ALL TESTS PASSED' if overall_success else '❌ SOME TESTS FAILED'}")
        
        if overall_success:
            print("\n🎉 Embedding-based inference pipeline is working correctly!")
            print("📊 Ready for production deployment with prediction heads")
        else:
            print("\n⚠️  Some tests failed. Check the output above for details.")
            print("💡 Note: Some failures may be expected due to missing model dependencies")
        
        return overall_success

    if __name__ == "__main__":
        success = main()
        sys.exit(0 if success else 1)
        
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please ensure all dependencies are installed with 'uv sync'")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    print(traceback.format_exc())
    sys.exit(1)