import datetime
import json

def generate_proposal(request):
    """HTTP Cloud Function to generate enterprise proposals"""
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    if request.method == 'OPTIONS':
        return ('', 204, headers)
    
    try:
        request_json = request.get_json(silent=True) or {}
        
        client_name = request_json.get('client_name', 'Enterprise Client')
        business_problem = request_json.get('business_problem', 'AI-powered business transformation')
        industry = request_json.get('industry', 'Finance')
        
        proposal_id = f"TRANSFORM-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        proposal = {
            "proposal_id": proposal_id,
            "client": client_name,
            "industry": industry,
            "date": current_date,
            "summary": f"Your challenge: {business_problem}. Our solution: Production-grade AI system deployed within 24 hours.",
            "timeline": {
                "8:00 AM": f"Deep dive on {business_problem}",
                "12:00 PM": "Architecture and development",
                "4:00 PM": "Testing and refinement", 
                "6:00 PM": "LIVE PRODUCTION DEPLOYMENT"
            },
            "deliverables": [
                "Cloud-native microservices architecture",
                "Auto-scaling AI inference engine", 
                "Enterprise-grade security & compliance",
                "Real-time monitoring & analytics",
                "Mobile-responsive web interface"
            ],
            "success_metrics": [
                "Production URL delivered within 24 hours",
                "System handling live traffic by EOD", 
                "ROI demonstrable within first week"
            ]
        }
        
        return (json.dumps(proposal, indent=2), 200, headers)
        
    except Exception as e:
        return (json.dumps({"error": str(e)}), 500, headers)