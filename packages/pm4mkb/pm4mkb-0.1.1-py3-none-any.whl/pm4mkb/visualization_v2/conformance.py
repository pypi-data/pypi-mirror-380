"""
Enhanced ConformanceAnalyzer with case ID tracking.
"""

import json
import tempfile
import webbrowser
from pathlib import Path
from typing import Optional, List, Dict, Union

from .processors.data_processor import DataProcessor
from .processors.reference_extractor import ReferenceExtractor
from .process_standard import ProcessStandard, create_standard_from_data
from .template_enhanced import ENHANCED_CONFORMANCE_TEMPLATE


class ConformanceAnalyzer:
    """Analyze process conformance with configurable standards."""
    
    def __init__(self):
        """Initialize ConformanceAnalyzer."""
        self.processor = DataProcessor()
        self.extractor = ReferenceExtractor()
        self.last_output = None
        self.last_analysis = None
        self.last_case_id = None  # Track the case being analyzed
    
    def analyze(self,
                filepath: str,
                case_col: Optional[str] = None,
                activity_col: Optional[str] = None,
                timestamp_col: Optional[str] = None,
                case_id: Optional[str] = None,
                standard: Optional[ProcessStandard] = None,
                auto_create_standard: bool = True,
                remove_patterns: Optional[List[str]] = None,
                mark_as_optional: Optional[List[str]] = None,
                output_path: Optional[str] = None,
                show: bool = True) -> str:
        """Analyze process conformance with enhanced categorization."""
        
        # Load and process data
        df = self.processor.load_file(filepath)
        case_col, activity_col, timestamp_col = self.processor.detect_columns(
            df, case_col, activity_col, timestamp_col
        )
        
        print(f"Using columns: Case={case_col}, Activity={activity_col}, Time={timestamp_col}")
        
        case_df = self.processor.process_dataframe(
            df, case_col, activity_col, timestamp_col, case_id
        )
        
        # Store the actual case ID being analyzed
        if case_id:
            self.last_case_id = case_id
        else:
            # Get the first case ID from the processed dataframe
            self.last_case_id = str(case_df[case_col].iloc[0]) if not case_df.empty else "Unknown"
        
        print(f"Analyzing Case ID: {self.last_case_id}")
        
        # Get activities
        actual_activities = case_df[activity_col].tolist()
        
        # Get or create standard
        if standard is None and auto_create_standard:
            print("Auto-creating process standard...")
            
            if mark_as_optional is None:
                mark_as_optional = ["PAUSE", "WAIT", "HOLD"]
            
            standard = ProcessStandard.from_reference_process(
                actual_activities,
                remove_patterns=remove_patterns,
                mark_as_optional=mark_as_optional
            )
            
            print(f"  Required: {', '.join(standard.required_sequence[:5])}...")
            if standard.optional_activities:
                print(f"  Optional: {', '.join(standard.optional_activities[:3])}...")
        
        elif standard is None:
            standard = ProcessStandard(required_sequence=actual_activities)
        
        # Analyze with standard
        analysis = self.extractor.analyze_with_standard(actual_activities, standard)
        self.last_analysis = analysis
        
        # Build graph data
        standard_nodes, standard_edges = self.extractor.build_graph_data(
            standard.required_sequence
        )
        actual_nodes, actual_edges = self.extractor.build_graph_data(
            actual_activities
        )
        
        # Generate HTML with case ID
        html = self._generate_enhanced_html(
            standard_nodes, standard_edges,
            actual_nodes, actual_edges,
            analysis, standard,
            self.last_case_id  # Pass case ID
        )
        
        # Save
        if output_path:
            output_file = Path(output_path)
        else:
            output_file = Path(tempfile.mkdtemp()) / f"conformance_case_{self.last_case_id}.html"
        
        output_file.write_text(html, encoding='utf-8')
        self.last_output = str(output_file)
        
        # Print summary
        print(f"\nConformance Analysis Complete for Case {self.last_case_id}:")
        print(f"  Conformance Level: {analysis['conformance_level']:.1f}%")
        
        for category, count in analysis['category_counts'].items():
            if count > 0:
                print(f"  {category.capitalize()}: {count} transitions")
        
        print(f"\nOutput: {output_file}")
        
        if show:
            webbrowser.open(f"file://{output_file.absolute()}")
        
        return str(output_file)
    
    def _generate_enhanced_html(self, standard_nodes, standard_edges, 
                                actual_nodes, actual_edges, analysis, standard,
                                case_id=None):
        """Generate enhanced HTML with categories and case ID."""
        
        # Use case ID or default
        display_case_id = str(case_id) if case_id is not None else "Unknown"
        
        # Build statistics HTML
        stats_html = ""
        for category, count in analysis['category_counts'].items():
            if count > 0:
                stats_html += f"""
                <div class="stat-row">
                    <span class="stat-label">{category.capitalize()}</span>
                    <span class="stat-value">{count}</span>
                </div>
                """
        
        # Build problems HTML
        problems_html = ""
        validation = analysis['validation']
        
        for forbidden in validation.get('forbidden_found', [])[:5]:
            problems_html += f'<div class="activity-item">❌ {forbidden} <span class="badge forbidden">запрещено</span></div>'
        
        for missing in validation.get('missing_required', [])[:5]:
            problems_html += f'<div class="activity-item">⚠️ Пропущен: {missing} <span class="badge required">обязательный</span></div>'
        
        # Show some deviations
        edge_analysis = analysis.get('edge_analysis', [])
        deviation_edges = [e for e in edge_analysis if e['category'] == 'deviation']
        for edge in deviation_edges[:3]:
            problems_html += f'<div class="activity-item">🔴 {edge["source"]} → {edge["target"]} <span class="badge forbidden">отклонение</span></div>'
        
        if not problems_html:
            problems_html = '<div class="activity-item">✅ Проблем не обнаружено</div>'
        
        # Replace placeholders
        html = ENHANCED_CONFORMANCE_TEMPLATE
        html = html.replace('{{CASE_ID}}', display_case_id)
        html = html.replace('{{CONFORMANCE_LEVEL}}', f"{analysis['conformance_level']:.1f}")
        html = html.replace('{{STATISTICS}}', stats_html)
        html = html.replace('{{PROBLEMS}}', problems_html)
        
        # Add graph data
        standard_data = {'nodes': standard_nodes, 'edges': standard_edges}
        actual_data = {'nodes': actual_nodes, 'edges': actual_edges}
        
        # Debug: print edge categories to console
        print(f"\nEdge categories for visualization:")
        for edge_id, category in analysis['edge_categories'].items():
            if category in ['deviation', 'forbidden']:
                print(f"  {edge_id}: {category} (will be RED)")
        
        html = html.replace('{{STANDARD_DATA}}', json.dumps(standard_data))
        html = html.replace('{{ACTUAL_DATA}}', json.dumps(actual_data))
        html = html.replace('{{EDGE_CATEGORIES}}', json.dumps(analysis['edge_categories']))
        
        return html
