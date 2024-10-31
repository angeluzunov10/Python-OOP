from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85

    def __init__(self, username, followers, engagement_rate):
        super().__init__(username, followers, engagement_rate)
        self.campaigns_participated = []

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * PremiumInfluencer.INITIAL_PAYMENT_PERCENTAGE
        return payment

    def reached_followers(self, campaign_type):
        reached_followers = 0

        if campaign_type == "HighBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 1.5
        elif campaign_type == "LowBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 0.8

        return int(reached_followers)
