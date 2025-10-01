"""Results formatting utilities for medical inference pipeline."""

from typing import Dict, Any, Tuple
from datetime import datetime


class ResultsFormatter:
    """Handles formatting and parsing of inference results."""
    
    @staticmethod
    def parse_generated_text(text: str) -> Tuple[Dict[str, str], list]:
        """Parse generated text to extract reports and recommendations."""
        # Simple parsing - can be improved with more sophisticated NLP
        lines = text.strip().split('\n')
        
        clinical_reports = {}
        recommendations = []
        
        # Look for recommendation patterns
        rec_keywords = ["recommend", "suggest", "advise", "should", "monitor", "consider"]
        report_keywords = ["assessment", "finding", "diagnosis", "risk", "result"]
        
        report_idx = 0
        for line in lines:
            line_lower = line.lower()
            
            # Check if it's a recommendation
            if any(keyword in line_lower for keyword in rec_keywords):
                recommendations.append(line.strip())
            # Check if it's a clinical report
            elif any(keyword in line_lower for keyword in report_keywords) or len(line) > 50:
                clinical_reports[f"report_{report_idx}"] = line.strip()
                report_idx += 1
        
        # Ensure we have some content
        if not clinical_reports:
            clinical_reports["report_0"] = text[:200] if len(text) > 200 else text
        
        if not recommendations:
            recommendations = [
                "Monitor cardiac function with regular ECGs",
                "Consider dose modification based on risk assessment",
                "Evaluate for cardioprotective interventions",
                "Schedule follow-up in 4-6 weeks"
            ]
        
        return clinical_reports, recommendations[:4]  # Limit to 4 recommendations
    
    @staticmethod
    def format_predictions(
        head_predictions: Dict[str, Any],
        clinical_reports: Dict[str, str],
        recommendations: list,
        generated_text: str,
        model_type: str,
        inference_time: float,
        language_model_id: str,
        encoders: Dict[str, Any] = None,
        modalities: Dict[str, Any] | None = None,
    ) -> Dict[str, Any]:
        """Format all predictions into the standard output structure."""
        return {
            "status": "success",
            "message": "Cardiotoxicity risk assessment completed",
            "predictions": {
                **head_predictions,  # Include all prediction head results
                "clinical_reports": clinical_reports,
                "recommendations": recommendations,
                "generated_response": generated_text,
                "metadata": {
                    "model_type": model_type,
                    "inference_time_seconds": inference_time,
                    "timestamp": datetime.now().isoformat()
                }
            },
            "metadata": {
                "inference_time_seconds": inference_time,
                "models_used": {
                    "language_model": language_model_id,
                    "encoders": encoders or {},
                },
                "model_type": model_type,
                "modalities": modalities or {},
                "timestamp": datetime.now().isoformat()
            }
        }
