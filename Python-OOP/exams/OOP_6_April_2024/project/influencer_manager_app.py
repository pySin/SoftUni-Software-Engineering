from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    def __init__(self):
        self.influencers: list = []
        self.campaigns: list = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        valid_influencer_types = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}

        if influencer_type not in valid_influencer_types:
            return f"{influencer_type} is not an allowed influencer type."

        username_non = next((u for u in self.influencers if u.username == username), None)
        if username_non:
            return f"{username_non.username} is already registered."

        create_influencer = valid_influencer_types[influencer_type](username,
                                                                     followers, engagement_rate)

        self.influencers.append(create_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        valid_campaigns = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

        if campaign_type not in valid_campaigns:
            return f"{campaign_type} is not a valid campaign type."

        campaign_exists = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)
        if campaign_exists:
            return f"Campaign ID {campaign_id} has already been created."

        self.campaigns.append(valid_campaigns[campaign_type](campaign_id, brand, required_engagement))
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer_found = next((inf for inf in self.influencers if inf.username == influencer_username), None)
        if not influencer_found:
            return f"Influencer '{influencer_username}' not found."

        campaign_found = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)
        if not campaign_found:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign_found.check_eligibility(influencer_found.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for " \
                   f"the campaign with ID {campaign_id}."

        influencer_payment = influencer_found.calculate_payment(campaign_found)
        if influencer_payment > 0.0:
            campaign_found.approved_influencers.append(influencer_found)
            campaign_found.budget -= influencer_payment
            influencer_found.campaigns_participated.append((campaign_found))
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with " \
                   f"ID {campaign_id}."

    def influencer_campaign_report(self, username: str):
        # print("Function influencer_campaign_report Running!")
        influencer_results = next((i for i in self.influencers if i.username == username), None)
        # print(influencer_results)
        if not influencer_results.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        # results = f"{influencer_results.__class__.__name__} :) {username} :) participated in the following campaigns:\n"
        results = influencer_results.display_campaigns_participated()
        return results

    def campaign_statistics(self):
        statistics_report = "$$ Campaign Statistics $$\n"
        self.campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        for campaign in self.campaigns:
            # print([{inf.username: inf.followers} for inf in campaign.approved_influencers])
            total_reached_followers = sum([inf.reached_followers(campaign.__class__.__name__) for inf in campaign.approved_influencers])
            statistics_report += f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, " \
                                 f"Total budget: ${campaign.budget:.2f}, Total reached followers:" \
                                 f" {total_reached_followers}\n"

        return statistics_report
