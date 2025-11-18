#!/usr/bin/env python3
"""
ATS Resume Benchmark Validation Script
Compares ATS-extracted resume data against source JSON Resume data
Calculates accuracy metrics and identifies parsing issues
"""

import json
import sys
from typing import Dict, List, Tuple, Any
from datetime import datetime

class ResumeValidator:
    """Validate ATS-extracted resume data against source JSON"""

    def __init__(self, source_resume: Dict, extracted_data: Dict):
        self.source = source_resume
        self.extracted = extracted_data
        self.results = {
            "overall_accuracy": 0,
            "field_results": {},
            "missing_fields": [],
            "extra_fields": [],
            "issues": []
        }

    def validate_all(self) -> Dict:
        """Run all validation checks"""
        self.validate_basics()
        self.validate_work_experience()
        self.validate_education()
        self.validate_skills()
        self.validate_languages()
        self.calculate_overall_accuracy()
        return self.results

    def validate_basics(self) -> None:
        """Validate contact and basic information"""
        field_scores = {}

        # Check each basic field
        basic_fields = ["name", "email", "phone", "label", "summary"]
        for field in basic_fields:
            source_val = self.source.get("basics", {}).get(field, "")
            extracted_val = self.extracted.get("basics", {}).get(field, "")

            if source_val and not extracted_val:
                self.results["issues"].append(f"MISSING: basics.{field}")
                field_scores[field] = 0
            elif source_val == extracted_val:
                field_scores[field] = 100
            elif self._fuzzy_match(source_val, extracted_val) > 0.85:
                field_scores[field] = 95  # Minor differences acceptable
                self.results["issues"].append(f"MINOR_DIFF: basics.{field}")
            else:
                field_scores[field] = 0
                self.results["issues"].append(f"MISMATCH: basics.{field}")

        self.results["field_results"]["basics"] = {
            "accuracy": sum(field_scores.values()) / len(field_scores) if field_scores else 0,
            "fields": field_scores
        }

    def validate_work_experience(self) -> None:
        """Validate employment history extraction"""
        source_work = self.source.get("work", [])
        extracted_work = self.extracted.get("work", [])

        if len(extracted_work) != len(source_work):
            self.results["issues"].append(
                f"WORK_COUNT_MISMATCH: Expected {len(source_work)}, got {len(extracted_work)}"
            )

        accuracy_scores = []

        for i, source_job in enumerate(source_work):
            if i >= len(extracted_work):
                self.results["issues"].append(f"MISSING_JOB: Position {i}")
                accuracy_scores.append(0)
                continue

            extracted_job = extracted_work[i]
            job_score = 0

            # Check key fields
            if source_job.get("name") == extracted_job.get("name"):
                job_score += 25
            else:
                self.results["issues"].append(f"JOB_{i}_NAME_MISMATCH")

            if source_job.get("position") == extracted_job.get("position"):
                job_score += 25
            else:
                self.results["issues"].append(f"JOB_{i}_POSITION_MISMATCH")

            if self._validate_date(source_job.get("startDate"), extracted_job.get("startDate")):
                job_score += 25
            else:
                self.results["issues"].append(f"JOB_{i}_START_DATE_MISMATCH")

            if self._validate_date(source_job.get("endDate"), extracted_job.get("endDate")):
                job_score += 25
            else:
                self.results["issues"].append(f"JOB_{i}_END_DATE_MISMATCH")

            accuracy_scores.append(job_score)

        avg_accuracy = sum(accuracy_scores) / len(accuracy_scores) if accuracy_scores else 0
        self.results["field_results"]["work"] = {
            "accuracy": avg_accuracy,
            "total_positions": len(source_work),
            "correctly_parsed": sum(1 for s in accuracy_scores if s == 100)
        }

    def validate_education(self) -> None:
        """Validate education extraction"""
        source_edu = self.source.get("education", [])
        extracted_edu = self.extracted.get("education", [])

        if len(extracted_edu) != len(source_edu):
            self.results["issues"].append(
                f"EDUCATION_COUNT_MISMATCH: Expected {len(source_edu)}, got {len(extracted_edu)}"
            )

        accuracy_scores = []
        for i, source_degree in enumerate(source_edu):
            if i >= len(extracted_edu):
                accuracy_scores.append(0)
                continue

            extracted_degree = extracted_edu[i]
            degree_score = 0

            if source_degree.get("institution") == extracted_degree.get("institution"):
                degree_score += 50
            else:
                self.results["issues"].append(f"EDU_{i}_INSTITUTION_MISMATCH")

            if source_degree.get("studyType") == extracted_degree.get("studyType"):
                degree_score += 50
            else:
                self.results["issues"].append(f"EDU_{i}_STUDY_TYPE_MISMATCH")

            accuracy_scores.append(degree_score)

        avg_accuracy = sum(accuracy_scores) / len(accuracy_scores) if accuracy_scores else 0
        self.results["field_results"]["education"] = {
            "accuracy": avg_accuracy,
            "total_degrees": len(source_edu)
        }

    def validate_skills(self) -> None:
        """Validate skills extraction"""
        source_skills = set(s.get("name", "") for s in self.source.get("skills", []))
        extracted_skills = set(s.get("name", "") for s in self.extracted.get("skills", []))

        if not source_skills:
            self.results["field_results"]["skills"] = {"accuracy": 100, "note": "No skills to validate"}
            return

        correctly_found = source_skills & extracted_skills
        missed = source_skills - extracted_skills
        false_positives = extracted_skills - source_skills

        precision = len(correctly_found) / len(extracted_skills) if extracted_skills else 0
        recall = len(correctly_found) / len(source_skills)
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        if missed:
            self.results["issues"].append(f"MISSED_SKILLS: {', '.join(missed)}")
        if false_positives:
            self.results["issues"].append(f"FALSE_POSITIVE_SKILLS: {', '.join(false_positives)}")

        self.results["field_results"]["skills"] = {
            "accuracy": f1_score * 100,
            "precision": precision * 100,
            "recall": recall * 100,
            "total_source": len(source_skills),
            "correctly_found": len(correctly_found)
        }

    def validate_languages(self) -> None:
        """Validate language detection"""
        source_langs = len(self.source.get("languages", []))
        extracted_langs = len(self.extracted.get("languages", []))

        if source_langs == 0:
            self.results["field_results"]["languages"] = {"accuracy": 100, "note": "No languages to validate"}
        elif source_langs == extracted_langs:
            self.results["field_results"]["languages"] = {"accuracy": 100, "total_languages": source_langs}
        else:
            accuracy = (extracted_langs / source_langs) * 100 if source_langs else 0
            self.results["field_results"]["languages"] = {
                "accuracy": accuracy,
                "expected": source_langs,
                "found": extracted_langs
            }
            self.results["issues"].append(f"LANGUAGE_COUNT_MISMATCH: Expected {source_langs}, got {extracted_langs}")

    def calculate_overall_accuracy(self) -> None:
        """Calculate weighted overall accuracy"""
        field_weights = {
            "basics": 0.20,
            "work": 0.35,
            "education": 0.20,
            "skills": 0.15,
            "languages": 0.10
        }

        weighted_accuracy = 0
        for field, weight in field_weights.items():
            if field in self.results["field_results"]:
                accuracy = self.results["field_results"][field].get("accuracy", 0)
                weighted_accuracy += accuracy * weight

        self.results["overall_accuracy"] = weighted_accuracy

    @staticmethod
    def _fuzzy_match(str1: str, str2: str) -> float:
        """Simple fuzzy string matching (Levenshtein-like)"""
        if str1 == str2:
            return 1.0
        if not str1 or not str2:
            return 0.0

        # Very basic similarity check
        common = sum(1 for c1, c2 in zip(str1.lower(), str2.lower()) if c1 == c2)
        max_len = max(len(str1), len(str2))
        return common / max_len if max_len > 0 else 0.0

    @staticmethod
    def _validate_date(source_date: str, extracted_date: str) -> bool:
        """Validate date matching (allowing slight format variations)"""
        if source_date == extracted_date:
            return True
        if not source_date and not extracted_date:
            return True
        if not source_date or not extracted_date:
            return False

        # Try parsing different date formats
        try:
            source_parsed = datetime.fromisoformat(source_date.split('T')[0])
            extracted_parsed = datetime.fromisoformat(extracted_date.split('T')[0])
            return source_parsed == extracted_parsed
        except:
            return False


