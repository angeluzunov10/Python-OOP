from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_CAMPAIGN_TYPES = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type, username, followers, engagement_rate):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        for i in self.influencers:
            if i.username == username:
                return f"{username} is already registered."

        influencer = self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type, campaign_id, brand, required_engagement):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        for c in self.campaigns:
            if c.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        campaign = self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username, campaign_id):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet " \
                   f"the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)

        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' " \
                   f"has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}

        for campaign in self.campaigns:
            if not campaign.approved_influencers:
                continue
            if campaign not in result.keys():
                result[campaign] = 0

            for influencer in campaign.approved_influencers:
                result[campaign] += influencer.reached_followers(campaign.__class__.__name__)

        return result

    def influencer_campaign_report(self, username):
        influencer = next(filter(lambda i: i.username == username, self.influencers))

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        result = influencer.display_campaigns_participated()

        return result

    def campaign_statistics(self):
        result = ["$$ Campaign Statistics $$"]
        for c in sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget)):
            result.append(f"  * Brand: {c.brand}, "
                               f"Total influencers: {len(c.approved_influencers)}, "
                               f"Total budget: ${c.budget}, "
                               f"Total reached followers: {self.calculate_total_reached_followers()}")

        result = '\n'.join(result)

        return result



