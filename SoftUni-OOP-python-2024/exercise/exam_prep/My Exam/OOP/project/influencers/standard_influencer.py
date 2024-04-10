from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign


class StandardInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.45

    def __init__(self, username, followers, engagement_rate):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        payment = self.PAYMENT_PERCENTAGE * campaign.budget
        return payment

    def reached_followers(self, campaign_type: str):
        reached_followers = 0
        if campaign_type == "HighBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 1.2
        elif campaign_type == "LowBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 0.9

        return int(reached_followers)