class BenchmarkRunner:
    """Run benchmark tests across multiple resumes"""

    def __init__(self, resume_file: str):
        with open(resume_file, 'r', encoding='utf-8') as f:
            self.resumes = json.load(f)
        self.results = []

    def validate_resume(self, resume_index: int, extracted_data: Dict) -> Dict:
        """Validate single resume"""
        validator = ResumeValidator(self.resumes[resume_index], extracted_data)
        return validator.validate_all()

    def generate_report(self, validation_results: List[Dict]) -> Dict:
        """Generate comprehensive benchmark report"""
        report = {
            "test_date": datetime.now().isoformat(),
            "total_resumes_tested": len(validation_results),
            "summary_metrics": {
                "average_accuracy": sum(r["overall_accuracy"] for r in validation_results) / len(validation_results),
                "resumes_above_95": sum(1 for r in validation_results if r["overall_accuracy"] >= 95),
                "resumes_above_90": sum(1 for r in validation_results if r["overall_accuracy"] >= 90),
                "resumes_below_80": sum(1 for r in validation_results if r["overall_accuracy"] < 80)
            },
            "detailed_results": validation_results,
            "recommendations": []
        }

        # Generate recommendations
        if report["summary_metrics"]["average_accuracy"] < 90:
            report["recommendations"].append("Review overall parsing algorithm for accuracy")

        field_accuracies = {}
        for result in validation_results:
            for field, data in result["field_results"].items():
                if field not in field_accuracies:
                    field_accuracies[field] = []
                field_accuracies[field].append(data.get("accuracy", 0))

        for field, accuracies in field_accuracies.items():
            avg = sum(accuracies) / len(accuracies)
            if avg < 85:
                report["recommendations"].append(f"Improve {field} extraction accuracy (currently {avg:.1f}%)")

        return report


# Example usage
if __name__ == "__main__":
    print("ATS Resume Benchmark Validation Script v1.0")
    print("=" * 60)
    print("\nUsage:")
    print("  1. Export extracted resume data from your ATS")
    print("  2. Save as JSON file")
    print("  3. Run: python validate.py source_resume.json extracted_data.json")
    print("\nExample:")
    print("  python validate.py resume_001.json ats_extracted_001.json")
    print("\nFor bulk validation:")
    print("  - Place all ATS extractions in /ats_output/ folder")
    print("  - Run: python bulk_validate.py")
