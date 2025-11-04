import datetime
import json
import random

def generate_enterprise_proposal(request):
    """Enhanced enterprise proposal generator with tiered pricing"""
    
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
        tier = request_json.get('tier', 'starter')  # starter, professional, enterprise
        
        proposal_id = f"TRANSFORM-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Tier-based pricing and features
        tiers = {
            'starter': {
                'price': 4997,
                'timeline': '48 hours',
                'features': ['Basic AI Integration', 'Single Environment', 'Email Support']
            },
            'professional': {
                'price': 14997, 
                'timeline': '24 hours',
                'features': ['Advanced AI Models', 'Multiple Environments', 'Priority Support', 'API Access']
            },
            'enterprise': {
                'price': 49997,
                'timeline': 'Same Day',
                'features': ['Custom AI Training', 'Dedicated Infrastructure', '24/7 Support', 'SLA Guarantee']
            }
        }
        
        selected_tier = tiers[tier]
        
        proposal = {
            "proposal_id": proposal_id,
            "client": client_name,
            "industry": industry,
            "date": current_date,
            "tier": tier,
            "investment": f"${selected_tier['price']:,}",
            "timeline": selected_tier['timeline'],
            "summary": f"Your challenge: {business_problem}. Our {tier.title()} solution delivers production-grade AI within {selected_tier['timeline']}.",
            "deliverables": [
                "Cloud-native microservices architecture",
                "Auto-scaling AI inference engine", 
                "Enterprise-grade security & compliance",
                "Real-time monitoring & analytics",
                "Mobile-responsive web interface"
            ] + selected_tier['features'],
            "success_metrics": [
                "Production URL delivered within timeline",
                "System handling live traffic by EOD", 
                "ROI demonstrable within first week",
                f"{tier.title()} features fully implemented"
            ],
            "next_steps": [
                "Digital signature required",
                "50% deposit to commence development",
                "Remaining 50% upon delivery",
                "Ongoing support and scaling available"
            ]
        }
        
        return (json.dumps(proposal, indent=2), 200, headers)
        
    except Exception as e:
        return (json.dumps({"error": str(e)}), 500, headers)