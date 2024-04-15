from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 45

    # def __init__(self, username: str, followers: int, engagement_rate: float):
    #     super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * (self.INITIAL_PAYMENT_PERCENTAGE / 100)
        return payment

    def reached_followers(self, campaign_type: str):
        campaign_types = {"HighBudgetCampaign": 1.2, "LowBudgetCampaign": 0.9}
        r_followers = campaign_types[campaign_type] * (self.followers * self.engagement_rate)
        return int(r_followers)
