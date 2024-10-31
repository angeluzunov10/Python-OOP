from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    INITIAL_BUDGET = 5000.0

    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, HighBudgetCampaign.INITIAL_BUDGET, required_engagement)
        self.approved_influencers = []

    def check_eligibility(self, engagement_rate):
        return engagement_rate >= self.required_engagement * 1.2
